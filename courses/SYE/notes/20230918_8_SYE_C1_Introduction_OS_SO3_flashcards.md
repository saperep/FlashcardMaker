---
course: "SYE"
generated_at: "2025-09-18T07:32:30"
source_pdf: "courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf"
---

# Flashcards – SYE

---
### Résumé essentiel

Les systèmes d'exploitation (OS) sont des logiciels fondamentaux qui gèrent le matériel informatique et fournissent des services aux applications. Leur évolution a commencé avec des concepts tels que la machine différentielle de Charles Babbage, et les premiers OS sont apparus entre 1945 et 1955, utilisant des technologies primitives comme les tubes à vide. La deuxième génération d'ordinateurs a introduit les transistors et des langages de programmation tels que Fortran, tandis que la multiprogrammation et le système de batch ont optimisé l'utilisation des ressources. UNIX, lancé en 1969, a établi des standards d'interopérabilité, influençant le développement de systèmes modernes comme Linux et Windows. 

Les OS se divisent en plusieurs familles, incluant ceux de Microsoft, Apple et les logiciels libres, chacun ayant des variantes adaptées à des besoins spécifiques. L'architecture d'un OS se compose de trois couches : le matériel, le noyau et les applications, où le noyau joue un rôle crucial dans la gestion des accès au matériel. SO3, un système d'exploitation léger et open source, est conçu pour les systèmes embarqués et permet d'explorer des techniques avancées comme la migration live de code. La gestion de la mémoire et la commutation entre tâches sont des aspects essentiels, avec des systèmes monotâches et multitâches ayant des implications différentes sur la performance et la complexité. Enfin, l'espace d'adressage, qui dépend de la taille des registres du processeur, est crucial pour la gestion de la mémoire, avec des distinctions importantes comme l'endianness.

### À retenir absolument

- Les systèmes d'exploitation gèrent le matériel et fournissent des services aux applications.
- L'architecture d'un OS comprend le matériel, le noyau et les applications, avec le noyau comme élément central.
- SO3 est un OS léger open source pour systèmes embarqués, permettant l'expérimentation avec des microcontrôleurs ARM.
- La gestion de la mémoire et la commutation entre tâches sont essentielles pour la performance des systèmes d'exploitation.
- L'espace d'adressage, déterminé par la taille des registres, est fondamental pour la gestion de la mémoire et inclut des concepts comme l'endianness.

---

<!-- QID:06de0554224d -->
### Qui sont les professeurs responsables du cours SYE ?  <sup>p. 1–7</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Daniel Rossier, Alexandre Corbaz, Fiorenzo Gamba.

**Pourquoi :** Connaître les enseignants permet de savoir à qui s'adresser pour des questions spécifiques sur le cours.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=1-7`

</details>

<!-- QID:0829c2950537 -->
### La première notion d'ordinateur a été introduite par _____ en 1833 avec la machine différentielle.  <sup>p. 1–7</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Charles Babbage

**Pourquoi :** Charles Babbage est souvent considéré comme le père de l'informatique pour ses contributions fondamentales.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=1-7`

</details>

<!-- QID:10dbaa30a40c -->
### Quel est l'objectif principal de la machine différentielle conçue par Charles Babbage ?  <sup>p. 1–7</sup>

**Choix :**

- A) Exécuter des opérations simples
- B) Résoudre n'importe quelle équation
- C) Imprimer des livres
- D) Calculer des statistiques

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** La machine différentielle était conçue pour effectuer des calculs complexes, ce qui est fondamental pour le développement des ordinateurs.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=1-7`

</details>

<!-- QID:c3a10fe9e0c9 -->
### La machine différentielle de Charles Babbage était capable d'exécuter des opérations de l'analyse mathématique.  <sup>p. 1–7</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Vrai

**Pourquoi :** La machine était spécifiquement conçue pour résoudre des équations et effectuer des opérations mathématiques complexes.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=1-7`

</details>

<!-- QID:6a446e336cca -->
### Quel est le rôle de l'Institut REDS ?  <sup>p. 1–7</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** L'Institut REDS se concentre sur les systèmes numériques embarqués reconfigurables.

**Pourquoi :** Comprendre le contexte de l'institut aide à situer l'importance des cours et des recherches menées.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=1-7`

</details>

<!-- QID:d9623297abc6 -->
### Quel type de matériel est disponible sur Cyberlearn (Moodle) pour le cours SYE ?  <sup>p. 1–7</sup>

**Choix :**

- A) Chapitres de cours uniquement
- B) Série d'exercices uniquement
- C) Chapitres de cours, série d'exercices, énoncés de laboratoire
- D) Aucun matériel

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C

**Pourquoi :** Le matériel de cours est essentiel pour la préparation et la compréhension des sujets abordés.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=1-7`

</details>

<!-- QID:48d7815f9b97 -->
### Quel était le principal composant des ordinateurs de première génération?  <sup>p. 8–10</sup>

**Choix :**

- A) Transistors
- B) Relais et tubes à vide
- C) Circuits intégrés
- D) Microprocesseurs

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Les ordinateurs de première génération utilisaient des relais et des tubes à vide comme composants principaux.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=8-10`

</details>

<!-- QID:b8cccca980b7 -->
### La deuxième génération d'ordinateurs a été basée sur l'invention du _____ en 1947.  <sup>p. 8–10</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** transistor

**Pourquoi :** L'invention du transistor a permis de remplacer les tubes à vide, rendant les ordinateurs plus petits et plus fiables.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=8-10`

</details>

<!-- QID:2aa8fb70fd79 -->
### Les systèmes d'exploitation de la deuxième génération étaient principalement conçus pour traiter des cartes perforées.  <sup>p. 8–10</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Vrai

**Pourquoi :** Les systèmes d'exploitation de la deuxième génération, comme FMS et IBSYS, étaient spécifiquement conçus pour lire et traiter les cartes perforées.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=8-10`

</details>

<!-- QID:4f97e94b40e3 -->
### Quel était un des principaux problèmes rencontrés avec les systèmes de la deuxième génération?  <sup>p. 8–10</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Le temps gaspillé lors des manipulations humaines et du chargement des programmes.

**Pourquoi :** Ces manipulations entraînaient des retards significatifs dans le traitement des données, ce qui était problématique pour les entreprises.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=8-10`

</details>

<!-- QID:63279523f7a5 -->
### Quel système a été introduit pour réduire le temps de traitement dans les systèmes d'exploitation?  <sup>p. 8–10</sup>

**Choix :**

- A) Système en temps réel
- B) Système de batch
- C) Système distribué
- D) Système d'exploitation mobile

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Le système de batch permettait de traiter plusieurs jobs de manière plus efficace en utilisant des machines spécialisées.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=8-10`

</details>

<!-- QID:769d7b3afe05 -->
### Quels langages de programmation étaient utilisés dans la deuxième génération d'ordinateurs?  <sup>p. 8–10</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Fortran ou assembleur.

**Pourquoi :** Ces langages étaient adaptés aux cartes perforées et aux capacités des ordinateurs de l'époque.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=8-10`

</details>

<!-- QID:da016fd7f762 -->
### Les ordinateurs de première génération étaient principalement utilisés par des entreprises.  <sup>p. 8–10</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Ils étaient principalement utilisés par des universités et des institutions militaires, avec un accès limité pour les entreprises.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=8-10`

</details>

<!-- QID:7eb67d5e58e5 -->
### Qu'est-ce que la troisième génération d'ordinateurs?  <sup>p. 11</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** La troisième génération d'ordinateurs est celle des ordinateurs à circuit intégré, offrant un meilleur rapport prix/performance.

**Pourquoi :** Cette génération a marqué une avancée technologique majeure, permettant une utilisation plus large de l'informatique.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=11-11`

</details>

<!-- QID:086ff8afff65 -->
### Quel était l'objectif principal de la famille IBM System/360?  <sup>p. 11</sup>

**Choix :**

- A) Développer des jeux vidéo
- B) Unifier plusieurs lignes de produits
- C) Réduire la taille des ordinateurs
- D) Améliorer la sécurité des données

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** IBM System/360 visait à créer une architecture compatible avec divers besoins, facilitant l'utilisation des circuits intégrés.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=11-11`

</details>

<!-- QID:c5a51de12a7e -->
### L'OS/360 d'IBM était exempt de bugs.  <sup>p. 11</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Bien que l'OS/360 ait connu un grand succès, il contenait de nombreux bugs et était complexe en raison de la diversité des tâches qu'il devait gérer.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=11-11`

</details>

<!-- QID:56084d4567a2 -->
### La multiprogrammation permet aux jobs actifs de ne plus attendre sur des ___ comme une bande.  <sup>p. 11</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** I/O (entrées-sorties)

**Pourquoi :** Cette technique optimise l'utilisation des ressources en permettant à plusieurs processus de s'exécuter simultanément.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=11-11`

</details>

<!-- QID:1750b55c0582 -->
### Qu'est-ce que le spool?  <sup>p. 11</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Le spool (Simultaneous Peripheral Operation On Line) permet le traitement des jobs au fur et à mesure.

**Pourquoi :** Cette technique améliore l'efficacité du traitement des tâches en gérant les opérations d'entrée/sortie de manière asynchrone.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=11-11`

</details>

<!-- QID:bc80edb955f3 -->
### Quel projet a introduit de nombreuses innovations notables dans le développement des systèmes d'exploitation?  <sup>p. 11</sup>

**Choix :**

- A) Unix
- B) Linux
- C) Multics
- D) POSIX

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C

**Pourquoi :** Multics a été un projet ambitieux qui a introduit des concepts avancés, bien qu'il n'ait pas connu un grand succès commercial.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=11-11`

</details>

<!-- QID:c4cb2a5f0b46 -->
### Quel est le lien entre UNIX et le projet Multics?  <sup>p. 11</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** UNIX a été développé par Ken Thompson comme une version allégée de Multics.

**Pourquoi :** Cette simplification a permis de créer un système plus accessible et adaptable, qui a eu un impact durable sur l'informatique.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=11-11`

</details>

<!-- QID:ad35b0b9a2c0 -->
### Le standard POSIX a été développé pour assurer la compatibilité entre les différentes versions d'UNIX.  <sup>p. 11</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Vrai

**Pourquoi :** POSIX a été créé pour standardiser les interfaces des systèmes UNIX, facilitant ainsi le développement de logiciels portables.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=11-11`

</details>

<!-- QID:603279309423 -->
### Le développement de ___ a été basé sur Minix et a été lancé en 1991.  <sup>p. 11</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Linux

**Pourquoi :** Linux est devenu un système d'exploitation open source influent, basé sur les concepts pédagogiques de Minix.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=11-11`

</details>

<!-- QID:bc0d5502269e -->
### Qu'est-ce qu'un microprocesseur ?  <sup>p. 12</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Un microprocesseur est un circuit intégré qui regroupe la plupart des composants de calcul sur un seul circuit.

**Pourquoi :** Cette définition souligne l'importance des microprocesseurs dans la miniaturisation et l'efficacité des ordinateurs modernes.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=12-12`

</details>

<!-- QID:21a4be763d3e -->
### Quel système d'exploitation a été développé par Bill Gates pour IBM ?  <sup>p. 12</sup>

**Choix :**

- A) Windows
- B) MS-DOS
- C) Linux
- D) Unix

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** MS-DOS a été acheté et modifié par Bill Gates pour répondre aux besoins d'IBM, marquant le début de l'ascension de Microsoft.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=12-12`

</details>

<!-- QID:2dc866bf08b7 -->
### La première version de MS-DOS était très sophistiquée.  <sup>p. 12</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** La première version de MS-DOS était très primitive, mais elle a permis d'implanter le système sur le long terme.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=12-12`

</details>

<!-- QID:03879613a100 -->
### Le concept d'_____ graphique a été un facteur décisif pour le succès des systèmes d'exploitation.  <sup>p. 12</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** IHM (Interface Humain-Machine)

**Pourquoi :** L'IHM graphique a amélioré l'interaction utilisateur et a été adoptée par des entreprises comme Apple et Microsoft.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=12-12`

</details>

<!-- QID:4b5e09530d9f -->
### Quel événement a conduit IBM à se tourner vers Bill Gates pour un système d'exploitation ?  <sup>p. 12</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Le refus de Gary Kindall, fondateur de Digital Research, de rencontrer IBM.

**Pourquoi :** Ce refus a ouvert la voie à Microsoft pour fournir un système d'exploitation à IBM, ce qui a été crucial pour son succès.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=12-12`

</details>

<!-- QID:869db95562ae -->
### Quelle innovation a été intégrée au noyau de Windows en 1995 ?  <sup>p. 12</sup>

**Choix :**

- A) Le multitâche
- B) L'IHM
- C) La virtualisation
- D) Le support réseau

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** L'intégration de l'IHM au noyau a marqué une étape importante dans l'évolution des systèmes d'exploitation Windows.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=12-12`

</details>

<!-- QID:aa22be651072 -->
### Quel était le modèle économique de Bill Gates pour MS-DOS ?  <sup>p. 12</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Vendre MS-DOS aux constructeurs de machines plutôt qu'aux particuliers.

**Pourquoi :** Ce modèle a permis d'assurer une large distribution de MS-DOS, contribuant à son adoption généralisée.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=12-12`

</details>

<!-- QID:5866ba1cb00c -->
### Le X Window System a été développé par Microsoft.  <sup>p. 12</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Le X Window System a été développé par le MIT et est commun à toutes les machines UNIX-like.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=12-12`

</details>

<!-- QID:7ac4c54dc1fe -->
### Qu'est-ce qu'un système d'exploitation ?  <sup>p. 13–15</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Un système d'exploitation est l'ensemble de programmes central d'un appareil informatique qui sert d'interface entre le matériel et les logiciels applicatifs.

**Pourquoi :** Cette définition souligne le rôle fondamental du système d'exploitation dans la gestion des ressources matérielles et logicielles.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=13-15`

</details>

<!-- QID:3e71b1c74941 -->
### Un système d'exploitation comprend également des ________ en plus des composants nécessaires aux interactions machine-application.  <sup>p. 13–15</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** applications

**Pourquoi :** Cela met en évidence que les systèmes d'exploitation modernes intègrent des applications pour améliorer l'expérience utilisateur.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=13-15`

</details>

<!-- QID:1dcf79c85c0a -->
### Quel est un exemple de système d'exploitation de type GPOS ?  <sup>p. 13–15</sup>

**Choix :**

- A) Windows
- B) RTOS
- C) Embedded OS
- D) Executive OS

<details>
<summary>Afficher la réponse</summary>

**Réponse :** A

**Pourquoi :** Les systèmes d'exploitation de type GPOS sont conçus pour une utilisation générale, comme Windows, tandis que les autres types sont spécialisés.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=13-15`

</details>

<!-- QID:6f3ad7510753 -->
### Tous les systèmes d'exploitation respectent les mêmes concepts fondamentaux liés aux architectures d'OS.  <sup>p. 13–15</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Vrai

**Pourquoi :** Malgré leurs différences, tous les systèmes d'exploitation partagent des concepts architecturaux fondamentaux qui sont essentiels à leur fonctionnement.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=13-15`

</details>

<!-- QID:d8d7b33f230c -->
### Quels sont les trois grandes familles de systèmes d'exploitation ?  <sup>p. 13–15</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Les systèmes d'exploitation provenant de Microsoft, ceux provenant d'Apple, et ceux développés dans le cadre des logiciels libres (comme Linux).

**Pourquoi :** Cette classification aide à comprendre les différents écosystèmes et philosophies de développement des systèmes d'exploitation.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=13-15`

</details>

<!-- QID:e100d3f099bc -->
### Quel type de système d'exploitation est destiné à des applications critiques ?  <sup>p. 13–15</sup>

**Choix :**

- A) General Purpose OS
- B) Real-Time OS
- C) Embedded OS
- D) Executive OS

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Les systèmes d'exploitation temps-réel strict sont conçus pour répondre à des exigences de temps de réponse critiques, ce qui est essentiel pour certaines applications.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=13-15`

</details>

<!-- QID:836e275b5c57 -->
### Sous Unix/Linux/Mac-OS-X, un système d'exploitation comprend également un ________.  <sup>p. 13–15</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** compilateur C

**Pourquoi :** Cela montre que ces systèmes d'exploitation sont souvent utilisés pour le développement logiciel, intégrant des outils de programmation.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=13-15`

</details>

<!-- QID:783e74a4b066 -->
### Quelles sont les trois couches principales de l'architecture d'un système d'exploitation ?  <sup>p. 16–19</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Le matériel, le noyau de l'OS, et les applications.

**Pourquoi :** Ces couches permettent de structurer le fonctionnement d'un système d'exploitation, chaque couche ayant des responsabilités spécifiques.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=16-19`

</details>

<!-- QID:2f0950e7227c -->
### Le noyau de l'OS est responsable de ________ les accès au matériel et de gérer différents contextes d'exécution.  <sup>p. 16–19</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** sécuriser

**Pourquoi :** La sécurisation des accès au matériel est essentielle pour protéger le système contre les accès non autorisés et garantir la stabilité.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=16-19`

</details>

<!-- QID:56c6f45ca6cc -->
### Quel est l'objectif principal de SO3 ?  <sup>p. 16–19</sup>

**Choix :**

- A) Développer des applications de bureau.
- B) Fournir un environnement de jeu.
- C) Un environnement compact et performant pour expérimenter avec des processeurs ARM.
- D) Créer un système d'exploitation pour serveurs.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C

**Pourquoi :** SO3 est spécifiquement conçu pour les systèmes embarqués et l'expérimentation avec des processeurs ARM, ce qui le distingue des autres systèmes d'exploitation.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=16-19`

</details>

<!-- QID:71930dd64b10 -->
### Quel langage de programmation est utilisé pour développer SO3 ?  <sup>p. 16–19</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C et assembleur ARM.

**Pourquoi :** L'utilisation de C et d'assembleur ARM permet d'optimiser les performances et d'accéder directement aux fonctionnalités du matériel.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=16-19`

</details>

<!-- QID:e872ee438df6 -->
### Quel système de compilation est utilisé pour SO3 ?  <sup>p. 16–19</sup>

**Choix :**

- A) Makefile
- B) KBuild
- C) CMake
- D) Autotools

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** KBuild est un système de construction spécifique à Linux, adapté pour gérer la compilation de projets comme SO3.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=16-19`

</details>

<!-- QID:a3287ff762ab -->
### SO3 peut fonctionner uniquement sur des systèmes physiques et ne peut pas être émulé.  <sup>p. 16–19</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** SO3 peut également tourner dans un environnement émulé avec Qemu, ce qui permet de tester et d'expérimenter sans matériel physique.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=16-19`

</details>

<!-- QID:5889a11142ef -->
### Quel type de processeur est émulé dans l'environnement de SO3?  <sup>p. 20–22</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Un processeur ARM 32-bit de type Cortex-A15.

**Pourquoi :** Cela permet d'étudier le fonctionnement d'un système d'exploitation sur une architecture spécifique.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=20-22`

</details>

<!-- QID:9006dd5ee1d5 -->
### Le noyau SO3 est ________ et est écrit en C et en assembleur ARM.  <sup>p. 20–22</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Open Source

**Pourquoi :** Le fait que le noyau soit open source permet aux étudiants de l'étudier et de le modifier librement.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=20-22`

</details>

<!-- QID:467a49d7291b -->
### Quel est l'avantage principal de l'utilisation de Qemu pour SO3?  <sup>p. 20–22</sup>

**Choix :**

- A) Coût réduit
- B) Facilité de débogage
- C) Compatibilité avec tous les systèmes d'exploitation
- D) Accès direct au matériel

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Qemu permet de simuler un environnement de développement qui facilite le débogage et l'analyse des programmes.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=20-22`

</details>

<!-- QID:ff4262dbf2a7 -->
### L'espace utilisateur dans l'architecture de SO3 inclut le noyau de l'OS.  <sup>p. 20–22</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** L'espace utilisateur comprend les applications développées, tandis que le noyau de l'OS se trouve dans l'espace noyau.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=20-22`

</details>

<!-- QID:c4f7fd7572f5 -->
### Quel IDE est utilisé pour le développement de SO3?  <sup>p. 20–22</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Visual Studio Code.

**Pourquoi :** Cet IDE permet une intégration facile avec des outils de débogage et de compilation.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=20-22`

</details>

<!-- QID:7a95af6be427 -->
### Quel outil est intégré dans Qemu pour faciliter le débogage?  <sup>p. 20–22</sup>

**Choix :**

- A) Serveur http
- B) Serveur gdb
- C) Serveur ftp
- D) Serveur ssh

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Le serveur gdb permet de se connecter à la cible émulée pour analyser le comportement des programmes en temps réel.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=20-22`

</details>

<!-- QID:fd7fe5652b9b -->
### La compilation du noyau SO3 s'effectue en ________.  <sup>p. 20–22</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** ligne de commande (Makefile)

**Pourquoi :** Utiliser un Makefile permet d'automatiser le processus de compilation et de gérer les dépendances.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=20-22`

</details>

<!-- QID:d7b4e20071f7 -->
### Il est possible de déboguer uniquement le noyau SO3, pas les applications.  <sup>p. 20–22</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Il est possible de déboguer à la fois le noyau SO3 et les applications qui s'exécutent sur celui-ci.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=20-22`

</details>

<!-- QID:a32a4efafd85 -->
### Quel est le rôle du répertoire 'so3' dans le projet?  <sup>p. 23–26</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Il contient l'ensemble du noyau de l'OS SO3.

**Pourquoi :** Le noyau est responsable de la gestion des ressources matérielles et de l'exécution des processus.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=23-26`

</details>

<!-- QID:ad9ad66eaef4 -->
### Que contient le répertoire 'usr'?  <sup>p. 23–26</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Il comprend les applications utilisateur et la librairie libc.

**Pourquoi :** La librairie libc fournit des fonctions standards en C et des appels systèmes nécessaires aux applications.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=23-26`

</details>

<!-- QID:f841dacbc42d -->
### Le démarrage de l'environnement SO3 s'effectue à l'aide du script ___.  <sup>p. 23–26</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** ./st

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=23-26`

</details>

<!-- QID:911bc01540fb -->
### Quel système de fichiers est principalement implémenté dans SO3?  <sup>p. 23–26</sup>

**Choix :**

- A) NTFS
- B) FAT-32
- C) ext4
- D) HFS+

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** FAT-32 est un système de fichiers couramment utilisé pour les cartes SD, ce qui le rend pertinent pour SO3.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=23-26`

</details>

<!-- QID:2cb71f204afa -->
### Le shell de SO3 peut terminer son exécution.  <sup>p. 23–26</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Le shell est démarré comme premier processus par le noyau et n'a pas de parent, il ne peut donc jamais terminer.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=23-26`

</details>

<!-- QID:1e5851d9f461 -->
### Quel est le rôle du répertoire 'ipc' dans SO3?  <sup>p. 23–26</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Il contient les mécanismes de communication inter-processus tels que les tubes anonymes et les signaux.

**Pourquoi :** Ces mécanismes sont essentiels pour permettre aux processus de communiquer et de synchroniser leurs actions.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=23-26`

</details>

<!-- QID:f49a90f428ac -->
### Comment se fait la compilation des applications dans SO3?  <sup>p. 23–26</sup>

**Choix :**

- A) Via VS Code
- B) En ligne de commande
- C) Automatiquement
- D) Avec un IDE graphique

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** La compilation en ligne de commande est nécessaire pour gérer les dépendances et les configurations spécifiques dans un environnement Linux.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=23-26`

</details>

<!-- QID:2285b30b626b -->
### Les binaires exécutables dans SO3 sont en format ___.  <sup>p. 23–26</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** ELF

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=23-26`

</details>

<!-- QID:e27f33abbf11 -->
### Qu'est-ce qu'un système monotâche ?  <sup>p. 27–29</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Un système monotâche est un système d'exploitation qui permet l'exécution d'une seule application à la fois, avec une adresse de chargement fixe pour l'application.

**Pourquoi :** Cela simplifie la gestion de la mémoire et améliore les performances, mais limite l'utilisation à une seule application.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=27-29`

</details>

<!-- QID:57c64b2996b2 -->
### Un système monotâche peut exécuter plusieurs applications simultanément.  <sup>p. 27–29</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Un système monotâche ne peut exécuter qu'une seule application à la fois, ce qui le rend moins efficace pour l'utilisation des ressources CPU.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=27-29`

</details>

<!-- QID:2426a940f506 -->
### Quel est un inconvénient majeur d'un système monotâche ?  <sup>p. 27–29</sup>

**Choix :**

- A) Il utilise plus de mémoire.
- B) Il nécessite un ordonnanceur complexe.
- C) La commutation entre tâches nécessite le remplacement de la tâche courante par une autre.
- D) Il ne peut pas être utilisé dans des systèmes embarqués.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C

**Pourquoi :** Cette limitation rend le système monotâche moins flexible et efficace pour des applications nécessitant une multitâche.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=27-29`

</details>

<!-- QID:9c54cdc0da47 -->
### Qu'est-ce qu'un système multitâche ?  <sup>p. 27–29</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Un système multitâche permet l'exécution de plusieurs applications en mémoire RAM, augmentant ainsi l'utilisation du CPU.

**Pourquoi :** Cela permet une meilleure utilisation des ressources et une réponse plus rapide aux demandes des utilisateurs.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=27-29`

</details>

<!-- QID:fc48a3424f3c -->
### L'espace d'adressage représente l'ensemble des octets que le processeur peut ________.  <sup>p. 27–29</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** référencer

**Pourquoi :** Chaque octet est adressable individuellement, ce qui permet au processeur d'accéder à la mémoire de manière précise.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=27-29`

</details>

<!-- QID:aefe5fb7e27d -->
### Quel est le principal avantage d'un système multitâche par rapport à un système monotâche ?  <sup>p. 27–29</sup>

**Choix :**

- A) Simplicité de gestion.
- B) Augmentation de l'utilisation du CPU.
- C) Moins de mémoire requise.
- D) Pas besoin d'ordonnanceur.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Un système multitâche permet à plusieurs applications de résider en RAM, ce qui optimise l'utilisation des ressources CPU.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=27-29`

</details>

<!-- QID:93f6ade72ee8 -->
### Un système byte-adressable signifie qu'un octet est la plus petite unité adressable par le processeur.  <sup>p. 27–29</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Vrai

**Pourquoi :** Cela signifie que chaque octet peut être référencé individuellement, facilitant l'accès à la mémoire.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=27-29`

</details>

<!-- QID:af02912907ab -->
### Qu'est-ce que le code relogeable ?  <sup>p. 27–29</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Le code relogeable est un code binaire qui nécessite un ajustement des adresses en fonction de l'adresse de base lors du chargement en mémoire.

**Pourquoi :** Cela permet à plusieurs programmes d'être chargés à des adresses différentes sans nécessiter de recompilation.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=27-29`

</details>

<!-- QID:2d5670b6cb63 -->
### Qu'est-ce que l'espace d'adressage ?  <sup>p. 30</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** L'espace d'adressage représente l'ensemble des octets que le processeur peut référencer.

**Pourquoi :** Cela définit la capacité du processeur à accéder à la mémoire et à gérer les données.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=30-30`

</details>

<!-- QID:e6fa198e4b5f -->
### L'octet est la plus petite entité adressable par le processeur, et chaque octet est référençable avec une ______.  <sup>p. 30</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** adresse

**Pourquoi :** L'adresse détermine l'emplacement exact d'un octet dans la mémoire.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=30-30`

</details>

<!-- QID:ba28f0370be9 -->
### Quelle est la quantité de bytes adressable sur une architecture 32 bits ?  <sup>p. 30</sup>

**Choix :**

- A) 2 Go
- B) 4 Go
- C) 8 Go
- D) 16 Go

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Sur une architecture 32 bits, le registre peut stocker une adresse représentable sur 32 bits, permettant d'adresser 2^32 octets.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=30-30`

</details>

<!-- QID:892a6373bc8a -->
### Sur une architecture 32 bits, les adresses vont de 0x0 à 0xffffffff.  <sup>p. 30</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Vrai

**Pourquoi :** Cela correspond à la plage d'adresses possible pour 4 Go de mémoire, soit 2^32 adresses.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=30-30`

</details>

<!-- QID:426c5d00a190 -->
### Qu'est-ce que le système byte-adressable ?  <sup>p. 30</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Un système byte-adressable permet d'accéder à chaque octet individuellement et indépendamment.

**Pourquoi :** Cela signifie que chaque octet peut être référencé par une adresse unique.

**Source :** `courses/SYE/data/pdf/20230918_8_SYE_C1_Introduction_OS_SO3.pdf#p=30-30`

</details>
