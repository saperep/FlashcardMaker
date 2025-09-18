---
course: "PCO"
generated_at: "2025-09-18T11:58:59"
source_pdf: "courses/PCO/data/pdf/pco_polycopie.pdf"
---

# Flashcards – PCO

---
### Résumé essentiel

La programmation concurrente permet l'exécution simultanée de plusieurs tâches, optimisant ainsi l'utilisation des ressources. Il est crucial de distinguer entre la concurrence, qui gère plusieurs tâches intercalées sur un seul processeur, et le parallélisme, qui implique l'exécution simultanée sur plusieurs processeurs. Les processus, qui sont des instances d'un programme, contiennent des threads, unités d'exécution partageant le même espace mémoire. Le multi-threading améliore la réactivité des applications, mais nécessite une gestion rigoureuse des accès concurrents pour éviter des erreurs telles que les conditions de course.

Les mécanismes de synchronisation, comme les moniteurs et les sémaphores, sont essentiels pour gérer l'accès aux ressources partagées. Les lecteurs-rédacteurs, par exemple, permettent à plusieurs threads de lire simultanément tout en garantissant qu'un seul peut écrire à la fois. Les algorithmes d'exclusion mutuelle, comme ceux de Dekker et de Peterson, illustrent des approches pour éviter les interblocages et la famine, bien que leur mise en œuvre pratique soit complexe.

Les verrous (mutex) et les sémaphores sont des outils fondamentaux pour contrôler l'accès aux sections critiques, chaque méthode ayant ses avantages et inconvénients. Les erreurs fréquentes incluent l'inversion de l'ordre des opérations de sémaphore, ce qui peut entraîner des conditions de course. Enfin, la bibliothèque Pthread en C fournit des primitives pour la gestion des threads et des mécanismes de synchronisation, permettant de développer des applications concurrentes robustes.

### À retenir absolument

- La programmation concurrente optimise l'utilisation des ressources en exécutant plusieurs tâches simultanément.
- La distinction entre concurrence (intercalée) et parallélisme (simultané) est essentielle pour comprendre les mécanismes de gestion des tâches.
- Les moniteurs et sémaphores sont cruciaux pour la synchronisation et l'accès aux ressources partagées.
- Les erreurs fréquentes incluent les conditions de course et les interblocages, souvent causés par une mauvaise gestion des accès concurrents.
- La bibliothèque Pthread en C offre des outils pour créer et gérer des threads, ainsi que des mécanismes de synchronisation efficaces.

---

<!-- QID:48e267972a4b -->
### Qu'est-ce que la programmation concurrente ?  <sup>p. 1–3</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** La programmation concurrente est un paradigme qui permet l'exécution simultanée de plusieurs processus ou threads, facilitant ainsi la gestion des tâches qui peuvent être effectuées en parallèle.

**Pourquoi :** Elle est essentielle pour améliorer l'efficacité des programmes, surtout sur les systèmes multi-core.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=1-3`

</details>

<!-- QID:4fa611f40fa2 -->
### Un _______ est une unité d'exécution qui peut être gérée indépendamment par un planificateur.  <sup>p. 1–3</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** thread

**Pourquoi :** Les threads permettent de diviser un programme en plusieurs tâches légères, facilitant ainsi la gestion des ressources et l'exécution simultanée.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=1-3`

</details>

<!-- QID:2a2b4aadda95 -->
### Vrai ou Faux : Les threads partagent la même mémoire et les mêmes ressources que les processus.  <sup>p. 1–3</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Vrai

**Pourquoi :** Les threads d'un même processus partagent la mémoire et les ressources, ce qui les rend plus légers que les processus, mais cela nécessite une gestion prudente pour éviter les conflits.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=1-3`

</details>

<!-- QID:8201cbfd238b -->
### Quels sont les avantages du multi-threading ?  <sup>p. 1–3</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Les avantages du multi-threading incluent une meilleure utilisation des ressources CPU, une réactivité accrue des applications et la possibilité de gérer des tâches simultanément.

**Pourquoi :** Cela permet d'optimiser les performances des applications, surtout dans les environnements où les tâches peuvent être parallélisées.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=1-3`

</details>

<!-- QID:b07ef41fb61f -->
### Quel modèle de séparation d'un programme en plusieurs threads permet de déléguer des tâches à d'autres threads ?  <sup>p. 1–3</sup>

**Choix :**

- A) A. Modèle pipeline
- B) B. Modèle pair
- C) C. Modèle délégation
- D) D. Modèle séquentiel

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C

**Pourquoi :** Le modèle délégation permet à un thread de confier certaines tâches à d'autres threads, optimisant ainsi la gestion des ressources.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=1-3`

</details>

<!-- QID:da19b05f336c -->
### Qu'est-ce qu'un verrou en programmation concurrente ?  <sup>p. 1–3</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Un verrou est un mécanisme de synchronisation qui permet de contrôler l'accès à une ressource partagée par plusieurs threads, garantissant ainsi l'exclusion mutuelle.

**Pourquoi :** Les verrous sont essentiels pour éviter les conditions de course et garantir l'intégrité des données partagées.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=1-3`

</details>

<!-- QID:87c9347c0373 -->
### Qu'est-ce qu'un moniteur en programmation concurrente ?  <sup>p. 4</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Un moniteur est une abstraction de synchronisation qui permet de contrôler l'accès à des ressources partagées en garantissant qu'un seul thread peut exécuter un segment de code critique à la fois.

**Pourquoi :** Les moniteurs facilitent la gestion de la concurrence en encapsulant les données et les opérations qui les manipulent, réduisant ainsi les risques de conditions de course.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=4-4`

</details>

<!-- QID:df7aa27be3a1 -->
### Quel est l'objectif principal des moniteurs ?  <sup>p. 4</sup>

**Choix :**

- A) Augmenter la vitesse d'exécution
- B) Contrôler l'accès concurrent aux ressources partagées
- C) Réduire la consommation de mémoire
- D) Améliorer la lisibilité du code

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Les moniteurs sont conçus pour gérer la synchronisation entre threads, ce qui est essentiel pour éviter les conflits d'accès aux ressources partagées.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=4-4`

</details>

<!-- QID:0a1e938e1f4d -->
### Un moniteur permet de garantir que _____ peut exécuter un segment de code critique à la fois.  <sup>p. 4</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** un seul thread

**Pourquoi :** Cette propriété est cruciale pour éviter les conditions de course et assurer l'intégrité des données partagées.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=4-4`

</details>

<!-- QID:0c16323e8d81 -->
### Les moniteurs peuvent être implémentés à partir de sémaphores.  <sup>p. 4</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Vrai

**Pourquoi :** Les sémaphores peuvent être utilisés pour créer des moniteurs en contrôlant l'accès aux sections critiques, bien que les moniteurs offrent une abstraction plus élevée.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=4-4`

</details>

<!-- QID:90f16f6fa6aa -->
### Quels sont les avantages des moniteurs par rapport aux sémaphores ?  <sup>p. 4</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Les moniteurs offrent une interface plus simple et plus sécurisée pour la synchronisation, encapsulant les données et les opérations, ce qui réduit les erreurs de programmation.

**Pourquoi :** Cette encapsulation aide à prévenir les erreurs courantes telles que l'oubli de libérer un sémaphore, ce qui peut entraîner des blocages.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=4-4`

</details>

<!-- QID:e93bf61c8e6c -->
### Quelle fonction est utilisée pour créer un thread en utilisant la bibliothèque Pthread ?  <sup>p. 4</sup>

**Choix :**

- A) pthread_start()
- B) pthread_create()
- C) pthread_init()
- D) pthread_thread()

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** La fonction pthread_create() est spécifiquement conçue pour initialiser et démarrer un nouveau thread dans la bibliothèque Pthread.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=4-4`

</details>

<!-- QID:07d3fbadf0db -->
### Un processus peut être bloqué en attendant un événement ou un mutex.  <sup>p. 5–6</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Vrai

**Pourquoi :** Un processus peut se retrouver dans un état bloqué lorsqu'il attend que certaines conditions soient remplies, comme le relâchement d'un mutex ou la survenue d'un événement.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=5-6`

</details>

<!-- QID:79d9234bcba1 -->
### Un processus est caractérisé par un code, une pile, un tas, un identifiant unique et une ______.  <sup>p. 5–6</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** priorité

**Pourquoi :** La priorité permet au système d'exploitation de gérer l'allocation du temps processeur entre plusieurs processus en cours d'exécution.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=5-6`

</details>

<!-- QID:beb13e4b3da1 -->
### Qu'est-ce qu'un thread dans le contexte de la programmation concurrente ?  <sup>p. 5–6</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Un thread est une unité d'exécution au sein d'un processus, permettant l'exécution pseudo-parallèle de tâches.

**Pourquoi :** Les threads permettent de décomposer un processus en sous-tâches qui peuvent s'exécuter simultanément, améliorant ainsi l'efficacité et la réactivité du programme.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=5-6`

</details>

<!-- QID:ade55f79fedd -->
### Quel mécanisme est utilisé pour gérer les threads en C ?  <sup>p. 5–6</sup>

**Choix :**

- A) A. stdlib
- B) B. pthread
- C) C. threadlib
- D) D. concurrent

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** La bibliothèque pthread fournit des fonctions pour créer et gérer des threads en C, permettant ainsi la programmation concurrente.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=5-6`

</details>

<!-- QID:98b2a5928837 -->
### Un processus peut être préempté sans que celui-ci en soit conscient.  <sup>p. 5–6</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Vrai

**Pourquoi :** L'ordonnanceur du système d'exploitation peut interrompre un processus en cours d'exécution pour permettre à un autre processus de s'exécuter, sans que le processus préempté ne le réalise.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=5-6`

</details>

<!-- QID:6a74bdfaac83 -->
### Qu'est-ce qu'un thread dans le contexte d'un processus ?  <sup>p. 7–8</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Un thread est un fil d'exécution de code à l'intérieur d'un processus, capable d'être ordonnancé.

**Pourquoi :** Les threads permettent l'exécution simultanée de plusieurs tâches au sein d'un même processus, optimisant ainsi l'utilisation des ressources.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=7-8`

</details>

<!-- QID:f2a063845993 -->
### Un processus est décomposé en deux parties : la première contient les ressources globales, et la deuxième contient des informations liées à l'état d'exécution, telles que le ______ et la ______.  <sup>p. 7–8</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** compteur de programme; pile d'exécution

**Pourquoi :** Ces deux éléments sont essentiels pour la gestion de l'exécution des threads au sein d'un processus.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=7-8`

</details>

<!-- QID:420bd5cab4f6 -->
### Un thread peut être lancé par un autre programme.  <sup>p. 7–8</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Un thread est lié à un programme particulier et ne peut pas être lancé par un autre programme, contrairement aux processus qui peuvent être lancés par d'autres processus.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=7-8`

</details>

<!-- QID:57a61bb741e5 -->
### Quels sont les risques associés à l'utilisation de threads dans un même processus ?  <sup>p. 7–8</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Les threads peuvent corrompre les données des autres et un accès mémoire erroné peut entraîner la terminaison de tout le processus.

**Pourquoi :** Ces risques sont dus au partage de l'espace d'adressage entre les threads, ce qui nécessite des outils de synchronisation pour éviter les corruptions.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=7-8`

</details>

<!-- QID:f5be5d627a08 -->
### Quel élément n'est pas partagé entre les threads d'un même processus ?  <sup>p. 7–8</sup>

**Choix :**

- A) Les variables globales
- B) Le compteur de programme
- C) La pile d'exécution
- D) L'identifiant du thread

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C

**Pourquoi :** Chaque thread possède sa propre pile d'exécution, tandis que les autres éléments comme les variables globales sont partagés.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=7-8`

</details>

<!-- QID:7a1c11936545 -->
### Les threads partagent des ressources avec les processus parents, mais ils n'ont pas leur propre ________.  <sup>p. 9–10</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** espace d'adressage

**Pourquoi :** Cela signifie que les threads d'un même processus peuvent accéder aux mêmes variables et données, facilitant la communication entre eux.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=9-10`

</details>

<!-- QID:daefa4d6502a -->
### Quel est un avantage du multi-threading par rapport à un programme à thread unique?  <sup>p. 9–10</sup>

**Choix :**

- A) Les threads consomment moins de mémoire.
- B) Un thread peut gérer les calculs pendant qu'un autre gère les entrées/sorties.
- C) Les threads sont plus faciles à programmer.
- D) Les threads ne partagent pas les ressources.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Le multi-threading permet de décharger le processeur en répartissant les tâches, ce qui améliore l'interaction utilisateur et la réactivité des applications.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=9-10`

</details>

<!-- QID:ec9de5841b46 -->
### Quels mécanismes doivent utiliser les processus parents et enfants pour communiquer?  <sup>p. 9–10</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Les processus parents et enfants doivent utiliser des mécanismes de communication inter-processus.

**Pourquoi :** Ces mécanismes sont nécessaires car chaque processus a son propre espace d'adressage, ce qui empêche un accès direct aux données.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=9-10`

</details>

<!-- QID:b7a563727462 -->
### Dans un programme multi-thread, un clic sur un bouton pour zoomer peut entraîner un blocage de l'application si ________ n'est pas utilisé.  <sup>p. 9–10</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** le multi-threading

**Pourquoi :** Sans multi-threading, le calcul de la nouvelle image monopoliserait le processeur, rendant l'application non réactive.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=9-10`

</details>

<!-- QID:7b7d7ed4effc -->
### Quels sont les inconvénients du multi-threading ?  <sup>p. 11–12</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Les inconvénients incluent la nécessité de mécanismes de synchronisation pour l'accès concurrent à la mémoire, le risque de polluer l'espace d'adressage du processus, et le fait que les threads n'existent que dans un processus, limitant leur réutilisabilité.

**Pourquoi :** Ces inconvénients peuvent compliquer le développement et la maintenance des applications multi-threadées.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=11-12`

</details>

<!-- QID:6fe9a36122e3 -->
### Le multi-threading permet d'exécuter des tâches sur des machines différentes.  <sup>p. 11–12</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Le multi-threading se limite à l'exécution de threads au sein d'un même processus, tandis que le multi-processing permet d'exécuter des processus sur des machines différentes.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=11-12`

</details>

<!-- QID:3cdab04a289e -->
### Dans le modèle délégation, un thread principal s'occupe de ________ la charge de travail sur les threads travailleurs.  <sup>p. 11–12</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** répartir

**Pourquoi :** Ce modèle est efficace pour gérer des tâches où un thread principal peut déléguer des requêtes à d'autres threads, optimisant ainsi le traitement.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=11-12`

</details>

<!-- QID:3d2a3a1f16d4 -->
### Qu'est-ce que le modèle délégation dans le contexte du multi-threading ?  <sup>p. 11–12</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Le modèle délégation consiste en un thread principal qui répartit la charge de travail sur plusieurs threads travailleurs, comme dans un serveur FTP où le thread principal attend des commandes et les délègue.

**Pourquoi :** Ce modèle permet une gestion efficace des tâches en utilisant plusieurs threads pour traiter des requêtes simultanément.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=11-12`

</details>

<!-- QID:2364746e9fb1 -->
### Dans le modèle de délégation, le thread principal crée des threads qui exécutent des tâches spécifiques en réponse à des ______.  <sup>p. 13–14</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** requêtes

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=13-14`

</details>

<!-- QID:7275f17ab0a0 -->
### Quel est l'avantage principal de l'utilisation de plusieurs threads dans un programme ?  <sup>p. 13–14</sup>

**Choix :**

- A) Augmentation de la complexité du code
- B) Réduction du temps d'exécution sur des machines multi-coeurs.
- C) Diminution de la consommation de mémoire
- D) Amélioration de la lisibilité du code

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** L'utilisation de plusieurs threads permet de répartir les tâches sur plusieurs cœurs, ce qui accélère le traitement global.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=13-14`

</details>

<!-- QID:36ae1b29abea -->
### Dans le modèle pair, tous les threads sont égaux et aucun n'est considéré comme principal.  <sup>p. 13–14</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Vrai

**Pourquoi :** Dans le modèle pair, chaque thread a le même niveau hiérarchique et est responsable de ses propres entrées/sorties, ce qui nécessite souvent une synchronisation.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=13-14`

</details>

<!-- QID:74b3eb920cc5 -->
### Quels sont les risques associés à la synchronisation entre threads dans un modèle pair ?  <sup>p. 13–14</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** La synchronisation entre threads peut entraîner des problèmes de concurrence, tels que des conditions de course, si elle n'est pas gérée correctement.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=13-14`

</details>

<!-- QID:d7b4b502cc4a -->
### Dans le modèle de délégation, le patron utilise une ______ pour gérer les requêtes des travailleurs.  <sup>p. 13–14</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** file d'attente

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=13-14`

</details>

<!-- QID:329464f0316c -->
### Quel est un exemple typique d'application utilisant le modèle pair ?  <sup>p. 13–14</sup>

**Choix :**

- A) Traitement d'images
- B) Simulation d'un système physique décomposé en éléments finis.
- C) Gestion de bases de données
- D) Développement web

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Les simulations physiques nécessitent souvent une répartition des calculs entre plusieurs threads pour optimiser le temps d'exécution.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=13-14`

</details>

<!-- QID:7ad00b0aebbe -->
### Qu'est-ce qu'un modèle pipeline en programmation concurrente ?  <sup>p. 15–17</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Un modèle pipeline est une architecture où une application traite une longue chaîne d'entrée en décomposant le traitement en sous-tâches (étages de pipeline) que chaque donnée doit traverser.

**Pourquoi :** Cela permet d'optimiser le traitement en parallèle, réduisant ainsi le temps d'exécution sur des processeurs multi-coeurs.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=15-17`

</details>

<!-- QID:e3de804e5a12 -->
### Dans un modèle pipeline, chaque étage peut traiter une donnée différente à chaque instant, ce qui permet d'optimiser le ________.  <sup>p. 15–17</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** temps d'exécution

**Pourquoi :** L'optimisation du temps d'exécution est cruciale pour améliorer les performances des applications traitant de grandes quantités de données.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=15-17`

</details>

<!-- QID:0261c7782be4 -->
### Quel est un exemple typique d'application utilisant le modèle pipeline ?  <sup>p. 15–17</sup>

**Choix :**

- A) Traitement de flux vidéo
- B) Calcul de matrices
- C) Tri de données
- D) Gestion de fichiers

<details>
<summary>Afficher la réponse</summary>

**Réponse :** A

**Pourquoi :** Le traitement de flux vidéo implique plusieurs étapes distinctes, comme la modification de la couleur et l'application de la compression, ce qui correspond parfaitement au modèle pipeline.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=15-17`

</details>

<!-- QID:a04d530a0de1 -->
### L'exclusion mutuelle permet à plusieurs tâches d'accéder simultanément à une ressource critique.  <sup>p. 15–17</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** L'exclusion mutuelle garantit qu'une seule tâche peut accéder à une ressource critique à la fois, évitant ainsi les conflits d'accès.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=15-17`

</details>

<!-- QID:022a66f75423 -->
### Qu'est-ce qu'une ressource critique ?  <sup>p. 15–17</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Une ressource critique est une ressource unique et non partageable qui ne peut être utilisée que par une seule tâche à la fois.

**Pourquoi :** La gestion des ressources critiques est essentielle pour éviter des comportements indésirables dans les programmes concurrents.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=15-17`

</details>

<!-- QID:0557357b8a6b -->
### Quelle est une des embûches à éviter lors de la gestion de l'exclusion mutuelle ?  <sup>p. 15–17</sup>

**Choix :**

- A) Interblocage
- B) Surcharge
- C) Délai d'attente
- D) Surutilisation

<details>
<summary>Afficher la réponse</summary>

**Réponse :** A

**Pourquoi :** L'interblocage se produit lorsque deux ou plusieurs tâches attendent indéfiniment l'accès à une ressource, ce qui bloque l'exécution du programme.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=15-17`

</details>

<!-- QID:6152daa2b0d9 -->
### Pourquoi est-il important d'éviter la famine dans un système de gestion des ressources ?  <sup>p. 15–17</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Il est important d'éviter la famine pour garantir que toutes les tâches aient un accès équitable aux ressources, empêchant ainsi certaines tâches d'être indéfiniment retardées.

**Pourquoi :** La famine peut entraîner une dégradation des performances et une mauvaise réactivité du système.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=15-17`

</details>

<!-- QID:445bad915b0f -->
### Quel type d'attente est caractérisé par le fait qu'une tâche ne peut pas dépasser une autre tâche en attente ?  <sup>p. 18</sup>

**Choix :**

- A) Attente PAPS
- B) Attente bornée
- C) Attente finie
- D) Attente linéaire

<details>
<summary>Afficher la réponse</summary>

**Réponse :** D

**Pourquoi :** L'attente linéaire impose un ordre strict d'accès, empêchant une tâche de dépasser celles qui sont déjà en attente.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=18-18`

</details>

<!-- QID:7f68454e1669 -->
### L'attente est ______ si une tâche atteindra la ressource après un temps fini.  <sup>p. 18</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** finie

**Pourquoi :** Une attente finie garantit qu'il n'y a pas de famine, c'est-à-dire que toutes les tâches auront un accès à la ressource.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=18-18`

</details>

<!-- QID:394cf0b5cb74 -->
### Une solution centralisée repose sur l'existence d'une mémoire centrale accessible par toutes les tâches.  <sup>p. 18</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Vrai

**Pourquoi :** Dans une solution centralisée, toutes les tâches peuvent lire et écrire dans une mémoire partagée, facilitant la coordination.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=18-18`

</details>

<!-- QID:2daaecfe277e -->
### Quelles sont les deux facettes intéressantes des solutions logicielles au problème de l'exclusion mutuelle ?  <sup>p. 18</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Elles permettent d'élucider les notions d'exécution atomique et d'attente bornée.

**Pourquoi :** Comprendre ces notions est crucial pour analyser le comportement des algorithmes en traitement parallèle.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=18-18`

</details>

<!-- QID:c928bbe25091 -->
### Dans une solution répartie, comment les tâches échangent-elles des résultats ?  <sup>p. 18</sup>

**Choix :**

- A) Via une mémoire centrale
- B) Par accès direct à la mémoire
- C) Par le biais de messages
- D) En utilisant des fichiers partagés

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C

**Pourquoi :** Dans une solution répartie, chaque tâche a sa propre mémoire locale et doit communiquer via des messages, ce qui évite les accès concurrents à une mémoire partagée.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=18-18`

</details>

<!-- QID:2533bac3872f -->
### L'attente est ______ par une fonction f(n) où n est le nombre de tâches participantes.  <sup>p. 18</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** bornée

**Pourquoi :** Cela signifie qu'une tâche ne peut être dépassée que par un nombre limité de tâches, ce qui aide à contrôler l'accès à la ressource.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=18-18`

</details>

<!-- QID:2601aab5d22a -->
### Quelles sont les hypothèses de base concernant les instructions dans l'attente active ?  <sup>p. 19–20</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Les instructions assembleurs sont exécutées atomiquement, sans hypothèse sur leur nombre ou leur vitesse relative.

**Pourquoi :** Cela garantit que les résultats des instructions sont cohérents, même si elles sont exécutées simultanément.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=19-20`

</details>

<!-- QID:c6ab9f569336 -->
### Quel est le rôle de la variable 'occupe' dans la première tentative d'exclusion mutuelle ?  <sup>p. 19–20</sup>

**Choix :**

- A) Indiquer l'identité de la tâche en cours
- B) Indiquer si une tâche est en section critique
- C) Contrôler l'accès à la mémoire
- D) Gérer les priorités des tâches

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** La variable 'occupe' est utilisée pour savoir si une tâche est actuellement dans sa section critique, afin d'éviter les conflits.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=19-20`

</details>

<!-- QID:80911bb93ee7 -->
### La première tentative d'exclusion mutuelle garantit l'exclusion mutuelle entre deux tâches.  <sup>p. 19–20</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Cette tentative échoue car les deux tâches peuvent entrer simultanément en section critique si elles lisent 'occupe' comme faux en même temps.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=19-20`

</details>

<!-- QID:47ec21607275 -->
### Dans la deuxième tentative d'exclusion mutuelle, la variable _____ indique l'identité de la tâche autorisée à accéder à la section critique.  <sup>p. 19–20</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** tour

**Pourquoi :** La variable 'tour' permet de contrôler quel processus peut entrer dans la section critique, mais elle ne garantit pas une exécution équitable.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=19-20`

</details>

<!-- QID:82a37d6c5e98 -->
### Quels sont les inconvénients de la deuxième tentative d'exclusion mutuelle ?  <sup>p. 19–20</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Elle ne garantit pas l'alternance des accès à la section critique et peut entraîner une attente indéfinie si une tâche disparaît.

**Pourquoi :** Cela peut provoquer une inefficacité dans l'exécution des tâches, car une tâche peut bloquer l'autre sans raison.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=19-20`

</details>

<!-- QID:a469464117e1 -->
### Quel problème la troisième tentative d'exclusion mutuelle cherche-t-elle à résoudre ?  <sup>p. 19–20</sup>

**Choix :**

- A) Le manque de synchronisation entre les tâches
- B) L'inefficacité de l'accès à la mémoire
- C) Le blocage indéfini d'une tâche
- D) Le contrôle de l'accès à la section critique

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C

**Pourquoi :** La troisième tentative utilise un vecteur de booléens pour tenir compte de l'état des tâches, évitant ainsi les blocages indéfinis.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=19-20`

</details>

<!-- QID:e47d2fb20ba6 -->
### Qu'est-ce que l'exclusion mutuelle en programmation concurrente ?  <sup>p. 21–22</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** L'exclusion mutuelle est un principe qui garantit qu'une seule tâche peut accéder à une section critique à un moment donné, empêchant ainsi les conflits d'accès aux ressources partagées.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=21-22`

</details>

<!-- QID:516ed5277275 -->
### Quel est le principal problème de l'algorithme 2.3 ?  <sup>p. 21–22</sup>

**Choix :**

- A) Il garantit l'exclusion mutuelle.
- B) Il ne garantit pas l'exclusion mutuelle.
- C) Il provoque un interblocage.
- D) Il est inefficace.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** L'algorithme 2.3 permet à deux tâches d'entrer simultanément dans leur section critique, ce qui viole le principe d'exclusion mutuelle.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=21-22`

</details>

<!-- QID:336444ff7ea1 -->
### L'algorithme 2.4 garantit l'exclusion mutuelle mais peut entraîner un interblocage.  <sup>p. 21–22</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Vrai

**Pourquoi :** Bien que l'algorithme 2.4 assure l'exclusion mutuelle, il peut conduire à un interblocage si les deux tâches s'exécutent en alternance dans leur prélude.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=21-22`

</details>

<!-- QID:c2c35aef3118 -->
### Dans l'algorithme 2.4, l'état de chaque tâche est représenté par un tableau appelé ______.  <sup>p. 21–22</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** etat

**Pourquoi :** Le tableau 'etat' est utilisé pour indiquer si une tâche souhaite entrer dans la section critique.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=21-22`

</details>

<!-- QID:60e209c2cd03 -->
### Quel est le rôle de la variable 'tour' dans l'algorithme 2.2 ?  <sup>p. 21–22</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** La variable 'tour' détermine quelle tâche a la priorité pour entrer dans la section critique, permettant ainsi de gérer l'accès concurrent.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=21-22`

</details>

<!-- QID:4c6e12864c55 -->
### Quel problème survient lorsque T0 et T1 mettent leur état à vrai dans l'algorithme 2.4 ?  <sup>p. 21–22</sup>

**Choix :**

- A) Les deux tâches s'exécutent correctement.
- B) Les deux tâches se bloquent mutuellement.
- C) Une tâche est toujours prioritaire.
- D) Les tâches s'exécutent en parallèle.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Lorsque T0 et T1 mettent leur état à vrai, elles peuvent croire que l'autre est déjà dans sa section critique, entraînant un blocage.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=21-22`

</details>

<!-- QID:c4f26ee6d75d -->
### Quelle est la principale modification apportée dans l'algorithme 2.5 par rapport aux précédents ?  <sup>p. 21–22</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** L'algorithme 2.5 oblige une tâche à renoncer temporairement à son désir d'entrer en section critique si l'autre tâche souhaite également y entrer.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=21-22`

</details>

<!-- QID:2c1773a3bc00 -->
### Qu'est-ce que l'algorithme de Dekker ?  <sup>p. 23–24</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** L'algorithme de Dekker est une solution d'exclusion mutuelle pour deux tâches qui combine des éléments de tentatives précédentes et utilise une variable de tour pour gérer l'accès à la section critique.

**Pourquoi :** Il est conçu pour éviter les interblocages tout en garantissant que deux tâches ne peuvent pas entrer simultanément dans leur section critique.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=23-24`

</details>

<!-- QID:9f8e9e167592 -->
### Quel est le rôle de la variable 'tour' dans l'algorithme de Dekker ?  <sup>p. 23–24</sup>

**Choix :**

- A) Elle détermine la priorité d'une tâche sur l'autre.
- B) Elle indique si une tâche est en section critique.
- C) Elle impose l'ordre d'accès à la section critique.
- D) Elle contrôle le temps d'exécution des tâches.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C

**Pourquoi :** La variable 'tour' est essentielle pour éviter les interblocages en permettant à une tâche de céder l'accès à l'autre en cas de conflit.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=23-24`

</details>

<!-- QID:7761025e62ff -->
### L'algorithme de Dekker garantit l'exclusion mutuelle.  <sup>p. 23–24</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Vrai

**Pourquoi :** L'exclusion mutuelle est garantie car si les deux tâches sont en section critique, elles ne peuvent pas sortir de leurs boucles d'attente, ce qui signifie qu'une seule tâche peut entrer à la fois.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=23-24`

</details>

<!-- QID:5c201ce5a220 -->
### Comment l'algorithme de Dekker évite-t-il les interblocages ?  <sup>p. 23–24</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Il évite les interblocages en permettant à une tâche de céder l'accès à l'autre en fonction de la valeur de la variable 'tour'.

**Pourquoi :** Cela garantit qu'une tâche ne peut pas bloquer l'autre indéfiniment, car l'accès à la section critique est régulé.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=23-24`

</details>

<!-- QID:cdb00ee4dffa -->
### Dans l'algorithme de Dekker, si T0 trouve etat[1] à vrai, elle attend dans sa boucle externe jusqu'à ce que etat[1] passe à ____.  <sup>p. 23–24</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** faux

**Pourquoi :** Cela permet à T0 de s'assurer que T1 a terminé son exécution avant d'entrer dans la section critique.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=23-24`

</details>

<!-- QID:4300df6a65ce -->
### Quel est un risque associé à l'algorithme de Dekker ?  <sup>p. 23–24</sup>

**Choix :**

- A) L'interblocage.
- B) La famine.
- C) La perte de données.
- D) L'inefficacité des tâches.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** La famine peut se produire si une tâche accède constamment à la section critique, empêchant l'autre tâche de progresser.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=23-24`

</details>

<!-- QID:0a307d5075b2 -->
### Qu'est-ce que l'algorithme de Peterson?  <sup>p. 25–26</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C'est un algorithme de synchronisation qui permet l'exclusion mutuelle entre deux tâches en utilisant des variables partagées pour gérer l'accès à une section critique.

**Pourquoi :** Il est simple et efficace pour résoudre les problèmes de concurrence dans les systèmes à deux tâches.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=25-26`

</details>

<!-- QID:7236cd6a3dde -->
### Dans l'algorithme de Peterson, les variables partagées sont __ et __.  <sup>p. 25–26</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** intention[2], tour

**Pourquoi :** Ces variables permettent de gérer l'intention d'accès des tâches et de déterminer laquelle doit entrer dans la section critique.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=25-26`

</details>

<!-- QID:1b316dc49504 -->
### Quel est le rôle de la variable 'tour' dans l'algorithme de Peterson?  <sup>p. 25–26</sup>

**Choix :**

- A) Elle détermine l'ordre d'exécution des tâches.
- B) Elle stocke l'état de la section critique.
- C) Elle départage les deux tâches si elles désirent accéder en même temps à la section critique.
- D) Elle indique si une tâche est en attente.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C

**Pourquoi :** La variable 'tour' est essentielle pour éviter les conflits d'accès à la section critique entre les deux tâches.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=25-26`

</details>

<!-- QID:863262bf6660 -->
### Comment l'algorithme de Peterson garantit-il l'équité?  <sup>p. 25–26</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Il garantit que si une tâche est en attente et l'autre dans la section critique, la tâche en attente pourra entrer dans la section critique avant que l'autre ne désire y retourner.

**Pourquoi :** Cela empêche une tâche de monopoliser l'accès à la section critique, assurant ainsi un traitement équitable.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=25-26`

</details>

<!-- QID:58cf99ee5798 -->
### Quel est un des avantages de l'algorithme de Peterson?  <sup>p. 25–26</sup>

**Choix :**

- A) Il fonctionne avec un nombre illimité de tâches.
- B) Il est complexe à mettre en œuvre.
- C) Sa simplicité et son efficacité pour deux tâches.
- D) Il nécessite un matériel spécifique.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C

**Pourquoi :** L'algorithme de Peterson est reconnu pour sa simplicité, ce qui le rend facile à comprendre et à implémenter pour deux tâches.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=25-26`

</details>

<!-- QID:0c4043e4250d -->
### Les opérations atomiques définies sur un verrou v sont ______ et ______.  <sup>p. 27–28</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Verrouille(v), Déverrouille(v)

**Pourquoi :** Ces opérations garantissent que l'accès au verrou est sécurisé et que les modifications sont effectuées sans interruption.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=27-28`

</details>

<!-- QID:509c614457ec -->
### Quelle fonction est utilisée pour déverrouiller un verrou en Pthread ?  <sup>p. 27–28</sup>

**Choix :**

- A) pthread_mutex_lock
- B) pthread_mutex_unlock
- C) pthread_mutex_trylock
- D) pthread_mutex_init

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** pthread_mutex_unlock est la fonction spécifiquement conçue pour libérer un verrou dans la bibliothèque Pthread.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=27-28`

</details>

<!-- QID:8720098dbdce -->
### Un verrou peut être utilisé pour résoudre des problèmes de synchronisation entre tâches.  <sup>p. 27–28</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Vrai

**Pourquoi :** Les verrous permettent de contrôler l'ordre d'exécution des tâches, garantissant que certaines instructions s'exécutent dans un ordre spécifique.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=27-28`

</details>

<!-- QID:ed291fa79ed7 -->
### Quelle est la différence entre V errouille(v) et D éverrouille(v) ?  <sup>p. 27–28</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** V errouille(v) bloque l'accès au verrou si celui-ci est déjà pris, tandis que D éverrouille(v) libère le verrou ou réveille une tâche en attente.

**Pourquoi :** Cette distinction est essentielle pour comprendre comment les tâches interagissent avec les ressources partagées.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=27-28`

</details>

<!-- QID:3a9ad9392e8f -->
### Quelle méthode est utilisée pour créer un verrou dynamiquement en Pthread ?  <sup>p. 27–28</sup>

**Choix :**

- A) pthread_mutex_create()
- B) pthread_mutex_init()
- C) pthread_mutex_setup()
- D) pthread_mutex_allocate()

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** pthread_mutex_init() est la fonction appropriée pour initialiser un verrou qui a été alloué dynamiquement.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=27-28`

</details>

<!-- QID:58d97534ef7b -->
### Qu'est-ce qu'une section critique ?  <sup>p. 27–28</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Une section critique est une partie du code où une tâche accède à une ressource partagée, nécessitant une protection contre l'accès simultané.

**Pourquoi :** La protection des sections critiques est cruciale pour éviter les incohérences et les corruptions de données.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=27-28`

</details>

<!-- QID:aecd39a5b90f -->
### La fonction pthread_mutex_trylock bloque l'appelant si le verrou est déjà pris.  <sup>p. 27–28</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** pthread_mutex_trylock retourne immédiatement EBUSY si le verrou est déjà pris, permettant à l'appelant de continuer à exécuter d'autres tâches.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=27-28`

</details>

<!-- QID:d4731c8b68dd -->
### Quelle est la fonction utilisée pour verrouiller un mutex en C ?  <sup>p. 29–30</sup>

**Choix :**

- A) pthread_mutex_lock
- B) pthread_mutex_unlock
- C) pthread_create
- D) pthread_join

<details>
<summary>Afficher la réponse</summary>

**Réponse :** A

**Pourquoi :** pthread_mutex_lock est la fonction qui bloque l'accès à la ressource protégée par le mutex.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=29-30`

</details>

<!-- QID:274713d0b3c1 -->
### Les sémaphores sont une généralisation des verrous.  <sup>p. 29–30</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Vrai

**Pourquoi :** Les sémaphores permettent de gérer l'accès à plusieurs ressources et incluent des opérations supplémentaires par rapport aux verrous.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=29-30`

</details>

<!-- QID:27e7158a9115 -->
### Un sémaphore s est une variable entière sur laquelle deux opérations atomiques sont définies, P(s) (pour tester : ________) et V(s) (pour ________).  <sup>p. 29–30</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Proberen; Verhogen

**Pourquoi :** Ces opérations permettent de tester et d'incrémenter le sémaphore, respectivement, pour gérer l'accès aux ressources.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=29-30`

</details>

<!-- QID:8540fb8b78a3 -->
### Quel est le principal inconvénient de la première solution de rendez-vous entre deux tâches ?  <sup>p. 29–30</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Elle entraîne un nombre élevé de changements de contexte, ce qui peut nuire aux performances.

**Pourquoi :** Les changements de contexte sont coûteux en termes de temps d'exécution, et une gestion inefficace peut ralentir l'application.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=29-30`

</details>

<!-- QID:6b65bcb75790 -->
### Dans l'algorithme de rendez-vous, que se passe-t-il si TâcheA arrive au point de rendez-vous avant TâcheB ?  <sup>p. 29–30</sup>

**Choix :**

- A) TâcheA continue sans attendre
- B) TâcheA se bloque
- C) TâcheA termine immédiatement
- D) TâcheA déverrouille le mutex

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** TâcheA doit attendre que TâcheB arrive au point de rendez-vous pour pouvoir continuer, assurant ainsi la synchronisation.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=29-30`

</details>

<!-- QID:416d3a903b2c -->
### Comment la seconde solution de rendez-vous minimise-t-elle les changements de contexte ?  <sup>p. 29–30</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** La dernière tâche à arriver au point de rendez-vous déverrouille l'autre tâche, permettant à celle-ci de continuer sans changement de contexte.

**Pourquoi :** Cela réduit le nombre de fois où les tâches doivent être suspendues et reprises, améliorant ainsi l'efficacité.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=29-30`

</details>

<!-- QID:65cb4b40e7f5 -->
### Qu'est-ce qu'un sémaphore binaire ?  <sup>p. 31–32</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Un sémaphore binaire est un type de sémaphore qui ne peut prendre que deux valeurs, généralement 0 et 1, et est utilisé pour gérer l'accès à une ressource partagée.

**Pourquoi :** Les sémaphores binaires permettent de contrôler l'accès exclusif à une ressource, ce qui est essentiel pour éviter les conflits entre tâches.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=31-32`

</details>

<!-- QID:02a1abe6b28e -->
### Les opérations P(s) et V(s) sont équivalentes à l'exécution atomique des séquences d'instructions suivantes : P(s) consiste à ______ et V(s) consiste à ______.  <sup>p. 31–32</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** décrémenter s; incrémenter s

**Pourquoi :** Ces opérations permettent de gérer l'accès aux ressources partagées de manière sécurisée et synchronisée.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=31-32`

</details>

<!-- QID:0d560670b20d -->
### Quel est le rôle principal d'un sémaphore dans la programmation concurrente ?  <sup>p. 31–32</sup>

**Choix :**

- A) Gérer la mémoire
- B) Contrôler l'accès à une ressource partagée.
- C) Augmenter la vitesse d'exécution
- D) Réduire la consommation d'énergie

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Les sémaphores sont utilisés pour éviter les conflits d'accès aux ressources partagées entre plusieurs tâches.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=31-32`

</details>

<!-- QID:68d18219bbc4 -->
### Comment un sémaphore gère-t-il les tâches bloquées ?  <sup>p. 31–32</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Un sémaphore maintient une file d'attente contenant toutes les tâches bloquées sur lui, et lors de l'opération V, une tâche est retirée de cette file et réactivée.

**Pourquoi :** Cela permet de gérer efficacement l'accès aux ressources partagées et de garantir que les tâches sont exécutées dans l'ordre approprié.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=31-32`

</details>

<!-- QID:39e28b013708 -->
### Quelle est la principale différence entre un sémaphore et un verrou ?  <sup>p. 31–32</sup>

**Choix :**

- A) Un sémaphore est plus rapide qu'un verrou.
- B) Un sémaphore peut gérer plusieurs tâches simultanément, tandis qu'un verrou permet l'accès exclusif.
- C) Un verrou est plus complexe qu'un sémaphore.
- D) Un sémaphore ne peut pas être utilisé pour la synchronisation.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Les sémaphores sont conçus pour contrôler l'accès à une ressource par plusieurs tâches, alors que les verrous sont utilisés pour garantir qu'une seule tâche accède à la ressource à la fois.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=31-32`

</details>

<!-- QID:93ddb6f19d4c -->
### Pour garantir l'atomicité des opérations P et V, il est nécessaire d'inhiber ______ sur une machine monoprocesseur.  <sup>p. 31–32</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** les interruptions

**Pourquoi :** Inhiber les interruptions permet d'éviter les commutations de tâches qui pourraient interférer avec l'exécution des opérations critiques.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=31-32`

</details>

<!-- QID:985a19807332 -->
### Dans l'implémentation d'un sémaphore, la fonction P() diminue la valeur du sémaphore et bloque si la valeur devient _____ .  <sup>p. 33–35</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** négative

**Pourquoi :** Cela signifie qu'il n'y a plus de ressources disponibles, et la tâche doit attendre.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=33-35`

</details>

<!-- QID:5408b65fc968 -->
### Quelle est la fonction de la méthode V() dans l'implémentation d'un sémaphore ?  <sup>p. 33–35</sup>

**Choix :**

- A) Diminuer la valeur du sémaphore.
- B) Augmenter la valeur du sémaphore.
- C) Bloquer une tâche.
- D) Débloquer toutes les tâches.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** La méthode V() est utilisée pour signaler qu'une ressource est devenue disponible.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=33-35`

</details>

<!-- QID:1101604adb7f -->
### La fonction DetruireSemaphore() libère les ressources allouées pour un sémaphore.  <sup>p. 33–35</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Vrai

**Pourquoi :** Elle appelle pthread_mutex_destroy() pour détruire les mutex et libère la mémoire allouée.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=33-35`

</details>

<!-- QID:dfb4251f65a3 -->
### Comment peut-on implémenter un verrou en utilisant des sémaphores ?  <sup>p. 33–35</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** On peut utiliser un sémaphore binaire initialisé à 1, où P() bloque si le sémaphore est 0 et V() le libère.

**Pourquoi :** Cela permet de garantir qu'une seule tâche peut accéder à la section critique à la fois.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=33-35`

</details>

<!-- QID:88d107b76053 -->
### Dans le problème des producteurs-consommateurs, les éléments du tampon doivent être consommés selon leur ordre de _____ .  <sup>p. 33–35</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** production

**Pourquoi :** Cela garantit que les tâches consomment les éléments dans l'ordre où ils ont été ajoutés, évitant ainsi des incohérences.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=33-35`

</details>

<!-- QID:dff3fd719ebb -->
### Dans le problème des producteurs-consommateurs, une productrice peut écraser un élément dans le tampon si celui-ci est plein.  <sup>p. 33–35</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Si le tampon est plein, la productrice doit attendre qu'un élément soit consommé avant de pouvoir ajouter un nouvel élément.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=33-35`

</details>

<!-- QID:20ab504bc5e9 -->
### Quel est le rôle de la fonction InitialiseTampon dans le code fourni ?  <sup>p. 36–37</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** InitialiseTampon initialise l'état du tampon avant que les tâches productrices et consommatrices ne commencent à fonctionner.

**Pourquoi :** Cela garantit que le tampon est dans un état connu et prêt à être utilisé, évitant ainsi des comportements indéfinis.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=36-37`

</details>

<!-- QID:1deefcfa38cc -->
### Quel est l'état du tampon lorsque la tâche productrice appelle Depose et trouve le tampon plein ?  <sup>p. 36–37</sup>

**Choix :**

- A) Elle dépose l'item sans problème.
- B) Elle se met dans une file d'attente et se bloque.
- C) Elle vide le tampon.
- D) Elle termine son exécution.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Cela permet de gérer la synchronisation entre les tâches productrices et consommatrices, évitant ainsi des erreurs d'accès concurrent.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=36-37`

</details>

<!-- QID:d7a6f8abbcbb -->
### Vrai ou Faux : Un sémaphore peut indiquer le nombre de tâches bloquées dans sa file d'attente.  <sup>p. 36–37</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Un sémaphore ne fournit pas d'information sur le nombre de tâches en attente, ce qui nécessite l'utilisation d'un compteur supplémentaire.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=36-37`

</details>

<!-- QID:a3c86ba3613d -->
### Dans l'algorithme de gestion du tampon, les tâches productrices utilisent l'instruction ______ pour insérer un item dans le tampon.  <sup>p. 36–37</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** tableau[ptEntree] = item

**Pourquoi :** Cette instruction permet de stocker l'item à la position libre indiquée par ptEntree dans le tableau circulaire.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=36-37`

</details>

<!-- QID:0b7b5a5a9930 -->
### Comment la tâche consommatrice sait-elle qu'elle peut prélever un item du tampon ?  <sup>p. 36–37</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Elle doit attendre que Produit(t) - Consommé(t) > 0, ce qui indique qu'il y a des items disponibles dans le tampon.

**Pourquoi :** Cela garantit que la consommatrice ne tente pas de prélever un item lorsque le tampon est vide, évitant ainsi des erreurs.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=36-37`

</details>

<!-- QID:0ee32e9d5451 -->
### Quel est l'avantage d'utiliser un sémaphore pour gérer l'état du tampon ?  <sup>p. 36–37</sup>

**Choix :**

- A) Il rend le code plus complexe.
- B) Il permet de gérer plusieurs tampons simultanément.
- C) Il simplifie la gestion de l'état du tampon.
- D) Il élimine complètement les erreurs de synchronisation.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C

**Pourquoi :** L'utilisation de sémaphores permet de gérer efficacement les accès concurrents sans avoir à gérer manuellement les états du tampon.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=36-37`

</details>

<!-- QID:7199e9861916 -->
### Quelle est la fonction de la variable attenteProd dans le contexte de la gestion du tampon ?  <sup>p. 36–37</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** La variable attenteProd compte le nombre de tâches productrices en attente lorsque le tampon est plein.

**Pourquoi :** Cela permet de gérer les tâches en attente et de les réveiller lorsque de l'espace devient disponible dans le tampon.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=36-37`

</details>

<!-- QID:dc98fcf19980 -->
### Qu'est-ce qu'un tampon dans le contexte de la programmation concurrente ?  <sup>p. 38–39</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Un tampon est une structure de données utilisée pour stocker temporairement des éléments entre un producteur et un consommateur, permettant ainsi de gérer la synchronisation entre ces deux entités.

**Pourquoi :** Il permet de gérer les situations où le producteur produit des données plus rapidement que le consommateur ne peut les traiter, et vice versa.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=38-39`

</details>

<!-- QID:b26149c54924 -->
### La première méthode d'implémentation d'un tampon utilise des sémaphores pour gérer l'état du tampon, qui peut être _____ ou _____.  <sup>p. 38–39</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Vide, Plein

**Pourquoi :** Ces états permettent de contrôler l'accès au tampon et d'éviter les conditions de course entre producteurs et consommateurs.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=38-39`

</details>

<!-- QID:66cce19e5a9f -->
### Quel est le rôle du sémaphore 'attendreVide' dans l'algorithme de dépôt ?  <sup>p. 38–39</sup>

**Choix :**

- A) Il bloque les producteurs lorsque le tampon est plein.
- B) Il bloque les consommateurs lorsque le tampon est vide.
- C) Il permet aux producteurs d'ajouter des éléments au tampon.
- D) Il indique le nombre total d'éléments dans le tampon.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** A

**Pourquoi :** Le sémaphore 'attendreVide' est utilisé pour signaler aux producteurs qu'ils doivent attendre avant de déposer un nouvel élément si le tampon est plein.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=38-39`

</details>

<!-- QID:8dac78a797c5 -->
### Quelle est la différence principale entre les algorithmes 4.1 et 4.2 ?  <sup>p. 38–39</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** L'algorithme 4.1 utilise un mutex et des sémaphores pour gérer l'état du tampon, tandis que l'algorithme 4.2 simplifie cette gestion en utilisant uniquement des sémaphores pour contrôler l'accès au tampon.

**Pourquoi :** Cette simplification peut réduire la complexité et le risque d'erreurs dans la gestion de la synchronisation.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=38-39`

</details>

<!-- QID:4500e3f302d9 -->
### Quel est l'effet de l'instruction 'sem_wait(&Tampon.attendrePlein)' dans la fonction Preleve ?  <sup>p. 38–39</sup>

**Choix :**

- A) Elle bloque le consommateur si le tampon est vide.
- B) Elle permet au consommateur de retirer un élément du tampon.
- C) Elle signale qu'un élément a été ajouté au tampon.
- D) Elle libère le mutex associé au tampon.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** A

**Pourquoi :** Cette instruction est utilisée pour s'assurer que le consommateur ne tente pas de retirer un élément d'un tampon vide, ce qui provoquerait une erreur.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=38-39`

</details>

<!-- QID:34716109fb53 -->
### Quel est le rôle du sémaphore mutex dans les algorithmes de producteurs-consommateurs ?  <sup>p. 40–42</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Le sémaphore mutex assure l'exclusion mutuelle entre les tâches productrices et consommatrices.

**Pourquoi :** Cela permet d'éviter les conflits d'accès aux ressources partagées, garantissant ainsi l'intégrité des données.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=40-42`

</details>

<!-- QID:da9bf3d1a589 -->
### Combien d'appels à des primitives de sémaphores sont nécessaires pour une insertion ou un retrait dans l'algorithme 4.4 ?  <sup>p. 40–42</sup>

**Choix :**

- A) 2
- B) 3
- C) 4
- D) 5

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C

**Pourquoi :** Chaque opération d'insertion ou de retrait dans l'algorithme 4.4 nécessite 4 appels à des primitives de sémaphores.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=40-42`

</details>

<!-- QID:78289aa4e1d4 -->
### L'algorithme 4.3 nécessite généralement plus d'appels de primitives que l'algorithme 4.4.  <sup>p. 40–42</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** L'algorithme 4.3 ne réalise généralement que 2 appels de primitives pour accomplir les mêmes actions, ce qui est moins que les 4 de l'algorithme 4.4.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=40-42`

</details>

<!-- QID:962926915995 -->
### Dans l'algorithme 4.4, les fonctions Depose et Preleve utilisent les sémaphores ______ et ______ pour gérer l'accès au tampon.  <sup>p. 40–42</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** attendreVide, attendrePlein

**Pourquoi :** Ces sémaphores permettent de synchroniser les producteurs et les consommateurs en fonction de l'état du tampon.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=40-42`

</details>

<!-- QID:4cfa39f79092 -->
### Quel est l'effet de l'inversion de l'ordre des opérations sem_post dans les fonctions Depose et Preleve de l'algorithme 4.4 ?  <sup>p. 40–42</sup>

**Choix :**

- A) Aucune conséquence
- B) Amélioration des performances
- C) Problèmes de synchronisation
- D) Réduction des appels de sémaphore

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C

**Pourquoi :** Inverser l'ordre des opérations pourrait perturber la logique de synchronisation, entraînant des accès non sécurisés au tampon.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=40-42`

</details>

<!-- QID:7bb84aadb955 -->
### Il est possible de remplacer le sémaphore mutex par deux sémaphores distincts pour les producteurs et les consommateurs.  <sup>p. 40–42</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Un seul sémaphore mutex est nécessaire pour assurer l'exclusion mutuelle entre les producteurs et les consommateurs, garantissant ainsi la sécurité des accès.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=40-42`

</details>

<!-- QID:e6f6d8efc112 -->
### Qu'est-ce qu'une situation de type lecteurs-rédacteurs ?  <sup>p. 43–44</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C'est un modèle d'accès concurrent à une ressource où plusieurs tâches peuvent lire simultanément, mais l'écriture est exclusive.

**Pourquoi :** Ce modèle est essentiel pour gérer l'accès concurrent aux ressources partagées tout en préservant l'intégrité des données.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=43-44`

</details>

<!-- QID:80d1205fbec8 -->
### Dans le problème des lecteurs-rédacteurs, les _______ ne font que consulter les données, tandis que les _______ peuvent les modifier.  <sup>p. 43–44</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** lecteurs; rédacteurs

**Pourquoi :** Cette distinction est cruciale pour comprendre les différentes interactions avec la ressource partagée.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=43-44`

</details>

<!-- QID:a9a73322642a -->
### Quelles sont les contraintes du problème des lecteurs-rédacteurs ?  <sup>p. 43–44</sup>

**Choix :**

- A) 1. Les lecteurs et rédacteurs peuvent accéder simultanément aux données.
- B) 2. Les rédacteurs peuvent lire pendant qu'un lecteur écrit.
- C) 3. Les lecteurs peuvent écrire pendant qu'un rédacteur lit.
- D) 4. Plusieurs lecteurs peuvent lire simultanément les données; les rédacteurs s’excluent mutuellement.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** D

**Pourquoi :** Ces contraintes garantissent l'intégrité des données tout en permettant une certaine concurrence dans les lectures.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=43-44`

</details>

<!-- QID:a7b8b5d3da62 -->
### Quels sémaphores sont nécessaires pour gérer l'accès dans un algorithme avec priorité aux lecteurs ?  <sup>p. 43–44</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** mutexLecteurs, redacteur, mutexRedacteurs.

**Pourquoi :** Ces sémaphores permettent de contrôler l'accès concurrent à la ressource tout en respectant les priorités définies.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=43-44`

</details>

<!-- QID:2cea9db8604d -->
### Quel est un des inconvénients d'une solution basée sur l'exclusion mutuelle pour le problème des lecteurs-rédacteurs ?  <sup>p. 43–44</sup>

**Choix :**

- A) Elle permet des écritures simultanées.
- B) Elle empêche les lectures concurrentes.
- C) Elle favorise l'accès des rédacteurs.
- D) Elle ne nécessite pas de sémaphores.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** L'exclusion mutuelle peut nuire aux performances en bloquant les lectures concurrentes, ce qui est souvent nécessaire dans des systèmes à forte demande de lecture.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=43-44`

</details>

<!-- QID:1f83e6602ce7 -->
### Quelles sont les priorités possibles dans la gestion des accès aux ressources dans le problème des lecteurs-rédacteurs ?  <sup>p. 43–44</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** 1. Priorité aux lecteurs; 2. Priorité aux lecteurs si un lecteur a déjà accès; 3. Priorité aux rédacteurs; 4. Accès selon l'ordre d'arrivée.

**Pourquoi :** Ces priorités influencent la performance et l'équité dans l'accès aux ressources partagées.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=43-44`

</details>

<!-- QID:6fae6ea0cc24 -->
### Quelle est la principale caractéristique de l'algorithme des lecteurs-rédacteurs avec priorité aux lecteurs ?  <sup>p. 45–47</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Il permet aux lecteurs d'accéder à la ressource même si des rédacteurs sont en attente, empêchant ainsi les rédacteurs d'accéder à la ressource tant qu'il y a des lecteurs actifs.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=45-47`

</details>

<!-- QID:22345ae2a007 -->
### Dans l'algorithme des lecteurs-rédacteurs, la structure de données utilisée pour gérer l'accès est appelée ______.  <sup>p. 45–47</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** RessourceLectRed

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=45-47`

</details>

<!-- QID:48ba61c5d075 -->
### Quel sémaphore est utilisé pour contrôler l'accès des rédacteurs dans l'algorithme 5.1 ?  <sup>p. 45–47</sup>

**Choix :**

- A) mutexLecteurs
- B) mutexRedacteurs
- C) redacteur
- D) lecteurs

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C

**Pourquoi :** Le sémaphore 'redacteur' est spécifiquement utilisé pour gérer l'accès des rédacteurs à la ressource.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=45-47`

</details>

<!-- QID:e6f74306cfe1 -->
### Vrai ou Faux : Les lecteurs peuvent bloquer l'accès des rédacteurs à la ressource dans l'algorithme 5.1.  <sup>p. 45–47</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Vrai

**Pourquoi :** L'algorithme donne priorité aux lecteurs, ce qui signifie qu'ils peuvent empêcher les rédacteurs d'accéder à la ressource tant qu'ils sont présents.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=45-47`

</details>

<!-- QID:a02cbab4403d -->
### Quel est le rôle de la fonction 'debutLecture' dans l'algorithme des lecteurs-rédacteurs ?  <sup>p. 45–47</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Elle permet à un lecteur d'entrer dans la section critique, en incrémentant le nombre de lecteurs et en bloquant l'accès des rédacteurs si c'est le premier lecteur.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=45-47`

</details>

<!-- QID:953929c25b71 -->
### Que se passe-t-il lorsque le dernier lecteur termine sa lecture ?  <sup>p. 45–47</sup>

**Choix :**

- A) Le rédacteur peut accéder à la ressource
- B) Tous les lecteurs sont bloqués
- C) Un nouveau lecteur est immédiatement autorisé
- D) Le système se bloque

<details>
<summary>Afficher la réponse</summary>

**Réponse :** A

**Pourquoi :** Lorsque le dernier lecteur termine sa lecture, il libère le sémaphore 'redacteur', permettant ainsi à un rédacteur d'accéder à la ressource.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=45-47`

</details>

<!-- QID:97721113993e -->
### Vrai ou Faux : L'algorithme 5.1 garantit que les rédacteurs auront toujours accès à la ressource avant les lecteurs.  <sup>p. 45–47</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** L'algorithme 5.1 donne priorité aux lecteurs, ce qui signifie que les rédacteurs peuvent être bloqués indéfiniment si des lecteurs continuent d'accéder à la ressource.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=45-47`

</details>

<!-- QID:675b7bbdb2bb -->
### Pourquoi est-il important d'encapsuler la structure 'RessourceLectRed' dans le programme principal ?  <sup>p. 45–47</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Pour éviter que le programme principal n'interfère directement avec la gestion de la ressource, ce qui pourrait entraîner un état incohérent du système.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=45-47`

</details>

<!-- QID:41ff862cd4be -->
### Quel est l'effet d'une modification de l'algorithme pour donner priorité aux rédacteurs lorsque plusieurs rédacteurs sont en attente ?  <sup>p. 45–47</sup>

**Choix :**

- A) Les lecteurs sont toujours prioritaires
- B) Les rédacteurs en attente accèdent avant les nouveaux lecteurs
- C) Les rédacteurs sont bloqués indéfiniment
- D) Les lecteurs ne peuvent plus accéder à la ressource

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Cette modification permet aux rédacteurs en attente d'accéder à la ressource avant les nouveaux lecteurs, équilibrant ainsi l'accès.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=45-47`

</details>

<!-- QID:933bc0e827fb -->
### Qu'est-ce que l'algorithme des lecteurs-rédacteurs ?  <sup>p. 48–50</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C'est un modèle de synchronisation qui permet à plusieurs lecteurs de lire une ressource simultanément, mais limite l'accès à un seul rédacteur à la fois pour éviter les conflits.

**Pourquoi :** Cet algorithme est essentiel pour gérer l'accès concurrent à des ressources partagées, garantissant ainsi l'intégrité des données.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=48-50`

</details>

<!-- QID:eecbfc5ede22 -->
### Dans l'algorithme des lecteurs-rédacteurs, le sémaphore _______ protège l'accès à la variable nbLecteurs.  <sup>p. 48–50</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** mutex

**Pourquoi :** Le sémaphore mutex est utilisé pour éviter les accès concurrents à la variable qui compte le nombre de lecteurs, garantissant ainsi la cohérence des données.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=48-50`

</details>

<!-- QID:a472c0623b91 -->
### Quel est le rôle du sémaphore 'redacteur' dans l'algorithme des lecteurs-rédacteurs ?  <sup>p. 48–50</sup>

**Choix :**

- A) Il permet de bloquer les lecteurs.
- B) Il permet de bloquer les rédacteurs lorsque des lecteurs sont en cours de lecture.
- C) Il compte le nombre de rédacteurs.
- D) Il gère l'accès à la mémoire partagée.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Le sémaphore 'redacteur' est crucial pour garantir qu'un rédacteur ne puisse pas écrire lorsque des lecteurs accèdent à la ressource, évitant ainsi les conflits.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=48-50`

</details>

<!-- QID:27fe8db649d7 -->
### Un rédacteur peut accéder à la ressource même si des lecteurs sont en cours de lecture.  <sup>p. 48–50</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Un rédacteur ne peut accéder à la ressource que si aucun lecteur n'est en cours de lecture, afin d'éviter les conflits d'accès.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=48-50`

</details>

<!-- QID:4a8b0845af07 -->
### Quelle est la fonction de la variable nbLecteurs dans l'algorithme des lecteurs-rédacteurs ?  <sup>p. 48–50</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Elle compte le nombre de lecteurs actuellement en phase de lecture.

**Pourquoi :** Cette variable est essentielle pour déterminer si un rédacteur peut accéder à la ressource ou non.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=48-50`

</details>

<!-- QID:80248a45d36e -->
### Quel est l'objectif principal de l'algorithme avec priorité aux lecteurs ?  <sup>p. 48–50</sup>

**Choix :**

- A) Permettre aux rédacteurs d'accéder à la ressource en premier.
- B) Permettre aux lecteurs d'accéder à la ressource tant qu'aucun rédacteur n'est en cours d'écriture.
- C) Bloquer tous les accès à la ressource.
- D) Accélérer l'accès des rédacteurs.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Cet algorithme favorise l'accès des lecteurs pour améliorer la performance lorsque l'écriture n'est pas nécessaire.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=48-50`

</details>

<!-- QID:5d0d3c5a7e5a -->
### L'algorithme des lecteurs-rédacteurs peut entraîner des interblocages.  <sup>p. 48–50</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Vrai

**Pourquoi :** Si les sémaphores ne sont pas gérés correctement, il peut y avoir des interblocages, notamment si les lecteurs et rédacteurs attendent indéfiniment l'accès à la ressource.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=48-50`

</details>

<!-- QID:b4bd561cfc56 -->
### Quel est le rôle du sémaphore 'mutex' dans l'algorithme des lecteurs-rédacteurs ?  <sup>p. 51–53</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Le sémaphore 'mutex' protège l'accès à la variable 'nbLecteurs' et assure l'exclusion mutuelle lors des modifications des compteurs de lecteurs et rédacteurs.

**Pourquoi :** Cela empêche les conditions de course, garantissant que les mises à jour des compteurs sont atomiques.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=51-53`

</details>

<!-- QID:fefd6535b2ae -->
### Un lecteur peut accéder à la ressource si le nombre de rédacteurs en cours d'écriture vaut _____ et le nombre de rédacteurs en attente d'écriture vaut également _____.  <sup>p. 51–53</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** 0; 0

**Pourquoi :** Ces conditions garantissent qu'aucun rédacteur n'interfère avec la lecture, permettant un accès simultané par plusieurs lecteurs.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=51-53`

</details>

<!-- QID:93846d8019c9 -->
### Quel sémaphore bloque les rédacteurs lorsqu'un lecteur accède à la ressource ?  <sup>p. 51–53</sup>

**Choix :**

- A) lecteur
- B) mutex
- C) redacteur
- D) fifo

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C

**Pourquoi :** Le sémaphore 'redacteur' est utilisé pour empêcher les rédacteurs d'écrire tant qu'un lecteur est en train de lire.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=51-53`

</details>

<!-- QID:8cee67375d2c -->
### Vrai ou Faux : Dans l'algorithme avec priorité aux lecteurs, un rédacteur peut commencer à écrire tant qu'il y a des lecteurs en cours de lecture.  <sup>p. 51–53</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Un rédacteur ne peut accéder à la ressource que si aucun lecteur n'est en cours de lecture, afin d'éviter les conflits d'accès.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=51-53`

</details>

<!-- QID:1d648364ed87 -->
### Quelles sont les deux conditions qui permettent à un rédacteur d'accéder à la ressource ?  <sup>p. 51–53</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Le nombre de rédacteurs en cours d'écriture doit être 0 et le nombre de lecteurs en cours de lecture doit également être 0.

**Pourquoi :** Ces conditions garantissent que l'écriture ne sera pas interrompue par des lectures simultanées.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=51-53`

</details>

<!-- QID:e9eccec986fa -->
### Quel est l'effet de la fonction 'finLecture' dans l'algorithme des lecteurs-rédacteurs ?  <sup>p. 51–53</sup>

**Choix :**

- A) Elle bloque tous les lecteurs
- B) Elle débloque tous les lecteurs
- C) Elle décrémente le nombre de lecteurs
- D) Elle bloque les rédacteurs

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C

**Pourquoi :** Cette fonction est essentielle pour gérer l'accès à la ressource en permettant aux rédacteurs d'écrire lorsque tous les lecteurs ont terminé.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=51-53`

</details>

<!-- QID:42ac2ab4e65b -->
### Un moniteur contient des _______ et des _______ qui manipulent ces variables.  <sup>p. 54–57</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** variables; procédures

**Pourquoi :** Cette structure permet de contrôler l'accès aux données et de synchroniser les tâches qui interagissent avec ces données.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=54-57`

</details>

<!-- QID:62f35d3a0f25 -->
### Quel est le rôle des variables conditions (VC) dans un moniteur ?  <sup>p. 54–57</sup>

**Choix :**

- A) Elles stockent des données temporaires.
- B) Elles permettent de bloquer et de réveiller les tâches selon les spécifications du problème.
- C) Elles gèrent les erreurs de synchronisation.
- D) Elles augmentent la vitesse d'exécution.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Les VC sont essentielles pour gérer la synchronisation des tâches dans un moniteur, permettant un contrôle précis sur l'accès aux ressources partagées.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=54-57`

</details>

<!-- QID:9c5903b46605 -->
### Les procédures d'un moniteur peuvent être appelées directement par les tâches extérieures.  <sup>p. 54–57</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Les tâches n'ont pas un accès direct aux variables du moniteur; elles doivent passer par les points d'entrée fournis par les procédures du moniteur.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=54-57`

</details>

<!-- QID:32ac4c0f2117 -->
### Quelle opération est effectuée par la primitive 'cond.attente' dans un moniteur ?  <sup>p. 54–57</sup>

**Choix :**

- A) Elle termine l'exécution de la tâche.
- B) Elle bloque la tâche appelante et relâche l'exclusion mutuelle sur le moniteur.
- C) Elle signale une autre tâche.
- D) Elle initialise le moniteur.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Cette opération est cruciale pour permettre à d'autres tâches d'accéder au moniteur pendant que la tâche appelante attend une condition.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=54-57`

</details>

<!-- QID:d3b86db2d589 -->
### Quel est le rôle de la procédure 'Deverrouille' dans l'algorithme du verrou par moniteur ?  <sup>p. 58–59</sup>

**Choix :**

- A) Modifier l'état du verrou uniquement.
- B) Réveiller une tâche en attente.
- C) Bloquer toutes les tâches.
- D) Initialiser le verrou.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** La procédure 'Deverrouille' est conçue pour réveiller une tâche qui attend l'accès à la ressource protégée par le verrou.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=58-59`

</details>

<!-- QID:ddd3fca00548 -->
### La procédure 'attente' bloque la tâche appelante jusqu'à ce qu'elle soit réveillée par une autre tâche.  <sup>p. 58–59</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Vrai

**Pourquoi :** La procédure 'attente' suspend l'exécution de la tâche jusqu'à ce qu'une condition soit remplie, permettant ainsi à d'autres tâches de s'exécuter.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=58-59`

</details>

<!-- QID:17c4a368a545 -->
### Quel est le problème classique illustré par l'algorithme 6.2 ?  <sup>p. 58–59</sup>

**Choix :**

- A) Le problème des lecteurs et des écrivains.
- B) Le problème des producteurs et des consommateurs.
- C) Le problème de la faim.
- D) Le problème de la synchronisation des tâches.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Ce problème met en évidence les défis de la synchronisation entre les tâches qui produisent et consomment des ressources partagées.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=58-59`

</details>

<!-- QID:9d518aacab9b -->
### Dans l'algorithme du moniteur 'Tampons', la variable 'taille' représente _____ des articles dans le tampon.  <sup>p. 58–59</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** le nombre

**Pourquoi :** La variable 'taille' est cruciale pour gérer l'état du tampon et contrôler l'accès des producteurs et des consommateurs.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=58-59`

</details>

<!-- QID:544f4e5c2fc6 -->
### Qu'est-ce qu'un moniteur en pthreads ?  <sup>p. 60–61</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Un moniteur en pthreads est une abstraction qui combine des verrous et des variables conditions pour gérer la synchronisation entre threads.

**Pourquoi :** Les moniteurs permettent de contrôler l'accès à des ressources partagées et de gérer les conditions d'attente des threads.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=60-61`

</details>

<!-- QID:6c9dc9752159 -->
### La fonction pour créer un verrou en pthreads est ___.  <sup>p. 60–61</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** pthread_mutex_init

**Pourquoi :** Cette fonction initialise un verrou qui peut être utilisé pour protéger des sections critiques dans un programme multithread.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=60-61`

</details>

<!-- QID:568f890e065e -->
### Quelle fonction est utilisée pour déverrouiller un mutex en pthreads ?  <sup>p. 60–61</sup>

**Choix :**

- A) int pthread_mutex_lock(pthread_mutex_t *mutex)
- B) int pthread_mutex_unlock(pthread_mutex_t *mutex)
- C) int pthread_mutex_destroy(pthread_mutex_t *mutex)
- D) int pthread_mutex_init(pthread_mutex_t *m, const pthread_mutex_attr *attr)

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** La fonction pthread_mutex_unlock est spécifiquement conçue pour libérer un verrou précédemment acquis.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=60-61`

</details>

<!-- QID:f4a7a691ceb0 -->
### La fonction pthread_cond_signal garantit que la tâche signalée obtient immédiatement le verrou correspondant.  <sup>p. 60–61</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** La tâche signalée peut rester bloquée tant qu'elle n'a pas réussi à réacquérir le verrou, ce qui dépend de l'état de la synchronisation.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=60-61`

</details>

<!-- QID:1649622b70db -->
### Quelle est la différence entre pthread_cond_signal et pthread_cond_broadcast ?  <sup>p. 60–61</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** pthread_cond_signal réveille une seule tâche bloquée, tandis que pthread_cond_broadcast réveille toutes les tâches bloquées sur la variable condition.

**Pourquoi :** Cela permet de gérer différentes situations de synchronisation selon le besoin d'un seul ou de plusieurs threads.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=60-61`

</details>

<!-- QID:8fecd5c871c7 -->
### Quel est le rôle de la variable nbSignale dans la structure T_Moniteur ?  <sup>p. 60–61</sup>

**Choix :**

- A) Elle détermine le nombre de mutex actifs.
- B) Elle compte le nombre de tâches en attente sur le sémaphore signale.
- C) Elle stocke l'état du moniteur.
- D) Elle gère les priorités des tâches.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Cette variable est essentielle pour savoir combien de tâches doivent être réveillées lors de l'utilisation de signaux.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=60-61`

</details>

<!-- QID:d23c2461ef2b -->
### Il est recommandé d'appeler pthread_cond_signal à l'intérieur de la zone d'exclusion mutuelle du moniteur.  <sup>p. 60–61</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Pour des raisons d'efficacité, il est préférable d'appeler pthread_cond_signal en dehors de la zone d'exclusion mutuelle afin de permettre à la tâche signalée d'acquérir plus facilement le verrou.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=60-61`

</details>

<!-- QID:926a3cd6912d -->
### Quel est l'avantage principal des moniteurs ?  <sup>p. 62–63</sup>

**Choix :**

- A) Simplicité d'implémentation
- B) Protection associée au moniteur (exclusion mutuelle)
- C) Utilisation de sémaphores
- D) Accès direct aux variables partagées

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** L'exclusion mutuelle est essentielle pour éviter les conditions de course lors de l'accès à des ressources partagées.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=62-63`

</details>

<!-- QID:caa0ca35e5bf -->
### Les moniteurs garantissent que toutes les variables partagées sont accédées uniquement depuis les points d'entrée du moniteur.  <sup>p. 62–63</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Dans le cas de pthread, il n'y a aucune garantie que les variables partagées sont effectivement accédées uniquement depuis les points d'entrée du moniteur.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=62-63`

</details>

<!-- QID:9ce7df8dd734 -->
### La procédure _____ permet de déposer un message dans le tampon tout en bloquant si le tampon est plein.  <sup>p. 62–63</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Deposer

**Pourquoi :** Cette procédure utilise des conditions de synchronisation pour gérer l'accès au tampon partagé.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=62-63`

</details>

<!-- QID:d7fd93900524 -->
### Quels sont les inconvénients des moniteurs ?  <sup>p. 62–63</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Les inconvénients incluent un risque de manque de lisibilité et des variables condition qui sont de bas niveau.

**Pourquoi :** Ces inconvénients peuvent rendre le code plus difficile à comprendre et à maintenir, surtout avec des variations sémantiques entre les implémentations.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=62-63`

</details>

<!-- QID:aa6fe24ab06f -->
### Quelle fonction est utilisée pour initialiser un moniteur dans l'exemple donné ?  <sup>p. 62–63</sup>

**Choix :**

- A) Deposer
- B) Prelever
- C) InitialiseTampon
- D) DetruitTampon

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C

**Pourquoi :** La fonction InitialiseTampon est responsable de l'initialisation des mutex et des conditions nécessaires au fonctionnement du moniteur.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=62-63`

</details>

<!-- QID:7afa8f808a7e -->
### Que fait la fonction Prelever dans le contexte d'un moniteur ?  <sup>p. 62–63</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Elle renvoie le message du tampon et bloque tant que le tampon est vide.

**Pourquoi :** Cela garantit que les consommateurs ne tentent pas de retirer un message lorsque le tampon est vide, évitant ainsi des erreurs de synchronisation.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=62-63`

</details>

<!-- QID:ae559906ad55 -->
### Dans le problème des producteurs et des consommateurs, la fonction ______________ est utilisée pour ajouter un article au tampon.  <sup>p. 64–66</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** deposer

**Pourquoi :** La fonction 'deposer' gère l'ajout d'articles dans le tampon tout en respectant les conditions de synchronisation.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=64-66`

</details>

<!-- QID:bb1e7e2df3dd -->
### Quel est le rôle de la variable condition 'pasPlein' dans l'algorithme des producteurs et des consommateurs ?  <sup>p. 64–66</sup>

**Choix :**

- A) Elle permet de signaler aux producteurs que le tampon n'est pas plein.
- B) Elle permet de signaler aux consommateurs que le tampon est vide.
- C) Elle permet de gérer l'accès exclusif au tampon.
- D) Elle permet de compter le nombre d'articles dans le tampon.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** A

**Pourquoi :** La variable condition 'pasPlein' est essentielle pour synchroniser les producteurs, leur indiquant quand ils peuvent ajouter des articles au tampon.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=64-66`

</details>

<!-- QID:722502cfafaf -->
### La fonction 'retirer' dans l'algorithme des producteurs et des consommateurs peut être appelée même si le tampon est vide.  <sup>p. 64–66</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** La fonction 'retirer' attend que le tampon contienne des articles avant de pouvoir retirer un élément, ce qui est géré par la variable condition 'pasVide'.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=64-66`

</details>

<!-- QID:3d190e276da8 -->
### Quelle est la principale différence entre les versions de l'algorithme des producteurs et des consommateurs présentées ?  <sup>p. 64–66</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** La version finale simplifie la gestion des signaux en supprimant l'utilisation de 'Tampons.nbSignale' et en simplifiant les conditions d'attente.

**Pourquoi :** Cette simplification réduit la complexité de l'algorithme tout en maintenant la fonctionnalité de synchronisation.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=64-66`

</details>

<!-- QID:2295b9c12f1f -->
### Quel est l'effet de l'instruction 'sem_wait(&Tampons.mutex)' dans les fonctions 'deposer' et 'retirer' ?  <sup>p. 64–66</sup>

**Choix :**

- A) Elle bloque l'accès concurrent à la section critique.
- B) Elle libère le mutex pour d'autres threads.
- C) Elle signale qu'un article a été ajouté.
- D) Elle augmente la taille du tampon.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** A

**Pourquoi :** L'instruction 'sem_wait' est utilisée pour acquérir un verrou, garantissant que seul un thread peut accéder à la section critique à la fois.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=64-66`

</details>

<!-- QID:28d37f9f51da -->
### Qu'est-ce que la bibliothèque Pthread en C ?  <sup>p. 67–68</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** La bibliothèque Pthread est une bibliothèque POSIX qui permet la gestion des threads en C, offrant des outils de synchronisation et de création de threads.

**Pourquoi :** Elle est essentielle pour la programmation concurrente en C, car le langage C n'a pas de mécanisme natif pour gérer les threads.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=67-68`

</details>

<!-- QID:c4e1f03043fc -->
### Pour utiliser un thread en Pthread, il est nécessaire de déclarer une variable de type ______.  <sup>p. 67–68</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** pthread_t

**Pourquoi :** Le type pthread_t est utilisé pour identifier les threads dans la bibliothèque Pthread.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=67-68`

</details>

<!-- QID:808557dc3d76 -->
### Quel est le rôle de la fonction pthread_join() ?  <sup>p. 67–68</sup>

**Choix :**

- A) Créer un thread
- B) Attendre la terminaison d'un thread
- C) Déverrouiller un mutex
- D) Annuler un thread

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** pthread_join() permet à un thread d'attendre qu'un autre thread se termine, ce qui est crucial pour la synchronisation.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=67-68`

</details>

<!-- QID:022b2ffb4c26 -->
### Pour créer un verrou en Pthread, il faut déclarer une variable de type ______ et l'initialiser avec ______.  <sup>p. 67–68</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** pthread_mutex_t, PTHREAD_MUTEX_INITIALIZER

**Pourquoi :** Cette initialisation est nécessaire pour garantir que le mutex est dans un état valide avant son utilisation.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=67-68`

</details>

<!-- QID:b589413335bb -->
### Quelle est la valeur de retour de pthread_create() en cas de succès ?  <sup>p. 67–68</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** 0

**Pourquoi :** Un retour de 0 indique que le thread a été créé avec succès, tandis qu'une valeur différente indique une erreur.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=67-68`

</details>

<!-- QID:2d1cfe21e0f0 -->
### La constante PTHREAD_THREADS_MAX définit le nombre minimum de threads pouvant être créés.  <sup>p. 67–68</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** PTHREAD_THREADS_MAX définit le nombre maximum de threads pouvant être créés sur un système donné.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=67-68`

</details>

<!-- QID:ff89c9e5e423 -->
### Quelle fonction permet de verrouiller un mutex de manière non bloquante ?  <sup>p. 67–68</sup>

**Choix :**

- A) pthread_mutex_lock()
- B) pthread_mutex_unlock()
- C) pthread_mutex_trylock()
- D) pthread_mutex_destroy()

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C

**Pourquoi :** pthread_mutex_trylock() tente de verrouiller un mutex sans bloquer le thread si le mutex est déjà verrouillé.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=67-68`

</details>

<!-- QID:1d2a34af7c4f -->
### Quelle est la fonction de pthread_mutex_lock() ?  <sup>p. 69–70</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Elle verrouille un mutex, bloquant le thread appelant si le mutex est déjà verrouillé.

**Pourquoi :** Cela permet de protéger les sections critiques dans un programme multithread.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=69-70`

</details>

<!-- QID:e2bce7fd9568 -->
### Que renvoie pthread_mutex_lock() en cas de succès ?  <sup>p. 69–70</sup>

**Choix :**

- A) 0
- B) 1
- C) EINVAL
- D) EDEADLK

<details>
<summary>Afficher la réponse</summary>

**Réponse :** A

**Pourquoi :** Un retour de 0 indique que le verrou a été acquis avec succès.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=69-70`

</details>

<!-- QID:3cbcc49399f8 -->
### pthread_mutex_lock() est une fonction non bloquante.  <sup>p. 69–70</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** pthread_mutex_lock() bloque le thread appelant si le mutex est déjà verrouillé.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=69-70`

</details>

<!-- QID:38bf26ec2ae5 -->
### La fonction pthread_mutex_trylock() est une fonction _____ qui tente de verrouiller un mutex.  <sup>p. 69–70</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** non bloquante

**Pourquoi :** Elle permet au thread d'essayer d'acquérir le mutex sans attendre, retournant EBUSY si le mutex est déjà verrouillé.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=69-70`

</details>

<!-- QID:89d11e8b6524 -->
### Que renvoie pthread_mutex_trylock() si le mutex est déjà verrouillé ?  <sup>p. 69–70</sup>

**Choix :**

- A) 0
- B) EBUSY
- C) EINVAL
- D) EFAULT

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** EBUSY indique que le mutex est déjà en cours d'utilisation par un autre thread.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=69-70`

</details>

<!-- QID:31ad62d6cf96 -->
### Quels sont les codes d'erreur possibles pour pthread_mutex_unlock() ?  <sup>p. 69–70</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** EINVAL et EPERM.

**Pourquoi :** EINVAL indique un verrou non initialisé, tandis qu'EPERM indique que le thread appelant ne détient pas le verrou.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=69-70`

</details>

<!-- QID:e269cc30b963 -->
### La fonction pthread_join() prend en paramètres un pthread_t thread et un ________ value_ptr.  <sup>p. 71–73</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** void **

**Pourquoi :** value_ptr est utilisé pour recevoir la valeur de retour du thread spécifié.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=71-73`

</details>

<!-- QID:2947d0fd8ed0 -->
### Que se passe-t-il lorsque pthread_detach() est appelé sur un thread ?  <sup>p. 71–73</sup>

**Choix :**

- A) Le thread est terminé immédiatement.
- B) Le thread est détaché et ses ressources sont libérées à sa terminaison.
- C) Le thread devient prioritaire.
- D) Le thread ne peut plus être créé.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Détacher un thread signifie qu'il ne peut plus être joint avec pthread_join(), et ses ressources sont automatiquement libérées.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=71-73`

</details>

<!-- QID:a967f468688f -->
### Quelle est la différence entre pthread_cancel() et pthread_detach() ?  <sup>p. 71–73</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** pthread_cancel() annule un thread en cours d'exécution, tandis que pthread_detach() détache un thread pour libérer ses ressources à sa terminaison sans attendre sa fin.

**Pourquoi :** Cela permet de gérer la synchronisation et la gestion des ressources de manière appropriée dans les programmes multithreads.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=71-73`

</details>

<!-- QID:60680b748e22 -->
### Quel est l'effet de pthread_self() ?  <sup>p. 71–73</sup>

**Choix :**

- A) Elle termine le thread courant.
- B) Elle retourne l'identifiant du thread courant.
- C) Elle crée un nouveau thread.
- D) Elle suspend le thread courant.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** pthread_self() est utilisée pour obtenir l'identifiant du thread qui appelle cette fonction, ce qui est utile pour des comparaisons ou des opérations spécifiques.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=71-73`

</details>

<!-- QID:b4972464ac2d -->
### La fonction pthread_cancel() utilise la ________ d'annulation pour déterminer comment un thread doit être annulé.  <sup>p. 71–73</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** politique

**Pourquoi :** La politique d'annulation détermine le moment et la manière dont un thread peut être annulé, ce qui est crucial pour la gestion des threads.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=71-73`

</details>

<!-- QID:df2421771b17 -->
### Quelle fonction permet de définir la politique d'annulation d'un thread en POSIX?  <sup>p. 74–75</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** pthread_setcancelstate()

**Pourquoi :** Cette fonction permet de contrôler si un thread peut être annulé par un autre thread.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=74-75`

</details>

<!-- QID:d511003c9337 -->
### Quel est l'effet de la fonction pthread_setcanceltype() avec le paramètre PTHREAD_CANCEL_ASYNCHRONOUS?  <sup>p. 74–75</sup>

**Choix :**

- A) Autorise l'annulation du thread à n'importe quel instant.
- B) Interdit l'annulation du thread.
- C) Autorise l'annulation du thread en des points d'annulation précis.
- D) Met le thread dans un état suspendu.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** A

**Pourquoi :** L'annulation asynchrone permet d'interrompre un thread à tout moment, ce qui peut entraîner des états instables.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=74-75`

</details>

<!-- QID:406a37e78af2 -->
### La fonction pthread_testcancel() doit être utilisée uniquement avec des threads ayant un type d'annulation asynchrone.  <sup>p. 74–75</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** pthread_testcancel() est utilisée pour vérifier les demandes d'annulation dans les threads avec un type d'annulation différée.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=74-75`

</details>

<!-- QID:e0965088a100 -->
### La fonction pthread_setcancelstate() prend comme paramètres un état qui peut être ______ ou ______.  <sup>p. 74–75</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** PTHREAD_CANCEL_ENABLE, PTHREAD_CANCEL_DISABLE

**Pourquoi :** Ces valeurs déterminent si le thread peut être annulé ou non.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=74-75`

</details>

<!-- QID:10cf9384c2ad -->
### Quelles sont les deux opérations de base sur les sémaphores?  <sup>p. 74–75</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Incrémenter le compteur (opération V) et décrémenter le compteur (opération P).

**Pourquoi :** Ces opérations permettent de gérer l'accès concurrent aux ressources partagées.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=74-75`

</details>

<!-- QID:a1c919b71493 -->
### Quelle fonction initialise un sémaphore en POSIX?  <sup>p. 74–75</sup>

**Choix :**

- A) sem_init()
- B) sem_destroy()
- C) sem_post()
- D) sem_wait()

<details>
<summary>Afficher la réponse</summary>

**Réponse :** A

**Pourquoi :** sem_init() est utilisée pour créer et initialiser un sémaphore avant son utilisation.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=74-75`

</details>

<!-- QID:cb700152dccb -->
### Quel type de sémaphore est créé par sem_init() lorsqu'il est alloué dynamiquement?  <sup>p. 74–75</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Sémaphore anonyme.

**Pourquoi :** Un sémaphore anonyme est créé sans nom et est utilisé uniquement dans le contexte du programme qui l'a créé.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=74-75`

</details>

<!-- QID:34a5277627f6 -->
### Les fonctions manipulant les sémaphores renvoient -1 en cas de succès.  <sup>p. 74–75</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Elles renvoient 0 en cas de succès et -1 en cas d'erreur.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=74-75`

</details>

<!-- QID:3846440099e6 -->
### Pour accéder à la variable errno, il faut inclure le fichier d'en-tête ______.  <sup>p. 74–75</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** errno.h

**Pourquoi :** Ce fichier contient les définitions nécessaires pour gérer les erreurs dans les appels système.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=74-75`

</details>

<!-- QID:ba44acd8a234 -->
### Quelle est la fonction utilisée pour initialiser un sémaphore en Pthreads?  <sup>p. 76</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** sem_init()

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=76-76`

</details>

<!-- QID:220e6e3280ca -->
### La fonction sem_init() retourne 0 si la création du sémaphore s'est déroulée sans ___.  <sup>p. 76</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** accros

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=76-76`

</details>

<!-- QID:ec81a8a65e21 -->
### Quel paramètre de sem_init() détermine si le sémaphore est partagé entre plusieurs processus?  <sup>p. 76</sup>

**Choix :**

- A) value
- B) sem
- C) pshare
- D) errno

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C

**Pourquoi :** Le paramètre pshare spécifie si le sémaphore est local au processus courant (0) ou partagé (différent de 0).

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=76-76`

</details>

<!-- QID:7160bba3f298 -->
### Vrai ou Faux: Un mutex est un sémaphore initialisé à 0.  <sup>p. 76</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Un mutex est un sémaphore initialisé à 1, permettant un accès exclusif à une ressource.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=76-76`

</details>

<!-- QID:a2bc91a81b0a -->
### Quels codes d'erreur peuvent être retournés par sem_init() en cas d'erreur?  <sup>p. 76</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** EINVAL et ENOSYS

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=76-76`

</details>

<!-- QID:d0ba5f7d1d8d -->
### Que se passe-t-il si sem_destroy() est appelé sur un sémaphore avec des threads bloqués?  <sup>p. 76</sup>

**Choix :**

- A) Le sémaphore est détruit sans problème
- B) Le sémaphore est réinitialisé
- C) Comportement indéfini
- D) Le sémaphore est automatiquement débloqué

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C

**Pourquoi :** Appeler sem_destroy() sur un sémaphore avec des threads bloqués entraîne un comportement indéfini, ce qui peut causer des erreurs dans le programme.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=76-76`

</details>

<!-- QID:aeaa737a2104 -->
### Quelle fonction est utilisée pour déverrouiller un sémaphore?  <sup>p. 76</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** sem_post()

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=76-76`

</details>

<!-- QID:66fc3dfbe22e -->
### Vrai ou Faux: La fonction sem_post() incrémente toujours la valeur du sémaphore.  <sup>p. 76</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** sem_post() incrémente la valeur du sémaphore seulement si le compteur est positif; sinon, elle débloque un thread en attente.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=76-76`

</details>

<!-- QID:025efe79064e -->
### La fonction sem_wait() est utilisée pour ___ un sémaphore.  <sup>p. 76</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** bloquer

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=76-76`

</details>

<!-- QID:90d956700d09 -->
### Quelle est la fonction de sem_wait() ?  <sup>p. 77–79</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** La fonction sem_wait() verrouille le sémaphore spécifié. Si la valeur du sémaphore est 0, le thread appelant est bloqué jusqu'à ce qu'il soit déverrouillé. Sinon, elle décrémente le compteur et retourne immédiatement.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=77-79`

</details>

<!-- QID:31f22ca84b05 -->
### Quelle est la différence entre sem_wait() et sem_trywait() ?  <sup>p. 77–79</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** sem_wait() bloque le thread si le sémaphore est à 0, tandis que sem_trywait() retourne -1 sans bloquer si le sémaphore est à 0.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=77-79`

</details>

<!-- QID:1b9ac3680ac1 -->
### Que retourne sem_trywait() si le sémaphore est à 0 ?  <sup>p. 77–79</sup>

**Choix :**

- A) 0
- B) -1
- C) 1
- D) EAGAIN

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** sem_trywait() retourne -1 lorsque le sémaphore est à 0, indiquant que l'opération n'a pas pu être effectuée.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=77-79`

</details>

<!-- QID:092616ba3807 -->
### La fonction sem_getvalue() affecte l'état du sémaphore.  <sup>p. 77–79</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** sem_getvalue() ne modifie pas l'état du sémaphore, elle retourne simplement sa valeur actuelle.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=77-79`

</details>

<!-- QID:c2d564e67017 -->
### La fonction sem_getvalue() place la valeur du sémaphore dans l'entier pointé par ___ .  <sup>p. 77–79</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** sval

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=77-79`

</details>

<!-- QID:2152d79693a7 -->
### Quel est le rôle de la fonction gettimeofday() ?  <sup>p. 77–79</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** gettimeofday() récupère le nombre de secondes et microsecondes écoulées depuis le début de la journée.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=77-79`

</details>

<!-- QID:c62aff422878 -->
### Quels champs contient la structure timeval utilisée par gettimeofday() ?  <sup>p. 77–79</sup>

**Choix :**

- A) tv_sec et tv_usec
- B) sec et usec
- C) seconds et microseconds
- D) time et duration

<details>
<summary>Afficher la réponse</summary>

**Réponse :** A

**Pourquoi :** La structure timeval contient deux champs : tv_sec pour les secondes et tv_usec pour les microsecondes.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=77-79`

</details>

<!-- QID:0e0d7c34a0bf -->
### Quelle fonction permet de mesurer le temps processeur consommé par un processus en C ?  <sup>p. 80–81</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** La fonction clock().

**Pourquoi :** Cette fonction retourne le nombre de coups d'horloge écoulés depuis le lancement du programme, permettant ainsi de calculer le temps d'exécution d'un traitement spécifique.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=80-81`

</details>

<!-- QID:7f7e59fe039b -->
### La constante ________ donne le nombre de coups d'horloge par seconde.  <sup>p. 80–81</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** CLOCKS_PER_SEC

**Pourquoi :** Cette constante est essentielle pour convertir le nombre de coups d'horloge en secondes, facilitant ainsi l'évaluation du temps d'exécution.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=80-81`

</details>

<!-- QID:f50196a89c12 -->
### Quel est le résultat de l'expression '((double) (end - start)) / CLOCKS_PER_SEC' ?  <sup>p. 80–81</sup>

**Choix :**

- A) Le nombre de coups d'horloge.
- B) Le temps écoulé en millisecondes.
- C) Le temps écoulé en secondes.
- D) Le temps d'exécution en nanosecondes.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C

**Pourquoi :** Cette expression convertit la différence entre les coups d'horloge de début et de fin en secondes, ce qui est utile pour évaluer la durée d'un traitement.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=80-81`

</details>

<!-- QID:bebbead396f5 -->
### La fonction clock() retourne le temps écoulé depuis le début de l'exécution du programme en secondes.  <sup>p. 80–81</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** La fonction clock() retourne le nombre de coups d'horloge, qui doit être divisé par CLOCKS_PER_SEC pour obtenir le temps en secondes.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=80-81`

</details>

<!-- QID:4f912fa973f3 -->
### Pourquoi est-il important de mesurer le temps processeur d'un processus ?  <sup>p. 80–81</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Pour savoir exactement le temps passé sur une tâche particulière, même si le processeur est partagé entre plusieurs processus.

**Pourquoi :** Cela permet d'optimiser les performances et d'identifier les goulets d'étranglement dans l'exécution des tâches.

**Source :** `courses/PCO/data/pdf/pco_polycopie.pdf#p=80-81`

</details>
