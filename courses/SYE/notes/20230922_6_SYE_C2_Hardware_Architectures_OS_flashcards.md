---
course: "SYE"
generated_at: "2025-09-17T14:19:25"
---

# Flashcards – SYE

> Astuce : cliquez pour dérouler la réponse.

<!-- QID:9954485d7da4 -->
### Quel est le rôle fondamental d'un système d'exploitation en matière de sécurité applicative ?  <sup>p. 1–3</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Le rôle fondamental d'un système d'exploitation est de garantir que les applications ne peuvent pas interférer illicitement entre elles et ne peuvent pas accéder au matériel de manière non autorisée.

**Pourquoi :** Cela permet de protéger le noyau de l'OS et d'assurer un fonctionnement sécurisé des applications.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=1-3`

</details>

<!-- QID:8d3a5d5de4e2 -->
### Quelles instructions ne peuvent être exécutées que par le noyau du système d'exploitation ?  <sup>p. 1–3</sup>

**Choix :**

- A) Instructions de base
- B) Instructions sensibles
- C) Instructions de contrôle
- D) Instructions de gestion

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Les instructions sensibles sont réservées au noyau pour garantir la sécurité et la protection du système.

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

<!-- QID:6a134efa9e88 -->
### Les requêtes en provenance de l'extérieur vers le processeur sont typiquement des __________.  <sup>p. 1–3</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** interruptions matérielles

**Pourquoi :** Ces interruptions provoquent l'interruption du programme en cours et redirigent l'exécution du code.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=1-3`

</details>

<!-- QID:5fb7f842a4f4 -->
### Qu'est-ce que l'architecture de Von Neumann et quels sont ses composants principaux ?  <sup>p. 1–3</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** L'architecture de Von Neumann est un modèle d'architecture matérielle qui comprend le CPU, l'unité de contrôle (CU), l'unité arithmétique et logique (ALU), les registres, la mémoire, et les entrées/sorties (IO).

**Pourquoi :** Ces composants interagissent pour exécuter des programmes et traiter des données.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=1-3`

</details>

<!-- QID:327ea50169d0 -->
### Quel est le rôle principal de la MMU ?  <sup>p. 4–5</sup>

**Choix :**

- A) Gérer les périphériques
- B) Traduire une adresse virtuelle en une adresse physique
- C) Exécuter des instructions sensibles
- D) Contrôler l'accès au matériel

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** La MMU est responsable de la traduction des adresses pour permettre la virtualisation.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=4-5`

</details>

<!-- QID:eba2dd6a8b9d -->
### Vrai ou Faux: Les instructions sensibles peuvent être exécutées par n'importe quelle application.  <sup>p. 4–5</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Seules les instructions sensibles peuvent être exécutées par le noyau, pas par les applications.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=4-5`

</details>

<!-- QID:c1cb6c60074e -->
### Pourquoi est-il important que les applications ne puissent pas interférer entre elles ?  <sup>p. 4–5</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Il est crucial pour la sécurité et la stabilité du système d'exploitation que les applications ne puissent pas interférer, afin d'éviter des comportements illicites et de protéger les ressources matérielles.

**Pourquoi :** Cela garantit la sécurité au niveau applicatif.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=4-5`

</details>

<!-- QID:aabb7f119f49 -->
### Quelles zones mémoires sont protégées par le processeur ?  <sup>p. 4–5</sup>

**Choix :**

- A) Régions contenant des données utilisateurs
- B) Régions contenant du code de l'OS
- C) Régions de cache
- D) Régions de mémoire vive

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Les régions contenant du code de l'OS sont protégées pour éviter les accès non autorisés.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=4-5`

</details>

<!-- QID:280bb1ad3e91 -->
### Le passage du mode kernel en mode user s'effectue en modifiant le _______ d'état du processeur.  <sup>p. 6–7</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** registre

**Pourquoi :** Le registre d'état est essentiel pour changer de mode d'exécution.

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

<!-- QID:3a9c94c8690f -->
### Le mode utilisateur permet d'exécuter du code au niveau du noyau de l'OS.  <sup>p. 6–7</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Le mode utilisateur est distinct du mode noyau, qui exécute le code au niveau de l'OS.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=6-7`

</details>

<!-- QID:5ba13f0b1646 -->
### Quelles sont les différences entre une interruption matérielle et une interruption logicielle ?  <sup>p. 6–7</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Une interruption matérielle est asynchrone et provient d'un périphérique, tandis qu'une interruption logicielle est synchrone et résulte de l'exécution d'une instruction par le processeur.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=6-7`

</details>

<!-- QID:f6be474a9110 -->
### Quel événement ne peut pas provoquer un passage du mode utilisateur au mode noyau ?  <sup>p. 6–7</sup>

**Choix :**

- A) Interruption matérielle
- B) Interruption logicielle
- C) Exécution d'une instruction normale
- D) Appel système

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C

**Pourquoi :** Le passage du mode user au mode kernel nécessite une interruption, pas une instruction normale.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=6-7`

</details>

<!-- QID:eae5fce92296 -->
### Lors d'une interruption, une fonction particulière appelée _______ de service est immédiatement exécutée.  <sup>p. 6–7</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** routine

**Pourquoi :** La routine de service gère le traitement de l'interruption.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=6-7`

</details>

<!-- QID:f3465cf01f10 -->
### Chaque périphérique dispose de sa propre ligne d'interruption, qui est reliée à un __________ permettant une gestion des interruptions plus efficace.  <sup>p. 8–9</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** contrôleur d'interruption

**Pourquoi :** Le contrôleur d'interruption gère les interruptions avant qu'elles n'atteignent le processeur.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=8-9`

</details>

<!-- QID:bf1216ad906a -->
### Quel est le rôle du vecteur d'interruption ?  <sup>p. 8–9</sup>

**Choix :**

- A) A. Il masque les interruptions
- B) B. Il associe à un numéro l'adresse de la routine de service.
- C) C. Il gère les caches
- D) D. Il exécute le code d'application

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Le vecteur d'interruption permet au processeur de localiser la routine de service correspondante.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=8-9`

</details>

<!-- QID:1b975f60fb65 -->
### Vrai ou Faux: Le processeur doit terminer l'instruction en cours avant de passer en mode noyau.  <sup>p. 8–9</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Vrai

**Pourquoi :** Le processeur doit d'abord terminer l'instruction en cours avant d'exécuter la routine de service.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=8-9`

</details>

<!-- QID:63d5177b2355 -->
### Qu'est-ce qu'une routine de service d'interruption (ISR) et quel est son rôle ?  <sup>p. 8–9</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Une ISR est une routine qui s'exécute en réponse à une interruption. Son rôle est de traiter immédiatement l'événement qui a causé l'interruption, comme acquitter l'interruption.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=8-9`

</details>

<!-- QID:ac0f6773af87 -->
### Quelle architecture est la plus utilisée pour les processeurs multicœurs ?  <sup>p. 8–9</sup>

**Choix :**

- A) A. MPP
- B) B. SMP
- C) C. NUMA
- D) D. RISC

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** SMP est le modèle standard pour répartir la mémoire entre plusieurs cœurs CPU.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=8-9`

</details>

<!-- QID:b8d0c8d89971 -->
### Vrai ou Faux: Chaque cœur de CPU dispose de sa propre mémoire cache, mais partage la mémoire RAM.  <sup>p. 8–9</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Vrai

**Pourquoi :** Chaque cœur a ses propres caches, mais la mémoire RAM est partagée entre tous les cœurs.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=8-9`

</details>

<!-- QID:598e76459354 -->
### Un système d'exploitation doit fournir une interface conviviale, performante et sécurisée aux applications utilisateur, ainsi que piloter le __________ en général.  <sup>p. 10–11</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** matériel

**Pourquoi :** L'OS joue un rôle essentiel dans la gestion du matériel et des applications.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=10-11`

</details>

<!-- QID:25da317c5465 -->
### Quelle architecture d'OS place tous les sous-systèmes dans l'espace noyau?  <sup>p. 10–11</sup>

**Choix :**

- A) Monolithique
- B) Micronoyau
- C) Client-serveur
- D) Distribué

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Monolithique

**Pourquoi :** L'architecture monolithique regroupe tous les sous-systèmes dans l'espace noyau, ce qui permet un accès rapide mais pose des problèmes de sécurité.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=10-11`

</details>

<!-- QID:a2782964b89c -->
### Vrai ou Faux: L'architecture micronoyau offre de meilleures performances que l'architecture monolithique.  <sup>p. 10–11</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** L'architecture monolithique est généralement plus performante car elle réduit le nombre de couches d'abstraction.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=10-11`

</details>

<!-- QID:c501347a6dcf -->
### Quelles sont les principales différences entre l'architecture monolithique et l'architecture micronoyau?  <sup>p. 10–11</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** L'architecture monolithique regroupe tous les sous-systèmes dans l'espace noyau, offrant de meilleures performances mais des risques de sécurité. L'architecture micronoyau, en revanche, place un minimum de sous-systèmes dans l'espace noyau, améliorant la sécurité et l'extensibilité, mais limitant les performances.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=10-11`

</details>

<!-- QID:4b625e03665f -->
### L'architecture micronoyau est plus sécurisée que l'architecture ________.  <sup>p. 12–14</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** monolithique

**Pourquoi :** L'architecture micronoyau tourne avec un minimum de fonctionnalités dans l'espace noyau, ce qui augmente la sécurité.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=12-14`

</details>

<!-- QID:c5c6b3216884 -->
### Quel type d'architecture est Windows Vista selon l'extrait?  <sup>p. 12–14</sup>

**Choix :**

- A) Monolithique
- B) Micronoyau
- C) Hybride
- D) Client-serveur

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C

**Pourquoi :** Windows Vista combine des éléments de l'architecture monolithique et micronoyau, ce qui en fait une architecture hybride.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=12-14`

</details>

<!-- QID:33c0aa3847f0 -->
### Vrai ou Faux: Dans une architecture micronoyau, les sous-systèmes ont un accès direct aux structures du noyau.  <sup>p. 12–14</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Les sous-systèmes n'ont pas directement accès aux structures du noyau, ce qui renforce la sécurité et l'isolation.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=12-14`

</details>

<!-- QID:9969c257efd0 -->
### Quelle est la principale caractéristique de la communication entre sous-systèmes dans une architecture micronoyau?  <sup>p. 12–14</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** La communication entre sous-systèmes doit être basée sur une approche client-serveur, permettant une spécification claire de l'interface et du protocole.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=12-14`

</details>

<!-- QID:891a532d81a4 -->
### Dans une architecture de type micronoyau, les services utilisateur et les services du noyau sont conservés dans un espace d'adressage __________.  <sup>p. 15–17</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** séparé

**Pourquoi :** C'est une caractéristique fondamentale des micro-noyaux qui vise à améliorer la sécurité et la modularité.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=15-17`

</details>

<!-- QID:8123c03de85b -->
### Quel est un exemple de système d'exploitation utilisant un noyau monolithique ?  <sup>p. 15–17</sup>

**Choix :**

- A) QNX
- B) Mac OS X
- C) Microsoft Windows
- D) Singularity

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C

**Pourquoi :** Microsoft Windows est un exemple classique de noyau monolithique, contrairement à des systèmes comme QNX qui utilisent un micro-noyau.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=15-17`

</details>

<!-- QID:a25099157507 -->
### Les micro-noyaux sont généralement plus gros que les noyaux monolithiques.  <sup>p. 15–17</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Les micro-noyaux sont en fait plus petits que les noyaux monolithiques, ce qui est une de leurs caractéristiques.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=15-17`

</details>

<!-- QID:9bfd80169d7b -->
### Quelles sont les principales différences entre un micro-noyau et un noyau monolithique en termes d'exécution et de sécurité ?  <sup>p. 15–17</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Les micro-noyaux ont une exécution plus lente mais sont plus sécurisés car les services sont séparés. En revanche, les noyaux monolithiques offrent une exécution rapide mais si un service échoue, tout le système peut se bloquer.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=15-17`

</details>

<!-- QID:ea78974418ff -->
### Quel composant est typiquement associé à l'espace utilisateur dans une architecture Linux ?  <sup>p. 15–17</sup>

**Choix :**

- A) Linux kernel
- B) systemd
- C) LibreOffice
- D) X11

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C

**Pourquoi :** LibreOffice est une application utilisateur qui fonctionne dans l'espace utilisateur, contrairement aux composants du noyau qui fonctionnent dans l'espace noyau.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=15-17`

</details>

<!-- QID:eeca31cea9c6 -->
### Le noyau monolithique est facilement extensible.  <sup>p. 15–17</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Le noyau monolithique est généralement plus difficile à étendre par rapport à un micro-noyau, qui est conçu pour être extensible.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=15-17`

</details>
