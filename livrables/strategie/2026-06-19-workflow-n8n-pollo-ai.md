# Workflow n8n - Pollo AI Video Generation pour Majdi Corail
**Date : 19 juin 2026**
**VPS : srv1470204.hstgr.cloud**

---

## Etape 1 : Creer un compte Pollo AI et obtenir la cle API

1. Va sur **https://pollo.ai** et cree un compte (gratuit pour commencer)
2. Une fois connectee, va sur **https://pollo.ai/api-platform/keys**
3. Clique sur "Create API Key"
4. Copie la cle API (elle commence par `pk_...` ou similaire)
5. Garde-la en securite, ne la partage jamais

### Prix API Pollo AI
- Essai gratuit : quelques credits offerts
- Les credits varient selon le modele utilise (Pollo 1.6 est le moins cher)
- Modeles disponibles : Pollo 1.6, Kling 3.0, Veo 3, Runway, et 300+ autres

---

## Etape 2 : Creer le workflow n8n

### Vue du workflow
```
[Webhook/Manual Trigger] -> [HTTP Request: Generer Video] -> [Wait 30s] -> [HTTP Request: Verifier Status] -> [IF: Status = succeed?] -> [OUI: HTTP Request: Telecharger] -> [Google Drive: Sauvegarder]
                                                                                                               -> [NON: Wait 30s] -> (retour a Verifier Status)
```

### Node 1 : Trigger (Manual ou Webhook)
- Type : **Manual Trigger** (pour tester) ou **Webhook** (pour automatiser)
- Si Webhook : Claude enverra les scripts directement a n8n

### Node 2 : HTTP Request - Generer la video
- **Methode** : POST
- **URL** : `https://pollo.ai/api/platform/generation/pollo/pollo-v1-6`
- **Headers** :
  - `Content-Type` : `application/json`
  - `x-api-key` : `{{ $env.POLLO_API_KEY }}` (ou colle ta cle directement)
- **Body (JSON)** :
```json
{
  "input": {
    "prompt": "Elegant red coral necklace from Mediterranean sea, luxury close-up shot, warm golden light, dark velvet background, cinematic quality, shallow depth of field, rich red tones, 9:16 vertical format",
    "resolution": "720p",
    "mode": "basic",
    "length": 5
  }
}
```

### Node 3 : Wait
- **Duree** : 30 secondes
- Raison : la generation prend du temps

### Node 4 : HTTP Request - Verifier le statut
- **Methode** : GET
- **URL** : `https://pollo.ai/api/platform/generation/task/{{ $node['Node 2'].json.data.task_id }}`
- **Headers** :
  - `x-api-key` : `{{ $env.POLLO_API_KEY }}`

### Node 5 : IF (condition)
- **Condition** : `{{ $json.data.status }}` est egal a `succeed`
- Si OUI : passer au telechargement
- Si NON : retourner au Node 3 (Wait) pour re-verifier

### Node 6 : HTTP Request - Telecharger la video
- **Methode** : GET
- **URL** : `{{ $json.data.output.video_url }}`
- **Options** : Reponse en binaire (fichier)

### Node 7 : Google Drive - Sauvegarder
- **Action** : Upload File
- **Dossier** : "Majdi Corail Videos"
- **Nom du fichier** : `reel-{{ $now.format('yyyy-MM-dd-HHmm') }}.mp4`

---

## Etape 3 : Configurer la cle API dans n8n

1. Connecte-toi a ton n8n : `https://n8n.srv1470204.hstgr.cloud` (ou ton URL n8n)
2. Va dans **Settings** > **Variables** (ou dans le node directement)
3. Ajoute une variable d'environnement :
   - Nom : `POLLO_API_KEY`
   - Valeur : ta cle API Pollo

---

## Etape 4 : Prompts video optimises pour Majdi Corail

### Prompt 1 : Collier en gros plan (produit luxe)
```
Cinematic close-up of a stunning red coral necklace on dark velvet, warm golden hour lighting from the side, shallow depth of field, each coral bead glistening with natural red tones, Mediterranean luxury feel, slow camera movement revealing the details, 9:16 vertical format, photorealistic, no text, no watermark
```

### Prompt 2 : Branches de corail brut (authenticite)
```
Raw red coral branches freshly harvested from the Mediterranean sea, placed on a rustic wooden table, water droplets on the surface, warm natural light, close-up macro shot revealing the intricate natural patterns, artisanal workshop atmosphere, 9:16 vertical format, photorealistic, no text
```

### Prompt 3 : Transformation brut vers bijou (storytelling)
```
Smooth transition from raw red coral branch to polished coral jewelry, split screen or morphing effect, artisan hands polishing coral in warm workshop light, Mediterranean workshop setting, golden warm tones, luxury artisanal feel, 9:16 vertical format, cinematic quality
```

### Prompt 4 : Bijou porte sur peau (emotion)
```
Elegant woman wearing a red coral necklace, close-up on neck and collarbone, warm golden sunset light, Mediterranean sea blurred in background, wind gently moving hair, intimate and luxurious mood, natural skin texture, shallow depth of field, 9:16 vertical, no text
```

### Prompt 5 : Plongee sous-marine (origine)
```
Underwater shot of red coral growing on Mediterranean sea rocks, crystal clear turquoise water, sunlight rays penetrating from above, small fish swimming around the coral, natural documentary style, slow motion, dreamy atmosphere, 9:16 vertical, cinematic
```

### Prompt 6 : Atelier artisanal (savoir-faire)
```
Artisan hands carefully polishing a red coral bead in a traditional Mediterranean workshop, warm interior lighting, tools and raw coral visible in background, extreme close-up on the craftsmanship, dust particles in the light, intimate documentary feel, 9:16 vertical
```

---

## Etape 5 : Workflow avance (automatisation complete)

### Version automatisee : Claude -> n8n -> Pollo -> Google Drive -> Instagram

```
[Webhook n8n] -> [Set: prompt + legende] -> [Pollo AI: generer video] -> [Wait + Poll] -> [Google Drive: upload] -> [Meta Business Suite: notification email]
```

Pour declencher depuis Claude :
- Claude prepare le script (Lina) et le prompt visuel (Mia)
- Claude envoie une requete au webhook n8n avec le prompt et la legende
- n8n genere la video via Pollo AI
- n8n sauvegarde sur Google Drive
- Tu recois un email quand la video est prete
- Tu publies via Meta Business Suite

---

## Modeles Pollo AI recommandes pour Majdi Corail

| Modele | Ideal pour | Prix relatif |
|--------|-----------|-------------|
| **Pollo 1.6** | Videos courtes produit, rapide et economique | Bas |
| **Kling 3.0** | Mouvements realistes, gros plans bijoux | Moyen |
| **Veo 3** | Qualite cinematique maximale, videos premium | Eleve |
| **Runway Gen-4** | Effets creatifs, transitions, transformations | Moyen |

### Recommandation
Commence avec **Pollo 1.6** (le moins cher) pour tester. Si la qualite te convient, reste dessus. Sinon, passe a **Kling 3.0** pour les gros plans bijoux.

---

## Resume des actions

1. Creer un compte sur pollo.ai
2. Obtenir la cle API
3. Ouvrir n8n sur ton VPS
4. Creer le workflow avec les nodes ci-dessus
5. Tester avec le Prompt 1 (collier luxe)
6. Verifier la video generee
7. Si OK, automatiser la publication
