# Workspace History

> Journal chronologique de toutes les sessions et décisions importantes.
> Le plus récent en haut. Mis à jour automatiquement par Claude.
>
> **Comment ça marche :** Quand je lance la commande `/update` après une session importante, ou quand je raconte un changement significatif, Claude ajoute une entrée ici automatiquement. Je n'ai pas à écrire ce fichier manuellement.

---

## 2026-06-09

### Création contenu Reel + plan vidéo automatique

- Script Reel "Le corail rouge est plus rare que le diamant" créé par Lina, prompts visuels par Mia
- 5 slides Canva générées pour chaque plan du Reel (HOOK, HISTOIRE, TRANSFORMATION, PRODUIT, CTA)
- Design Canva ajouté au compte Hanna (Mediterranean Luxury Story Slide)
- Photos bijoux corail retrouvées sur Google Drive (colliers, boucles d'oreilles, parure)
- Vidéo originale Majdi Corail sauvegardée en MP4
- Plan stratégique de génération vidéo automatique établi :
  - Outils identifiés : HeyGen (avatar Maya), ElevenLabs (voix off), Creatomate (montage)
  - Méthode : Zapier + n8n combinés
  - Budget : test gratuit d'abord, puis ~38$/mois pour la production complète
  - Workflow cible : Lina > ElevenLabs > HeyGen > Creatomate > Google Drive

---

## 2026-06-08

### Connexion n8n + Claude API + intégration des agents Notion

- n8n réparé sur le VPS Hostinger (srv1470204.hstgr.cloud, KVM 2, Ubuntu 24.04)
- Problèmes résolus : Docker DNS cassé (fix via daemon.json avec Google DNS 8.8.8.8), réseau Docker recréé, conteneurs Traefik + n8n redémarrés
- Connexion API Anthropic configurée dans n8n (clé API via en-têtes HTTP)
- Premier workflow "Majdi Corail" opérationnel : génère des captions TikTok/Instagram via Claude Sonnet
- Compte API Anthropic créé avec 5$ de crédits
- 3 agents IA récupérés depuis Notion (créés le 5 juin) et intégrés comme commandes Claude Code :
  - /lina : contenu (légendes, hashtags, scripts Reels, calendrier éditorial)
  - /mia : visuels (prompts d'images pour Canva/générateurs)
  - /sami : e-commerce (fiches produits Shopify, SEO, FAQ)
- Hanna comprend maintenant la différence entre Claude Code (interactif) et n8n (automatisation sans intervention)

---

## 2026-06-06

### Installation initiale du Jarvis

- Workspace personnalisé pour Hanna, basée à Annemasse (France)
- Profil principal : Employée (aide-soignante à Genève) + créatrice de contenu entrepreneuriale
- Activité : Développement de la marque Majdi Corail (bijoux de corail) sur TikTok et Instagram, avec un avatar IA "Maya" créé le 5 juin 2026
- Objectifs court terme identifiés : 10 000 abonnés TikTok, lancement boutique Shopify, publication régulière avec Maya
- Vision long terme : Vivre de sa boutique et de son contenu, quitter le travail d'aide-soignante
- Projets actifs au démarrage : Planning de contenu quotidien, boutique Shopify bijoux de corail, développement de Maya, projet boutique skincare
- Domaine d'aide prioritaire : Stratégie réseaux sociaux, croissance abonnés et création de contenu
- Style de communication choisi : Détaillé et pédagogique avec exemples concrets
