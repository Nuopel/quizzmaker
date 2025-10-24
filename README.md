# 🎓 Système de Quiz Interactif

Un système modulaire et extensible pour créer et exécuter des quiz interactifs en ligne de commande.  C'est un refactoring d'un vieux projet en utilisant l'ia Claude. 

## 📋 Table des matières

- [Caractéristiques](#-caractéristiques)
- [Installation](#-installation)
- [Structure du projet](#-structure-du-projet)
- [Guide d'utilisation](#-guide-dutilisation)
  - [Créer des questions](#1-créer-des-questions)
  - [Exécuter un quiz](#2-exécuter-un-quiz)
  - [Exporter en HTML](#3-exporter-en-html)
- [Format des questions](#-format-des-questions)
- [Exemples](#-exemples)
- [API](#-api)

---

## ✨ Caractéristiques

- ✅ **3 types de questions** : Choix multiple, Vrai/Faux, Réponse courte
- 📊 **3 niveaux de difficulté** : Easy, Medium, Hard
- 🔍 **Filtres avancés** : Par section, difficulté, type de question
- 🎲 **Randomisation** : Questions et options mélangées aléatoirement
- 📈 **Statistiques détaillées** : Performance par difficulté, score global
- 💾 **Sauvegarde des résultats** : Export JSON des résultats de quiz
- 🌐 **Export HTML** : Génération de quiz web interactifs avec pagination configurable
- 🏗️ **Architecture modulaire** : Séparation claire des responsabilités
- 🐼 **Format CSV** : Utilisation de pandas pour la gestion des données

---

## 🔧 Installation

### Prérequis

- Python 3.8 ou supérieur
- pandas

### Installation des dépendances

```bash
pip install pandas
```

---

## 📁 Structure du projet

```
quizzmaker/
│
├── src/quizzmaker/
│   ├── models.py                      # Modèles de données (Question, QuizResult, QuizSummary)
│   ├── question_generator.py          # Générateur de questions
│   ├── quiz_runner.py                 # Exécuteur de quiz
│   ├── html_exporter.py               # Exporteur HTML (nouveau)
│   └── __init__.py
│
├── examples/
│   ├── example_create_questions.py    # Exemple : créer des questions
│   ├── example_run_quiz.py            # Exemple : exécuter un quiz
│   ├── example_html_export.py         # Exemple : export HTML interactif
│   └── example_direct_html_export.py  # Exemple : export HTML direct (nouveau)
│
├── README.md                          # Documentation (ce fichier)
│
└── *.csv                              # Bases de questions (générées)
```

### Description des modules

| Module                  | Responsabilité                                                        |
| ----------------------- | --------------------------------------------------------------------- |
| `models.py`             | Définit les structures de données (Question, QuizResult, QuizSummary) |
| `question_generator.py` | Création, validation et sauvegarde de questions                       |
| `quiz_runner.py`        | Chargement de questions, création et exécution de quiz                |
| `html_exporter.py`      | Génération de quiz HTML interactifs avec pagination                   |

---

## 📚 Guide d'utilisation

### 1. Créer des questions

#### Méthode 1 : Utiliser l'exemple fourni

```bash
python example_create_questions.py
```

Cela génère un fichier `example_python_questions.csv` avec 8 questions d'exemple.

#### Méthode 2 : Créer vos propres questions

```python
from question_generator import QuestionGenerator

# Initialiser le générateur
generator = QuestionGenerator()

# Ajouter une question à choix multiple
generator.add_multiple_choice_question(
    id=1,
    section="1.1",
    section_title="Introduction",
    difficulty="Easy",
    question="Quelle est la capitale de la France?",
    options=["Paris", "Londres", "Berlin", "Madrid"],
    answer="Paris",
    explanation="Paris est la capitale de la France."
)

# Ajouter une question Vrai/Faux
generator.add_true_false_question(
    id=2,
    section="1.2",
    section_title="Géographie",
    difficulty="Easy",
    question="La France est en Europe.",
    answer="True",
    explanation="La France est un pays européen."
)

# Ajouter une question à réponse courte
generator.add_short_answer_question(
    id=3,
    section="2.1",
    section_title="Histoire",
    difficulty="Medium",
    question="En quelle année a eu lieu la Révolution française?",
    answer="1789",
    explanation="La Révolution française a débuté en 1789."
)

# Sauvegarder dans un CSV
generator.save_to_csv("mes_questions.csv")

# Afficher les statistiques
stats = generator.get_stats()
print(f"Total: {stats['total']} questions")
```

### 2. Exécuter un quiz

#### Méthode 1 : Utiliser les exemples interactifs

```bash
# Lancer le menu principal
python example_run_quiz.py
```

Ou choisir une démonstration spécifique :

- **Démonstration simple** : Quiz rapide de 5 questions
- **Démonstration avec filtres** : Menu interactif avec options de filtrage
- **Quiz personnalisé** : Configuration complète des paramètres

#### Méthode 2 : Créer un script personnalisé

```python
from quiz_runner import QuizRunner

# Initialiser le runner
runner = QuizRunner()

# Charger les questions
runner.load_questions("mes_questions.csv")

# Voir les statistiques
runner.show_stats()

# Créer un quiz
runner.create_quiz(
    num_questions=10,
    section_filter="1",        # Optionnel : filtrer par section
    difficulty_filter="Easy",  # Optionnel : filtrer par difficulté
    shuffle=True               # Mélanger les questions
)

# Lancer le quiz
summary = runner.run_quiz()

# Sauvegarder les résultats
runner.save_results("resultats.json")

# Afficher le score
print(f"Score: {summary.score}/{summary.total}")
```

### 3. Exporter en HTML

#### Méthode 1 : Export HTML basique

```python
from quizzmaker import QuizRunner

runner = QuizRunner()
runner.load_questions("mes_questions.csv")

# Créer un quiz
runner.create_quiz(num_questions=10)

# Exporter en HTML (toutes les questions sur une page par défaut)
runner.export_html_quiz("mon_quiz.html")
```

#### Méthode 2 : Export HTML avec pagination

```python
from quizzmaker import QuizRunner

runner = QuizRunner()
runner.load_questions("mes_questions.csv")
runner.create_quiz(num_questions=20)

# Exporter avec 5 questions par page
runner.export_html_quiz("mon_quiz.html", questions_per_page=5)
```

#### Méthode 3 : Filtrer les types de questions

```python
from quizzmaker import QuizRunner

runner = QuizRunner()
runner.load_questions("mes_questions.csv")

# Filtrer pour garder seulement les questions Multiple Choice et True/False
# (exclure Short Answer)
runner.questions = [
    q for q in runner.questions
    if q.type in ["Multiple Choice", "True/False"]
]

# Créer et exporter le quiz filtré
runner.create_quiz(num_questions=len(runner.questions))
runner.export_html_quiz("quiz_mc_tf_only.html")
```

#### Méthode 4 : Exemples directs (sans menus interactifs)

Pour des scripts automatisés, voir `examples/example_direct_html_export.py` qui contient 9 exemples complets :

```bash
python examples/example_direct_html_export.py
```

Exemples inclus :
- Export basique (toutes questions, une page)
- Export paginé (5, 10 questions par page)
- Filtrage par difficulté (Easy, Medium, Hard)
- Filtrage par section
- Filtrage par type de question (MC only, TF only, MC+TF)
- Combinaison de filtres
- Nom de fichier auto-généré
- Sélection personnalisée de questions

---

## 📝 Format des questions

### Structure CSV

Les questions sont stockées dans un fichier CSV avec les colonnes suivantes :

| Colonne         | Type | Description                                        |
| --------------- | ---- | -------------------------------------------------- |
| `id`            | int  | Identifiant unique                                 |
| `section`       | str  | Numéro de section (ex: "1.1", "2.3")               |
| `section_title` | str  | Titre de la section                                |
| `difficulty`    | str  | "Easy", "Medium", ou "Hard"                        |
| `type`          | str  | "Multiple Choice", "True/False", ou "Short Answer" |
| `question`      | str  | Texte de la question                               |
| `options`       | JSON | Liste des options (format JSON string)             |
| `answer`        | str  | Réponse correcte                                   |
| `explanation`   | str  | Explication de la réponse                          |

### Exemple CSV

```csv
id,section,section_title,difficulty,type,question,options,answer,explanation
1,1.1,Introduction,Easy,Multiple Choice,Capitale de la France?,"[""Paris"", ""Londres"", ""Berlin""]",Paris,Paris est la capitale.
2,1.2,Géographie,Easy,True/False,La France est en Europe.,"[""True"", ""False""]",True,La France est un pays européen.
```

---

## 💡 Exemples

### Exemple 1 : Quiz ciblé (questions faciles uniquement)

```python
from quiz_runner import QuizRunner

runner = QuizRunner()
runner.load_questions("questions.csv")
runner.create_quiz(num_questions=5, difficulty_filter="Easy")
runner.run_quiz()
```

### Exemple 2 : Quiz sur une section spécifique

```python
from quiz_runner import QuizRunner

runner = QuizRunner()
runner.load_questions("questions.csv")

# Toutes les questions de la section 1 (1.1, 1.2, 1.3, etc.)
runner.create_quiz(num_questions=10, section_filter="1")
runner.run_quiz()

# Questions de la section 1.1 uniquement
runner.create_quiz(num_questions=5, section_filter="1.1")
runner.run_quiz()
```

### Exemple 3 : Créer plusieurs bases de questions

```python
from question_generator import QuestionGenerator

# Base 1 : Mathématiques
math_gen = QuestionGenerator()
math_gen.add_multiple_choice_question(...)
math_gen.save_to_csv("math_questions.csv")

# Base 2 : Histoire
history_gen = QuestionGenerator()
history_gen.add_multiple_choice_question(...)
history_gen.save_to_csv("history_questions.csv")
```

### Exemple 4 : Analyse des résultats

```python
from quiz_runner import QuizRunner

runner = QuizRunner()
runner.load_questions("questions.csv")
runner.create_quiz(num_questions=10)
summary = runner.run_quiz()

# Accéder aux résultats détaillés
print(f"Score: {summary.score}/{summary.total}")
print(f"Pourcentage: {summary.percentage}%")

# Performance par difficulté
for diff, stats in summary.get_performance_by_difficulty().items():
    print(f"{diff}: {stats['correct']}/{stats['total']}")

# Examiner chaque question
for result in summary.results:
    if not result.is_correct:
        print(f"Erreur sur: {result.question}")
```

### Exemple 5 : Export HTML avec filtres multiples

```python
from quizzmaker import QuizRunner

runner = QuizRunner()
runner.load_questions("questions.csv")

# Filtrer les types de questions (seulement MC et TF)
runner.questions = [
    q for q in runner.questions
    if q.type in ["Multiple Choice", "True/False"]
]

# Créer un quiz avec filtre de difficulté
runner.create_quiz(
    num_questions=15,
    difficulty_filter="Medium",
    shuffle=True
)

# Exporter avec pagination
runner.export_html_quiz("medium_mc_tf.html", questions_per_page=5)
```

### Exemple 6 : Export HTML - Seulement Multiple Choice

```python
from quizzmaker import QuizRunner

runner = QuizRunner()
runner.load_questions("questions.csv")

# Garder seulement les questions à choix multiple
runner.questions = [q for q in runner.questions if q.type == "Multiple Choice"]

print(f"Found {len(runner.questions)} Multiple Choice questions")

# Créer et exporter
runner.create_quiz(num_questions=len(runner.questions))
runner.export_html_quiz("only_multiple_choice.html")
```

---

## 🔌 API

### QuestionGenerator

#### Méthodes principales

- `add_multiple_choice_question(...)` - Ajoute une question à choix multiple
- `add_true_false_question(...)` - Ajoute une question Vrai/Faux
- `add_short_answer_question(...)` - Ajoute une question à réponse courte
- `save_to_csv(filename)` - Sauvegarde les questions dans un CSV
- `load_from_csv(filename)` - Charge des questions depuis un CSV
- `get_stats()` - Retourne les statistiques de la base
- `preview(num_questions)` - Affiche un aperçu des questions
- `clear()` - Efface toutes les questions
- `validate_all()` - Valide toutes les questions

### QuizRunner

#### Méthodes principales

- `load_questions(csv_file)` - Charge les questions depuis un CSV
- `create_quiz(num_questions, section_filter, difficulty_filter, shuffle)` - Crée un quiz
- `run_quiz()` - Exécute le quiz de manière interactive
- `save_results(filename)` - Sauvegarde les résultats en JSON
- `export_html_quiz(filename, questions_per_page)` - **[NOUVEAU]** Exporte le quiz en HTML
- `show_stats()` - Affiche les statistiques de la base
- `get_available_sections()` - Liste les sections disponibles
- `get_available_difficulties()` - Liste les difficultés disponibles

#### Méthode export_html_quiz

```python
runner.export_html_quiz(filename=None, questions_per_page='all')
```

**Paramètres :**
- `filename` (str, optionnel) : Nom du fichier HTML. Si `None`, génère un nom avec timestamp (ex: `quiz_20251024_143022.html`)
- `questions_per_page` (int ou 'all', défaut: 'all') : Nombre de questions par page, ou 'all' pour une seule page

**Retour :** Chemin du fichier HTML créé

**Fonctionnalités du quiz HTML généré :**
- ✅ Navigation libre entre les pages (si paginé)
- ✅ Bouton Submit par question avec validation instantanée
- ✅ Feedback visuel coloré (vert=correct, rouge=incorrect)
- ✅ Affichage des explications après soumission
- ✅ Verrouillage des réponses après soumission
- ✅ Score final avec analyse par difficulté
- ✅ Design responsive (mobile et desktop)
- ✅ Aucune dépendance externe (fonctionne hors ligne)

---

## 🎯 Cas d'usage

### Pour l'apprentissage

1. **Révision avant examen** : Créez des quiz ciblés par chapitre
2. **Entraînement progressif** : Commencez par les questions faciles, puis augmentez
3. **Suivi des progrès** : Sauvegardez vos résultats pour analyser votre évolution
4. **Quiz hors ligne** : Exportez en HTML et étudiez sans connexion internet

### Pour l'enseignement

1. **Création de tests** : Générez facilement des batteries de questions
2. **Évaluation formative** : Proposez des quiz d'entraînement à vos étudiants
3. **Banque de questions** : Maintenez une base centralisée de questions
4. **Quiz web** : Partagez des quiz HTML avec vos étudiants (par email, LMS, etc.)
5. **Auto-évaluation** : Les étudiants peuvent s'entraîner de manière autonome

---

## 🐛 Dépannage

### Problème : "❌ Fichier non trouvé"

**Solution** : Vérifiez que le fichier CSV existe dans le répertoire actuel ou fournissez le chemin complet.

```python
runner.load_questions("/chemin/complet/vers/questions.csv")
```

### Problème : "❌ Aucune question ne correspond aux filtres"

**Solution** : Vérifiez les valeurs de vos filtres avec `get_available_sections()` et `get_available_difficulties()`.

```python
print(runner.get_available_sections())
print(runner.get_available_difficulties())
```

### Problème : Erreur lors de l'ajout d'une question

**Solution** : Vérifiez que :

- La difficulté est "Easy", "Medium" ou "Hard"
- Pour Multiple Choice : la réponse est bien dans les options
- Pour True/False : la réponse est "True" ou "False"

---

## 📄 Licence

Ce projet est un outil éducatif libre d'utilisation.

---

## 🤝 Contribution

Pour ajouter des fonctionnalités :

1. Modèles de données → `models.py`
2. Génération de questions → `question_generator.py`
3. Exécution de quiz → `quiz_runner.py`

---

**Bon apprentissage! 🎓**
