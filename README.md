# SiLeMI/O Control Library

Bibliothèque déclarative versionnée pour [SiLeMI/O Control Hub](https://github.com/Mamat79/SiLeMIO-Control-Hub).

Le dépôt est **privé pendant le développement**. Il pourra être rendu public séparément du code de l'application lorsque le format, la neutralisation et le processus de contribution auront été validés.

## Contenu

```text
manifest-v1.json
schemas/
controllers/<fabricant>/<modèle>/<version>/profile.json
plugin-profiles/<fabricant>/<plug-in>/<version>/profile.json
```

- `builtin` : profil livré avec le Hub ;
- `verified` : profil testé selon une procédure reproductible ;
- `community` : profil structurellement valide, sans promesse de test matériel.

Les profils de plug-ins partagés utilisent la couche `suggested`. La couche `user` reste locale et prioritaire dans le Hub.

## Contribution

1. créer une branche ;
2. ajouter un nouveau dossier de version, sans remplacer une version existante ;
3. lancer `python scripts/update_manifest.py` ;
4. lancer `python scripts/validate_library.py` ;
5. ouvrir une pull request avec le matériel et la procédure de test réellement utilisés.

Le Hub télécharge uniquement le manifeste et les JSON qu'il référence. Les scripts de ce dépôt servent à la maintenance et ne sont jamais téléchargés ni exécutés par l'application.
