# SiLeMI/O Control Library

Bibliothèque déclarative et versionnée pour [Controller Studio for LiveProfessor](https://github.com/Mamat79/EC4-LiveProfessor-Bridge).

Le dépôt est public afin que Controller Studio puisse télécharger facilement les profils et que chacun puisse proposer un contrôleur ou un profil de plug-in. Les profils sont uniquement des fichiers JSON déclaratifs : aucun code téléchargé n'est exécuté par l'application.

## Contenu

```text
manifest-v1.json
schemas/
controllers/<fabricant>/<modèle>/<version>/profile.json
plugin-profiles/<fabricant>/<plug-in>/<version>/profile.json
```

- `builtin` : profil livré avec Controller Studio ;
- `verified` : profil testé selon une procédure reproductible ;
- `community` : profil structurellement valide, sans promesse de test matériel.

Les profils de plug-ins partagés utilisent la couche `suggested`. La couche `user` reste locale et prioritaire dans Controller Studio.

## Contribution

1. créer une branche ;
2. ajouter un nouveau dossier de version, sans remplacer une version existante ;
3. lancer `python scripts/update_manifest.py` ;
4. installer `requirements-validation.txt`, puis lancer `python scripts/validate_library.py` et `python scripts/validate_schemas.py` ;
5. ouvrir une pull request avec le matériel et la procédure de test réellement utilisés.

Controller Studio télécharge uniquement le manifeste et les JSON qu'il référence. Les scripts de ce dépôt servent à la maintenance et ne sont jamais téléchargés ni exécutés par l'application.
