"""Exercise Git bytes and strict rejection of changed download payloads."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_git import export_revision


class GitValidationTests(unittest.TestCase):
    def setUp(self):
        self.workspace = tempfile.TemporaryDirectory(prefix="silemio-library-test-")
        self.addCleanup(self.workspace.cleanup)
        self.snapshot = Path(self.workspace.name)
        self.sha = export_revision(self.snapshot)
        spec = importlib.util.spec_from_file_location(
            "snapshot_validator", self.snapshot / "scripts" / "validate_library.py"
        )
        self.validator = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.validator)
        manifest = json.loads((self.snapshot / "manifest-v1.json").read_bytes())
        self.entry = manifest["profiles"][0]
        self.profile = self.snapshot / self.entry["path"]

    def test_git_snapshot_passes_hashes_and_schemas(self):
        self.assertEqual(len(self.sha), 40)
        self.assertNotIn(b"\r\n", self.profile.read_bytes())
        self.assertEqual(
            hashlib.sha256(self.profile.read_bytes()).hexdigest().upper(),
            self.entry["sha256"].upper(),
        )
        self.assertEqual(self.validator.main(), 0)
        subprocess.run(
            [sys.executable, "-B", str(self.snapshot / "scripts" / "validate_schemas.py")],
            cwd=self.snapshot,
            check=True,
        )

    def test_crlf_download_is_rejected_without_normalization(self):
        original = self.profile.read_bytes()
        converted = original.replace(b"\n", b"\r\n")
        self.assertNotEqual(original, converted)
        self.profile.write_bytes(converted)
        with self.assertRaisesRegex(self.validator.ValidationError, "sha256"):
            self.validator.main()
        self.assertEqual(self.profile.read_bytes(), converted)

    def test_changed_valid_json_download_is_rejected(self):
        self.profile.write_bytes(self.profile.read_bytes() + b"\n")
        json.loads(self.profile.read_bytes())
        with self.assertRaisesRegex(self.validator.ValidationError, "sha256"):
            self.validator.main()

    def test_invalid_reference_fails_without_export(self):
        with tempfile.TemporaryDirectory() as folder:
            destination = Path(folder)
            with patch("validate_git.subprocess.check_output", wraps=subprocess.check_output) as run:
                with self.assertRaises(subprocess.CalledProcessError):
                    export_revision(destination, "refs/heads/nonexistent-validation-test")
                self.assertEqual(run.call_count, 1)
            self.assertEqual(list(destination.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
