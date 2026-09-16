# Préparation Q4 2026 : connexion TrendTrack + tendances produits

> Créé le 16 septembre 2026
> Contexte : Hanna reprend sa formation e-commerce pour préparer le Q4

---

## 1. L'outil de recherche produit : TrackWinner

**Correction du 16 septembre :** l'outil de Hanna est **TrackWinner** (`trackwinner.io`), pas TrendTrack. Ce sont deux produits différents et la méthode de travail n'est pas la même.

### TrackWinner, ce que c'est

TrackWinner sélectionne des produits issus de différentes boutiques et les classe selon des signaux observables : publicités en cours, niveau de concurrence, avis, fournisseurs, risques et indice de confiance. Pour chaque produit, il fournit un plan de test : angle créatif, budget, CPA maximum, marge avant publicité et étapes de validation.

C'est un outil d'aide à la décision, pas une base de données brute. Il ne promet pas un produit gagnant, il réduit l'incertitude avant un test.

### Ce que je ne peux pas faire

**TrackWinner ne propose pas d'API ni de connecteur MCP publics.** Je ne peux donc pas interroger leur base directement depuis la conversation, et leur site est en plus bloqué par le proxy réseau de cette session. Il n'y a pas de connexion automatique à mettre en place.

À ne pas confondre : TrendTrack (`trendtrack.io`) est un autre outil, lui a un connecteur MCP. Si un jour tu bascules dessus, la connexion se fait sur claude.ai via **Paramètres → Connecteurs → Ajouter un connecteur personnalisé**, avec l'URL `https://api.trendtrack.io/v1/mcp`.

### La méthode de travail avec TrackWinner

Le transfert se fait par toi, et ça fonctionne très bien :

1. Tu lances tes recherches dans TrackWinner avec ton mois gratuit
2. Tu récupères les rapports produits : export CSV ou PDF si l'outil le propose, sinon copier-coller du texte, sinon captures d'écran
3. Tu déposes les fichiers dans `context/import/`
4. Je les analyse, je recalcule les marges, je croise avec les tendances du marché, et je te dis lesquels tiennent la route

**Ce que je veux voir pour chaque produit :** le nom, le prix de vente pratiqué par les concurrents, le prix d'achat fournisseur, le nombre de publicités actives, la date de première détection, et le niveau de concurrence.

Ne me colle jamais tes identifiants TrackWinner. Si l'outil te donne une clé d'API un jour, elle va dans `secrets/keys.env`.

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
