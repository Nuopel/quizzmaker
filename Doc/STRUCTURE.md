# 📁 Structure du Projet

## Vue d'ensemble

```
quiz-system/
│
├── 🔧 MODULES PRINCIPAUX
│   ├── models.py                              # Modèles de données
│   ├── question_generator.py                  # Génération de questions
│   ├── quiz_runner.py                         # Exécution de quiz
│   └── __init__.py                            # Package init
│
├── 📚 EXEMPLES & DÉMOS
│   ├── example_create_questions.py            # Exemple: créer des questions
│   ├── example_run_quiz.py                    # Exemple: exécuter un quiz
│   └── demo_systems_engineering.py            # Démo avec vraies questions
│
├── 📄 DOCUMENTATION
│   ├── README.md                              # Documentation complète
│   ├── QUICKSTART.md                          # Guide de démarrage rapide
│   └── STRUCTURE.md                           # Ce fichier
│
├── 🧪 TESTS
│   └── test_system.py                         # Tests automatisés
│
└── 📊 DONNÉES
    ├── example_python_questions.csv           # Questions Python (exemple)
    └── systems_engineering_concept_questions.csv  # Questions SE (réelles)
```

## Description détaillée des fichiers

### 🔧 Modules principaux

#### `models.py` (149 lignes)
**Rôle**: Définit les structures de données

Classes:
- `Question`: Représente une question de quiz
  - Validation automatique des questions
  - Conversion dict/objet pour CSV
  - Support de 3 types: Multiple Choice, True/False, Short Answer
  
- `QuizResult`: Résultat d'une question
  - Stocke la réponse utilisateur vs correcte
  - Indicateur de succès
  
- `QuizSummary`: Résumé complet d'un quiz
  - Score total et pourcentage
  - Performance par difficulté
  - Export JSON

**Dépendances**: dataclasses, typing, json

---

#### `question_generator.py` (312 lignes)
**Rôle**: Création et gestion de questions

Fonctionnalités:
- ✅ Ajout de questions (3 types)
- ✅ Validation automatique
- ✅ Import/Export CSV
- ✅ Statistiques de la base
- ✅ Prévisualisation
- ✅ Gestion des questions (suppression, recherche)

Méthodes clés:
- `add_multiple_choice_question()`: Ajoute question choix multiple
- `add_true_false_question()`: Ajoute question vrai/faux
- `add_short_answer_question()`: Ajoute question ouverte
- `save_to_csv()`: Sauvegarde en CSV
- `load_from_csv()`: Charge depuis CSV
- `get_stats()`: Statistiques complètes
- `validate_all()`: Valide toutes les questions

**Dépendances**: pandas, models

---

#### `quiz_runner.py` (405 lignes)
**Rôle**: Exécution de quiz interactifs

Fonctionnalités:
- ✅ Chargement de questions depuis CSV
- ✅ Création de quiz avec filtres (section, difficulté)
- ✅ Randomisation des questions et options
- ✅ Interface interactive en ligne de commande
- ✅ Gestion des 3 types de questions
- ✅ Affichage des résultats et statistiques
- ✅ Sauvegarde des résultats en JSON

Méthodes clés:
- `load_questions()`: Charge questions depuis CSV
- `create_quiz()`: Crée un quiz avec filtres
- `run_quiz()`: Lance le quiz interactif
- `save_results()`: Sauvegarde résultats
- `show_stats()`: Affiche statistiques

**Dépendances**: pandas, json, random, models

---

#### `__init__.py` (35 lignes)
**Rôle**: Initialisation du package

- Export des classes principales
- Métadonnées du package (version, auteur)
- Documentation du module

---

### 📚 Exemples & Démos

#### `example_create_questions.py` (162 lignes)
**Objectif**: Template pour créer des questions

Contient:
- Fonction `create_example_questions()` avec 8 questions Python
- Démonstration des 3 types de questions
- Différentes difficultés (Easy/Medium/Hard)
- Script exécutable pour générer le CSV

**Usage**: `python example_create_questions.py`

---

#### `example_run_quiz.py` (185 lignes)
**Objectif**: Démonstration des fonctionnalités du quiz runner

Modes:
1. **Démo simple**: Quiz rapide de 5 questions
2. **Démo avec filtres**: Menu interactif complet
3. **Quiz personnalisé**: Configuration sur mesure

**Usage**: `python example_run_quiz.py`

---

#### `demo_systems_engineering.py` (159 lignes)
**Objectif**: Application réelle avec questions de Systems Engineering

Fonctionnalités:
- 7 modes de quiz différents
- Quiz par difficulté (Easy/Medium/Hard)
- Quiz personnalisé avec filtres
- Mode entraînement rapide

**Usage**: `python demo_systems_engineering.py`

---

### 📄 Documentation

#### `README.md` (488 lignes)
**Contenu complet**:
- Guide d'installation
- Tutoriel complet
- Format des questions
- API complète
- Exemples de code
- Troubleshooting

---

#### `QUICKSTART.md` (256 lignes)
**Guide pratique**:
- Démarrage en 3 étapes
- Workflow avec IA
- Exemples de prompts
- Astuces et bonnes pratiques
- Structure de projet recommandée

---

#### `STRUCTURE.md` (ce fichier)
**Vue d'ensemble**:
- Arborescence complète
- Description de chaque fichier
- Diagrammes de dépendances
- Guide de contribution

---

### 🧪 Tests

#### `test_system.py` (206 lignes)
**Suite de tests automatisés**:
- Test des modèles de données
- Test de la validation
- Test du générateur de questions
- Test du runner de quiz
- Test de l'intégration complète

**Usage**: `python test_system.py`

---

### 📊 Données

#### `example_python_questions.csv`
**8 questions d'exemple sur Python**
- 4 Multiple Choice
- 2 True/False  
- 2 Short Answer
- Difficultés variées

---

#### `systems_engineering_concept_questions.csv`
**Base réelle de questions SE**
- 51 questions sur le Systems Engineering
- Couvre plusieurs chapitres
- 3 niveaux de difficulté
- Types de questions variés

---

## Diagramme de dépendances

```
models.py
   ↑
   ├── question_generator.py
   │      ↑
   │      └── example_create_questions.py
   │
   └── quiz_runner.py
          ↑
          ├── example_run_quiz.py
          └── demo_systems_engineering.py

test_system.py → (tous les modules)
__init__.py → (tous les modules)
```

## Flux de données

```
1. CRÉATION
   QuestionGenerator → CSV
   
2. UTILISATION
   CSV → QuizRunner → QuizSummary → JSON

3. CYCLE COMPLET
   IA → Code Python → QuestionGenerator → CSV → QuizRunner → Résultats JSON
```

## Points d'entrée

| Fichier | Usage | Type |
|---------|-------|------|
| `example_create_questions.py` | Créer des questions | Script exécutable |
| `example_run_quiz.py` | Lancer un quiz | Script exécutable |
| `demo_systems_engineering.py` | Démo complète | Script exécutable |
| `test_system.py` | Valider le système | Tests automatisés |
| `question_generator.py` | Créer questions (import) | Module Python |
| `quiz_runner.py` | Exécuter quiz (import) | Module Python |

## Utilisation en tant que package

```python
# Option 1: Import individuel
from question_generator import QuestionGenerator
from quiz_runner import QuizRunner

# Option 2: Import du package
import quiz_system
gen = quiz_system.QuestionGenerator()
runner = quiz_system.QuizRunner()
```

## Extensibilité

### Ajouter un nouveau type de question

1. Mettre à jour `models.py` → validation dans `Question.is_valid()`
2. Ajouter méthode dans `question_generator.py` → `add_xxx_question()`
3. Ajouter handler dans `quiz_runner.py` → `_handle_xxx()`

### Ajouter un nouveau format d'export

1. Ajouter méthode dans `question_generator.py` → `save_to_xxx()`
2. Optionnel: ajouter méthode dans `quiz_runner.py` → `save_results_xxx()`

### Ajouter des statistiques

1. Ajouter méthode dans `QuizSummary` (models.py)
2. Utiliser dans `quiz_runner.py` → `_display_summary()`

## Taille du code

| Fichier | Lignes | Lignes de code* |
|---------|--------|----------------|
| models.py | 149 | ~90 |
| question_generator.py | 312 | ~180 |
| quiz_runner.py | 405 | ~240 |
| **Total système** | **866** | **~510** |

*Hors docstrings et commentaires

## Bonnes pratiques implémentées

✅ **Separation of Concerns**: Chaque module a une responsabilité claire
✅ **Documentation**: Docstrings français complètes
✅ **Type Hints**: Annotations de type partout
✅ **Validation**: Vérification automatique des données
✅ **Error Handling**: Gestion des erreurs appropriée
✅ **Testabilité**: Code facilement testable
✅ **Extensibilité**: Architecture ouverte à l'extension

## Contribution

Pour ajouter des fonctionnalités:

1. **Nouveau type de question** → Modifier models.py, question_generator.py, quiz_runner.py
2. **Nouveau filtre** → Modifier quiz_runner.py
3. **Nouvelles stats** → Modifier models.py ou question_generator.py
4. **Nouveau format** → Ajouter méthodes d'import/export

Toujours:
- Ajouter des docstrings
- Mettre à jour les tests
- Maintenir la séparation des responsabilités

---

**Architecture propre = Code maintenable! 🏗️**
