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
