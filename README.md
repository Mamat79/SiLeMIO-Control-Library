# SiLeMI/O Control Library

Bibliothèque déclarative et versionnée historique pour [Controller Studio for LiveProfessor](https://github.com/Mamat79/Controller-Studio-for-LiveProfessor).

## Référence active et compatibilité

Controller Studio 2026.6 utilise par défaut la [banque intégrée au dépôt Controller Studio](https://github.com/Mamat79/Controller-Studio-for-LiveProfessor/tree/main/library), sur la branche `main`, dans le sous-dossier `library`. Cette banque est la référence pour les mises à jour et les nouvelles contributions. Les valeurs par défaut sont définies dans `src/silemio_control_hub/library_remote.py` du dépôt Controller Studio.

Ce dépôt dédié est conservé pour l'historique et la compatibilité avec les usages qui le référencent explicitement. Il ne constitue pas une seconde source active de mises à jour. Ses versions, chemins et empreintes existants restent conservés ; aucun transfert ni remplacement automatique de catalogue n'est prévu.

Repère vérifié le 10 octobre 2026, au commit Controller Studio `4a62ad2a7e0dd7ff8c73aaf4e840a97e11042948` : la banque intégrée contient 33 contrôleurs (31 `community`, 1 `verified`, 1 `builtin`). Ce dépôt dédié contient 2 contrôleurs et 1 profil de plug-in exemple. Ces nombres décrivent ce repère et ne promettent pas la validation matérielle des profils communautaires.

Les profils sont uniquement des fichiers JSON déclaratifs : aucun code téléchargé n'est exécuté par l'application.

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

Les nouveaux contrôleurs et profils de plug-ins se proposent par pull request dans le [dépôt Controller Studio](https://github.com/Mamat79/Controller-Studio-for-LiveProfessor), sous `library/`, en suivant ses consignes et sa validation. Ne pas ajouter la même contribution aux deux catalogues.

Une correction de compatibilité propre à ce dépôt historique passe également par pull request. Préserver chaque version existante ; si une nouvelle version de compatibilité est nécessaire, créer son dossier distinct et mettre à jour le manifeste selon les consignes de maintenance. Ne pas régénérer les empreintes pour masquer un fichier altéré ou une conversion CRLF. Documenter le matériel et la procédure réellement utilisés : le statut `verified` exige une recette reproductible, et une simple validation JSON ne constitue pas une recette matérielle.

## Validation locale et Windows

Prérequis : Git, Python 3.11 ou supérieur et les dépendances de `requirements-validation.txt`. Depuis la racine de ce dépôt, installer les dépendances si elles ne sont pas déjà disponibles :

```powershell
python -m pip install -r requirements-validation.txt
```

Pour valider une version enregistrée dans Git, y compris sur Windows :

```powershell
python -B scripts/validate_git.py --ref HEAD
python -B -m unittest discover -s tests -v
```

`validate_git.py` résout la référence en SHA exact, exporte les octets du commit avec `git archive` dans un dossier temporaire, puis exécute les contrôles d'empreintes et de schémas de cette version. L'export évite la conversion LF/CRLF du checkout Windows. Le script affiche le SHA contrôlé, ne modifie pas le dépôt et ne valide pas les changements non commités. Un SHA exact peut remplacer `HEAD` pour une passation.

Pour contrôler des fichiers locaux ou téléchargés sur leurs octets exacts :

```powershell
python -B scripts/validate_library.py
python -B scripts/validate_schemas.py
```

Le contrôle d'empreintes reste strict. Un profil converti en CRLF ou modifié doit échouer si ses octets ne correspondent plus au manifeste. Un résultat réussi sur l'export Git ne qualifie pas les fichiers différents du checkout ou d'un téléchargement. Pour préparer une modification, utiliser une copie de travail avec les fins de ligne LF prescrites par `.gitattributes`, puis contrôler les octets qui seront réellement distribués. Ne jamais normaliser un téléchargement avant son contrôle SHA-256.

Controller Studio télécharge uniquement le manifeste et les JSON qu'il référence dans la banque sélectionnée. Les scripts de ce dépôt servent à sa maintenance et ne sont jamais téléchargés ni exécutés par l'application.
