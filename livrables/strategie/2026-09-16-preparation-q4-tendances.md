# Préparation Q4 2026 : connexion TrendTrack + tendances produits

> Créé le 16 septembre 2026
> Contexte : Hanna reprend sa formation e-commerce pour préparer le Q4

---

## 1. Connecter TrendTrack à Claude

TrendTrack a ouvert son API et son serveur MCP. Ça veut dire que je peux interroger leur base directement dans la conversation (produits qui scalent, pubs gagnantes, boutiques en croissance), au lieu que tu fasses des captures d'écran de leur dashboard.

### Ce que je ne peux pas faire moi-même

La connexion passe par OAuth : c'est toi qui dois te connecter à ton compte TrendTrack et autoriser Claude. Je ne peux pas le faire à ta place depuis cette session, et je ne dois jamais te demander tes identifiants.

### Prérequis

- Un abonnement TrendTrack actif (la base est chez eux, le MCP ne donne pas accès gratuitement)
- Un plan Claude Pro ou supérieur (les connecteurs personnalisés sont réservés à ces plans)

### Étapes (à faire sur claude.ai, pas ici)

1. Ouvre **claude.ai** dans ton navigateur, connecte-toi
2. Va dans **Paramètres** (ton avatar en bas à gauche) puis **Connecteurs**
3. Clique sur **Ajouter un connecteur personnalisé**
4. Dans le champ URL, colle : `https://api.trendtrack.io/v1/mcp`
5. Valide. Claude ouvre une fenêtre TrendTrack : connecte-toi avec ton compte et **autorise l'accès**
6. Reviens dans une conversation, vérifie que "TrendTrack" apparaît bien dans la liste des connecteurs activés

Si TrendTrack te demande une clé plutôt qu'un login, elle se trouve dans ton compte TrendTrack sous **API Access → MCP Integration**. Ne me la colle pas dans le chat : range-la dans `secrets/keys.env`.

### Une fois connecté, ce qu'on pourra faire ensemble

- Sortir les produits en explosion sur les 7 / 14 / 30 derniers jours
- Voir les pubs qui tournent en ce moment sur une niche et les hooks qui convertissent
- Repérer les boutiques Shopify qui scalent avant tout le monde
- Croiser tout ça avec ton positionnement et te sortir un plan de contenu

### Point de vigilance

L'info sur le connecteur vient de la doc TrendTrack et de leurs annonces publiques, je n'ai pas pu ouvrir leur site depuis cette session (bloqué par le proxy réseau). Si l'URL ne fonctionne pas, vérifie directement dans ton compte TrendTrack, section API / MCP.

---

## 2. Le calendrier Q4 2026

| Temps fort | Date | Quand lancer |
|---|---|---|
| Halloween | 31 octobre 2026 | Contenu dès début octobre, ventes du 10 au 28 octobre |
| Black Friday | **27 novembre 2026** | Audiences chaudes construites dès début novembre |
| Cyber Monday | 30 novembre 2026 | Enchaîne directement, même stock |
| Noël | 25 décembre 2026 | Pic d'achat du 1er au 15 décembre (limite livraison) |
| Ramadan | vers début février 2027 | Hors Q4, mais préparation en décembre / janvier |

**Deux choses à retenir :**

1. Presque la moitié des consommateurs commencent leurs achats de Noël avant fin octobre. Ton contenu doit être en place début octobre, pas mi-novembre.
2. Le coût de la publicité augmente de 40 à 80 % en novembre. Si tu comptes faire de la pub payante, il faut une marge qui encaisse ça. Si tu restes en organique TikTok / Instagram, c'est justement ton avantage ce trimestre.

**Sur le Ramadan :** il tombe en février 2027, donc ce n'est pas du Q4. Mais c'est un temps fort réel pour les bijoux et les cadeaux, et la préparation (stock, contenu, visuels) se fait pendant le Q4. À traiter comme une campagne séparée.

---

## 3. Tendances produits Q4 2026 (vue marché générale)

Ces données viennent de recherches web publiques, pas de TrendTrack. C'est une base de travail, pas une liste de produits validés. La validation se fait avec les vrais chiffres de TrendTrack une fois connecté.

### Catégories qui montent le plus au Q4

- **Maison et cocooning** : plaids chauffants, guirlandes LED, bougies, diffuseurs
- **Cadeaux personnalisés** : colliers avec prénom, boîtes souvenirs, photo-cadeaux
- **Tech et gadgets** : accessoires de bureau, lampes de lecture, chauffe-mains rechargeables
- **Beauté et soin personnel** : appareils de massage compacts, skincare (à noter vu ton projet boutique skincare)
- **Animaux** : croissance à trois chiffres avec une concurrence encore faible
- **Cuisine** : mousseurs à lait, petits appareils

### Ce qui est directement pertinent pour toi

Si on reste sur l'axe bijoux :

- **Le bijou personnalisé est la catégorie cadeau numéro un du Q4.** "Cadeaux de Noël personnalisés" est un des termes les plus recherchés du trimestre. Si tu peux proposer une gravure, une carte personnalisée ou un message, tu entres directement dans cette demande.
- **Les cadeaux "souvenir" résistent mieux que les gadgets** quand le pouvoir d'achat est tendu. Un bijou en corail authentique coche cette case bien mieux qu'un produit dropshipping jetable. C'est ton vrai angle pour le Q4.
- **Le packaging cadeau et le rangement à bijoux** sont des produits complémentaires à faible coût qui augmentent le panier moyen : écrin, pochette de voyage, boîte à bijoux.
- **Halloween n'est pas ton temps fort.** Le corail rouge ne colle pas naturellement à cette saisonnalité. Mieux vaut concentrer l'énergie sur Black Friday et Noël, où ton produit est légitime.

---

## 4. Ce qu'il me faut de ta part

1. **Ce Q4, tu le prépares pour Majdi Corail, ou tu lances une activité dropshipping à côté ?** La stratégie n'est pas du tout la même. Une marque de bijoux artisanaux et une boutique de produits gagnants génériques ne se travaillent pas pareil, et ta crédibilité sur le corail est un actif qu'il ne faut pas diluer.
2. **Quelle formation tu reprends ?** Si je sais ce qu'elle t'enseigne, je peux t'aider à appliquer sa méthode plutôt que d'en superposer une deuxième.
3. **Ton abonnement TrendTrack est actif ?** Si oui, on peut connecter et sortir des vrais chiffres. Si non, on choisit une autre approche, il existe des méthodes gratuites de recherche produit.

---

## Sources

- [Doc TrendTrack MCP](https://docs.trendtrack.io/connect/claude)
- [TrendTrack MCP feature](https://www.trendtrack.io/features/mcp)
- [Connecteurs personnalisés Claude](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp)
- [Q4 Dropshipping 2026](https://easync.io/articles/q4-dropshipping-2026/)
- [Best Q4 Dropshipping Products 2026 (AutoDS)](https://www.autods.com/blog/q4-dropshipping-products/)
- [Christmas Market Insight 2026](https://printway.io/en/blogs/christmas-market-insight-2026)
- [Etsy Trends 2026](https://www.sellerapp.com/blog/etsy-trends/)
