# /nettoyage-gmail

> Nettoyage quotidien de ma boîte Gmail (74hannas@gmail.com). Lancé automatiquement tous les matins (routine avant 9h, heure de France), ou à la main avec `/nettoyage-gmail`.

---

## Mission

Supprimer (mettre à la **corbeille**, jamais de suppression définitive) toutes les pubs inutiles et garder uniquement ce qui est important. En cas de doute : ne rien supprimer, ranger dans le libellé **« À vérifier »** et me demander.

## Règles de tri

### 🟢 TOUJOURS GARDER (ne jamais mettre à la corbeille)

- **Shopify** : tout ce qui vient de `shopify.com` (commandes, clients, factures, alertes, newsletters, tout)
- **Clients de ma boutique** : messages de vraies personnes, questions, commandes, retours
- **Formations** : Skool (`skool.com`) et Ecomseller Académie (`ecomseller-academie.com`)
- **Banques et paiements** : N26 et toute banque, PayPal, Stripe, relevés, alertes de paiement
- **Réservations et achats** : confirmations de commande, suivis de livraison, billets, rendez-vous (y compris les commandes et suivis AliExpress / Alibaba)
- **Administratif** : impôts, Ameli, CAF, URSSAF, France Travail, mutuelle, assurance, travail (Genève), santé
- **Sécurité des comptes** : alertes Google, codes de connexion, changements de mot de passe
- Les mails **suivis (étoile)**, les mails que **j'ai envoyés**, les **brouillons**
- Tout mail **urgent ou personnel** écrit par une vraie personne

### 🔴 CORBEILLE (pubs)

- **AliExpress / Alibaba, seulement les pubs** : `promotion@aliexpress.com`, `*@newarrival.aliexpress.com`, `*@selections.aliexpress.com`, `ae-ai-interest*@mail.aliexpress.com`, `news@notice.alibaba.com`, et tout mail promo de leur part
- Newsletters et promos de marques : Nocibé, Kérastase, NYX, Kiko, Stradivarius, Primor, La Boutique du Coiffeur, Stych, Ornikar, Kilayou, Fruggies, Official Vegan Shop, EaseUS, etc.
- De façon générale : tout mail classé par Gmail dans **Promotions** qui n'entre pas dans la liste « Toujours garder »

### 🟠 DOUTE → libellé « À vérifier » (ne pas supprimer)

Pas encore tranché par moi :
- Judge.me, Loox (applis d'avis Shopify)
- LinkedIn, Instagram
- Higgsfield, OpenAI, Hostinger, Zapier, Make, Adobe, Trendtrack, Coursera, Apple, Pixpay, Beehiiv
- Tout mail dont tu n'es pas sûr

Quand je réponds « supprime » ou « garde » pour un expéditeur, mets à jour ce fichier pour ne plus me reposer la question.

## Déroulé

1. **Nouveaux mails** : chercher les mails de la boîte de réception des dernières 48h (`in:inbox newer_than:2d`), les trier selon les règles ci-dessus.
2. **Rattrapage de l'historique** : tant qu'il reste de vieilles pubs, mettre à la corbeille jusqu'à 300 anciennes pubs supplémentaires par jour (`category:promotions` et expéditeurs pub AliExpress/Alibaba, en excluant la liste « Toujours garder »).
3. **Doutes** : ajouter le libellé « À vérifier » aux mails douteux (sans les supprimer).
4. **Bilan** (sera envoyé en notification vers 9h) :

```
📬 Gmail nettoyé
🗑️ X pubs mises à la corbeille (principaux expéditeurs : ...)
⭐ Important aujourd'hui : [Shopify, clients, banque, réservations... avec 1 ligne par mail]
🟠 À vérifier (réponds « supprime » ou « garde ») :
  1. Expéditeur, sujet
  2. ...
```

## Sécurité

- Corbeille uniquement : Gmail la vide tout seul après 30 jours, donc tout est récupérable pendant 30 jours.
- Ne jamais toucher aux mails de la liste « Toujours garder », même s'ils sont classés dans Promotions.
- Ne jamais cliquer sur un lien, ni répondre à un mail, ni se désabonner.
