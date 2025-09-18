---
course: "SYE"
generated_at: "2025-09-18T07:35:18"
source_pdf: "courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf"
---

# Flashcards – SYE

---
### Résumé essentiel

Un système d'exploitation (OS) joue un rôle crucial en assurant la sécurité applicative, empêchant les applications d'interférer entre elles et d'accéder au matériel de manière non autorisée. Les microprocesseurs modernes intègrent des modes d'exécution, comme le mode utilisateur et le mode noyau, qui restreignent l'exécution d'instructions sensibles au noyau de l'OS. L'architecture de Von Neumann, qui comprend un CPU, une unité de contrôle, une unité arithmétique et logique, ainsi que des mémoires et des entrées/sorties, est fondamentale pour comprendre le fonctionnement des systèmes informatiques. 

Les accès mémoire sont régulés par la Memory Management Unit (MMU), qui traduit les adresses virtuelles en adresses physiques, permettant ainsi la virtualisation. Les interruptions, qu'elles soient matérielles ou logicielles, permettent une communication asynchrone entre les périphériques et le CPU, nécessitant des routines de service (ISR) pour gérer les événements. Les architectures d'OS se divisent principalement en architectures monolithiques et micronoyaux, chacune ayant ses avantages et inconvénients en termes de performances et de sécurité. 

Les appels système (syscalls) sont essentiels pour la communication entre l'espace utilisateur et l'espace noyau, garantissant une séparation claire des espaces d'adressage. Les systèmes d'exploitation modernes, comme Windows et Mac OS X, adoptent souvent une architecture hybride pour équilibrer performances et sécurité. Enfin, la gestion de la cohérence des caches est cruciale dans les systèmes multicœurs pour éviter les incohérences de données.

### À retenir absolument
- Un OS assure la sécurité applicative en isolant les applications et en contrôlant l'accès au matériel.
- Les modes d'exécution (utilisateur et noyau) protègent l'intégrité du système en restreignant l'accès aux instructions sensibles.
- La MMU gère la translation d'adresses virtuelles en adresses physiques, permettant la virtualisation.
- Les interruptions permettent une communication asynchrone entre périphériques et CPU, nécessitant des routines de service pour leur gestion.
- Les architectures d'OS se classifient en monolithiques et micronoyaux, chacune ayant des compromis entre performances et sécurité.

---

<!-- QID:24e54434cec2 -->
### Quel est le rôle fondamental d'un système d'exploitation en matière de sécurité ?  <sup>p. 1–3</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Garantir que les applications ne peuvent pas interférer illicitement entre elles et ne peuvent pas accéder au matériel sans autorisation.

**Pourquoi :** Cela permet de protéger les ressources système et d'assurer un fonctionnement stable et sécurisé des applications.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=1-3`

</details>

<!-- QID:ac510f17f809 -->
### Les instructions sensibles ne peuvent être exécutées que par le _____ et non pas par les applications.  <sup>p. 1–3</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** noyau

**Pourquoi :** Le noyau a des privilèges élevés pour gérer les ressources système et protéger l'intégrité du système d'exploitation.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=1-3`

</details>

<!-- QID:f83b3c1010ea -->
### Quels types de requêtes un système d'exploitation traite-t-il principalement ?  <sup>p. 1–3</sup>

**Choix :**

- A) Requêtes de l'utilisateur vers le système
- B) Requêtes du processeur vers l'extérieur
- C) Requêtes de l'extérieur vers le processeur
- D) Requêtes de maintenance du système

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B|C

**Pourquoi :** Ces deux types de requêtes sont essentiels pour la communication entre le processeur et les périphériques.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=1-3`

</details>

<!-- QID:64385a9cb424 -->
### Les requêtes en provenance de l'extérieur vers le processeur sont toujours de nature synchrones.  <sup>p. 1–3</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Ces requêtes sont de nature asynchrone, car elles proviennent d'événements externes comme les interruptions matérielles.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=1-3`

</details>

<!-- QID:dea6de149b31 -->
### Quelles zones mémoires ne peuvent pas être accédées par n'importe quelle application ?  <sup>p. 1–3</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Certaines zones mémoires dédiées à la gestion de périphériques.

**Pourquoi :** Cela empêche les applications de compromettre la sécurité et la stabilité du système en accédant à des zones critiques.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=1-3`

</details>

<!-- QID:42f9539c40f7 -->
### Quel composant est chargé du séquençage des opérations dans l'architecture de Von Neumann ?  <sup>p. 1–3</sup>

**Choix :**

- A) Unité arithmétique et logique (ALU)
- B) Registres
- C) Unité de contrôle (CU)
- D) Mémoire

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C

**Pourquoi :** L'unité de contrôle est responsable de la coordination des opérations du processeur.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=1-3`

</details>

<!-- QID:d3c2311948c0 -->
### Quels sont les types de mémoire mentionnés dans l'architecture matérielle ?  <sup>p. 1–3</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Caches, RAM, GPU.

**Pourquoi :** Ces types de mémoire jouent un rôle crucial dans le stockage temporaire et l'accès rapide aux données.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=1-3`

</details>

<!-- QID:15bb1f6bc2ca -->
### Qu'est-ce qu'une MMU ?  <sup>p. 4–5</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** La MMU (Memory Management Unit) est une unité matérielle qui traduit les adresses virtuelles en adresses physiques.

**Pourquoi :** Elle permet au processeur d'accéder à la mémoire de manière sécurisée et efficace en utilisant des adresses virtuelles.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=4-5`

</details>

<!-- QID:e6cb99a852fd -->
### Un espace d'adressage est l'ensemble des adresses que le processeur peut ____.  <sup>p. 4–5</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** accéder

**Pourquoi :** Cette définition est essentielle pour comprendre comment le processeur interagit avec la mémoire.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=4-5`

</details>

<!-- QID:18bc07cb19cb -->
### Quel est le rôle principal de la MMU dans un système d'exploitation ?  <sup>p. 4–5</sup>

**Choix :**

- A) Gérer les entrées/sorties
- B) Traduire les adresses virtuelles en adresses physiques.
- C) Exécuter des instructions sensibles
- D) Accéder directement au matériel

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** La MMU est essentielle pour la gestion de la mémoire et la virtualisation, permettant au processeur d'utiliser des adresses virtuelles.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=4-5`

</details>

<!-- QID:37eded97bfa5 -->
### Les instructions sensibles peuvent être exécutées par n'importe quelle application.  <sup>p. 4–5</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Seul le noyau du système d'exploitation peut exécuter des instructions sensibles pour garantir la sécurité et la protection des ressources.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=4-5`

</details>

<!-- QID:9039bc7955fa -->
### Quels types d'instructions sont considérées comme sensibles ?  <sup>p. 4–5</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Les instructions privilégiées, d'accès I/O, de modification du registre d'état, et d'accès aux coprocesseurs.

**Pourquoi :** Ces instructions nécessitent des niveaux de privilège élevés pour éviter les abus et garantir la sécurité du système.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=4-5`

</details>

<!-- QID:5854951b853d -->
### Pourquoi est-il important de protéger certaines régions mémoire dans un système d'exploitation ?  <sup>p. 4–5</sup>

**Choix :**

- A) Pour améliorer la vitesse d'exécution
- B) Pour empêcher les applications d'interférer avec le noyau et d'accéder à des ressources critiques.
- C) Pour faciliter l'accès aux périphériques
- D) Pour réduire la consommation d'énergie

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** La protection des régions mémoire est cruciale pour maintenir la stabilité et la sécurité du système d'exploitation.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=4-5`

</details>

<!-- QID:dd2da1ef0843 -->
### Quels sont les deux modes d'exécution d'un processeur?  <sup>p. 6–7</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Le mode utilisateur (user mode) et le mode noyau (kernel mode).

**Pourquoi :** Ces modes permettent de différencier l'exécution de code au niveau du noyau de celle au niveau des applications, garantissant ainsi la sécurité et la stabilité du système.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=6-7`

</details>

<!-- QID:9a51c49ca143 -->
### Le passage du mode kernel en mode user s'effectue en modifiant le registre d'état du processeur, ce qui nécessite l'exécution d'une instruction _____ .  <sup>p. 6–7</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** sensible

**Pourquoi :** Cette instruction sensible est nécessaire pour assurer que seules des opérations autorisées peuvent changer le mode d'exécution.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=6-7`

</details>

<!-- QID:ec6017f70926 -->
### Quel type d'interruption est déclenché par l'exécution d'une instruction par le processeur?  <sup>p. 6–7</sup>

**Choix :**

- A) Interruption matérielle
- B) Interruption logicielle
- C) Interruption asynchrone
- D) Interruption synchrone

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Les interruptions logicielles, également appelées exceptions ou traps, se produisent en réponse à des erreurs d'exécution ou à des instructions spécifiques.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=6-7`

</details>

<!-- QID:03f33ff26909 -->
### Qu'est-ce qu'une routine de service d'interruption (ISR)?  <sup>p. 6–7</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C'est une fonction qui est exécutée en réponse à une interruption, permettant de traiter l'événement qui a déclenché l'interruption.

**Pourquoi :** Les ISR sont essentielles pour gérer les interruptions, qu'elles soient matérielles ou logicielles, et permettent au système d'exploitation de répondre rapidement aux événements.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=6-7`

</details>

<!-- QID:523d6f5f4ee3 -->
### Quelle est la principale différence entre une interruption matérielle et une interruption logicielle?  <sup>p. 6–7</sup>

**Choix :**

- A) L'asynchronie
- B) La synchronie
- C) Le type d'instruction
- D) Le niveau d'accès

<details>
<summary>Afficher la réponse</summary>

**Réponse :** A

**Pourquoi :** Les interruptions matérielles sont asynchrones car elles peuvent survenir à tout moment, tandis que les interruptions logicielles sont synchrones et se produisent en réponse à des instructions spécifiques.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=6-7`

</details>

<!-- QID:a57582742579 -->
### Le contrôleur d'interruption permet de ________ les interruptions et de les ________ au CPU.  <sup>p. 8–9</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** prioriser, propager

**Pourquoi :** Cela permet une gestion efficace des interruptions, surtout lorsque plusieurs interruptions se produisent simultanément.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=8-9`

</details>

<!-- QID:e77d33da87bd -->
### Quel est le rôle principal du vecteur d'interruption ?  <sup>p. 8–9</sup>

**Choix :**

- A) Il gère la mémoire cache.
- B) Il associe un numéro d'interruption à l'adresse de la routine de service.
- C) Il masque les interruptions.
- D) Il priorise les tâches en cours.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Le vecteur d'interruption est crucial pour que le processeur sache où trouver la routine de service correspondante à une interruption donnée.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=8-9`

</details>

<!-- QID:256c32ae1d40 -->
### Les processeurs multicœurs utilisent une architecture SMP pour partager la mémoire entre les cœurs.  <sup>p. 8–9</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Vrai

**Pourquoi :** L'architecture SMP permet à chaque cœur d'accéder à une mémoire partagée, facilitant ainsi l'exécution simultanée de plusieurs tâches.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=8-9`

</details>

<!-- QID:40182018d8d1 -->
### Quelles sont les implications de l'utilisation de caches individuels dans une architecture multicœur ?  <sup>p. 8–9</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Cela nécessite une gestion de la cohérence des caches pour s'assurer que les données modifiées dans un cache soient mises à jour dans les autres caches.

**Pourquoi :** Sans cette gestion, des incohérences peuvent survenir, entraînant des erreurs dans le traitement des données.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=8-9`

</details>

<!-- QID:60ae68ecc45f -->
### Quel est l'avantage principal d'un contrôleur d'interruption local dans une architecture multicœur ?  <sup>p. 8–9</sup>

**Choix :**

- A) Il augmente la vitesse d'exécution des instructions.
- B) Il permet de dispatcher les interruptions sur plusieurs cœurs pour équilibrer la charge.
- C) Il réduit le besoin de mémoire cache.
- D) Il simplifie la gestion des processus.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Cela améliore l'efficacité du traitement des interruptions, ce qui est crucial pour les performances des systèmes multicœurs.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=8-9`

</details>

<!-- QID:54c274998ecb -->
### Quels sont les deux espaces principaux dans l'architecture moderne d'un OS ?  <sup>p. 10–11</sup>

**Choix :**

- A) Espaces utilisateur et espaces noyau
- B) Espaces mémoire et espaces disque
- C) Espaces réseau et espaces local
- D) Espaces application et espaces système

<details>
<summary>Afficher la réponse</summary>

**Réponse :** A

**Pourquoi :** Ces deux espaces sont essentiels pour la séparation des privilèges et la gestion des ressources dans un système d'exploitation.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=10-11`

</details>

<!-- QID:7677e828ce04 -->
### L'architecture monolithique d'un OS offre une meilleure sécurité que l'architecture micronoyau.  <sup>p. 10–11</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** L'architecture monolithique, bien qu'elle offre de meilleures performances, présente des risques de sécurité plus élevés car tous les sous-systèmes sont dans l'espace noyau, ce qui peut entraîner des plantages du système.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=10-11`

</details>

<!-- QID:413ca83e7472 -->
### Dans une architecture monolithique, tous les sous-systèmes, y compris les ______, sont localisés dans l'espace noyau.  <sup>p. 10–11</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** drivers

**Pourquoi :** Les drivers sont essentiels pour la communication entre le matériel et le système d'exploitation, et leur présence dans l'espace noyau facilite l'accès aux ressources système.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=10-11`

</details>

<!-- QID:212832168572 -->
### Quels sont les avantages de l'architecture micronoyau ?  <sup>p. 10–11</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** L'architecture micronoyau offre une sécurité accrue au niveau des applications, une extensibilité aisée et une meilleure isolation des processus.

**Pourquoi :** Ces avantages proviennent de la séparation des sous-systèmes dans l'espace utilisateur, réduisant ainsi les risques de défaillance du système.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=10-11`

</details>

<!-- QID:21c68b85edce -->
### Quel est un inconvénient majeur de l'architecture micronoyau ?  <sup>p. 10–11</sup>

**Choix :**

- A) Performance accrue
- B) Simplicité d'accès
- C) Limitation dans les performances
- D) Sécurité renforcée

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C

**Pourquoi :** L'architecture micronoyau, en raison de sa structure à plusieurs couches, peut entraîner des surcoûts en termes de performances par rapport à une architecture monolithique.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=10-11`

</details>

<!-- QID:4846a019e70f -->
### Comment la séparation entre espace utilisateur et espace noyau est-elle réalisée ?  <sup>p. 10–11</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Elle est réalisée grâce à l'utilisation d'appels système (syscalls) qui nécessitent des instructions machine dédiées.

**Pourquoi :** Les appels système permettent aux applications de demander des services au noyau tout en maintenant une séparation sécurisée entre les deux espaces.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=10-11`

</details>

<!-- QID:020bb462c9f6 -->
### Qu'est-ce qu'une architecture micronoyau ?  <sup>p. 12–14</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Une architecture où un minimum de fonctionnalités tourne dans l'espace noyau, augmentant ainsi la sécurité du système.

**Pourquoi :** Cela réduit les risques de plantage du système en limitant les opérations critiques au noyau.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=12-14`

</details>

<!-- QID:306966918f6b -->
### Quels sont les avantages de l'architecture micronoyau par rapport à l'architecture monolithique ?  <sup>p. 12–14</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Elle offre une meilleure sécurité et un compartimentage des applications, réduisant les interférences entre elles.

**Pourquoi :** Le compartimentage permet de protéger les processus les uns des autres, ce qui est essentiel pour la stabilité du système.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=12-14`

</details>

<!-- QID:8c6e583455e8 -->
### Dans une architecture micronoyau, la communication entre sous-systèmes doit être basée sur une approche ________.  <sup>p. 12–14</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** client-serveur

**Pourquoi :** Cette approche permet une spécification claire des interfaces et des protocoles de communication.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=12-14`

</details>

<!-- QID:5eb8f325c530 -->
### Quel type d'architecture est Windows Vista selon l'extrait ?  <sup>p. 12–14</sup>

**Choix :**

- A) monolithique
- B) micronoyau
- C) hybride
- D) client-serveur

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C

**Pourquoi :** Windows Vista combine des éléments des architectures monolithique et micronoyau pour équilibrer performances et sécurité.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=12-14`

</details>

<!-- QID:ecee78b64a5b -->
### Vrai ou Faux : Dans une architecture micronoyau, les sous-systèmes ont un accès direct aux structures du noyau.  <sup>p. 12–14</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Les sous-systèmes n'ont pas d'accès direct au noyau, ce qui renforce la sécurité et la stabilité du système.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=12-14`

</details>

<!-- QID:e5b528994835 -->
### Comment la notion de processus contribue-t-elle à la sécurité dans une architecture micronoyau ?  <sup>p. 12–14</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Elle introduit un compartimentage des applications avec une séparation nette des espaces d'adressage.

**Pourquoi :** Cela empêche une application de nuire à une autre, augmentant ainsi la robustesse du système.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=12-14`

</details>

<!-- QID:dd3ed5d9867d -->
### Quelles sont les principales différences entre un micro-noyau et un noyau monolithique ?  <sup>p. 15–17</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Les micro-noyaux ont des services séparés dans des espaces d'adressage distincts, sont plus petits, extensibles et moins rapides. Les noyaux monolithiques ont des services dans le même espace d'adressage, sont plus gros, difficiles à étendre et plus rapides.

**Pourquoi :** Comprendre ces différences est essentiel pour évaluer les compromis en matière de performance et de sécurité dans la conception des systèmes d'exploitation.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=15-17`

</details>

<!-- QID:c703eb89038a -->
### Dans un micro-noyau, les services utilisateur et les services du noyau sont conservés dans un espace d'adressage ______.  <sup>p. 15–17</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** séparé

**Pourquoi :** Cette séparation contribue à la modularité et à la sécurité du système d'exploitation.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=15-17`

</details>

<!-- QID:0388a5ae803a -->
### Quel est un exemple de micro-noyau ?  <sup>p. 15–17</sup>

**Choix :**

- A) QNX
- B) Linux
- C) Windows
- D) Solaris

<details>
<summary>Afficher la réponse</summary>

**Réponse :** A

**Pourquoi :** QNX est un exemple typique de micro-noyau, tandis que Linux et Windows sont des noyaux monolithiques.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=15-17`

</details>

<!-- QID:65462b235187 -->
### Un noyau monolithique est généralement plus rapide qu'un micro-noyau.  <sup>p. 15–17</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Vrai

**Pourquoi :** Les noyaux monolithiques, ayant tous leurs services dans le même espace d'adressage, peuvent exécuter des opérations plus rapidement, contrairement aux micro-noyaux qui nécessitent des communications inter-processus.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=15-17`

</details>

<!-- QID:306750f9c5ea -->
### Quels sont les avantages d'un micro-noyau par rapport à un noyau monolithique ?  <sup>p. 15–17</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Les micro-noyaux sont plus extensibles et offrent une meilleure sécurité, car une panne d'un service n'affecte pas l'ensemble du système.

**Pourquoi :** Ces caractéristiques sont cruciales pour des systèmes nécessitant une haute disponibilité et une sécurité renforcée.

**Source :** `courses/SYE/data/pdf/20230922_6_SYE_C2_Hardware_Architectures_OS.pdf#p=15-17`

</details>
