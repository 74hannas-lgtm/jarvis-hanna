# /commit

> Sauvegarde l'état actuel du workspace avec Git.

---

## Mission

Quand je lance `/commit`, exécute la séquence suivante :

### Étape 1 : Initialiser Git si nécessaire

Vérifie si le dossier est déjà un dépôt Git :
- S'il ne l'est pas, lance `git init` et crée un fichier `.gitignore` adapté (voir contenu ci-dessous)
- S'il l'est déjà, passe à l'étape suivante

Contenu du `.gitignore` à créer si absent :
```
secrets/keys.env
.env
*.env
!*.env.example
.DS_Store
```

### Étape 2 : Voir ce qui a changé

Lance `git status` et `git diff --stat` pour identifier les fichiers modifiés ou nouveaux.

Présente-moi un résumé court de ce qui va être committé :
- Nouveaux fichiers
- Fichiers modifiés
- Fichiers supprimés

### Étape 3 : Demander un message de commit

Propose-moi un message de commit court et descriptif basé sur les changements détectés. Format :

```
[type] : description courte

Exemples :
- contenu : ajout script TikTok corail rouge
- boutique : fiche produit bracelet été
- strategie : plan 30 jours TikTok
- config : mise à jour CLAUDE.md
- maya : script présentation Maya
```

Demande-moi de confirmer ou modifier le message avant de committer.

### Étape 4 : Committer

Une fois le message validé :
1. `git add -A` (tout sauf ce qui est dans `.gitignore`)
2. `git commit -m "[message validé]"`
3. Confirme que le commit a réussi avec le hash court

---

## Règles importantes

- Ne jamais committer `secrets/keys.env` ni aucun fichier contenant de vraies clés
- Si un fichier suspect est détecté (contenant des clés, tokens, mots de passe), bloquer et me prévenir
- Toujours demander confirmation avant de committer
- Répondre en français
