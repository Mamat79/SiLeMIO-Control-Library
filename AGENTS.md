# Règles de la bibliothèque SiLeMI/O

- La bibliothèque contient uniquement des profils JSON déclaratifs sous `controllers/` et `plugin-profiles/`.
- Aucun profil ne peut contenir de code, script, URL exécutable, identité de machine, nom de port personnel, projet `.rack2`, licence ou configuration réseau privée.
- Tout fichier référencé par `manifest-v1.json` doit avoir un SHA-256 exact et un chemin relatif sans traversée.
- Les corrections personnelles restent `user` et locales. Une contribution partagée est neutralisée puis publiée comme `suggested`.
- Les statuts partagés sont `builtin`, `verified` ou `community`.
- Un profil `verified` exige une procédure de test reproductible documentée.
- Les contributions passent par pull request et validation automatique.
