---
course: "MAC"
generated_at: "2025-09-17T14:13:16"
---

# Flashcards – MAC

> Astuce : cliquez pour dérouler la réponse.

<!-- QID:2bd8d4af8433 -->
### Qu'est-ce qu'une base de données orientée documents ?  <sup>p. 1–4</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Une base de données orientée documents est un système de stockage qui permet de stocker des données au format natif, comme JSON, sans avoir besoin de les organiser en tables séparées.

**Pourquoi :** Cette méthode facilite la recherche et la récupération des documents dans leur format d'origine.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=1-4`

</details>

<!-- QID:b4e0b11103fc -->
### Les bases de données orientées documents nécessitent un mappage lors du chargement des données.  <sup>p. 1–4</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Dans les bases de données orientées documents, toutes les informations pour un document peuvent être stockées dans une seule instance, ce qui élimine le besoin de mappage.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=1-4`

</details>

<!-- QID:c18ebdde0ed6 -->
### Quelles sont les principales différences entre les bases de données orientées documents et les bases de données relationnelles ?  <sup>p. 1–4</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Les bases de données relationnelles stockent les données dans des tables séparées, tandis que les bases de données orientées documents stockent toutes les informations d'un document dans une seule instance, ce qui simplifie la récupération des données.

**Pourquoi :** Cette différence structurelle impacte la performance et la flexibilité des systèmes de gestion de données.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=1-4`

</details>

<!-- QID:cf6e0ae6a05a -->
### Les stores de documents ont un schéma __________ et dynamique, adaptable au changement.  <sup>p. 5–10</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** auto-descriptif

**Pourquoi :** Le schéma auto-descriptif permet une flexibilité dans la structure des documents.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=5-10`

</details>

<!-- QID:466071c65e90 -->
### Les bases de données orientées documents garantissent des transactions ACID comme les bases de données relationnelles.  <sup>p. 5–10</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** La gestion des transactions peut poser des défis dans les bases de données orientées documents, contrairement aux bases relationnelles.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=5-10`

</details>

<!-- QID:5f8e96d77573 -->
### Qu'est-ce qui caractérise Couchbase par rapport à CouchDB ?  <sup>p. 5–10</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Couchbase est une fusion entre CouchDB et Membase, et elle offre une architecture distribuée pour garantir les performances, l'évolutivité et la disponibilité.

**Pourquoi :** Couchbase combine les fonctionnalités de CouchDB et Membase tout en améliorant les performances.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=5-10`

</details>

<!-- QID:1f0e285fa2a5 -->
### Quel attribut peut être utilisé pour indiquer la catégorie des données dans Couchbase ?  <sup>p. 5–10</sup>

**Choix :**

- A) A. type
- B) B. _type
- C) C. category
- D) D. dataType

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** L'attribut _type est spécifiquement mentionné pour indiquer la catégorie des données dans Couchbase.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=5-10`

</details>

<!-- QID:9c5f38ef1539 -->
### La structure d'un document consiste en son organisation interne des paires ________.  <sup>p. 11–15</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** attribut-valeur

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=11-15`

</details>

<!-- QID:7fbfe2885351 -->
### Quelle approche de structuration est unique aux bases de données relationnelles?  <sup>p. 11–15</sup>

**Choix :**

- A) Dénormalisation
- B) Normalisation
- C) Imbrication
- D) Séparation

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** La normalisation est la seule approche de structuration dans les bases de données relationnelles.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=11-15`

</details>

<!-- QID:d99f7d9dde86 -->
### L'approche d'imbrication nécessite que InvoiceId soit présent comme clé étrangère dans les objets de tableau Items.  <sup>p. 11–15</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=11-15`

</details>

<!-- QID:f50f45d9a7ba -->
### Quels sont les deux types d'approches de structuration dans les bases de données de documents?  <sup>p. 11–15</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Les deux approches sont l'approche de séparation et l'approche d'imbrication. L'approche de séparation maintient les données normalisées dans des documents séparés, tandis que l'approche d'imbrication dénormalise les données en les intégrant dans leur document parent.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=11-15`

</details>

<!-- QID:5a81329b4178 -->
### Quel est un compromis fait par les bases de données de documents?  <sup>p. 11–15</sup>

**Choix :**

- A) Sécurité
- B) Flexibilité
- C) Complexité
- D) Rigidité

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Les bases de données de documents sont conçues pour offrir flexibilité, évolutivité et performances.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=11-15`

</details>

<!-- QID:89dea1c36055 -->
### Pourquoi est-il important de considérer les impacts des choix de modélisation sur l'application cible?  <sup>p. 11–15</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Les choix de modélisation influencent la performance, la flexibilité et l'évolutivité de l'application. Chaque approche a ses avantages et inconvénients, et le choix doit être fait en fonction des besoins spécifiques de l'application.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=11-15`

</details>

<!-- QID:7d9603ca21f5 -->
### Quel énoncé est juste concernant l'approche de séparation pour modéliser les relations 1:N?  <sup>p. 16–20</sup>

**Choix :**

- A) A
- B) B
- C) C
- D) D

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Cet énoncé précise que l'approche de séparation est efficace lorsque les requêtes ne concernent qu'un type d'élément, ce qui est correct.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=16-20`

</details>

<!-- QID:9fba5931a328 -->
### L'approche d'imbrication permet d'améliorer la vitesse d'accès aux données.  <sup>p. 16–20</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Vrai

**Pourquoi :** L'imbrication permet d'intégrer toutes les données dans un seul document, ce qui réduit le besoin de jointures et améliore la vitesse d'accès.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=16-20`

</details>

<!-- QID:99a48535b878 -->
### L'imbrication des données garantit toujours la cohérence des informations.  <sup>p. 16–20</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** L'imbrication peut entraîner des incohérences en raison de la redondance des données, ce qui complique les mises à jour.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=16-20`

</details>

<!-- QID:3ecabd76a0b8 -->
### Quels sont les désavantages de l'approche d'imbrication?  <sup>p. 16–20</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Les désavantages incluent l'incohérence due à la redondance des données, la complexité des requêtes sur les parties imbriquées, et la création de documents volumineux.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=16-20`

</details>

<!-- QID:2fd3f03e997f -->
### Couchbase utilise des items pour stocker des clés-______.  <sup>p. 21–26</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** valeurs

**Pourquoi :** C'est une caractéristique fondamentale de Couchbase qui le distingue des bases de données relationnelles.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=21-26`

</details>

<!-- QID:7725f74a39b6 -->
### Quel est le rôle d'un Bucket dans Couchbase ?  <sup>p. 21–26</sup>

**Choix :**

- A) A. Stocker des clés uniquement
- B) B. Regrouper les items
- C) C. Organiser les collections
- D) D. Analyser les données

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Le Bucket est utilisé pour regrouper les items dans Couchbase.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=21-26`

</details>

<!-- QID:a10c94718e4a -->
### Les valeurs binaires dans Couchbase peuvent être analysées et indexées.  <sup>p. 21–26</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Les valeurs binaires ne peuvent pas être analysées, indexées ou interrogées.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=21-26`

</details>

<!-- QID:e73334c30647 -->
### Qu'est-ce qu'un Scope dans Couchbase et comment est-il utilisé ?  <sup>p. 21–26</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Un Scope est un mécanisme de regroupement de plusieurs collections. Il permet d'organiser les collections en fonction du type de contenu ou de la phase de déploiement, comme test ou production.

**Pourquoi :** Cela aide à structurer les données de manière logique et efficace.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=21-26`

</details>

<!-- QID:7284e3fea07f -->
### Quelle est la priorité lorsque les lectures sont beaucoup plus nombreuses que les écritures ?  <sup>p. 21–26</sup>

**Choix :**

- A) A. Assurer la cohérence des données
- B) B. Optimiser la vitesse d'accès
- C) C. Accepter le risque de données incohérentes
- D) D. Utiliser le cache efficacement

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Lorsque les lectures sont plus fréquentes, l'optimisation de la vitesse d'accès devient cruciale.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=21-26`

</details>

<!-- QID:a5caefe045a5 -->
### Les attributs de document JSON peuvent représenter des types de base tels que _____, chaîne de caractères, booléen, etc.  <sup>p. 27–28</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** nombre

**Pourquoi :** Les types de base incluent le nombre, la chaîne de caractères et le booléen.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=27-28`

</details>

<!-- QID:4cb9d3f18320 -->
### Quel type de structure est représenté par 'a3' dans l'exemple JSON?  <sup>p. 27–28</sup>

**Choix :**

- A) Tableau
- B) Document imbriqué
- C) Chaîne de caractères
- D) Nombre

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** 'a3' est un document imbriqué contenant un tableau.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=27-28`

</details>

<!-- QID:66dbb14b402d -->
### Les attributs 'a1' et 'a2' dans l'exemple JSON représentent des types complexes.  <sup>p. 27–28</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** 'a1' et 'a2' représentent des types simples (nombre et chaîne de caractères).

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=27-28`

</details>

<!-- QID:8a3305bb47fc -->
### Décrivez la structure de 'a4' dans l'exemple JSON.  <sup>p. 27–28</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** 'a4' est un tableau contenant deux objets, chacun avec des attributs 'c1' et 'c2' ou 'c3'.

**Pourquoi :** Cela montre comment les tableaux peuvent contenir des documents imbriqués.

**Source :** `courses/MAC/data/pdf/02-DocumentBasedPart1.pdf#p=27-28`

</details>
