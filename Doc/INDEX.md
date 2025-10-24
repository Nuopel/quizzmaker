# 🎓 Système de Quiz Interactif - INDEX

## 🚀 Démarrage Rapide (3 fichiers à lire)

1. **QUICKSTART.md** → Commencez ici pour démarrer en 5 minutes
2. **README.md** → Documentation complète
3. **STRUCTURE.md** → Architecture et structure du code

---

## 📋 Checklist de démarrage

- [ ] Installer pandas: `pip install pandas`
- [ ] Tester le système: `python test_system.py`
- [ ] Créer des questions d'exemple: `python example_create_questions.py`
- [ ] Lancer un quiz: `python example_run_quiz.py`
- [ ] Essayer avec Systems Engineering: `python demo_systems_engineering.py`

---

## 📁 Fichiers par catégorie

### 🔧 Modules du système (à importer dans vos scripts)
```
models.py                  # Classes de données
question_generator.py      # Créer et gérer des questions
quiz_runner.py            # Exécuter des quiz
__init__.py               # Package Python
```

### ▶️ Scripts exécutables (à lancer directement)
```
example_create_questions.py       # Créer des questions (exemple Python)
example_run_quiz.py              # Lancer un quiz (menu interactif)
demo_systems_engineering.py      # Démo avec vraies questions SE
test_system.py                   # Tester que tout fonctionne
```

### 📚 Documentation
```
README.md                 # Documentation complète (488 lignes)
QUICKSTART.md            # Guide de démarrage rapide
STRUCTURE.md             # Architecture du projet
INDEX.md                 # Ce fichier
```

### 📊 Données
```
example_python_questions.csv                  # 8 questions Python (exemple)
systems_engineering_concept_questions.csv     # 51 questions SE (réelles)
```

### ⚙️ Configuration
```
requirements.txt         # Dépendances Python (pandas)
```

---

## 🎯 Workflows recommandés

### Workflow 1: Créer votre première base de questions

```bash
# 1. Créer un nouveau fichier Python
nano create_my_questions.py

# 2. Copier-coller le code d'example_create_questions.py

# 3. Remplacer les questions par les vôtres

# 4. Exécuter
python create_my_questions.py
```

### Workflow 2: Utiliser l'IA pour générer des questions

```bash
# 1. Demander à l'IA de générer du code Python
# Prompt: "Génère 10 questions sur [SUJET] au format Python 
#          avec gen.add_multiple_choice_question(...)"

# 2. Créer un fichier avec le code généré
nano create_questions_from_ai.py

# 3. Ajouter l'import et la structure
from question_generator import QuestionGenerator

def create_questions():
    gen = QuestionGenerator()
    
    # COLLER ICI LE CODE DE L'IA
    
    return gen

if __name__ == "__main__":
    gen = create_questions()
    gen.save_to_csv("mes_questions.csv")

# 4. Exécuter
python create_questions_from_ai.py
```

### Workflow 3: S'entraîner pour un examen

```bash
# Créer un quiz ciblé
python -c "
from quiz_runner import QuizRunner
r = QuizRunner()
r.load_questions('systems_engineering_concept_questions.csv')
r.create_quiz(num_questions=10, difficulty_filter='Hard')
r.run_quiz()
r.save_results('training_results.json')
"
```

---

## 🔍 Trouver rapidement ce dont vous avez besoin

### Je veux...

#### ...créer des questions
→ Voir `example_create_questions.py` ou `QUICKSTART.md` section "Créer des questions"

#### ...lancer un quiz
→ Exécuter `python example_run_quiz.py` ou `python demo_systems_engineering.py`

#### ...comprendre l'architecture
→ Lire `STRUCTURE.md`

#### ...voir toutes les fonctionnalités
→ Lire `README.md` section "API"

#### ...utiliser comme package Python
→ Voir `__init__.py` et `README.md` section "Guide d'utilisation"

#### ...ajouter des fonctionnalités
→ Lire `STRUCTURE.md` section "Extensibilité"

#### ...tester que tout marche
→ Exécuter `python test_system.py`

#### ...voir des exemples de prompts IA
→ Lire `QUICKSTART.md` section "Exemples de prompts"

---

## 📊 Statistiques du projet

| Métrique | Valeur |
|----------|--------|
| Lignes de code | ~510 (hors docs/tests) |
| Modules Python | 3 (models, generator, runner) |
| Scripts d'exemple | 4 |
| Fichiers de doc | 4 |
| Questions d'exemple | 59 (8 Python + 51 SE) |
| Tests automatisés | ✅ Oui |
| Dépendances | 1 (pandas) |

---

## 🎓 Parcours d'apprentissage suggéré

### Niveau 1: Débutant (15 min)
1. Lire `QUICKSTART.md` (5 min)
2. Exécuter `python test_system.py` (2 min)
3. Exécuter `python example_run_quiz.py` → Démo simple (8 min)

### Niveau 2: Utilisateur (30 min)
1. Exécuter `python example_create_questions.py` (5 min)
2. Modifier le script pour créer vos questions (15 min)
3. Tester vos questions avec `example_run_quiz.py` (10 min)

### Niveau 3: Avancé (1h)
1. Lire `STRUCTURE.md` (20 min)
2. Lire `README.md` section API (20 min)
3. Créer un script personnalisé qui combine generator et runner (20 min)

### Niveau 4: Expert (2h+)
1. Lire tout le code source avec les docstrings
2. Ajouter une nouvelle fonctionnalité
3. Contribuer avec des améliorations

---

## 🆘 Aide rapide

### Problème: "ModuleNotFoundError: No module named 'pandas'"
**Solution**: `pip install pandas`

### Problème: "❌ Fichier non trouvé"
**Solution**: Vérifier que vous êtes dans le bon répertoire avec `ls` ou `dir`

### Problème: Comment utiliser mes propres questions?
**Solution**: 
```python
from question_generator import QuestionGenerator
gen = QuestionGenerator()
gen.add_multiple_choice_question(...)  # Ajouter vos questions
gen.save_to_csv("mes_questions.csv")
```

Puis:
```python
from quiz_runner import QuizRunner
runner = QuizRunner()
runner.load_questions("mes_questions.csv")
runner.create_quiz()
runner.run_quiz()
```

### Problème: Comment modifier le système?
**Solution**: Lire `STRUCTURE.md` section "Extensibilité"

---

## 🎯 Use Cases

### Pour étudiants
- Révision avant examens
- Auto-évaluation
- Suivi de progression

### Pour enseignants
- Création de tests
- Évaluation formative
- Banque de questions

### Pour formation professionnelle
- Onboarding
- Certification
- Knowledge checks

### Pour développeurs
- Base pour système de quiz web
- Backend pour application mobile
- API de quiz

---

## 📞 Support

- Documentation complète: `README.md`
- Guide rapide: `QUICKSTART.md`
- Architecture: `STRUCTURE.md`
- Tests: `python test_system.py`

---

## ✨ Fonctionnalités principales

✅ 3 types de questions (Multiple Choice, True/False, Short Answer)
✅ 3 niveaux de difficulté (Easy, Medium, Hard)
✅ Filtres avancés (section, difficulté)
✅ Randomisation (questions + options)
✅ Statistiques détaillées
✅ Export/Import CSV
✅ Sauvegarde résultats JSON
✅ Interface CLI interactive
✅ Code documenté en français
✅ Architecture modulaire
✅ Tests automatisés
✅ Facile à étendre

---

## 🚦 Statut du projet

| Composant | Statut |
|-----------|--------|
| Core système | ✅ Fonctionnel |
| Documentation | ✅ Complète |
| Tests | ✅ Passent |
| Exemples | ✅ Fournis |
| Production-ready | ✅ Oui |

---

**Commencez par QUICKSTART.md puis explorez! 🚀**
