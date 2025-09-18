---
course: "MAC"
generated_at: "2025-09-18T07:48:44"
source_pdf: "courses/MAC/data/pdf/01-NoSQL-Intro.pdf"
---

# Flashcards – MAC

---
### Résumé essentiel

Le modèle relationnel, introduit par Edgar Codd en 1970, structure les données en relations, qui sont des ensembles de tuples non ordonnés. Bien que d'autres modèles, comme le modèle réseau et hiérarchique, aient été proposés, le modèle relationnel a dominé le paysage des bases de données. Les bases de données orientées objet, bien qu'elles aient été populaires dans les années 1980-1990, n'ont pas réussi à s'imposer, tout comme les bases de données XML au début des années 2000. Un défi majeur dans l'intégration des modèles de données relationnels avec les applications orientées objet est connu sous le nom d'Impedance Mismatch, qui nécessite souvent des solutions comme les frameworks de mappage objet-relationnel (ORM) pour faciliter la compatibilité.

Avec l'essor des données sur le Web, les bases de données NoSQL ont émergé pour répondre aux besoins de scalabilité et de flexibilité, se divisant en catégories telles que les stores clé-valeur, orientés documents, orientés colonnes et graphes. Les stores clé-valeur sont optimisés pour des opérations simples et à faible latence, tandis que les bases de données orientées documents permettent des schémas flexibles et sont adaptées à des applications variées. Les bases de données orientées colonnes améliorent l'efficacité des requêtes analytiques en organisant les données par colonnes, et les bases de données graphes facilitent le parcours des relations sans nécessiter de jointures complexes. Chaque type de base de données a ses propres cas d'utilisation, avantages et inconvénients, soulignant l'importance de choisir la bonne technologie en fonction des besoins spécifiques des applications.

### À retenir absolument
- Le modèle relationnel organise les données en relations, dominantes depuis leur introduction en 1970.
- L'Impedance Mismatch pose des défis d'intégration entre modèles relationnels et orientés objet, nécessitant des ORM.
- Les bases de données NoSQL, telles que MongoDB et Couchbase, répondent aux besoins de scalabilité et de flexibilité.
- Les stores clé-valeur, orientés documents, orientés colonnes et graphes sont les quatre principales catégories de bases de données NoSQL.
- Chaque type de base de données a des cas d'utilisation spécifiques, influençant le choix technologique selon les exigences des applications.

---

<!-- QID:63fe0cd3eb4d -->
### Qui a proposé le modèle relationnel et en quelle année ?  <sup>p. 1–4</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Edgar Codd en 1970.

**Pourquoi :** Le modèle relationnel est fondamental dans le domaine des bases de données et a établi les bases de l'organisation des données en relations.

**Source :** `courses/MAC/data/pdf/01-NoSQL-Intro.pdf#p=1-4`

</details>

<!-- QID:79e082a951b7 -->
### Quel modèle de données a dominé les alternatives comme le modèle réseau et le modèle hiérarchique ?  <sup>p. 1–4</sup>

**Choix :**

- A) Modèle hiérarchique
- B) Modèle réseau
- C) Modèle relationnel
- D) Modèle objet

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C

**Pourquoi :** Le modèle relationnel a été adopté en raison de sa flexibilité et de sa capacité à gérer des données complexes de manière efficace.

**Source :** `courses/MAC/data/pdf/01-NoSQL-Intro.pdf#p=1-4`

</details>

<!-- QID:eb00cf2bed93 -->
### Les bases de données XML ont eu une adoption massive depuis leur apparition au début des années 2000.  <sup>p. 1–4</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Les bases de données XML ont eu une adoption très limitée malgré leur introduction, ce qui montre que d'autres modèles ont été préférés.

**Source :** `courses/MAC/data/pdf/01-NoSQL-Intro.pdf#p=1-4`

</details>

<!-- QID:eeaf38397b2d -->
### Le modèle de données le plus connu aujourd'hui est le modèle ________, proposé par Edgar Codd en 1970.  <sup>p. 1–4</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** relationnel

**Pourquoi :** Cette définition est essentielle pour comprendre la base des systèmes de gestion de bases de données modernes.

**Source :** `courses/MAC/data/pdf/01-NoSQL-Intro.pdf#p=1-4`

</details>

<!-- QID:43dda3cf537a -->
### Quelles étaient les principales alternatives au modèle relationnel dans les années 1970-1980 ?  <sup>p. 1–4</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Le modèle réseau et le modèle hiérarchique.

**Pourquoi :** Ces modèles ont été des tentatives de structurer les données avant que le modèle relationnel ne devienne dominant.

**Source :** `courses/MAC/data/pdf/01-NoSQL-Intro.pdf#p=1-4`

</details>

<!-- QID:f3ac4f09e494 -->
### Quel type de bases de données a émergé entre 1980 et 1990 mais a ensuite disparu ?  <sup>p. 1–4</sup>

**Choix :**

- A) Bases de données relationnelles
- B) Bases de données XML
- C) Bases de données objets
- D) Bases de données NoSQL

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C

**Pourquoi :** Les bases de données objets n'ont pas réussi à s'imposer face aux modèles relationnels, qui offraient une meilleure compatibilité et des outils plus robustes.

**Source :** `courses/MAC/data/pdf/01-NoSQL-Intro.pdf#p=1-4`

</details>

<!-- QID:bdcb15aeba09 -->
### Qu'est-ce que le terme NoSQL désigne?  <sup>p. 5–9</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Le terme NoSQL désigne des bases de données qui permettent de stocker et de rechercher plus facilement des documents, comme MongoDB et Couchbase.

**Pourquoi :** Cette définition souligne la nature non relationnelle et orientée document des bases de données NoSQL, qui répondent à des besoins spécifiques non couverts par les bases de données relationnelles.

**Source :** `courses/MAC/data/pdf/01-NoSQL-Intro.pdf#p=5-9`

</details>

<!-- QID:6ab563acfcdb -->
### Quel est un moteur d'adoption des bases de données NoSQL?  <sup>p. 5–9</sup>

**Choix :**

- A) Une préférence généralisée pour les logiciels libres et open source.
- B) Une meilleure sécurité des données.
- C) Une réduction des coûts d'infrastructure.
- D) Une standardisation des schémas de données.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** A

**Pourquoi :** La préférence pour les logiciels libres et open source est un facteur clé qui a conduit à l'adoption des bases de données NoSQL, car elles offrent plus de flexibilité et d'accessibilité.

**Source :** `courses/MAC/data/pdf/01-NoSQL-Intro.pdf#p=5-9`

</details>

<!-- QID:42a092990c5b -->
### L'impedance mismatch fait référence à la déconnexion entre les objets du code d'application et les tables relationnelles.  <sup>p. 5–9</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Vrai

**Pourquoi :** L'impedance mismatch est un problème courant dans le développement d'applications où les données sont stockées dans des bases de données relationnelles, nécessitant une couche de traduction entre les deux modèles.

**Source :** `courses/MAC/data/pdf/01-NoSQL-Intro.pdf#p=5-9`

</details>

<!-- QID:8084581873bd -->
### Le terme NoSQL était à l'origine proposé comme un hashtag Twitter pour une rencontre sur des bases de données _____ et _____ et non relationnelles.  <sup>p. 5–9</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** open source, distribuées

**Pourquoi :** Cette origine souligne l'aspect communautaire et innovant des bases de données NoSQL, qui ont émergé en réponse à des besoins spécifiques dans le domaine des données.

**Source :** `courses/MAC/data/pdf/01-NoSQL-Intro.pdf#p=5-9`

</details>

<!-- QID:18eca7c26fde -->
### Quels sont les principaux inconvénients des schémas relationnels qui ont conduit à l'émergence des bases de données NoSQL?  <sup>p. 5–9</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Les schémas relationnels sont souvent considérés comme restrictifs et peu dynamiques, ce qui limite la flexibilité des modèles de données.

**Pourquoi :** Cette restriction peut poser des problèmes dans des environnements où les données évoluent rapidement et nécessitent des structures plus adaptables.

**Source :** `courses/MAC/data/pdf/01-NoSQL-Intro.pdf#p=5-9`

</details>

<!-- QID:089a82976fb5 -->
### Qu'est-ce que l'impedance mismatch?  <sup>p. 10–15</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** L'impedance mismatch est une désadaptation qui se produit lorsque les impédances de la ligne de transmission et de la charge ne sont pas identiques.

**Pourquoi :** Cela entraîne des réflexions d'énergie et des ondes stationnaires, affectant la performance des systèmes de transmission.

**Source :** `courses/MAC/data/pdf/01-NoSQL-Intro.pdf#p=10-15`

</details>

<!-- QID:2b7d83da09c9 -->
### Quel est un des principaux avantages des frameworks de mappage objet-relationnel?  <sup>p. 10–15</sup>

**Choix :**

- A) Ils augmentent la complexité des requêtes.
- B) Ils suppriment beaucoup de travail fastidieux.
- C) Ils rendent les bases de données OO plus populaires.
- D) Ils obligent à utiliser uniquement SQL.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Ces frameworks facilitent la gestion des désadaptations d'impédance en automatisant le mappage entre objets et bases de données.

**Source :** `courses/MAC/data/pdf/01-NoSQL-Intro.pdf#p=10-15`

</details>

<!-- QID:98facf20f1d4 -->
### Les services Web permettent moins de flexibilité sur la structure des données échangées par rapport à SQL.  <sup>p. 10–15</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Les services Web permettent des structures de données plus riches, comme des listes imbriquées en XML/JSON, contrairement à SQL qui impose des relations strictes.

**Source :** `courses/MAC/data/pdf/01-NoSQL-Intro.pdf#p=10-15`

</details>

<!-- QID:e7825a449515 -->
### L'impedance mismatch se produit également dans les applications traitant du stockage et de la récupération de ______.  <sup>p. 10–15</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** documents

**Pourquoi :** Cela souligne que le problème de désadaptation d'impédance n'est pas limité aux bases de données relationnelles, mais s'étend également aux documents.

**Source :** `courses/MAC/data/pdf/01-NoSQL-Intro.pdf#p=10-15`

</details>

<!-- QID:74bf4ee84247 -->
### Quelle est la principale raison pour laquelle les bases de données relationnelles ont triomphé des bases de données orientées objet?  <sup>p. 10–15</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Le rôle de SQL en tant que mécanisme d'intégration entre les applications.

**Pourquoi :** SQL a fourni une méthode standardisée pour interagir avec les données, ce qui a facilité l'intégration des systèmes.

**Source :** `courses/MAC/data/pdf/01-NoSQL-Intro.pdf#p=10-15`

</details>

<!-- QID:8638fcf8bf24 -->
### Quel est un des défis du mappage des documents en relations?  <sup>p. 10–15</sup>

**Choix :**

- A) Comment réduire la taille des documents.
- B) Comment mapper au mieux les documents en relations.
- C) Comment convertir les relations en documents.
- D) Comment supprimer les documents obsolètes.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Le mappage efficace des documents en relations est crucial pour maintenir l'intégrité des données tout en utilisant des structures de données variées.

**Source :** `courses/MAC/data/pdf/01-NoSQL-Intro.pdf#p=10-15`

</details>

<!-- QID:64bfa2f559f7 -->
### Les relations M:N peuvent être facilement représentées dans un document JSON.  <sup>p. 16–23</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Les relations M:N sont problématiques à représenter dans un document JSON car elles nécessitent des structures plus complexes.

**Source :** `courses/MAC/data/pdf/01-NoSQL-Intro.pdf#p=16-23`

</details>

<!-- QID:a21e58ddeebf -->
### Quelle est une caractéristique des bases de données NoSQL?  <sup>p. 16–23</sup>

**Choix :**

- A) Elles utilisent le modèle relationnel.
- B) Elles n'ont aucun schéma.
- C) Elles sont toutes payantes.
- D) Elles ne peuvent pas être scalées.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Les bases de données NoSQL sont conçues pour être flexibles et adaptées aux besoins modernes, sans schéma fixe.

**Source :** `courses/MAC/data/pdf/01-NoSQL-Intro.pdf#p=16-23`

</details>

<!-- QID:a609b5031a25 -->
### Quelles sont les deux solutions possibles pour gérer l'évolutivité des bases de données?  <sup>p. 16–23</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Scale up et Scale out.

**Pourquoi :** Scale up consiste à améliorer les machines existantes, tandis que Scale out implique d'ajouter de nombreuses petites machines dans un cluster.

**Source :** `courses/MAC/data/pdf/01-NoSQL-Intro.pdf#p=16-23`

</details>

<!-- QID:5d9146718a0d -->
### Les bases de données NoSQL sont souvent décrites comme étant ___ et ___, et elles sont basées sur les besoins du Web et du 21e siècle.  <sup>p. 16–23</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** open source, scalables horizontalement

**Pourquoi :** Ces caractéristiques permettent aux bases de données NoSQL de s'adapter à des volumes de données croissants et à des environnements distribués.

**Source :** `courses/MAC/data/pdf/01-NoSQL-Intro.pdf#p=16-23`

</details>

<!-- QID:9b837e2f6269 -->
### Quel type de base de données est principalement utilisé pour des accès via une clé primaire?  <sup>p. 16–23</sup>

**Choix :**

- A) Bases de données orientées documents.
- B) Stores orientés colonnes.
- C) Bases de données graphes.
- D) Stores clé-valeur.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** D

**Pourquoi :** Les stores clé-valeur utilisent un mappage clé-valeur, ce qui les rend efficaces pour des accès rapides basés sur une clé.

**Source :** `courses/MAC/data/pdf/01-NoSQL-Intro.pdf#p=16-23`

</details>

<!-- QID:cfe40fcd563e -->
### Qu'est-ce que 'eventually consistent' dans le contexte des bases de données NoSQL?  <sup>p. 16–23</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C'est un modèle de cohérence où les données peuvent ne pas être immédiatement synchronisées, mais finiront par l'être.

**Pourquoi :** Cela permet d'améliorer la disponibilité et la performance des systèmes distribués, au détriment d'une stricte cohérence immédiate.

**Source :** `courses/MAC/data/pdf/01-NoSQL-Intro.pdf#p=16-23`

</details>

<!-- QID:45f9cd18853d -->
### Quels sont les principaux cas d'utilisation des stores clé-valeur ?  <sup>p. 24–31</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Gestion de session à grande échelle, préférences utilisateur, recommandations de produits, publicités personnalisées, et comme cache pour des données très consultées.

**Pourquoi :** Ces cas d'utilisation tirent parti de la faible latence et de la capacité à gérer de grandes tailles de données.

**Source :** `courses/MAC/data/pdf/01-NoSQL-Intro.pdf#p=24-31`

</details>

<!-- QID:2a23948e7f49 -->
### Les documents dans une base de données orientée documents sont des données ________.  <sup>p. 24–31</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** auto-descriptives

**Pourquoi :** Cette caractéristique permet aux documents de contenir des informations sur leur propre structure, facilitant ainsi leur manipulation.

**Source :** `courses/MAC/data/pdf/01-NoSQL-Intro.pdf#p=24-31`

</details>

<!-- QID:d00b2a5e3be8 -->
### Quel est un avantage des stores orientés colonnes par rapport aux SGBDR classiques ?  <sup>p. 24–31</sup>

**Choix :**

- A) Les données sont stockées par ligne.
- B) Les requêtes sont toujours plus lentes.
- C) Les données sont stockées par colonnes, ce qui permet des requêtes ciblées.
- D) Ils ne peuvent pas gérer de grandes quantités de données.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C

**Pourquoi :** Le stockage par colonnes permet d'optimiser les requêtes analytiques en ne parcourant que les colonnes nécessaires.

**Source :** `courses/MAC/data/pdf/01-NoSQL-Intro.pdf#p=24-31`

</details>

<!-- QID:c9d1e4300766 -->
### Les documents d'une collection dans une base de données orientée documents doivent avoir le même schéma.  <sup>p. 24–31</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Les documents peuvent avoir des schémas différents, ce qui offre une flexibilité dans la structure des données.

**Source :** `courses/MAC/data/pdf/01-NoSQL-Intro.pdf#p=24-31`

</details>

<!-- QID:8964ccc07aae -->
### Quelles sont les structures de données typiques utilisées dans les documents d'une base de données orientée documents ?  <sup>p. 24–31</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Structures arborescentes hiérarchiques, objets imbriqués, collections, et valeurs scalaires comme XML et JSON.

**Pourquoi :** Ces structures permettent de représenter des données complexes de manière organisée et accessible.

**Source :** `courses/MAC/data/pdf/01-NoSQL-Intro.pdf#p=24-31`

</details>

<!-- QID:aaf02695f176 -->
### Quel langage de requête est utilisé dans MongoDB ?  <sup>p. 24–31</sup>

**Choix :**

- A) SQL
- B) JSON
- C) XML
- D) CQL

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** MongoDB utilise une syntaxe de requête basée sur JSON, ce qui facilite l'interaction avec les documents.

**Source :** `courses/MAC/data/pdf/01-NoSQL-Intro.pdf#p=24-31`

</details>

<!-- QID:f1ca49981cc4 -->
### Quels types de données peuvent être stockés dans une base de données orientée documents ?  <sup>p. 24–31</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Des articles, blogs, documents, médias, profils utilisateurs, contenus personnalisés, et modèles pour le Machine Learning.

**Pourquoi :** Cette diversité d'applications montre la flexibilité des bases de données orientées documents.

**Source :** `courses/MAC/data/pdf/01-NoSQL-Intro.pdf#p=24-31`

</details>

<!-- QID:cf4e3170d140 -->
### Qu'est-ce qu'un store orienté colonnes ?  <sup>p. 32–40</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Un store orienté colonnes est une base de données qui organise les données en colonnes plutôt qu'en lignes, permettant un accès efficace aux colonnes individuelles.

**Pourquoi :** Cette structure est particulièrement adaptée aux requêtes analytiques et aux données semi-structurées.

**Source :** `courses/MAC/data/pdf/01-NoSQL-Intro.pdf#p=32-40`

</details>

<!-- QID:d5e76862e31d -->
### Dans un store orienté colonnes, chaque colonne est composée d'une paire nom-valeur où le nom se comporte également comme la ____.  <sup>p. 32–40</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** clé

**Pourquoi :** Cela signifie que chaque colonne est unique et identifiable par son nom, facilitant l'accès aux données.

**Source :** `courses/MAC/data/pdf/01-NoSQL-Intro.pdf#p=32-40`

</details>

<!-- QID:1863cabf122a -->
### Quel est un avantage des stores orientés colonnes par rapport aux stores clé-valeur ?  <sup>p. 32–40</sup>

**Choix :**

- A) On peut lire ou écrire une colonne précise.
- B) Les données sont toujours stockées sous forme de lignes.
- C) Les stores clé-valeur sont plus rapides.
- D) Les colonnes doivent avoir les mêmes types de données.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** A

**Pourquoi :** Cette capacité permet une plus grande flexibilité et efficacité dans la gestion des données.

**Source :** `courses/MAC/data/pdf/01-NoSQL-Intro.pdf#p=32-40`

</details>

<!-- QID:5d5d6bd6bc0a -->
### Les lignes dans un store orienté colonnes doivent avoir les mêmes colonnes.  <sup>p. 32–40</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Les lignes n'ont pas besoin d'avoir les mêmes colonnes, ce qui permet une grande flexibilité dans la structure des données.

**Source :** `courses/MAC/data/pdf/01-NoSQL-Intro.pdf#p=32-40`

</details>

<!-- QID:14a87c57a528 -->
### Quels sont quelques cas d'utilisation des stores orientés colonnes ?  <sup>p. 32–40</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Logs d'événements, comptage, recherche de produits, reporting à grande échelle.

**Pourquoi :** Ces cas d'utilisation tirent parti de la capacité des stores orientés colonnes à gérer des volumes élevés de données semi-structurées.

**Source :** `courses/MAC/data/pdf/01-NoSQL-Intro.pdf#p=32-40`

</details>

<!-- QID:3d906ffa62f2 -->
### Comment les familles de colonnes sont-elles définies dans un store orienté colonnes ?  <sup>p. 32–40</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Les familles de colonnes sont des regroupements logiques de colonnes souvent recherchées ensemble.

**Pourquoi :** Cela permet d'organiser les données de manière cohérente et d'optimiser les requêtes.

**Source :** `courses/MAC/data/pdf/01-NoSQL-Intro.pdf#p=32-40`

</details>

<!-- QID:f129809b3067 -->
### Dans un SGBDR, l'ajout d'une autre relation signifie généralement de nombreux changements de _____.  <sup>p. 41–47</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** schéma

**Pourquoi :** Cela souligne la rigidité des SGBDR en matière de structure de données, où chaque modification peut nécessiter une refonte significative.

**Source :** `courses/MAC/data/pdf/01-NoSQL-Intro.pdf#p=41-47`

</details>

<!-- QID:b2732d7976a1 -->
### Quel est un avantage des bases de données graphes par rapport aux SGBDR ?  <sup>p. 41–47</sup>

**Choix :**

- A) Elles sont plus rapides pour les écritures.
- B) Elles nécessitent moins de stockage.
- C) Il n'y a pas besoin de jointure car la relation persiste.
- D) Elles sont plus faciles à modéliser.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C

**Pourquoi :** Les bases de données graphes sont conçues pour gérer des relations complexes de manière efficace, ce qui élimine le besoin de jointures coûteuses.

**Source :** `courses/MAC/data/pdf/01-NoSQL-Intro.pdf#p=41-47`

</details>

<!-- QID:dd456c036efb -->
### Les bases de données graphes sont adaptées pour les applications où les lectures sont rares mais les écritures très fréquentes.  <sup>p. 41–47</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Les bases de données graphes sont généralement plus adaptées aux applications où les lectures sont fréquentes, comme les moteurs de recommandation, car elles optimisent l'accès aux relations entre les données.

**Source :** `courses/MAC/data/pdf/01-NoSQL-Intro.pdf#p=41-47`

</details>

<!-- QID:a6799cbcc54b -->
### Citez deux cas d'utilisation des bases de données graphes.  <sup>p. 41–47</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Réseaux sociaux et moteurs de recommandation.

**Pourquoi :** Ces cas d'utilisation tirent parti des relations complexes entre les entités, ce qui est le point fort des bases de données graphes.

**Source :** `courses/MAC/data/pdf/01-NoSQL-Intro.pdf#p=41-47`

</details>
