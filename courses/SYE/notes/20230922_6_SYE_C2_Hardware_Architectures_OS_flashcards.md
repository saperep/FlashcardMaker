---
course: "SYE"
generated_at: "2025-09-16T10:34:42"
---

# Flashcards – SYE

> Astuce : cliquez pour dérouler la réponse.

<!-- QID:df5197722904 -->
### Quel est le rôle fondamental d'un système d'exploitation en matière de sécurité?  <sup>p. 1–3</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Garantir que les applications ne peuvent pas interférer entre elles et ne peuvent pas accéder au matériel de manière illicite.

**Pourquoi :** Cela permet de protéger le noyau de l'OS et d'assurer un fonctionnement sécurisé des applications.

**Source :** `data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=1-3`

</details>

<!-- QID:6c9bdb2343c6 -->
### Quelles instructions ne peuvent être exécutées que par le noyau?  <sup>p. 1–3</sup>

<details>
<summary>Afficher la réponse</summary>

**Choix :**

- A) Instructions de base
- B) Instructions sensibles
- C) Instructions de contrôle
- D) Instructions de gestion

**Réponse :** B

**Pourquoi :** Les instructions sensibles sont réservées au noyau pour garantir la sécurité du système.

**Source :** `data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=1-3`

</details>

<!-- QID:3c8230b96a50 -->
### Les requêtes du processeur vers l'extérieur sont de nature asynchrone.  <sup>p. 1–3</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Ces requêtes sont de nature synchrone car elles sont initiées par le processeur et exécutées immédiatement.

**Source :** `data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=1-3`

</details>

<!-- QID:72d37267e345 -->
### Quel composant est chargé du séquençage des opérations dans l'architecture Von Neumann?  <sup>p. 1–3</sup>

<details>
<summary>Afficher la réponse</summary>

**Choix :**

- A) ALU
- B) Registres
- C) Unité de contrôle (CU)
- D) Mémoire

**Réponse :** C

**Pourquoi :** L'unité de contrôle est responsable du séquençage des opérations dans l'architecture Von Neumann.

**Source :** `data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=1-3`

</details>

<!-- QID:08c3311f6f7c -->
### Comment le processeur gère-t-il les accès mémoire?  <sup>p. 1–3</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Il différencie les accès en fonction des adresses, certaines zones mémoires étant protégées et non accessibles par toutes les applications.

**Pourquoi :** Cela permet de sécuriser l'accès aux ressources matérielles et de protéger le système d'exploitation.

**Source :** `data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=1-3`

</details>

<!-- QID:a08b73f33de5 -->
### Quel est le rôle principal de la MMU dans un système d'exploitation ?  <sup>p. 4–5</sup>

<details>
<summary>Afficher la réponse</summary>

**Choix :**

- A) A. Gérer les entrées/sorties
- B) B. Traduire une adresse virtuelle en une adresse physique
- C) C. Exécuter des instructions sensibles
- D) D. Accéder directement au matériel

**Réponse :** B

**Pourquoi :** La MMU est spécifiquement mentionnée pour traduire les adresses dans l'extrait.

**Source :** `data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=4-5`

</details>

<!-- QID:a915d3849cc5 -->
### Vrai ou Faux: Les applications peuvent exécuter des instructions sensibles sans restriction.  <sup>p. 4–5</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Les instructions sensibles ne peuvent être exécutées que par le noyau, comme indiqué dans l'extrait.

**Source :** `data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=4-5`

</details>

<!-- QID:547c5833e312 -->
### Pourquoi est-il important que les applications ne puissent pas interférer entre elles dans un système d'exploitation ?  <sup>p. 4–5</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Il est crucial pour la sécurité au niveau applicatif, afin d'éviter que des applications n'accèdent illégalement aux ressources ou n'interfèrent avec d'autres applications en cours d'exécution.

**Pourquoi :** Cette justification est directement tirée de l'extrait qui aborde la sécurité des applications.

**Source :** `data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=4-5`

</details>

<!-- QID:67c00266bf55 -->
### Le passage du mode kernel en mode user nécessite l'exécution d'une instruction ____.  <sup>p. 6–7</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** sensible

**Pourquoi :** C'est spécifié dans l'extrait que le passage du mode kernel en mode user nécessite une instruction sensible.

**Source :** `data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=6-7`

</details>

<!-- QID:53cc0b04cb1a -->
### Quel type d'interruption est synchrone ?  <sup>p. 6–7</sup>

<details>
<summary>Afficher la réponse</summary>

**Choix :**

- A) Interruption matérielle
- B) Interruption logicielle
- C) Interruption asynchrone
- D) Interruption de service

**Réponse :** B

**Pourquoi :** L'extrait mentionne que l'interruption logicielle est de type synchrone, contrairement à l'interruption matérielle qui est asynchrone.

**Source :** `data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=6-7`

</details>

<!-- QID:9546df34c0e8 -->
### Le CPU est en mode utilisateur au démarrage d'un système.  <sup>p. 6–7</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** L'extrait indique que le CPU est en mode noyau au démarrage d'un système.

**Source :** `data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=6-7`

</details>

<!-- QID:be8c0b49f696 -->
### Comment un périphérique informe-t-il le CPU qu'il a terminé de traiter une requête ?  <sup>p. 6–7</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Un périphérique informe le CPU via des interruptions matérielles en sollicitant une ligne électrique dédiée entre lui et le CPU, en passant par le contrôleur d'interruption.

**Source :** `data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=6-7`

</details>

<!-- QID:0b6a14b2bb00 -->
### Quel type d'interruption est déclenché par une instruction réservée comme 'int' ou 'sysenter' ?  <sup>p. 6–7</sup>

<details>
<summary>Afficher la réponse</summary>

**Choix :**

- A) Interruption matérielle
- B) Interruption logicielle
- C) Interruption asynchrone
- D) Interruption de service

**Réponse :** B

**Pourquoi :** L'extrait précise que des instructions réservées entraînent des interruptions logicielles.

**Source :** `data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=6-7`

</details>

<!-- QID:765aa867002d -->
### Lors d'une interruption, une fonction particulière appelée ____ est immédiatement exécutée.  <sup>p. 6–7</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** routine de service

**Pourquoi :** L'extrait mentionne que lors d'une interruption, une routine de service est exécutée.

**Source :** `data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=6-7`

</details>

<!-- QID:112f51cb0005 -->
### Chaque périphérique dispose de sa propre ligne d'interruption, qui est reliée à un __________ permettant une gestion des interruptions plus efficace.  <sup>p. 8–9</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** contrôleur d'interruption

**Pourquoi :** Le contrôleur d'interruption gère les interruptions de manière indépendante du processeur.

**Source :** `data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=8-9`

</details>

<!-- QID:9f253a522130 -->
### Quel est le rôle du vecteur d'interruption ?  <sup>p. 8–9</sup>

<details>
<summary>Afficher la réponse</summary>

**Choix :**

- A) A. Il masque les interruptions
- B) B. Il associe à un numéro l'adresse de la routine de service.
- C) C. Il termine l'instruction en cours
- D) D. Il gère la mémoire cache

**Réponse :** B

**Pourquoi :** Le vecteur d'interruption permet au processeur de connaître l'emplacement de la routine de service.

**Source :** `data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=8-9`

</details>

<!-- QID:40759ebd07c4 -->
### Le passage en mode noyau est nécessaire avant d'exécuter la routine de service.  <sup>p. 8–9</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Vrai

**Pourquoi :** Le processeur doit passer en mode noyau pour exécuter la routine de service après une interruption.

**Source :** `data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=8-9`

</details>

<!-- QID:e747b19f6a39 -->
### Quelles sont les conséquences de l'utilisation de caches individuels dans une architecture multicœur ?  <sup>p. 8–9</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** L'utilisation de caches individuels nécessite une gestion de la cohérence entre les caches. Si un processeur modifie le contenu de son cache, les données dans les autres caches doivent être mises à jour pour éviter des incohérences.

**Source :** `data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=8-9`

</details>

<!-- QID:38f8fe8f39e4 -->
### Quel modèle d'architecture est le plus utilisé pour les processeurs multicœurs ?  <sup>p. 8–9</sup>

<details>
<summary>Afficher la réponse</summary>

**Choix :**

- A) A. MPP
- B) B. SMP
- C) C. NUMA
- D) D. RISC

**Réponse :** B

**Pourquoi :** Le modèle SMP permet de répartir la mémoire entre les différents cœurs CPU.

**Source :** `data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=8-9`

</details>

<!-- QID:18a511097ba7 -->
### Un système d'exploitation doit fournir une interface conviviale, performante et sécurisée aux __________.  <sup>p. 10–11</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** applications utilisateur

**Pourquoi :** C'est une des deux perspectives selon lesquelles un OS est défini.

**Source :** `data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=10-11`

</details>

<!-- QID:7ee125c4d4a1 -->
### Quel est un des compromis que les systèmes d'exploitation doivent souvent gérer ?  <sup>p. 10–11</sup>

<details>
<summary>Afficher la réponse</summary>

**Choix :**

- A) Sécurité et coût
- B) Performance et complexité
- C) Sécurité et performance
- D) Simplicité et robustesse

**Réponse :** C

**Pourquoi :** Les OS doivent faire face à des compromis entre ces deux aspects.

**Source :** `data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=10-11`

</details>

<!-- QID:122142ed9085 -->
### Quelles sont les deux architectures principales des systèmes d'exploitation et quelles sont leurs caractéristiques ?  <sup>p. 10–11</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Les deux architectures principales sont monolithique et micronoyau. L'architecture monolithique offre de meilleures performances mais présente des risques de sécurité, tandis que l'architecture micronoyau améliore la sécurité et l'extensibilité, mais peut limiter les performances.

**Source :** `data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=10-11`

</details>

<!-- QID:67ded8427972 -->
### Quel espace est associé aux appels système dans un système d'exploitation ?  <sup>p. 10–11</sup>

<details>
<summary>Afficher la réponse</summary>

**Choix :**

- A) Espace utilisateur
- B) Espace noyau
- C) Espace mémoire
- D) Espace de stockage

**Réponse :** B

**Pourquoi :** Les appels système permettent la communication entre l'espace utilisateur et l'espace noyau.

**Source :** `data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=10-11`

</details>

<!-- QID:709035d06425 -->
### L'architecture micronoyau est plus sécurisée que l'architecture ________.  <sup>p. 12–14</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** monolithique

**Pourquoi :** L'architecture micronoyau minimise les fonctionnalités dans l'espace noyau, rendant le système moins susceptible de planter.

**Source :** `data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=12-14`

</details>

<!-- QID:2c12fad8a8f6 -->
### Quel est l'avantage principal de l'architecture micronoyau par rapport à l'architecture monolithique ?  <sup>p. 12–14</sup>

<details>
<summary>Afficher la réponse</summary>

**Choix :**

- A) A) Performances élevées
- B) B) Sécurité accrue
- C) C) Simplicité
- D) D) Coût réduit

**Réponse :** B

**Pourquoi :** L'architecture micronoyau réduit les fonctionnalités dans l'espace noyau, ce qui augmente la sécurité du système.

**Source :** `data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=12-14`

</details>

<!-- QID:75728f37e8d2 -->
### Vrai ou Faux: Dans une architecture micronoyau, les sous-systèmes ont un accès direct aux structures du noyau.  <sup>p. 12–14</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Les sous-systèmes n'ont pas accès direct aux structures du noyau, ce qui renforce la sécurité et l'isolation.

**Source :** `data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=12-14`

</details>

<!-- QID:e4e0f8d3acc8 -->
### Comment la communication entre sous-systèmes est-elle organisée dans une architecture micronoyau ?  <sup>p. 12–14</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** La communication entre sous-systèmes est organisée selon une approche client-serveur, permettant une spécification claire de l'interface et du protocole de communication.

**Source :** `data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=12-14`

</details>

<!-- QID:4f5ae237ac9b -->
### Quel type d'architecture est Windows Vista selon l'extrait ?  <sup>p. 12–14</sup>

<details>
<summary>Afficher la réponse</summary>

**Choix :**

- A) A) Monolithique
- B) B) Micronoyau
- C) C) Hybride
- D) D) Client-serveur

**Réponse :** C

**Pourquoi :** Windows Vista combine des éléments des architectures monolithiques et micronoyau, ce qui en fait une architecture hybride.

**Source :** `data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=12-14`

</details>

<!-- QID:6297f707876f -->
### Dans une architecture de type micronoyau, les services utilisateur et le noyau sont conservés dans un espace d'adressage ___.  <sup>p. 15–17</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** séparé

**Pourquoi :** C'est une caractéristique fondamentale des micro-noyaux.

**Source :** `data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=15-17`

</details>

<!-- QID:d318dd24f80d -->
### Un micro-noyau est plus gros qu'un noyau monolithique.  <sup>p. 15–17</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Les micro-noyaux sont généralement plus petits que les noyaux monolithiques.

**Source :** `data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=15-17`

</details>

<!-- QID:d98e3ec1bde5 -->
### Quelles sont les principales différences entre un micro-noyau et un noyau monolithique en termes d'exécution et de sécurité ?  <sup>p. 15–17</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Les micro-noyaux ont une exécution plus lente mais sont plus extensibles, tandis que les noyaux monolithiques offrent une exécution rapide mais sont plus difficiles à étendre. En termes de sécurité, une panne de service dans un micro-noyau n'affecte pas nécessairement tout le système, alors qu'une panne dans un noyau monolithique peut le bloquer complètement.

**Pourquoi :** Ces différences sont essentielles pour comprendre les compromis entre les deux architectures.

**Source :** `data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=15-17`

</details>

<!-- QID:784c2ed0e272 -->
### Quel est le rôle fondamental d'un système d'exploitation en matière de sécurité applicative ?  <sup>p. 1–3</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Le rôle fondamental d'un système d'exploitation est de garantir que les applications ne peuvent pas interférer illicitement entre elles et ne peuvent pas accéder au matériel de manière non autorisée.

**Pourquoi :** Cela permet de protéger les applications et le noyau de l'OS contre des accès non sécurisés.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=1-3`

</details>

<!-- QID:6b16f870cb8c -->
### Quelles instructions ne peuvent être exécutées que par le noyau du système d'exploitation ?  <sup>p. 1–3</sup>

**Choix :**

- A) Instructions de base
- B) Instructions sensibles
- C) Instructions de contrôle
- D) Instructions de mémoire

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Seules les instructions sensibles sont réservées au noyau pour garantir la sécurité du système.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=1-3`

</details>

<!-- QID:3c8230b96a50 -->
### Les requêtes du processeur vers l'extérieur sont de nature asynchrone.  <sup>p. 1–3</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Ces requêtes sont de nature synchrone car elles sont initiées par le processeur et exécutées immédiatement.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=1-3`

</details>

<!-- QID:087dbf022a0b -->
### Quel composant est chargé du séquençage des opérations dans l'architecture Von Neumann ?  <sup>p. 1–3</sup>

**Choix :**

- A) ALU
- B) Registres
- C) Unité de contrôle
- D) Mémoire

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C

**Pourquoi :** L'unité de contrôle est responsable du séquençage des opérations dans l'architecture Von Neumann.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=1-3`

</details>

<!-- QID:bba5afc610dc -->
### Comment les requêtes en provenance de l'extérieur vers le processeur sont-elles définies ?  <sup>p. 1–3</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Ces requêtes sont typiquement des interruptions matérielles, provoquées par des contrôleurs de périphérique qui interrompent le programme en cours d'exécution.

**Pourquoi :** Elles sont toujours de nature asynchrone par définition.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=1-3`

</details>

<!-- QID:9dbefc479610 -->
### L'espace d'adressage est l'ensemble des adresses que le processeur peut ____.  <sup>p. 4–5</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** accéder

**Pourquoi :** Définition de l'espace d'adressage dans le contexte du processeur.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=4-5`

</details>

<!-- QID:07fcaa5fadb1 -->
### Quel est le rôle principal de la MMU ?  <sup>p. 4–5</sup>

**Choix :**

- A) Gérer l'exécution des applications
- B) Traduire une adresse virtuelle en une adresse physique
- C) Contrôler l'accès au matériel
- D) Augmenter la vitesse du processeur

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** La MMU est spécifiquement responsable de la traduction des adresses.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=4-5`

</details>

<!-- QID:c6792c01c2da -->
### Vrai ou Faux: Les instructions sensibles peuvent être exécutées par n'importe quelle application.  <sup>p. 4–5</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Seules les instructions sensibles peuvent être exécutées par le noyau, pas par les applications.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=4-5`

</details>

<!-- QID:d33d28f3597a -->
### Pourquoi est-il important que les applications ne puissent pas interférer avec d'autres applications en cours d'exécution ?  <sup>p. 4–5</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Il est crucial pour la sécurité au niveau applicatif, afin d'éviter des interférences illicites qui pourraient compromettre le fonctionnement des autres applications et du système d'exploitation.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=4-5`

</details>

<!-- QID:d30a9dd2eb3e -->
### Quel type d'instructions ne peut être exécuté que par le noyau ?  <sup>p. 4–5</sup>

**Choix :**

- A) Instructions d'accès I/O
- B) Instructions de modification du registre d'état
- C) Instructions privilégiées
- D) Instructions de calcul

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C

**Pourquoi :** Les instructions privilégiées sont réservées au noyau pour garantir la sécurité du système.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=4-5`

</details>

<!-- QID:6b9478513331 -->
### Le passage du mode kernel en mode user s'effectue en modifiant le ______ du processeur.  <sup>p. 6–7</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** registre d'état

**Pourquoi :** Le registre d'état est essentiel pour changer les modes d'exécution du CPU.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=6-7`

</details>

<!-- QID:48e733961b0c -->
### Quel type d'interruption est déclenché par l'exécution d'une instruction par le processeur ?  <sup>p. 6–7</sup>

**Choix :**

- A) Interruption matérielle
- B) Interruption logicielle
- C) Interruption asynchrone
- D) Interruption synchrone

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** L'interruption logicielle est causée par des exceptions lors de l'exécution d'instructions.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=6-7`

</details>

<!-- QID:c0fcb7d1f921 -->
### Le mode utilisateur permet d'exécuter des instructions sensibles.  <sup>p. 6–7</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Le mode utilisateur ne permet pas l'exécution d'instructions sensibles, seul le mode noyau le permet.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=6-7`

</details>

<!-- QID:4653a1357866 -->
### Quelles sont les différences principales entre une interruption matérielle et une interruption logicielle ?  <sup>p. 6–7</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Une interruption matérielle est asynchrone et provient d'un périphérique, tandis qu'une interruption logicielle est synchrone et est causée par l'exécution d'une instruction qui entraîne une exception.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=6-7`

</details>

<!-- QID:8567a0c38a64 -->
### Quel est le rôle d'une routine de service (ISR) lors d'une interruption ?  <sup>p. 6–7</sup>

**Choix :**

- A) Terminer le programme
- B) Exécuter une fonction spécifique en réponse à l'interruption
- C) Modifier le registre d'état
- D) Passer en mode utilisateur

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** La routine de service est conçue pour gérer les interruptions et exécuter des tâches spécifiques.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=6-7`

</details>

<!-- QID:ddf93ad2e039 -->
### Quel composant est responsable de la gestion des interruptions avant qu'elles n'atteignent le processeur ?  <sup>p. 8–9</sup>

**Choix :**

- A) A: Processeur
- B) B: Contrôleur d'interruption
- C) C: Mémoire
- D) D: Périphérique

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Le contrôleur d'interruption gère les lignes d'interruption et permet une gestion efficace des interruptions avant qu'elles ne soient transmises au CPU.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=8-9`

</details>

<!-- QID:10ee8eceb08a -->
### Vrai ou Faux: Le vecteur d'interruption associe directement l'adresse de la routine de service au numéro d'interruption.  <sup>p. 8–9</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Le vecteur d'interruption utilise une indirection pour associer un numéro d'interruption à l'adresse de la routine de service, ce qui permet une flexibilité entre différents systèmes d'exploitation.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=8-9`

</details>

<!-- QID:65a1f3eec711 -->
### Lorsqu'une interruption est reçue, le CPU doit d'abord _____ l'exécution en cours avant de passer en mode noyau.  <sup>p. 8–9</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** interrompre

**Pourquoi :** Le CPU doit terminer l'instruction en cours pour pouvoir exécuter la routine de service associée à l'interruption.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=8-9`

</details>

<!-- QID:6d74cba8af3e -->
### Comment les processeurs multicœurs gèrent-ils les interruptions ?  <sup>p. 8–9</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Les processeurs multicœurs utilisent un contrôleur d'interruption local à chaque cœur pour dispatcher les interruptions. Cela permet d'équilibrer la charge des interruptions entre les cœurs de calcul, améliorant ainsi l'efficacité du traitement.

**Pourquoi :** Cette gestion permet d'optimiser les performances en répartissant les interruptions sur plusieurs unités de traitement.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=8-9`

</details>

<!-- QID:c199cc12c392 -->
### Un système d'exploitation doit fournir une interface conviviale, performante et sécurisée aux __________.  <sup>p. 10–11</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** applications utilisateur

**Pourquoi :** C'est une des deux perspectives selon lesquelles un OS est défini.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=10-11`

</details>

<!-- QID:e0679927314b -->
### Quelle architecture d'OS place tous les sous-systèmes dans l'espace noyau?  <sup>p. 10–11</sup>

**Choix :**

- A) Monolithique
- B) Micronoyau
- C) Client-serveur
- D) Distribué

<details>
<summary>Afficher la réponse</summary>

**Réponse :** A

**Pourquoi :** L'architecture monolithique consiste à regrouper tous les sous-systèmes dans l'espace noyau.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=10-11`

</details>

<!-- QID:e004f10eab2d -->
### L'architecture micronoyau offre une meilleure sécurité au niveau des applications.  <sup>p. 10–11</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Vrai

**Pourquoi :** L'architecture micronoyau est conçue pour améliorer la sécurité des applications en séparant les sous-systèmes.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=10-11`

</details>

<!-- QID:a02f24fc7f76 -->
### Quelles sont les deux grandes architectures de systèmes d'exploitation mentionnées dans le cours?  <sup>p. 10–11</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Les deux grandes architectures de systèmes d'exploitation sont l'architecture monolithique et l'architecture micronoyau.

**Pourquoi :** Ces deux architectures sont fondamentales pour comprendre le fonctionnement des systèmes d'exploitation.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=10-11`

</details>

<!-- QID:f7777c0cc689 -->
### Quel est un inconvénient de l'architecture monolithique?  <sup>p. 10–11</sup>

**Choix :**

- A) Performance accrue
- B) Simplicité d'accès
- C) Problèmes liés à la sécurité d'exécution
- D) Extensibilité aisée

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C

**Pourquoi :** L'architecture monolithique, bien que performante, présente des risques de sécurité car tous les sous-systèmes sont dans l'espace noyau.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=10-11`

</details>

<!-- QID:d5ef54009563 -->
### Les appels système nécessitent l'utilisation d'une __________ dédiée.  <sup>p. 10–11</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** instruction machine

**Pourquoi :** Les appels système sont des mécanismes particuliers qui nécessitent une instruction machine spécifique pour être traités.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=10-11`

</details>

<!-- QID:bec78f6071f8 -->
### L'architecture micronoyau est beaucoup plus ______ que l'architecture monolithique.  <sup>p. 12–14</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** sécurisée

**Pourquoi :** L'architecture micronoyau minimise les fonctionnalités dans l'espace noyau, augmentant ainsi la sécurité.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=12-14`

</details>

<!-- QID:52b5be424e54 -->
### Quel est l'avantage principal de l'architecture micronoyau par rapport à l'architecture monolithique?  <sup>p. 12–14</sup>

**Choix :**

- A) A. Performances élevées
- B) B. Sécurité accrue
- C) C. Simplicité
- D) D. Coût réduit

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** L'architecture micronoyau réduit les fonctionnalités dans l'espace noyau, rendant le système moins susceptible de planter.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=12-14`

</details>

<!-- QID:46cac129772d -->
### L'architecture de Windows Vista est entièrement de type micronoyau.  <sup>p. 12–14</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Windows Vista utilise une architecture hybride, combinant des éléments de micronoyau et de monolithique.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=12-14`

</details>

<!-- QID:8aa9041f41c2 -->
### Qu'est-ce que l'approche client-serveur dans le contexte de l'architecture micronoyau?  <sup>p. 12–14</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** L'approche client-serveur permet une communication claire entre les sous-systèmes et les processus utilisateurs, en spécifiant les interfaces et les protocoles de communication.

**Pourquoi :** Cette approche est essentielle pour maintenir la séparation et la sécurité dans un système d'exploitation basé sur un micronoyau.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=12-14`

</details>

<!-- QID:7ea854c35e74 -->
### Quel type d'architecture est décrit comme un compromis entre les architectures monolithique et micronoyau?  <sup>p. 12–14</sup>

**Choix :**

- A) A. Architecture monolithique
- B) B. Architecture micronoyau
- C) C. Architecture hybride
- D) D. Architecture distribuée

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C

**Pourquoi :** L'architecture hybride combine des éléments des deux types pour optimiser performances et sécurité.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=12-14`

</details>

<!-- QID:5377f930c63d -->
### Dans une architecture de type micronoyau, les services utilisateur et le noyau sont conservés dans un espace d'adressage _____.  <sup>p. 15–17</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** séparé

**Pourquoi :** C'est une caractéristique fondamentale des architectures de type micronoyau.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=15-17`

</details>

<!-- QID:d318dd24f80d -->
### Un micro-noyau est plus gros qu'un noyau monolithique.  <sup>p. 15–17</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Les micro-noyaux sont généralement plus petits que les noyaux monolithiques.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=15-17`

</details>

<!-- QID:da7ee30730ff -->
### Quelles sont les principales différences entre un micro-noyau et un noyau monolithique en termes de sécurité ?  <sup>p. 15–17</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Dans un micro-noyau, si un service tombe en panne, cela n'affecte pas nécessairement le fonctionnement du système entier. En revanche, dans un noyau monolithique, une panne de service peut entraîner un blocage complet du système.

**Pourquoi :** Cette distinction est cruciale pour comprendre les implications de chaque architecture sur la stabilité du système.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=15-17`

</details>

<!-- QID:c5faad2b3788 -->
### Quel est l'impact de la taille du code nécessaire pour écrire un micro-noyau par rapport à un noyau monolithique ?  <sup>p. 15–17</sup>

**Choix :**

- A) Moins de code
- B) Autant de code
- C) Plus de code
- D) Aucun code

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C

**Pourquoi :** La complexité et la séparation des services dans un micro-noyau nécessitent généralement plus de code.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=15-17`

</details>
