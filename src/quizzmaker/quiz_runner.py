"""
Module d'exécution de quiz interactifs.

Ce module permet de charger des questions depuis un CSV, créer des quiz
avec filtres, et exécuter des sessions interactives avec l'utilisateur.
"""

import pandas as pd
import json
import random
from typing import List, Dict, Optional
from pathlib import Path

from quizzmaker.models import Question, QuizResult, QuizSummary


class QuizRunner:
    """
    Gestionnaire d'exécution de quiz interactifs.
    
    Cette classe charge des questions depuis un CSV, permet de créer
    des quiz personnalisés avec filtres, et gère l'interaction avec
    l'utilisateur pendant le quiz.
    
    Attributs:
        questions (List[Question]): Base de questions chargées
        quiz_questions (List[Question]): Questions sélectionnées pour le quiz actuel
        current_summary (Optional[QuizSummary]): Résumé du dernier quiz complété
    """
    
    def __init__(self):
        """Initialise un runner de quiz vide."""
        self.questions: List[Question] = []
        self.quiz_questions: List[Question] = []
        self.current_summary: Optional[QuizSummary] = None
    
    def load_questions(self, csv_file: str) -> bool:
        """
        Charge les questions depuis un fichier CSV.
        
        Args:
            csv_file (str): Chemin du fichier CSV contenant les questions
            
        Returns:
            bool: True si le chargement a réussi
            
        Example:
            >>> runner = QuizRunner()
            >>> runner.load_questions("questions.csv")
        """
        try:
            df = pd.read_csv(csv_file)
            self.questions = []
            
            for _, row in df.iterrows():
                q = Question.from_dict(row.to_dict())
                self.questions.append(q)
            
            print(f"✅ Chargé {len(self.questions)} questions depuis {csv_file}")
            return True
            
        except FileNotFoundError:
            print(f"❌ Fichier non trouvé: {csv_file}")
            return False
        except Exception as e:
            print(f"❌ Erreur lors du chargement: {e}")
            return False
    
    def create_quiz(
        self,
        num_questions: int = 10,
        section_filter: Optional[str] = None,
        difficulty_filter: Optional[str] = None,
        shuffle: bool = True
    ) -> bool:
        """
        Crée un quiz avec des filtres optionnels.
        
        Args:
            num_questions (int): Nombre de questions à inclure (défaut: 10)
            section_filter (Optional[str]): Filtrer par section (ex: "1.1" ou "1")
            difficulty_filter (Optional[str]): Filtrer par difficulté ("Easy", "Medium", "Hard")
            shuffle (bool): Mélanger les questions (défaut: True)
            
        Returns:
            bool: True si le quiz a été créé avec succès
            
        Example:
            >>> runner = QuizRunner()
            >>> runner.load_questions("questions.csv")
            >>> runner.create_quiz(num_questions=5, difficulty_filter="Easy")
        """
        if not self.questions:
            print("❌ Aucune question chargée!")
            return False
        
        # Filtrer les questions
        filtered = self.questions.copy()
        
        if section_filter:
            filtered = [q for q in filtered if q.section.startswith(section_filter)]
            print(f"📂 Filtré par section: {section_filter}")
        
        if difficulty_filter:
            filtered = [q for q in filtered if q.difficulty == difficulty_filter]
            print(f"🎯 Filtré par difficulté: {difficulty_filter}")
        
        if not filtered:
            print("❌ Aucune question ne correspond aux filtres!")
            return False
        
        # Sélectionner les questions
        num_questions = min(num_questions, len(filtered))
        
        if shuffle:
            self.quiz_questions = random.sample(filtered, num_questions)
        else:
            self.quiz_questions = filtered[:num_questions]
        
        print(f"✅ Quiz créé avec {len(self.quiz_questions)} questions")
        return True
    
    def run_quiz(self) -> Optional[QuizSummary]:
        """
        Exécute le quiz de manière interactive.
        
        Returns:
            Optional[QuizSummary]: Résumé du quiz si complété, None sinon
            
        Example:
            >>> runner = QuizRunner()
            >>> runner.load_questions("questions.csv")
            >>> runner.create_quiz()
            >>> summary = runner.run_quiz()
            >>> print(f"Score: {summary.score}/{summary.total}")
        """
        if not self.quiz_questions:
            print("❌ Aucun quiz créé! Utilisez create_quiz() d'abord.")
            return None
        
        print(f"\n{'='*60}")
        print(f"🎯 DÉBUT DU QUIZ - {len(self.quiz_questions)} questions")
        print(f"{'='*60}")
        
        score = 0
        results: List[QuizResult] = []
        
        for i, question in enumerate(self.quiz_questions, 1):
            print(f"\n{'─'*60}")
            print(f"📝 Question {i}/{len(self.quiz_questions)}")
            print(f"{'─'*60}")
            print(f"Section: {question.section} - {question.section_title}")
            print(f"Difficulté: {question.difficulty}")
            print(f"\n{question.question}")
            
            is_correct = False
            user_answer = ""
            
            # Gestion selon le type de question
            if question.type == 'Multiple Choice':
                is_correct, user_answer = self._handle_multiple_choice(question)
            elif question.type == 'True/False':
                is_correct, user_answer = self._handle_true_false(question)
            elif question.type == 'Short Answer':
                is_correct, user_answer = self._handle_short_answer(question)
            
            # Incrémenter le score si correct
            if is_correct:
                score += 1
            
            # Stocker le résultat
            result = QuizResult(
                question_id=question.id,
                question=question.question,
                user_answer=user_answer,
                correct_answer=question.answer,
                is_correct=is_correct,
                difficulty=question.difficulty
            )
            results.append(result)
            
            # Afficher l'explication
            print(f"\n💡 Explication: {question.explanation}")
            
            # Pause avant la prochaine question
            if i < len(self.quiz_questions):
                input("\n⏭️  Appuyez sur Entrée pour continuer...")
        
        # Créer et afficher le résumé
        summary = QuizSummary(
            score=score,
            total=len(self.quiz_questions),
            percentage=(score / len(self.quiz_questions)) * 100,
            results=results
        )
        
        self.current_summary = summary
        self._display_summary(summary)
        
        return summary
    
    def _handle_multiple_choice(self, question: Question) -> tuple[bool, str]:
        """
        Gère une question à choix multiple.
        
        Args:
            question (Question): La question à poser
            
        Returns:
            tuple[bool, str]: (est_correct, réponse_utilisateur)
        """
        # Mélanger les options
        options = question.options.copy()
        random.shuffle(options)
        
        # Afficher les options avec lettres
        letters = ['A', 'B', 'C', 'D']
        print("\nOptions:")
        for j, option in enumerate(options[:4]):
            print(f"  {letters[j]}) {option}")
        
        # Obtenir la réponse utilisateur
        while True:
            user_input = input("\nVotre réponse (A/B/C/D): ").strip().upper()
            if user_input in letters[:len(options)]:
                selected_option = options[letters.index(user_input)]
                user_answer = f"{user_input}) {selected_option}"
                is_correct = (selected_option == question.answer)
                
                if is_correct:
                    print("✅ Correct!")
                else:
                    print(f"❌ Incorrect. La bonne réponse était: {question.answer}")
                
                return is_correct, user_answer
            
            print("⚠️  Veuillez entrer A, B, C ou D")
    
    def _handle_true_false(self, question: Question) -> tuple[bool, str]:
        """
        Gère une question Vrai/Faux.
        
        Args:
            question (Question): La question à poser
            
        Returns:
            tuple[bool, str]: (est_correct, réponse_utilisateur)
        """
        print("\nOptions:")
        print("  A) True")
        print("  B) False")
        
        while True:
            user_input = input("\nVotre réponse (A/B ou True/False): ").strip().upper()
            
            if user_input in ['A', 'TRUE', 'T']:
                user_answer = "True"
                break
            elif user_input in ['B', 'FALSE', 'F']:
                user_answer = "False"
                break
            
            print("⚠️  Veuillez entrer A/B ou True/False")
        
        is_correct = (user_answer == question.answer)
        
        if is_correct:
            print("✅ Correct!")
        else:
            print(f"❌ Incorrect. La bonne réponse était: {question.answer}")
        
        return is_correct, user_answer
    
    def _handle_short_answer(self, question: Question) -> tuple[bool, str]:
        """
        Gère une question à réponse courte (auto-évaluation).
        
        Args:
            question (Question): La question à poser
            
        Returns:
            tuple[bool, str]: (est_correct, réponse_utilisateur)
        """
        print("\n💭 Réfléchissez à votre réponse...")
        input("Appuyez sur Entrée quand vous êtes prêt à voir la réponse...")
        
        print(f"\n📋 Réponse attendue: {question.answer}")
        
        while True:
            self_grade = input("\nAvez-vous bien répondu? (o/n): ").strip().lower()
            
            if self_grade in ['o', 'oui', 'y', 'yes']:
                print("✅ Excellent!")
                return True, "Auto-évalué: Correct"
            elif self_grade in ['n', 'non', 'no']:
                print("📚 Continuez à réviser!")
                return False, "Auto-évalué: Incorrect"
            
            print("⚠️  Veuillez entrer o (oui) ou n (non)")
    
    def _display_summary(self, summary: QuizSummary) -> None:
        """
        Affiche le résumé du quiz.
        
        Args:
            summary (QuizSummary): Le résumé à afficher
        """
        print(f"\n{'='*60}")
        print("🏁 QUIZ TERMINÉ!")
        print(f"{'='*60}")
        print(f"Score: {summary.score}/{summary.total} ({summary.percentage:.1f}%)")
        
        # Évaluation
        if summary.percentage >= 90:
            print("🏆 Excellent!")
        elif summary.percentage >= 80:
            print("🌟 Très bien!")
        elif summary.percentage >= 70:
            print("👍 Bien!")
        elif summary.percentage >= 60:
            print("📚 Passable")
        else:
            print("📖 Continuez à étudier!")
        
        # Performance par difficulté
        difficulty_stats = summary.get_performance_by_difficulty()
        
        if difficulty_stats:
            print(f"\n📊 Performance par difficulté:")
            for diff, stats in sorted(difficulty_stats.items()):
                pct = (stats['correct'] / stats['total']) * 100
                print(f"  {diff}: {stats['correct']}/{stats['total']} ({pct:.1f}%)")
    
    def save_results(self, filename: str = "quiz_results.json") -> bool:
        """
        Sauvegarde les résultats du dernier quiz dans un fichier JSON.
        
        Args:
            filename (str): Nom du fichier de destination (défaut: "quiz_results.json")
            
        Returns:
            bool: True si la sauvegarde a réussi
            
        Example:
            >>> runner = QuizRunner()
            >>> # ... exécuter un quiz ...
            >>> runner.save_results("mes_resultats.json")
        """
        if not self.current_summary:
            print("❌ Aucun résultat à sauvegarder")
            return False
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.current_summary.to_dict(), f, indent=2, ensure_ascii=False)
            print(f"💾 Résultats sauvegardés dans {filename}")
            return True
        except Exception as e:
            print(f"❌ Erreur lors de la sauvegarde: {e}")
            return False
    
    def get_available_sections(self) -> List[str]:
        """
        Retourne la liste des sections disponibles.
        
        Returns:
            List[str]: Liste triée des sections
        """
        if not self.questions:
            return []
        return sorted(set(q.section for q in self.questions))
    
    def get_available_difficulties(self) -> List[str]:
        """
        Retourne la liste des difficultés disponibles.
        
        Returns:
            List[str]: Liste triée des difficultés
        """
        if not self.questions:
            return []
        return sorted(set(q.difficulty for q in self.questions))
    
    def show_stats(self) -> None:
        """Affiche les statistiques de la base de questions chargée."""
        if not self.questions:
            print("❌ Aucune question chargée")
            return
        
        df = pd.DataFrame([q.to_dict() for q in self.questions])
        
        print(f"\n📊 Statistiques de la base de questions:")
        print(f"{'─'*60}")
        print(f"Total: {len(self.questions)} questions")
        print(f"\nPar difficulté:")
        for diff, count in df['difficulty'].value_counts().items():
            print(f"  • {diff}: {count}")
        print(f"\nPar type:")
        for type_q, count in df['type'].value_counts().items():
            print(f"  • {type_q}: {count}")
        print(f"\nPar section:")
        for section, count in sorted(df['section'].value_counts().items()):
            title = df[df['section'] == section]['section_title'].iloc[0]
            print(f"  • {section} ({title}): {count}")
