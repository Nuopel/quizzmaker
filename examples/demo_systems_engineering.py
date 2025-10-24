"""
Exemple d'utilisation avec les questions de Systems Engineering.

Ce script démontre comment utiliser le système avec un vrai jeu de questions.
"""

from quizzmaker.quiz_runner import QuizRunner


def demo_systems_enginering():
    """Démonstration avec les questions de Systems Engineering."""
    print("="*60)
    print("🎓 QUIZ SYSTEMS ENGINEERING")
    print("="*60)
    
    # Charger les questions
    runner = QuizRunner()
    if not runner.load_questions("systems_engineering_concept_questions.csv"):
        print("\n❌ Fichier non trouvé!")
        print("💡 Assurez-vous que 'systems_engineering_concept_questions.csv' est présent")
        return
    
    # Afficher les statistiques
    runner.show_stats()
    
    # Menu principal
    while True:
        print(f"\n{'='*60}")
        print("CHOISISSEZ UN MODE DE QUIZ:")
        print("="*60)
        print("1. Quiz de révision (10 questions aléatoires)")
        print("2. Quiz facile (Easy uniquement)")
        print("3. Quiz moyen (Medium uniquement)")
        print("4. Quiz difficile (Hard uniquement)")
        print("5. Quiz complet (toutes les questions)")
        print("6. Quiz personnalisé")
        print("7. Afficher les stats et quitter")
        print("="*60)
        
        choice = input("\nVotre choix (1-7): ").strip()
        
        if choice == '1':
            # Quiz standard
            print("\n📝 Quiz de révision - 10 questions aléatoires")
            if runner.create_quiz(num_questions=10, shuffle=True):
                input("\n▶️  Appuyez sur Entrée pour commencer...")
                summary = runner.run_quiz()
                
                # Proposer de sauvegarder
                save = input("\n💾 Sauvegarder les résultats? (o/n): ").strip().lower()
                if save in ['o', 'oui', 'y', 'yes']:
                    runner.save_results("se_revision_results.json")
        
        elif choice == '2':
            # Quiz facile
            print("\n📝 Quiz facile - Questions Easy uniquement")
            if runner.create_quiz(num_questions=20, difficulty_filter="Easy", shuffle=True):
                input("\n▶️  Appuyez sur Entrée pour commencer...")
                summary = runner.run_quiz()
                
                if summary and input("\n💾 Sauvegarder? (o/n): ").lower() in ['o', 'oui']:
                    runner.save_results("se_easy_results.json")
        
        elif choice == '3':
            # Quiz moyen
            print("\n📝 Quiz moyen - Questions Medium uniquement")
            if runner.create_quiz(num_questions=20, difficulty_filter="Medium", shuffle=True):
                input("\n▶️  Appuyez sur Entrée pour commencer...")
                summary = runner.run_quiz()
                
                if summary and input("\n💾 Sauvegarder? (o/n): ").lower() in ['o', 'oui']:
                    runner.save_results("se_medium_results.json")
        
        elif choice == '4':
            # Quiz difficile
            print("\n📝 Quiz difficile - Questions Hard uniquement")
            if runner.create_quiz(num_questions=20, difficulty_filter="Hard", shuffle=True):
                input("\n▶️  Appuyez sur Entrée pour commencer...")
                summary = runner.run_quiz()
                
                if summary and input("\n💾 Sauvegarder? (o/n): ").lower() in ['o', 'oui']:
                    runner.save_results("se_hard_results.json")
        
        elif choice == '5':
            # Quiz complet
            print(f"\n📝 Quiz complet - Toutes les {len(runner.questions)} questions")
            confirm = input("⚠️  Cela peut prendre du temps. Continuer? (o/n): ").strip().lower()
            
            if confirm in ['o', 'oui', 'y', 'yes']:
                if runner.create_quiz(num_questions=len(runner.questions), shuffle=True):
                    input("\n▶️  Appuyez sur Entrée pour commencer...")
                    summary = runner.run_quiz()
                    
                    if summary and input("\n💾 Sauvegarder? (o/n): ").lower() in ['o', 'oui']:
                        runner.save_results("se_complete_results.json")
        
        elif choice == '6':
            # Quiz personnalisé
            print(f"\n{'='*60}")
            print("QUIZ PERSONNALISÉ")
            print("="*60)
            
            # Nombre de questions
            try:
                num = int(input(f"\nNombre de questions (max {len(runner.questions)}): ").strip())
            except ValueError:
                num = 10
                print(f"⚠️  Valeur invalide, utilisation de {num}")
            
            # Filtre difficulté
            print(f"\nDifficultés: {runner.get_available_difficulties()}")
            diff = input("Filtrer par difficulté (Entrée pour toutes): ").strip() or None
            
            # Filtre section
            print(f"\nSections: {runner.get_available_sections()}")
            sect = input("Filtrer par section (Entrée pour toutes): ").strip() or None
            
            # Créer et lancer
            if runner.create_quiz(num_questions=num, section_filter=sect, 
                                 difficulty_filter=diff, shuffle=True):
                input("\n▶️  Appuyez sur Entrée pour commencer...")
                summary = runner.run_quiz()
                
                if summary and input("\n💾 Sauvegarder? (o/n): ").lower() in ['o', 'oui']:
                    filename = input("Nom du fichier (défaut: se_custom_results.json): ").strip()
                    if not filename:
                        filename = "se_custom_results.json"
                    runner.save_results(filename)
        
        elif choice == '7':
            print("\n📊 Statistiques finales:")
            runner.show_stats()
            print("\n👋 Au revoir et bon apprentissage!")
            break
        
        else:
            print("⚠️  Choix invalide, veuillez entrer un nombre entre 1 et 7")


def quick_practice():
    """Mode d'entraînement rapide pour les questions difficiles."""
    print("="*60)
    print("⚡ MODE ENTRAÎNEMENT RAPIDE")
    print("="*60)
    
    runner = QuizRunner()
    if not runner.load_questions("systems_engineering_concept_questions.csv"):
        return
    
    # Focus sur les questions difficiles
    print("\n🎯 Entraînement sur les questions les plus difficiles")
    if runner.create_quiz(num_questions=5, difficulty_filter="Hard", shuffle=True):
        runner.run_quiz()


def main():
    """Menu principal."""
    print("\n" + "🎓 SYSTÈME DE QUIZ - SYSTEMS ENGINEERING")
    print("="*60)
    print("\nChoisissez un mode:")
    print("1. Mode complet (menu interactif)")
    print("2. Entraînement rapide (5 questions difficiles)")
    print("="*60)
    
    choice = input("\nVotre choix (1-2): ").strip()
    
    if choice == '1':
        demo_systems_engineering()
    elif choice == '2':
        quick_practice()
    else:
        print("⚠️  Choix invalide")


if __name__ == "__main__":
    main()
