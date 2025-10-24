"""
Exemple d'utilisation du QuizRunner.

Ce script montre comment charger des questions et exécuter un quiz interactif.
"""

from quizzmaker.quiz_runner import QuizRunner


def demo_simple():
    """Démonstration simple: charge des questions et lance un quiz."""
    print("="*60)
    print("🎯 DÉMONSTRATION SIMPLE")
    print("="*60)
    
    # Créer le runner
    runner = QuizRunner()
    
    # Charger les questions
    if not runner.load_questions("example_python_questions.csv"):
        print("❌ Impossible de charger les questions.")
        print("💡 Exécutez d'abord 'python example_create_questions.py'")
        return
    
    # Afficher les stats
    runner.show_stats()
    
    # Créer un quiz de 5 questions aléatoires
    print(f"\n{'='*60}")
    print("📝 Création d'un quiz de 5 questions...")
    print(f"{'='*60}")
    
    if runner.create_quiz(num_questions=5, shuffle=True):
        input("\n▶️  Appuyez sur Entrée pour commencer le quiz...")
        
        # Lancer le quiz
        summary = runner.run_quiz()
        
        # Proposer de sauvegarder
        if summary:
            save = input("\n💾 Voulez-vous sauvegarder les résultats? (o/n): ").strip().lower()
            if save in ['o', 'oui', 'y', 'yes']:
                runner.save_results("mes_resultats.json")


def demo_filtres():
    """Démonstration avec filtres: quiz ciblé par difficulté ou section."""
    print("="*60)
    print("🎯 DÉMONSTRATION AVEC FILTRES")
    print("="*60)
    
    runner = QuizRunner()
    
    # Charger les questions
    if not runner.load_questions("example_python_questions.csv"):
        print("❌ Impossible de charger les questions.")
        return
    
    # Afficher les sections et difficultés disponibles
    print("\n📂 Sections disponibles:", runner.get_available_sections())
    print("🎯 Difficultés disponibles:", runner.get_available_difficulties())
    
    # Menu interactif
    while True:
        print(f"\n{'='*60}")
        print("Choisissez un type de quiz:")
        print("1. Questions faciles uniquement")
        print("2. Questions moyennes uniquement")
        print("3. Questions difficiles uniquement")
        print("4. Section spécifique")
        print("5. Quiz complet (toutes les questions)")
        print("6. Quitter")
        print("="*60)
        
        choice = input("\nVotre choix (1-6): ").strip()
        
        if choice == '1':
            if runner.create_quiz(num_questions=10, difficulty_filter="Easy"):
                runner.run_quiz()
                runner.save_results("resultats_facile.json")
        
        elif choice == '2':
            if runner.create_quiz(num_questions=10, difficulty_filter="Medium"):
                runner.run_quiz()
                runner.save_results("resultats_moyen.json")
        
        elif choice == '3':
            if runner.create_quiz(num_questions=10, difficulty_filter="Hard"):
                runner.run_quiz()
                runner.save_results("resultats_difficile.json")
        
        elif choice == '4':
            sections = runner.get_available_sections()
            print(f"\nSections: {sections}")
            section = input("Entrez le numéro de section (ex: 1.1, 2, 3.2): ").strip()
            if runner.create_quiz(num_questions=10, section_filter=section):
                runner.run_quiz()
                runner.save_results(f"resultats_section_{section.replace('.', '_')}.json")
        
        elif choice == '5':
            if runner.create_quiz(num_questions=len(runner.questions), shuffle=True):
                runner.run_quiz()
                runner.save_results("resultats_complet.json")
        
        elif choice == '6':
            print("👋 Au revoir!")
            break
        
        else:
            print("⚠️  Choix invalide")


def demo_personnalise():
    """Démonstration personnalisée: l'utilisateur choisit tous les paramètres."""
    print("="*60)
    print("🎯 QUIZ PERSONNALISÉ")
    print("="*60)
    
    runner = QuizRunner()
    
    # Charger les questions
    csv_file = input("\nFichier CSV de questions: ").strip()
    if not csv_file:
        csv_file = "example_python_questions.csv"
    
    if not runner.load_questions(csv_file):
        return
    
    # Afficher les stats
    runner.show_stats()
    
    # Paramètres du quiz
    print(f"\n{'='*60}")
    print("CONFIGURATION DU QUIZ")
    print("="*60)
    
    # Nombre de questions
    try:
        num_q = int(input(f"\nNombre de questions (max {len(runner.questions)}): ").strip())
    except ValueError:
        num_q = 10
        print(f"⚠️  Valeur invalide, utilisation de {num_q} par défaut")
    
    # Filtre de section
    print(f"\nSections disponibles: {runner.get_available_sections()}")
    section = input("Filtrer par section (Entrée pour toutes): ").strip() or None
    
    # Filtre de difficulté
    print(f"\nDifficultés disponibles: {runner.get_available_difficulties()}")
    difficulty = input("Filtrer par difficulté (Entrée pour toutes): ").strip() or None
    
    # Mélanger ou non
    shuffle_input = input("\nMélanger les questions? (o/n, défaut: o): ").strip().lower()
    shuffle = shuffle_input not in ['n', 'non', 'no']
    
    # Créer et lancer le quiz
    if runner.create_quiz(num_questions=num_q, section_filter=section, 
                         difficulty_filter=difficulty, shuffle=shuffle):
        input("\n▶️  Appuyez sur Entrée pour commencer...")
        summary = runner.run_quiz()
        
        if summary:
            # Nom du fichier de résultats
            save = input("\n💾 Sauvegarder les résultats? (o/n): ").strip().lower()
            if save in ['o', 'oui', 'y', 'yes']:
                filename = input("Nom du fichier (défaut: quiz_results.json): ").strip()
                if not filename:
                    filename = "quiz_results.json"
                runner.save_results(filename)


def main():
    """Menu principal."""
    while True:
        print("\n" + "="*60)
        print("🎓 SYSTÈME DE QUIZ INTERACTIF")
        print("="*60)
        print("\nChoisissez une démonstration:")
        print("1. Démonstration simple (5 questions aléatoires)")
        print("2. Démonstration avec filtres (menu interactif)")
        print("3. Quiz personnalisé (configuration complète)")
        print("4. Quitter")
        print("="*60)
        
        choice = input("\nVotre choix (1-4): ").strip()
        
        if choice == '1':
            demo_simple()
        elif choice == '2':
            demo_filtres()
        elif choice == '3':
            demo_personnalise()
        elif choice == '4':
            print("\n👋 Merci d'avoir utilisé le système de quiz!")
            break
        else:
            print("⚠️  Choix invalide, veuillez entrer 1, 2, 3 ou 4")


if __name__ == "__main__":
    # Vous pouvez aussi utiliser directement sans menu:
    
    # Exemple direct:
    # runner = QuizRunner()
    # runner.load_questions("example_python_questions.csv")
    # runner.create_quiz(num_questions=5)
    # runner.run_quiz()
    
    # Ou lancer le menu:
    main()
