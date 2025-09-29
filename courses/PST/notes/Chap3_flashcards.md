---
course: "PST"
generated_at: "2025-09-29T15:45:21"
source_pdf: "courses/PST/data/pdf/Chap3.pdf"
---

# Flashcards – PST

---
### Résumé essentiel

Les systèmes de contrôle sont des dispositifs qui régulent le comportement d'autres systèmes à l'aide de boucles de rétroaction, permettant ainsi de maintenir des performances souhaitées. Un système est considéré comme stable s'il revient à son état d'équilibre après une perturbation, sans oscillations croissantes. La fonction de transfert est un outil clé qui relie l'entrée à la sortie d'un système dans le domaine de Laplace, facilitant l'analyse des systèmes dynamiques. Les systèmes à rétroaction négative sont généralement préférés, car ils améliorent la stabilité et réduisent les erreurs de suivi, contrairement aux systèmes à rétroaction positive. Les contrôleurs PID (Proportionnel, Intégral, Dérivé) sont largement utilisés pour optimiser la réponse des systèmes, chaque terme jouant un rôle spécifique dans la régulation des erreurs. La modélisation précise du système est cruciale pour le succès d'un contrôleur, car des modèles incorrects peuvent entraîner des performances sous-optimales. La stabilité d'un système peut être évaluée à l'aide de critères tels que le critère de Routh-Hurwitz ou le diagramme de Nyquist, qui aident à déterminer la réponse du système aux perturbations. Les erreurs fréquentes dans l'analyse et la conception des systèmes incluent la négligence des effets de saturation, de non-linéarité, et un réglage inapproprié des gains du contrôleur, pouvant mener à des oscillations ou à une réponse lente. Enfin, la compréhension des systèmes dynamiques, y compris les notions de bifurcation et d'attracteurs, est essentielle pour anticiper les comportements complexes des systèmes réels.

### À retenir absolument
- Les systèmes de contrôle régulent d'autres systèmes via des boucles de rétroaction.
- Un système est stable si, après perturbation, il revient à son état d'équilibre.
- La fonction de transfert relie l'entrée et la sortie d'un système dans le domaine de Laplace.
- Les contrôleurs PID optimisent la réponse des systèmes en combinant trois actions distinctes.
- Les erreurs fréquentes incluent la négligence des effets de saturation et un réglage inapproprié des gains.

---

<!-- QID:55836a7d55fb -->
### Qu'est-ce qu'un algorithme ?  <sup>p. 1–4</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Un algorithme est une suite finie d'instructions ou d'étapes permettant de résoudre un problème ou d'effectuer une tâche.

**Pourquoi :** Les algorithmes sont fondamentaux en ingénierie car ils permettent de formaliser des processus de calcul et de prise de décision.

**Source :** `courses/PST/data/pdf/Chap3.pdf#p=1-4`

</details>

<!-- QID:bcaf97729409 -->
### Un algorithme est une suite finie d'_____ permettant de résoudre un problème.  <sup>p. 1–4</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** instructions

**Pourquoi :** Les instructions sont les étapes précises que l'on suit pour atteindre un résultat.

**Source :** `courses/PST/data/pdf/Chap3.pdf#p=1-4`

</details>

<!-- QID:7634a146911f -->
### Quel est l'objectif principal d'un algorithme ?  <sup>p. 1–4</sup>

**Choix :**

- A) Résoudre un problème
- B) Rendre un programme plus lent
- C) Augmenter la complexité
- D) Éliminer les erreurs de syntaxe

<details>
<summary>Afficher la réponse</summary>

**Réponse :** A

**Pourquoi :** L'objectif principal d'un algorithme est de fournir une méthode systématique pour résoudre un problème donné.

**Source :** `courses/PST/data/pdf/Chap3.pdf#p=1-4`

</details>

<!-- QID:de95c301ed62 -->
### Tous les algorithmes doivent être exécutés en un temps fini.  <sup>p. 1–4</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Vrai

**Pourquoi :** Un algorithme est défini comme une procédure finie, ce qui signifie qu'il doit se terminer après un nombre fini d'étapes.

**Source :** `courses/PST/data/pdf/Chap3.pdf#p=1-4`

</details>

<!-- QID:bb115114593a -->
### Quels sont les critères d'évaluation d'un algorithme ?  <sup>p. 1–4</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Les critères incluent la correction, l'efficacité (temps et espace), la clarté et la robustesse.

**Pourquoi :** Ces critères permettent de juger de la qualité d'un algorithme et de son adéquation à un problème donné.

**Source :** `courses/PST/data/pdf/Chap3.pdf#p=1-4`

</details>

<!-- QID:7d173fb8ae1a -->
### Quel est un inconvénient potentiel des algorithmes complexes ?  <sup>p. 1–4</sup>

**Choix :**

- A) Facilité d'implémentation
- B) Difficulté de compréhension
- C) Rapidité d'exécution
- D) Efficacité énergétique

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Les algorithmes complexes peuvent être difficiles à comprendre et à maintenir, ce qui peut entraîner des erreurs.

**Source :** `courses/PST/data/pdf/Chap3.pdf#p=1-4`

</details>

<!-- QID:0df9e2f6659e -->
### Un algorithme peut être considéré comme correct s'il produit toujours le bon résultat pour toutes les entrées possibles.  <sup>p. 1–4</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Vrai

**Pourquoi :** La correction d'un algorithme est déterminée par sa capacité à produire les résultats attendus pour toutes les entrées valides.

**Source :** `courses/PST/data/pdf/Chap3.pdf#p=1-4`

</details>

<!-- QID:ad197e32e17e -->
### Quel est l'un des principaux avantages d'un algorithme bien conçu ?  <sup>p. 5–8</sup>

**Choix :**

- A) Il augmente la complexité du code.
- B) Il permet d'optimiser le temps de traitement.
- C) Il rend le code moins lisible.
- D) Il nécessite plus de ressources matérielles.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Un algorithme bien conçu permet de résoudre un problème de manière efficace, réduisant ainsi le temps nécessaire pour obtenir un résultat.

**Source :** `courses/PST/data/pdf/Chap3.pdf#p=5-8`

</details>

<!-- QID:f0d7ab856e39 -->
### Tous les algorithmes sont efficaces.  <sup>p. 5–8</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** L'efficacité d'un algorithme dépend de sa conception et de la complexité des opérations qu'il effectue. Certains algorithmes peuvent être très lents ou gourmands en ressources.

**Source :** `courses/PST/data/pdf/Chap3.pdf#p=5-8`

</details>

<!-- QID:94e2b2292193 -->
### Quelles sont les caractéristiques d'un bon algorithme ?  <sup>p. 5–8</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Un bon algorithme doit être clair, fini, efficace, et produire un résultat correct pour toutes les entrées valides.

**Source :** `courses/PST/data/pdf/Chap3.pdf#p=5-8`

</details>

<!-- QID:b935348a28ba -->
### Quelle est la première étape dans la conception d'un algorithme ?  <sup>p. 5–8</sup>

**Choix :**

- A) Écrire le code.
- B) Définir le problème à résoudre.
- C) Tester l'algorithme.
- D) Optimiser les performances.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Comprendre le problème est essentiel pour concevoir un algorithme efficace qui répond aux besoins spécifiques.

**Source :** `courses/PST/data/pdf/Chap3.pdf#p=5-8`

</details>

<!-- QID:8bb72527628a -->
### Les algorithmes peuvent être classés en fonction de leur ______ et de leur ______.  <sup>p. 5–8</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** complexité, efficacité

**Source :** `courses/PST/data/pdf/Chap3.pdf#p=5-8`

</details>

<!-- QID:2319414f7678 -->
### Un algorithme peut être considéré comme un programme informatique.  <sup>p. 5–8</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Vrai

**Pourquoi :** Un algorithme est une série d'instructions qui peut être implémentée dans un programme informatique pour exécuter une tâche spécifique.

**Source :** `courses/PST/data/pdf/Chap3.pdf#p=5-8`

</details>

<!-- QID:3b807afcad34 -->
### Qu'est-ce qu'un système dynamique ?  <sup>p. 9–11</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Un système dynamique est un système dont l'état évolue dans le temps en fonction de ses entrées et de ses conditions initiales.

**Pourquoi :** Comprendre la dynamique d'un système est essentiel pour modéliser et contrôler des processus en ingénierie.

**Source :** `courses/PST/data/pdf/Chap3.pdf#p=9-11`

</details>

<!-- QID:cf75f9195762 -->
### Un système dynamique peut être décrit par une équation différentielle de type _____ ou _____ selon qu'il est linéaire ou non linéaire.  <sup>p. 9–11</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** linéaire; non linéaire

**Pourquoi :** La nature de l'équation différentielle influence les méthodes de résolution et le comportement du système.

**Source :** `courses/PST/data/pdf/Chap3.pdf#p=9-11`

</details>

<!-- QID:5fa3197ff9fb -->
### Les systèmes non linéaires ne peuvent pas être analysés par des méthodes de superposition.  <sup>p. 9–11</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Vrai

**Pourquoi :** La non-linéarité implique que les réponses du système ne peuvent pas être simplement additionnées, rendant leur analyse plus complexe.

**Source :** `courses/PST/data/pdf/Chap3.pdf#p=9-11`

</details>

<!-- QID:4e88a1129bd5 -->
### Quel type de réponse un système dynamique linéaire présente-t-il en réponse à une entrée sinusoïdale ?  <sup>p. 9–11</sup>

**Choix :**

- A) Une réponse sinusoïdale de même fréquence.
- B) Une réponse aléatoire.
- C) Une réponse exponentielle.
- D) Une réponse en escalier.

<details>
<summary>Afficher la réponse</summary>

**Réponse :** A

**Pourquoi :** Les systèmes linéaires répondent à des entrées sinusoïdales par des sorties sinusoïdales de même fréquence, ce qui est une caractéristique clé de leur comportement.

**Source :** `courses/PST/data/pdf/Chap3.pdf#p=9-11`

</details>

<!-- QID:651f67a4a052 -->
### Un système dynamique peut être décrit par des ________ différentielles.  <sup>p. 12–15</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** équations

**Pourquoi :** Les équations différentielles sont fondamentales pour modéliser les changements d'état dans le temps.

**Source :** `courses/PST/data/pdf/Chap3.pdf#p=12-15`

</details>

<!-- QID:7fe336595c48 -->
### Tous les systèmes dynamiques sont linéaires.  <sup>p. 12–15</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Les systèmes dynamiques peuvent être linéaires ou non linéaires, ce qui influence leur comportement et leur modélisation.

**Source :** `courses/PST/data/pdf/Chap3.pdf#p=12-15`

</details>

<!-- QID:ef8bc7057732 -->
### Quel est un avantage des systèmes linéaires par rapport aux systèmes non linéaires ?  <sup>p. 12–15</sup>

**Choix :**

- A) Ils sont plus réalistes
- B) Ils sont plus faciles à analyser
- C) Ils nécessitent moins de ressources
- D) Ils sont plus rapides

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Les systèmes linéaires peuvent être analysés à l'aide de techniques mathématiques plus simples, ce qui facilite leur étude.

**Source :** `courses/PST/data/pdf/Chap3.pdf#p=12-15`

</details>

<!-- QID:523d8e157510 -->
### Les systèmes dynamiques ne peuvent pas être modélisés par des simulations numériques.  <sup>p. 12–15</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Les simulations numériques sont souvent utilisées pour modéliser des systèmes dynamiques complexes, en particulier lorsque des solutions analytiques ne sont pas disponibles.

**Source :** `courses/PST/data/pdf/Chap3.pdf#p=12-15`

</details>

<!-- QID:52de6ecdaac1 -->
### Qu'est-ce qu'un algorithme en ingénierie?  <sup>p. 16–20</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Un algorithme est une suite finie d'instructions ou d'étapes permettant de résoudre un problème ou d'accomplir une tâche spécifique.

**Pourquoi :** Les algorithmes sont fondamentaux en ingénierie car ils permettent de formaliser et d'automatiser des processus complexes.

**Source :** `courses/PST/data/pdf/Chap3.pdf#p=16-20`

</details>

<!-- QID:d34f6ac2a1a4 -->
### Quelle est la complexité temporelle d'un algorithme de tri par insertion dans le pire des cas?  <sup>p. 16–20</sup>

**Choix :**

- A) O(n)
- B) O(n log n)
- C) O(n²)
- D) O(1)

<details>
<summary>Afficher la réponse</summary>

**Réponse :** C

**Pourquoi :** Dans le pire des cas, le tri par insertion nécessite de comparer chaque élément avec tous les autres, ce qui donne une complexité quadratique.

**Source :** `courses/PST/data/pdf/Chap3.pdf#p=16-20`

</details>

<!-- QID:17b03f65e2d8 -->
### La complexité spatiale d'un algorithme ne prend pas en compte la mémoire utilisée par les variables temporaires.  <sup>p. 16–20</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** La complexité spatiale inclut toute la mémoire utilisée, y compris celle des variables temporaires, pour évaluer l'impact global sur les ressources.

**Source :** `courses/PST/data/pdf/Chap3.pdf#p=16-20`

</details>

<!-- QID:c261d91fc8a6 -->
### Un système dynamique peut être décrit par des ________ qui relient les entrées, les sorties et l'état du système.  <sup>p. 21–23</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** équations différentielles

**Pourquoi :** Les équations différentielles sont fondamentales pour modéliser le comportement temporel des systèmes dynamiques.

**Source :** `courses/PST/data/pdf/Chap3.pdf#p=21-23`

</details>

<!-- QID:93d34cb5bec6 -->
### Quel est l'objectif principal de l'analyse des systèmes dynamiques ?  <sup>p. 21–23</sup>

**Choix :**

- A) A) Optimiser les coûts de production
- B) B) Prédire le comportement futur du système
- C) C) Réduire le temps de calcul
- D) D) Améliorer l'esthétique du produit

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** L'analyse des systèmes dynamiques vise à comprendre et prédire comment un système évolue au fil du temps.

**Source :** `courses/PST/data/pdf/Chap3.pdf#p=21-23`

</details>

<!-- QID:d89cb0fa3503 -->
### Vrai ou Faux : Tous les systèmes dynamiques sont linéaires.  <sup>p. 21–23</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Faux

**Pourquoi :** Les systèmes dynamiques peuvent être linéaires ou non linéaires, et la nature de la dynamique dépend des équations qui les décrivent.

**Source :** `courses/PST/data/pdf/Chap3.pdf#p=21-23`

</details>

<!-- QID:349b8f0e1cd2 -->
### Quels sont les deux types de systèmes dynamiques ?  <sup>p. 21–23</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Les systèmes dynamiques peuvent être classés en systèmes linéaires et systèmes non linéaires.

**Pourquoi :** Cette classification est cruciale car elle influence les méthodes d'analyse et de contrôle utilisées.

**Source :** `courses/PST/data/pdf/Chap3.pdf#p=21-23`

</details>

<!-- QID:bd96b7dbc656 -->
### Un système dynamique est caractérisé par des ________ qui changent au fil du temps.  <sup>p. 24–27</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** états

**Source :** `courses/PST/data/pdf/Chap3.pdf#p=24-27`

</details>

<!-- QID:09bd64017dd5 -->
### Quel est l'élément clé qui distingue un système dynamique d'un système statique ?  <sup>p. 24–27</sup>

**Choix :**

- A) A. La présence d'entrées
- B) B. L'évolution des états dans le temps
- C) C. La complexité du modèle
- D) D. La taille du système

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Un système dynamique est défini par le fait que ses états changent au cours du temps, contrairement à un système statique qui reste constant.

**Source :** `courses/PST/data/pdf/Chap3.pdf#p=24-27`

</details>

<!-- QID:a4b9bf37d27f -->
### Un système dynamique peut être modélisé par des équations différentielles.  <sup>p. 24–27</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** Vrai

**Pourquoi :** Les équations différentielles sont souvent utilisées pour décrire l'évolution des états dans le temps d'un système dynamique.

**Source :** `courses/PST/data/pdf/Chap3.pdf#p=24-27`

</details>

<!-- QID:591c69c7af6f -->
### Quel est un exemple de système dynamique continu ?  <sup>p. 24–27</sup>

**Choix :**

- A) A. Un pendule
- B) B. Un ordinateur
- C) C. Un réseau électrique
- D) D. Un thermostat

<details>
<summary>Afficher la réponse</summary>

**Réponse :** A

**Pourquoi :** Un pendule est un exemple classique de système dynamique continu, car son mouvement est décrit par des équations différentielles continues.

**Source :** `courses/PST/data/pdf/Chap3.pdf#p=24-27`

</details>

<!-- QID:25d9c97a884d -->
### Les systèmes dynamiques non linéaires peuvent présenter des ________ complexes, comme le chaos.  <sup>p. 24–27</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** comportements

**Source :** `courses/PST/data/pdf/Chap3.pdf#p=24-27`

</details>

<!-- QID:bebedf50b575 -->
### Quels sont les avantages de modéliser un système dynamique ?  <sup>p. 24–27</sup>

<details>
<summary>Afficher la réponse</summary>

**Réponse :** La modélisation permet de prédire le comportement futur du système, d'optimiser les performances et de concevoir des contrôleurs adaptés.

**Source :** `courses/PST/data/pdf/Chap3.pdf#p=24-27`

</details>

<!-- QID:2d528985b189 -->
### Quel est un exemple de système dynamique à temps discret ?  <sup>p. 28–30</sup>

**Choix :**

- A) Un pendule simple
- B) Un automate à états finis.
- C) Un circuit électrique
- D) Un fluide en mouvement

<details>
<summary>Afficher la réponse</summary>

**Réponse :** B

**Pourquoi :** Les automates à états finis évoluent par étapes discrètes, ce qui les classe comme des systèmes à temps discret.

**Source :** `courses/PST/data/pdf/Chap3.pdf#p=28-30`

</details>
