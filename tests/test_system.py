"""
Script de test pour vérifier le bon fonctionnement du système de quiz.
Ce script teste les fonctionnalités sans interaction utilisateur.
"""

from quiz_runner import QuizRunner
from question_generator import QuestionGenerator


def test_question_generator():
    """Test du générateur de questions."""
    print("="*60)
    print("TEST 1: QuestionGenerator")
    print("="*60)
    
    gen = QuestionGenerator()
    
    # Test ajout de questions
    gen.add_multiple_choice_question(
        id=1, section="1.1", section_title="Test",
        difficulty="Easy", question="Question test?",
        options=["A", "B", "C"], answer="A",
        explanation="Explication test"
    )
    
    gen.add_true_false_question(
        id=2, section="1.2", section_title="Test",
        difficulty="Medium", question="Vrai ou faux?",
        answer="True", explanation="C'est vrai"
    )
    
    gen.add_short_answer_question(
        id=3, section="2.1", section_title="Test",
        difficulty="Hard", question="Expliquez...",
        answer="Réponse attendue", explanation="Voici l'explication"
    )
    
    # Test stats
    stats = gen.get_stats()
    assert stats['total'] == 3, "Erreur: nombre de questions incorrect"
    assert 'Easy' in stats['by_difficulty'], "Erreur: difficulté Easy manquante"
    
    # Test sauvegarde
    gen.save_to_csv("test_questions.csv")
    
    # Test chargement
    gen2 = QuestionGenerator()
    gen2.load_from_csv("test_questions.csv")
    assert len(gen2.questions) == 3, "Erreur: chargement CSV incorrect"
    
    print("✅ QuestionGenerator: tous les tests passent!")
    return True


def test_quiz_runner():
    """Test du runner de quiz."""
    print("\n" + "="*60)
    print("TEST 2: QuizRunner")
    print("="*60)
    
    # Charger les questions d'exemple
    runner = QuizRunner()
    success = runner.load_questions("example_python_questions.csv")
    assert success, "Erreur: chargement des questions échoué"
    
    # Test filtres
    sections = runner.get_available_sections()
    difficulties = runner.get_available_difficulties()
    assert len(sections) > 0, "Erreur: aucune section trouvée"
    assert len(difficulties) > 0, "Erreur: aucune difficulté trouvée"
    
    # Test création de quiz
    success = runner.create_quiz(num_questions=3, shuffle=False)
    assert success, "Erreur: création de quiz échouée"
    assert len(runner.quiz_questions) == 3, "Erreur: nombre de questions incorrect"
    
    # Test filtre par difficulté
    success = runner.create_quiz(num_questions=10, difficulty_filter="Easy")
    assert success, "Erreur: filtre par difficulté échoué"
    for q in runner.quiz_questions:
        assert q.difficulty == "Easy", "Erreur: filtre difficulté incorrect"
    
    # Test filtre par section
    success = runner.create_quiz(num_questions=10, section_filter="1")
    assert success, "Erreur: filtre par section échoué"
    for q in runner.quiz_questions:
        assert q.section.startswith("1"), "Erreur: filtre section incorrect"
    
    print("✅ QuizRunner: tous les tests passent!")
    return True


def test_models():
    """Test des modèles de données."""
    print("\n" + "="*60)
    print("TEST 3: Models")
    print("="*60)
    
    from models import Question, QuizResult, QuizSummary
    
    # Test Question
    q = Question(
        id=1, section="1.1", section_title="Test",
        difficulty="Easy", type="Multiple Choice",
        question="Test?", options=["A", "B"], answer="A",
        explanation="Test"
    )
    
    is_valid, error = q.is_valid()
    assert is_valid, f"Erreur: question invalide - {error}"
    
    # Test conversion dict
    q_dict = q.to_dict()
    assert q_dict['id'] == 1, "Erreur: conversion to_dict incorrecte"
    
    # Test QuizResult
    result = QuizResult(
        question_id=1, question="Test?",
        user_answer="A", correct_answer="A",
        is_correct=True, difficulty="Easy"
    )
    result_dict = result.to_dict()
    assert result_dict['is_correct'] == True, "Erreur: QuizResult incorrect"
    
    # Test QuizSummary
    summary = QuizSummary(
        score=8, total=10, percentage=80.0,
        results=[result]
    )
    assert summary.score == 8, "Erreur: QuizSummary score incorrect"
    
    print("✅ Models: tous les tests passent!")
    return True


def test_validation():
    """Test de la validation des questions."""
    print("\n" + "="*60)
    print("TEST 4: Validation")
    print("="*60)
    
    from models import Question
    
    # Test question invalide (type incorrect)
    q1 = Question(
        id=1, section="1.1", section_title="Test",
        difficulty="Easy", type="Invalid Type",
        question="Test?", options=["A"], answer="A",
        explanation="Test"
    )
    is_valid, error = q1.is_valid()
    assert not is_valid, "Erreur: devrait détecter type invalide"
    
    # Test difficulté invalide
    q2 = Question(
        id=2, section="1.1", section_title="Test",
        difficulty="VeryHard", type="Multiple Choice",
        question="Test?", options=["A", "B"], answer="A",
        explanation="Test"
    )
    is_valid, error = q2.is_valid()
    assert not is_valid, "Erreur: devrait détecter difficulté invalide"
    
    # Test réponse pas dans les options
    q3 = Question(
        id=3, section="1.1", section_title="Test",
        difficulty="Easy", type="Multiple Choice",
        question="Test?", options=["A", "B"], answer="C",
        explanation="Test"
    )
    is_valid, error = q3.is_valid()
    assert not is_valid, "Erreur: devrait détecter réponse invalide"
    
    print("✅ Validation: tous les tests passent!")
    return True


def main():
    """Lance tous les tests."""
    print("\n" + "🧪 SUITE DE TESTS COMPLÈTE")
    print("="*60)
    
    all_pass = True
    
    try:
        all_pass = test_models() and all_pass
    except Exception as e:
        print(f"❌ Test Models échoué: {e}")
        all_pass = False
    
    try:
        all_pass = test_validation() and all_pass
    except Exception as e:
        print(f"❌ Test Validation échoué: {e}")
        all_pass = False
    
    try:
        all_pass = test_question_generator() and all_pass
    except Exception as e:
        print(f"❌ Test QuestionGenerator échoué: {e}")
        all_pass = False
    
    try:
        all_pass = test_quiz_runner() and all_pass
    except Exception as e:
        print(f"❌ Test QuizRunner échoué: {e}")
        all_pass = False
    
    print("\n" + "="*60)
    if all_pass:
        print("🎉 TOUS LES TESTS RÉUSSIS!")
    else:
        print("❌ CERTAINS TESTS ONT ÉCHOUÉ")
    print("="*60)


if __name__ == "__main__":
    main()
