"""
Système de Quiz Interactif

Un système modulaire pour créer et exécuter des quiz interactifs.

Modules:
    - models: Modèles de données (Question, QuizResult, QuizSummary)
    - question_generator: Création et gestion de questions
    - quiz_runner: Exécution de quiz interactifs

Usage basique:
    # Créer des questions
    from question_generator import QuestionGenerator
    gen = QuestionGenerator()
    gen.add_multiple_choice_question(...)
    gen.save_to_csv("questions.csv")
    
    # Exécuter un quiz
    from quiz_runner import QuizRunner
    runner = QuizRunner()
    runner.load_questions("questions.csv")
    runner.create_quiz()
    runner.run_quiz()
"""

__version__ = "1.0.0"
__author__ = "Système de Quiz"

from quizzmaker.models import Question, QuizResult, QuizSummary
from quizzmaker.question_generator import QuestionGenerator
from quizzmaker.quiz_runner import QuizRunner

__all__ = [
    'Question',
    'QuizResult', 
    'QuizSummary',
    'QuestionGenerator',
    'QuizRunner'
]
