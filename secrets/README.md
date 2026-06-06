# Secrets & Clés d'API

Ce dossier contient tes clés d'API et secrets. **Ne partage jamais ce dossier.**

## Comment ça marche

Tes vraies clés sont dans `keys.env` (ce fichier n'existe pas encore, tu dois le créer à partir du modèle ci-dessous).
Le fichier `keys.env.example` est un modèle vide, sans vraies valeurs.

Pour créer ton fichier de clés :
1. Copie `keys.env.example` en `keys.env`
2. Remplis les valeurs réelles
3. Ne partage jamais `keys.env`

## Utilisation avec Claude

Quand tu as besoin qu'une intégration fonctionne, dis à Claude :
> "Ma clé API Shopify est dans secrets/keys.env"

Claude peut lire le fichier pour utiliser la clé dans la session, sans que tu aies à la recopier dans le chat.
