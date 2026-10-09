"""Validate an exact Git revision without checkout newline conversion."""

from __future__ import annotations

import argparse
from io import BytesIO
from pathlib import Path
import subprocess
import sys
import tempfile
from zipfile import ZipFile


ROOT = Path(__file__).parents[1].resolve()


def export_revision(destination: Path, ref: str = "HEAD") -> str:
    """Export committed bytes only; never normalize profile content."""
    sha = subprocess.check_output(
        ["git", "rev-parse", "--verify", "--end-of-options", f"{ref}^{{commit}}"],
        cwd=ROOT,
        text=True,
    ).strip()
    archive = subprocess.check_output(
        ["git", "archive", "--format=zip", sha], cwd=ROOT
    )
    with ZipFile(BytesIO(archive)) as snapshot:
        snapshot.extractall(destination)
    return sha


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ref", default="HEAD", help="Git commit/reference (default: HEAD)")
    args = parser.parse_args()
    with tempfile.TemporaryDirectory(prefix="silemio-library-validation-") as folder:
        destination = Path(folder)
        sha = export_revision(destination, args.ref)
        print(f"Git snapshot: {sha} (committed bytes only)", flush=True)
        for script in ("validate_library.py", "validate_schemas.py"):
            subprocess.run(
                [sys.executable, "-B", str(destination / "scripts" / script)],
                cwd=destination,
                check=True,
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
