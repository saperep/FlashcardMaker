---
course: "MAC"
generated_at: "2025-09-18T07:45:58"
source_pdf: "courses/MAC/data/pdf/00-Introduction.pdf"
---

# Flashcards – MAC

---
### Résumé essentiel

Le cours souligne que "Data is the New Oil", mettant en avant l'importance croissante des données dans l'économie moderne, où les ingénieurs de données jouent un rôle clé dans la conception de l'architecture de collecte, de stockage et de transformation des données. L'accès aux données, qu'elles soient structurées ou non, est crucial pour tout projet de data engineering, et les récents développements dans les bases de données et systèmes distribués ont révolutionné la construction d'applications, notamment pour gérer des volumes massifs de données. Les entreprises doivent adopter des méthodes agiles pour tester rapidement des hypothèses et s'adapter aux exigences du marché, tout en maintenant des cycles de développement courts. Les ingénieurs de données doivent maîtriser des technologies récentes, telles que les bases de données NoSQL, pour structurer et accéder aux données, tout en intégrant des logiciels libres et open source qui surpassent souvent les solutions commerciales. 

Les architectures distribuées, comme celles proposées par AWS, facilitent le développement de systèmes sur plusieurs machines, rendant la disponibilité des services cruciale pour réduire les temps d'arrêt. Les applications "data intensive" se concentrent sur la gestion de la quantité, de la complexité et de la vitesse des données, nécessitant des technologies spécifiques comme des systèmes NoSQL, des files d'attente de messages et des frameworks d'analyse de données. Le cours est structuré autour de quatre thèmes principaux : modèles de données NoSQL, distribution et cohérence des données, recherche d'informations textuelles, et analyse de données big data, avec une approche pratique utilisant des outils comme Elasticsearch et Apache Spark. Enfin, il est essentiel de comprendre les principes durables derrière les changements technologiques pour éviter les pièges courants.

### À retenir absolument
- Les données sont désormais considérées comme la ressource la plus précieuse, surpassant le pétrole.
- Les ingénieurs de données conçoivent l'architecture pour la collecte et le stockage des données.
- Les méthodes agiles sont essentielles pour s'adapter rapidement aux exigences du marché.
- Les applications "data intensive" nécessitent des technologies spécifiques comme NoSQL et Apache Spark.
- La compréhension des principes technologiques est cruciale pour éviter les erreurs fréquentes.

---

<!-- QID:5bfc98989ed8 -->
### Quelle est la ressource la plus précieuse selon l'article de The Economist de juin 2017 ?  <sup>p. 1–8</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Les données.

**Pourquoi :** Cette affirmation souligne l'importance croissante des données dans l'économie moderne, remplaçant le pétrole comme ressource clé.

**Source :** `courses/MAC/data/pdf/00-Introduction.pdf#p=1-8`

</details>

<!-- QID:241e2f6947aa -->
### Quel est le rôle principal d'un ingénieur de données ?  <sup>p. 1–8</sup>

**Choix :**

- A) Créer des hypothèses et analyser des données.
- B) Concevoir et créer l'architecture pour la collecte, le stockage et l'accès aux données.
- C) Développer des applications web.
- D) Gérer des projets de développement logiciel.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** L'ingénieur de données se concentre sur l'architecture des données, tandis que le data scientist se concentre sur l'analyse des données.

**Source :** `courses/MAC/data/pdf/00-Introduction.pdf#p=1-8`

</details>

<!-- QID:61c4821aa048 -->
### L'accès aux données __________ est une question centrale en data engineering.  <sup>p. 1–8</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** structurées/non-structurées, centralisées/distribuées, temps réel/historiques, moyen/grand volume.

**Pourquoi :** Ces catégories d'accès aux données sont essentielles pour comprendre les défis et les solutions en ingénierie des données.

**Source :** `courses/MAC/data/pdf/00-Introduction.pdf#p=1-8`

</details>

<!-- QID:5d2295f18520 -->
### Les ingénieurs de données doivent maîtriser uniquement les bases de données relationnelles.  <sup>p. 1–8</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Les ingénieurs de données doivent également maîtriser des technologies et algorithmes récents au-delà des bases de données relationnelles pour gérer des données complexes.

**Source :** `courses/MAC/data/pdf/00-Introduction.pdf#p=1-8`

</details>

<!-- QID:8f83dee203c5 -->
### Quels sont les principaux défis auxquels font face les entreprises dans le développement d'applications modernes ?  <sup>p. 1–8</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Les entreprises doivent être agiles, tester des hypothèses à moindre coût et répondre rapidement aux exigences du marché.

**Pourquoi :** Ces défis nécessitent des cycles de développement courts et des modèles de données flexibles pour s'adapter aux changements rapides du marché.

**Source :** `courses/MAC/data/pdf/00-Introduction.pdf#p=1-8`

</details>

<!-- QID:9883754a01c3 -->
### Quels acteurs clés d'Internet gèrent d'énormes volumes de données ?  <sup>p. 1–8</sup>

**Choix :**

- A) Apple, IBM, Oracle, Netflix.
- B) Google, Yahoo!, Amazon, Facebook, LinkedIn, Microsoft et Twitter.
- C) Adobe, Salesforce, Dropbox, Spotify.
- D) Tesla, SpaceX, Airbnb, Uber.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Ces entreprises sont connues pour leur capacité à gérer de grandes quantités de données et à développer des outils adaptés à cette échelle.

**Source :** `courses/MAC/data/pdf/00-Introduction.pdf#p=1-8`

</details>

<!-- QID:fcfc1f1d7afa -->
### Qu'est-ce qu'une application 'data intensive'?  <sup>p. 9–15</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Une application 'data intensive' est celle où les données constituent le principal défi, notamment en termes de quantité, complexité et vitesse de changement.

**Pourquoi :** Cette définition permet de distinguer les applications qui dépendent principalement des données de celles qui sont limitées par les cycles de processeur.

**Source :** `courses/MAC/data/pdf/00-Introduction.pdf#p=9-15`

</details>

<!-- QID:2b742f69c092 -->
### Quel type de système de bases de données est particulièrement adapté aux applications data intensive?  <sup>p. 9–15</sup>

**Choix :**

- A) Systèmes relationnels
- B) Systèmes NoSQL
- C) Systèmes de fichiers
- D) Systèmes de gestion de contenu

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Les systèmes NoSQL sont conçus pour gérer de grandes quantités de données non structurées et sont donc mieux adaptés aux applications data intensive.

**Source :** `courses/MAC/data/pdf/00-Introduction.pdf#p=9-15`

</details>

<!-- QID:4c8e6383f7fc -->
### Les temps d'arrêt prolongés sont devenus acceptables dans les services modernes.  <sup>p. 9–15</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Les temps d'arrêt prolongés sont de plus en plus inacceptables dans les services modernes, car la disponibilité est une exigence cruciale.

**Source :** `courses/MAC/data/pdf/00-Introduction.pdf#p=9-15`

</details>

<!-- QID:3ce1ccdd0588 -->
### Les ________ sont des outils qui aident les applications data intensive à stocker et à traiter les données.  <sup>p. 9–15</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** systèmes de bases de données NoSQL

**Pourquoi :** Les systèmes de bases de données NoSQL sont spécialement conçus pour répondre aux besoins des applications qui traitent de grandes quantités de données.

**Source :** `courses/MAC/data/pdf/00-Introduction.pdf#p=9-15`

</details>

<!-- QID:26ae002efacf -->
### Quels sont les principaux défis des applications data intensive?  <sup>p. 9–15</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Les principaux défis sont la quantité, la complexité et la vitesse à laquelle les données changent.

**Pourquoi :** Comprendre ces défis est essentiel pour concevoir des systèmes efficaces qui peuvent gérer des volumes de données importants.

**Source :** `courses/MAC/data/pdf/00-Introduction.pdf#p=9-15`

</details>

<!-- QID:4dc1eabda7a6 -->
### Quel est l'impact des processeurs multi-cœurs sur la construction d'applications?  <sup>p. 9–15</sup>

**Choix :**

- A) Ils ralentissent le traitement des données
- B) Ils permettent de créer des systèmes répartis sur de nombreuses machines
- C) Ils rendent les applications moins disponibles
- D) Ils augmentent la complexité des systèmes

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Les processeurs multi-cœurs facilitent le traitement parallèle, ce qui est essentiel pour les architectures distribuées modernes.

**Source :** `courses/MAC/data/pdf/00-Introduction.pdf#p=9-15`

</details>

<!-- QID:b86e4c516cb4 -->
### Les buzzwords dans le domaine des technologies de données doivent être pris au pied de la lettre.  <sup>p. 9–15</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Il est important de comprendre les principes techniques sous-jacents plutôt que de se laisser emporter par le jargon et les tendances.

**Source :** `courses/MAC/data/pdf/00-Introduction.pdf#p=9-15`

</details>

<!-- QID:b28cb5e66a89 -->
### Quels sont les quatre thèmes principaux abordés dans ce cours ?  <sup>p. 16–21</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** 1. Modèles de données et langages de requête NoSQL, 2. Modèles de distribution et cohérence des données, 3. Modèles et techniques de recherche d’informations textuelles, 4. Analyse de données big data.

**Pourquoi :** Ces thèmes couvrent les aspects fondamentaux des bases de données et de l'analyse de données, essentiels pour un ingénieur travaillant avec des systèmes de données modernes.

**Source :** `courses/MAC/data/pdf/00-Introduction.pdf#p=16-21`

</details>

<!-- QID:52371214d6c4 -->
### Quel est le pourcentage de l'évaluation attribué aux cours théoriques ?  <sup>p. 16–21</sup>

**Choix :**

- A) 50%
- B) 67%
- C) 75%
- D) 33%

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** L'évaluation est divisée en 67% pour les cours théoriques et 33% pour les labos, ce qui reflète l'importance de la théorie dans le cursus.

**Source :** `courses/MAC/data/pdf/00-Introduction.pdf#p=16-21`

</details>

<!-- QID:4d97d2551550 -->
### Les bases de données NoSQL étudiées dans ce cours incluent Couchbase et _____ .  <sup>p. 16–21</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Neo4J

**Pourquoi :** Neo4J est un exemple de base de données orientée graphes, ce qui permet d'explorer des relations complexes entre les données.

**Source :** `courses/MAC/data/pdf/00-Introduction.pdf#p=16-21`

</details>

<!-- QID:6632ba4a94e1 -->
### Les exercices pratiques sont une partie intégrante de ce cours.  <sup>p. 16–21</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Vrai

**Pourquoi :** Les labos et exercices permettent aux étudiants d'appliquer les concepts théoriques à des cas pratiques, renforçant ainsi leur compréhension.

**Source :** `courses/MAC/data/pdf/00-Introduction.pdf#p=16-21`

</details>

<!-- QID:a6f2f3f1b9c9 -->
### Quel outil est mentionné pour l'analyse des données dans ce cours ?  <sup>p. 16–21</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Apache Spark RDDs et DataFrames.

**Pourquoi :** Apache Spark est un framework puissant pour le traitement de grandes quantités de données, et les RDDs et DataFrames sont des abstractions clés pour manipuler ces données.

**Source :** `courses/MAC/data/pdf/00-Introduction.pdf#p=16-21`

</details>
