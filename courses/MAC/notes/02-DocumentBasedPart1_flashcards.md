---
course: "MAC"
generated_at: "2025-09-18T07:51:24"
source_pdf: "courses/MAC/data/pdf/02-DocumentBasedPart1.pdf"
---

# Flashcards – MAC

---
### Résumé essentiel

Les bases de données orientées documents, telles que MongoDB et Couchbase, stockent des données au format natif (ex. : JSON), ce qui simplifie la recherche et la récupération sans conversion préalable. Contrairement aux bases de données relationnelles qui organisent les données en tables, ces bases regroupent toutes les informations d'un document en une seule instance, ce qui accélère le processus de chargement et de récupération. Elles offrent une flexibilité accrue, permettant des modifications de structure sans nécessiter de migrations complexes, et sont mieux adaptées au développement agile grâce à leur modèle intuitif. 

La modélisation des données dans ces bases nécessite des choix entre l'approche de séparation, qui utilise des clés étrangères pour maintenir des données normalisées, et l'approche d'imbrication, qui regroupe les données connexes dans un seul document. Chaque méthode présente des avantages et des inconvénients : l'imbrication favorise la rapidité d'accès et la tolérance aux pannes, tandis que la séparation assure la cohérence des données. Les règles empiriques de modélisation doivent prendre en compte la fréquence des lectures et des écritures pour choisir la structure appropriée.

Couchbase se distingue par son architecture distribuée et son langage de requête N1QL, similaire à SQL, facilitant l'interrogation des données. Les documents JSON permettent une structure flexible et hiérarchique, et il est crucial de comprendre les types simples et complexes pour manipuler efficacement les données. Les concepts de Collection et Scope dans Couchbase aident à organiser les documents, tandis que les valeurs se divisent en binaires et JSON, chacune ayant ses propres caractéristiques d'interrogation.

### À retenir absolument

- Les bases de données orientées documents stockent des données au format JSON, facilitant la recherche sans conversion.
- Elles regroupent toutes les informations d'un document, simplifiant le chargement et la récupération par rapport aux bases relationnelles.
- Deux approches de structuration existent : séparation (normalisée) et imbrication (dé-normalisée), chacune avec ses avantages.
- Couchbase utilise un langage de requête N1QL et permet une organisation flexible des documents via Collections et Scopes.
- Comprendre les types simples et complexes en JSON est essentiel pour une manipulation efficace des données.

---

<!-- QID:8da1ffe9051b -->
### Quel est un avantage des bases de données orientées documents par rapport aux bases de données relationnelles ?  <sup>p. 1–4</sup>

**Choix :**

- A) Elles utilisent des tables séparées pour chaque objet.
- B) Elles permettent de stocker toutes les informations d'un document dans une seule instance.
- C) Elles nécessitent un mappage complexe lors de la récupération des données.
- D) Elles sont toujours plus lentes que les bases de données relationnelles.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Cela simplifie le processus de chargement et de récupération des données, rendant les opérations plus rapides.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=1-4`

</details>

<!-- QID:931420ba3a2a -->
### Les bases de données orientées documents sont généralement plus lentes que les bases de données relationnelles.  <sup>p. 1–4</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Les bases de données orientées documents peuvent être plus rapides car elles stockent toutes les informations d'un document dans une seule instance, évitant ainsi des opérations de jointure complexes.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=1-4`

</details>

<!-- QID:ee606a644413 -->
### Les bases de données orientées documents permettent de stocker des données au format _____ plutôt que dans des tables séparées.  <sup>p. 1–4</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** natif (ex: JSON)

**Pourquoi :** Le stockage au format natif permet une manipulation plus directe et efficace des données.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=1-4`

</details>

<!-- QID:c78ebdf044f2 -->
### Citez deux systèmes de bases de données orientées documents.  <sup>p. 1–4</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** MongoDB et Couchbase.

**Pourquoi :** Ces systèmes sont des exemples populaires qui illustrent l'utilisation de bases de données orientées documents.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=1-4`

</details>

<!-- QID:054719048fbe -->
### Qu'est-ce qu'un schéma auto-descriptif dans les bases de données orientées documents ?  <sup>p. 5–10</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Un schéma auto-descriptif permet aux documents d'avoir des champs variés sans nécessiter de schéma prédéfini, rendant la structure dynamique et adaptable.

**Pourquoi :** Cela facilite les modifications de conception à tout moment sans perturber la structure globale.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=5-10`

</details>

<!-- QID:abad6e87004a -->
### Les bases de données orientées documents garantissent des transactions ACID comme les bases de données relationnelles.  <sup>p. 5–10</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** La gestion des transactions dans les bases de données orientées documents peut poser des défis, contrairement aux bases de données relationnelles qui garantissent des transactions ACID.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=5-10`

</details>

<!-- QID:503ad9f56a12 -->
### Dans Couchbase, le langage de requête s'appelle _____ et a une syntaxe proche de SQL.  <sup>p. 5–10</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** N1QL

**Pourquoi :** N1QL facilite l'interrogation des données en utilisant une syntaxe familière pour ceux qui connaissent SQL.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=5-10`

</details>

<!-- QID:ebde31dd970c -->
### Comment Couchbase gère-t-elle la distribution des documents ?  <sup>p. 5–10</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Couchbase traite chaque document comme une unité indépendante, permettant une répartition facile sur les serveurs tout en maintenant la localité des données.

**Pourquoi :** Cela améliore la disponibilité et permet d'isoler les charges de travail dans un cluster.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=5-10`

</details>

<!-- QID:147871507c79 -->
### Quel attribut peut-on utiliser dans Couchbase pour indiquer la catégorie des données ?  <sup>p. 5–10</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** On peut utiliser un attribut nommé 'type' ou '_type'.

**Pourquoi :** Cet attribut permet de regrouper les documents par catégorie, facilitant ainsi leur gestion.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=5-10`

</details>

<!-- QID:108f4d61d8d5 -->
### Qu'est-ce qu'un schéma dynamique dans le contexte des bases de données de documents?  <sup>p. 11–15</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Un schéma dynamique permet de représenter les données sous forme de paires attribut-valeur, offrant flexibilité et évolutivité sans nécessiter de mises à jour simultanées des autres documents.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=11-15`

</details>

<!-- QID:95692c7a2cbe -->
### Avec une base de données relationnelle, la seule approche de structuration est la ________.  <sup>p. 11–15</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** normalisation

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=11-15`

</details>

<!-- QID:9c28c83643f9 -->
### Quelle est l'approche qui consiste à maintenir des données normalisées dans des documents séparés?  <sup>p. 11–15</sup>

**Choix :**

- A) approche d'imbrication
- B) approche de séparation
- C) approche de fusion
- D) approche de duplication

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** L'approche de séparation permet de garder les données normalisées, ce qui est essentiel pour certaines applications nécessitant une intégrité référentielle.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=11-15`

</details>

<!-- QID:b21a080f9d0a -->
### L'approche d'imbrication nécessite que les clés étrangères soient présentes dans les documents imbriqués.  <sup>p. 11–15</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Dans l'approche d'imbrication, les données sont intégrées directement dans le document parent, éliminant ainsi le besoin de clés étrangères.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=11-15`

</details>

<!-- QID:f71ce82ee35e -->
### Quel compromis est fait lors du choix entre l'approche de séparation et l'approche d'imbrication?  <sup>p. 11–15</sup>

**Choix :**

- A) Sécurité et complexité
- B) Flexibilité et performances
- C) Coût et maintenance
- D) Simplicité et évolutivité

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Le choix entre les deux approches dépend des besoins spécifiques de l'application, notamment en termes de flexibilité et de performances.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=11-15`

</details>

<!-- QID:ce7904390e7d -->
### Pourquoi est-il important de considérer les impacts des choix de modélisation sur l'application cible?  <sup>p. 11–15</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Les choix de modélisation affectent la performance, la flexibilité et la maintenabilité de l'application, influençant ainsi son efficacité globale.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=11-15`

</details>

<!-- QID:0cc5e5d526df -->
### Quel énoncé est juste concernant l'approche d'imbrication et de séparation?  <sup>p. 16–20</sup>

**Choix :**

- A) Pour modéliser les relations M:N, l’approche d’imbrication est plus adaptée que l’approche de séparation.
- B) Pour modéliser les relations 1:N, l’approche de séparation est plus adaptée si les requêtes portent seulement sur des éléments parents ou enfants mais pas les deux ensemble.
- C) Pour modéliser les relations 1:N, l’approche de séparation est adaptée si on interroge souvent les champs parents et enfants ensemble.
- D) Le choix de l’approche de séparation vs l’approche d’imbrication a un impact sur le stockage des données mais pas sur la rapidité des recherches.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Cet énoncé est correct car il reflète la situation où l'approche de séparation est plus efficace pour des requêtes ciblées sur des éléments spécifiques.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=16-20`

</details>

<!-- QID:c403c4fb9f6d -->
### Quels sont les avantages de l'imbrication?  <sup>p. 16–20</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Les avantages de l'imbrication incluent une vitesse d'accès améliorée, une tolérance aux pannes plus élevée lors de la lecture, et une simplification de l'application.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=16-20`

</details>

<!-- QID:888c42ceb116 -->
### Quels sont les désavantages de l'imbrication?  <sup>p. 16–20</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Les désavantages de l'imbrication comprennent l'incohérence des données, la complexité des requêtes, et la création de documents volumineux avec des données dupliquées.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=16-20`

</details>

<!-- QID:b8d3965b4e9c -->
### Quels sont les avantages de la séparation?  <sup>p. 16–20</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Les avantages de la séparation incluent la cohérence des données, des requêtes simplifiées, une meilleure utilisation du cache mémoire, et une utilisation plus efficace du matériel.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=16-20`

</details>

<!-- QID:d42cfe877290 -->
### Quels sont les désavantages de la séparation?  <sup>p. 16–20</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Les désavantages de la séparation incluent la nécessité de recherches multiples et de jointures, ainsi que la contrainte de cohérence qui peut ne pas être souhaitable dans tous les contextes.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=16-20`

</details>

<!-- QID:5c0b6afa7b1a -->
### L'imbrication des données garantit toujours la cohérence des informations.  <sup>p. 16–20</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** L'imbrication peut entraîner des problèmes d'incohérence en raison de la redondance des données, ce qui complique les mises à jour.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=16-20`

</details>

<!-- QID:29ddc2a15ff3 -->
### L'approche de séparation est plus adaptée pour les requêtes qui portent sur des éléments _____ ou _____ mais pas les deux ensemble.  <sup>p. 16–20</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** parents, enfants

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=16-20`

</details>

<!-- QID:4c597450ec88 -->
### Qu'est-ce qu'un bucket dans Couchbase ?  <sup>p. 21–26</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Un bucket est un conteneur qui regroupe des items, permettant de stocker des clés-valeurs.

**Pourquoi :** Les buckets facilitent l'organisation et la gestion des données dans Couchbase.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=21-26`

</details>

<!-- QID:fc6589d03b1a -->
### Quelle est la principale différence entre Couchbase et une base de données relationnelle ?  <sup>p. 21–26</sup>

**Choix :**

- A) Couchbase utilise des tables pour stocker des données.
- B) Couchbase utilise des items pour stocker des clés-valeurs.
- C) Couchbase ne permet pas le stockage de documents JSON.
- D) Couchbase nécessite des schémas rigides.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Couchbase est conçu pour être flexible et efficace avec des données non structurées, contrairement aux bases de données relationnelles.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=21-26`

</details>

<!-- QID:5a6a272c25ce -->
### Dans Couchbase, les _______ organisent les documents à l'intérieur d'un bucket.  <sup>p. 21–26</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** collections

**Pourquoi :** Les collections permettent de regrouper des documents similaires, facilitant leur gestion.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=21-26`

</details>

<!-- QID:1563cd3192f1 -->
### Les valeurs binaires dans Couchbase peuvent être analysées et indexées.  <sup>p. 21–26</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Les valeurs binaires ne peuvent pas être analysées, indexées ou interrogées, elles ne peuvent être récupérées que par clé.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=21-26`

</details>

<!-- QID:237dd476f6de -->
### Qu'est-ce qu'un scope dans Couchbase ?  <sup>p. 21–26</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Un scope est un mécanisme de regroupement de plusieurs collections dans un bucket.

**Pourquoi :** Les scopes permettent d'organiser les collections selon des critères tels que le type de contenu ou la phase de déploiement.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=21-26`

</details>

<!-- QID:624e0874ba67 -->
### Quel type de valeur permet une interrogation et une indexation dans Couchbase ?  <sup>p. 21–26</sup>

**Choix :**

- A) Binaire
- B) JSON
- C) Texte brut
- D) XML

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Les valeurs JSON fournissent une structure riche qui permet l'analyse et l'interrogation des données.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=21-26`

</details>

<!-- QID:027b648af332 -->
### Lors de la création d'un nouveau bucket, une nouvelle _______ et un nouveau _______ lui sont attribués.  <sup>p. 21–26</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** collection, scope

**Pourquoi :** Cela permet d'organiser les données de manière structurée dès le départ.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=21-26`

</details>

<!-- QID:6d74788bf7f5 -->
### Dans Couchbase, il est préférable d'utiliser une version imbriquée des données pour garantir la cohérence.  <sup>p. 21–26</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Une version imbriquée peut entraîner des incohérences, surtout si les lectures sont plus nombreuses que les écritures.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=21-26`

</details>

<!-- QID:7a94c8c4aa76 -->
### Quels types de données peuvent être représentés par les attributs d'un document JSON ?  <sup>p. 27–28</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Les attributs d'un document JSON peuvent représenter des types de base tels que les nombres, les chaînes de caractères, les booléens, ainsi que des types complexes comme les documents imbriqués et les tableaux intégrés.

**Pourquoi :** Cette diversité de types permet de modéliser des structures de données complexes de manière flexible.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=27-28`

</details>

<!-- QID:422bebcb0770 -->
### Dans un document JSON, un attribut peut être un tableau de documents imbriqués, comme dans l'exemple ci-dessous : { 'a4': [ { 'c1': 'simple', 'c2': 10 }, { 'c1': 'example', 'c3': 10 } ] }. Ici, 'a4' est un _____ de documents imbriqués.  <sup>p. 27–28</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** tableau

**Pourquoi :** Le terme 'tableau' est utilisé pour désigner une collection ordonnée d'éléments, qui dans ce cas sont des documents JSON.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=27-28`

</details>

<!-- QID:a6ab72c340cd -->
### Quel attribut dans l'exemple JSON représente un document imbriqué ?  <sup>p. 27–28</sup>

**Choix :**

- A) a1
- B) a2
- C) a3
- D) a4

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C

**Pourquoi :** L'attribut 'a3' contient un objet JSON, ce qui en fait un document imbriqué, contrairement aux autres attributs qui sont des types simples ou des tableaux.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=27-28`

</details>
