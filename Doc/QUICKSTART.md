# 🚀 Guide de Démarrage Rapide

## Installation

```bash
pip install pandas
```

## Démarrage en 3 étapes

### 1️⃣ Créer votre première base de questions

```bash
python example_create_questions.py
```

Cela génère `example_python_questions.csv` avec 8 questions d'exemple.

### 2️⃣ Lancer un quiz

```bash
python example_run_quiz.py
```

Choisissez l'option 1 pour un quiz simple de 5 questions.

### 3️⃣ Créer vos propres questions

```python
from question_generator import QuestionGenerator

gen = QuestionGenerator()

# Ajouter vos questions
gen.add_multiple_choice_question(
    id=1,
    section="1.1",
    section_title="Mon Sujet",
    difficulty="Easy",
    question="Ma question?",
    options=["Option A", "Option B", "Option C"],
    answer="Option A",
    explanation="Parce que..."
)

# Sauvegarder
gen.save_to_csv("mes_questions.csv")
```

## Workflow recommandé avec l'IA

### Étape 1 : Générer les questions avec l'IA

Demandez à l'IA de générer des questions au format Python :

```
Prompt : "Génère 10 questions sur [SUJET] au format Python pour mon système de quiz.
Format requis :
- 5 questions Multiple Choice (Easy à Medium)
- 3 questions True/False (Easy)
- 2 questions Short Answer (Medium à Hard)

Utilise ce code Python :
gen.add_multiple_choice_question(id=1, section="1.1", ...)
```

### Étape 2 : Intégrer le code généré

Copiez le code généré par l'IA dans un nouveau fichier Python :

```python
from question_generator import QuestionGenerator

def create_my_questions():
    gen = QuestionGenerator()
    
    # COLLEZ ICI LE CODE GÉNÉRÉ PAR L'IA
    gen.add_multiple_choice_question(...)
    gen.add_multiple_choice_question(...)
    # etc.
    
    return gen

if __name__ == "__main__":
    gen = create_my_questions()
    gen.save_to_csv("mes_questions.csv")
    gen.preview()
```

### Étape 3 : Générer et tester

```bash
python mon_script.py
python example_run_quiz.py  # Utilisez votre nouveau CSV
```

## Exemples de prompts pour l'IA

### Pour Systems Engineering

```
Génère 15 questions sur les principes du Systems Engineering.
Sections : 1.1 (Introduction), 1.2 (Processus), 1.3 (Outils)
Difficultés : 5 Easy, 7 Medium, 3 Hard
Types : 8 Multiple Choice, 4 True/False, 3 Short Answer

Format : code Python avec gen.add_multiple_choice_question(...)
```

### Pour Python Programming

```
Crée 20 questions sur Python (niveau intermédiaire).
Thèmes : variables, fonctions, classes, modules
Format : 12 Multiple Choice (avec code snippets), 5 True/False, 3 Short Answer

Format Python pour mon QuestionGenerator
```

### Pour Business/Management

```
Génère 10 questions sur la gestion de projet Agile.
5 questions sur Scrum, 5 sur Kanban
Mélange de difficultés et types de questions

Format : gen.add_multiple_choice_question(id=..., section=..., ...)
```

## Astuces

### ✅ Bonnes pratiques

1. **IDs séquentiels** : Commencez à 1 et incrémentez
2. **Sections logiques** : Utilisez "1.1", "1.2", "2.1" pour organiser
3. **Difficultés progressives** : Easy → Medium → Hard par section
4. **Explanations complètes** : Expliquez pourquoi la réponse est correcte
5. **Options réalistes** : Pour Multiple Choice, rendez les distracteurs crédibles

### ⚠️ À éviter

1. ❌ Options en désordre (A/B/C/D) - le système les mélange automatiquement
2. ❌ Réponses trop évidentes
3. ❌ Questions ambiguës
4. ❌ Oublier les explanations

## Structure d'un projet type

```
mon_projet_quiz/
│
├── questions/
│   ├── chapitre1_questions.csv
│   ├── chapitre2_questions.csv
│   └── examen_final_questions.csv
│
├── scripts/
│   ├── create_chapitre1.py
│   ├── create_chapitre2.py
│   └── create_examen.py
│
├── resultats/
│   ├── quiz_20241023_results.json
│   └── ...
│
└── system/
    ├── models.py
    ├── question_generator.py
    ├── quiz_runner.py
    └── ...
```

## Commandes utiles

### Voir les stats d'un fichier CSV

```python
from quiz_runner import QuizRunner

runner = QuizRunner()
runner.load_questions("mes_questions.csv")
runner.show_stats()
```

### Valider toutes les questions

```python
from question_generator import QuestionGenerator

gen = QuestionGenerator()
gen.load_from_csv("mes_questions.csv")
num_errors, errors = gen.validate_all()

if num_errors > 0:
    for error in errors:
        print(error)
```

### Fusionner plusieurs CSV

```python
from question_generator import QuestionGenerator

gen = QuestionGenerator()
gen.load_from_csv("questions1.csv")

gen2 = QuestionGenerator()
gen2.load_from_csv("questions2.csv")

# Fusionner (attention aux IDs dupliqués!)
gen.questions.extend(gen2.questions)
gen.save_to_csv("questions_fusionnees.csv")
```

## Support

Pour toute question :
1. Consultez le README.md complet
2. Regardez les exemples dans `example_*.py`
3. Lancez `python test_system.py` pour vérifier votre installation

---

**Bon apprentissage ! 🎓**
