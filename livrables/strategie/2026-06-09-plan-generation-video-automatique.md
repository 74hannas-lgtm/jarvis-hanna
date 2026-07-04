# Plan : Génération vidéo automatique pour Majdi Corail
# Date : 9 juin 2026
# Objectif : Automatiser la création de Reels TikTok/Instagram avec Maya

## Outils à tester (versions gratuites)

### 1. HeyGen - Avatar vidéo Maya
- Site : heygen.com
- Essai gratuit : 1 crédit (1 vidéo de test)
- Ce qu'il fait : tu uploades une photo de Maya, tu lui donnes un script, il génère une vidéo où Maya parle
- Connexion : Zapier + n8n

### 2. ElevenLabs - Voix off IA
- Site : elevenlabs.io
- Plan gratuit : 10 000 caractères/mois
- Ce qu'il fait : génère une voix off réaliste en français à partir du texte
- Connexion : Zapier + n8n

### 3. Creatomate - Montage vidéo automatique
- Site : creatomate.com
- Essai gratuit : 5 vidéos
- Ce qu'il fait : assemble des templates vidéo avec tes images, textes et audio automatiquement
- Connexion : n8n (API)

## Workflow cible

```
Lina (script) → ElevenLabs (voix) → HeyGen (avatar Maya) → Creatomate (montage) → Google Drive (stockage)
```

Tout automatisé via Zapier (tests rapides) et n8n (production).

## Étapes à suivre

1. Créer un compte gratuit sur heygen.com
2. Créer un compte gratuit sur elevenlabs.io
3. Créer un compte gratuit sur creatomate.com
4. Tester une vidéo complète avec Maya
5. Si la qualité est bonne, passer aux abonnements payants

## Budget estimé (après essais gratuits)

| Outil | Prix/mois | Inclus |
|-------|-----------|--------|
| HeyGen Creator | ~24$ | 15 vidéos/mois |
| ElevenLabs Starter | ~5$ | 30 000 caractères |
| Creatomate Starter | ~9$ | 50 vidéos/mois |
| **Total** | **~38$/mois** | Production complète |

## Alternative économique

| Outil | Prix/mois | Inclus |
|-------|-----------|--------|
| D-ID Lite | ~5.90$ | 5 min de vidéo |
| ElevenLabs Free | 0$ | 10 000 caractères |
| **Total** | **~6$/mois** | Production limitée |
