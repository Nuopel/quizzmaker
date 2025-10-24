"""
Exemple d'utilisation du QuestionGenerator.

Ce script montre comment créer des questions et les sauvegarder dans un CSV.
Utilisez ce template pour générer vos propres bases de questions.
"""

from quizzmaker.question_generator import QuestionGenerator


def create_example_questions():
    """
    Crée un exemple de base de questions sur la programmation Python.
    
    Cette fonction sert de template pour créer vos propres questions.
    Modifiez simplement les questions selon votre sujet.
    """
    generator = QuestionGenerator()
    
    print("🔧 Création de questions d'exemple...")
    print("="*60)
    
    # Question 1: Multiple Choice
    generator.add_multiple_choice_question(
        id=1,
        section="1.1",
        section_title="Introduction à Python",
        difficulty="Easy",
        question="Quel mot-clé est utilisé pour définir une fonction en Python?",
        options=[
            "function",
            "def",
            "func",
            "define"
        ],
        answer="def",
        explanation="Le mot-clé 'def' (definition) est utilisé pour définir une fonction en Python."
    )
    
    # Question 2: Multiple Choice
    generator.add_multiple_choice_question(
        id=2,
        section="1.2",
        section_title="Types de données",
        difficulty="Easy",
        question="Quel type de données Python est mutable?",
        options=[
            "tuple",
            "string",
            "list",
            "int"
        ],
        answer="list",
        explanation="Les listes sont mutables, contrairement aux tuples et strings qui sont immuables."
    )
    
    # Question 3: True/False
    generator.add_true_false_question(
        id=3,
        section="1.3",
        section_title="Opérateurs",
        difficulty="Easy",
        question="L'opérateur '==' vérifie l'égalité de valeur entre deux objets.",
        answer="True",
        explanation="L'opérateur '==' compare les valeurs, tandis que 'is' compare les identités."
    )
    
    # Question 4: Multiple Choice - Plus difficile
    generator.add_multiple_choice_question(
        id=4,
        section="2.1",
        section_title="Structures de contrôle",
        difficulty="Medium",
        question="Quelle est la sortie de: [x**2 for x in range(3)]?",
        options=[
            "[0, 1, 2]",
            "[0, 1, 4]",
            "[1, 2, 3]",
            "[1, 4, 9]"
        ],
        answer="[0, 1, 4]",
        explanation="La list comprehension calcule le carré de 0, 1, et 2: [0², 1², 2²] = [0, 1, 4]."
    )
    
    # Question 5: Short Answer
    generator.add_short_answer_question(
        id=5,
        section="2.2",
        section_title="Fonctions avancées",
        difficulty="Medium",
        question="Expliquez la différence entre *args et **kwargs dans une fonction Python.",
        answer="*args permet de passer un nombre variable d'arguments positionnels (tuple), "
               "**kwargs permet de passer un nombre variable d'arguments nommés (dictionnaire).",
        explanation="*args collecte les arguments positionnels en tuple, "
                   "**kwargs collecte les arguments nommés en dictionnaire."
    )
    
    # Question 6: Multiple Choice - Difficile
    generator.add_multiple_choice_question(
        id=6,
        section="3.1",
        section_title="Programmation orientée objet",
        difficulty="Hard",
        question="Quelle méthode est appelée automatiquement lors de la création d'un objet?",
        options=[
            "__create__",
            "__init__",
            "__new__",
            "__start__"
        ],
        answer="__init__",
        explanation="__init__ est le constructeur appelé après la création de l'objet par __new__."
    )
    
    # Question 7: True/False
    generator.add_true_false_question(
        id=7,
        section="3.2",
        section_title="Héritage",
        difficulty="Medium",
        question="Une classe peut hériter de plusieurs classes parentes en Python (héritage multiple).",
        answer="True",
        explanation="Python supporte l'héritage multiple, contrairement à certains langages comme Java."
    )
    
    # Question 8: Short Answer - Difficile
    generator.add_short_answer_question(
        id=8,
        section="3.3",
        section_title="Décorateurs",
        difficulty="Hard",
        question="Qu'est-ce qu'un décorateur en Python et à quoi sert-il?",
        answer="Un décorateur est une fonction qui modifie le comportement d'une autre fonction. "
               "Il permet d'ajouter des fonctionnalités sans modifier le code original.",
        explanation="Les décorateurs utilisent la syntaxe @decorator_name et sont très utiles "
                   "pour le logging, la validation, le caching, etc."
    )
    
    return generator


def main():
    """Fonction principale d'exemple."""
    
    # Créer les questions
    generator = create_example_questions()
    
    # Afficher les statistiques
    stats = generator.get_stats()
    print(f"\n📊 Statistiques:")
    print(f"  Total: {stats['total']} questions")
    print(f"  Par difficulté: {stats['by_difficulty']}")
    print(f"  Par type: {stats['by_type']}")
    
    # Prévisualiser quelques questions
    print(f"\n{'='*60}")
    print("👀 Aperçu des questions:")
    print(f"{'='*60}")
    generator.preview(3)
    
    # Sauvegarder dans un CSV
    output_file = "example_python_questions.csv"
    generator.save_to_csv(output_file)
    
    print(f"\n{'='*60}")
    print(f"✅ Questions sauvegardées dans '{output_file}'")
    print(f"{'='*60}")
    print("\n💡 Vous pouvez maintenant utiliser ce fichier avec quiz_runner.py")
    print("   pour créer et exécuter des quiz!")


if __name__ == "__main__":
    main()
