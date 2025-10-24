"""
Module de génération et gestion de questions pour les quiz.

Ce module permet de créer, valider et sauvegarder des questions
dans une base de données CSV.
"""

import pandas as pd
from typing import List, Dict, Any, Optional
from pathlib import Path

from quizzmaker.models import Question


class QuestionGenerator:
    """
    Générateur et gestionnaire de base de données de questions.
    
    Cette classe permet de créer des questions de différents types,
    de les valider, et de les sauvegarder dans un fichier CSV.
    
    Attributs:
        questions (List[Question]): Liste des questions créées
    """
    
    def __init__(self):
        """Initialise un générateur vide."""
        self.questions: List[Question] = []
    
    def add_multiple_choice_question(
        self,
        id: int,
        section: str,
        section_title: str,
        difficulty: str,
        question: str,
        options: List[str],
        answer: str,
        explanation: str
    ) -> None:
        """
        Ajoute une question à choix multiple.
        
        Args:
            id (int): Identifiant unique de la question
            section (str): Numéro de section (ex: "1.1")
            section_title (str): Titre de la section
            difficulty (str): "Easy", "Medium", ou "Hard"
            question (str): Texte de la question
            options (List[str]): Liste des options de réponse (2-4 options)
            answer (str): Réponse correcte (doit être dans options)
            explanation (str): Explication de la réponse
            
        Raises:
            ValueError: Si la réponse n'est pas dans les options
            ValueError: Si la question n'est pas valide
            
        Example:
            >>> gen = QuestionGenerator()
            >>> gen.add_multiple_choice_question(
            ...     id=1,
            ...     section="1.1",
            ...     section_title="Introduction",
            ...     difficulty="Easy",
            ...     question="Quelle est la capitale de la France?",
            ...     options=["Paris", "Londres", "Berlin", "Rome"],
            ...     answer="Paris",
            ...     explanation="Paris est la capitale de la France depuis 987."
            ... )
        """
        q = Question(
            id=id,
            section=section,
            section_title=section_title,
            difficulty=difficulty,
            type='Multiple Choice',
            question=question,
            options=options,
            answer=answer,
            explanation=explanation
        )
        
        is_valid, error = q.is_valid()
        if not is_valid:
            raise ValueError(f"Question invalide: {error}")
        
        self.questions.append(q)
    
    def add_true_false_question(
        self,
        id: int,
        section: str,
        section_title: str,
        difficulty: str,
        question: str,
        answer: str,
        explanation: str
    ) -> None:
        """
        Ajoute une question Vrai/Faux.
        
        Args:
            id (int): Identifiant unique de la question
            section (str): Numéro de section (ex: "1.1")
            section_title (str): Titre de la section
            difficulty (str): "Easy", "Medium", ou "Hard"
            question (str): Texte de la question
            answer (str): "True" ou "False"
            explanation (str): Explication de la réponse
            
        Raises:
            ValueError: Si la réponse n'est pas "True" ou "False"
            ValueError: Si la question n'est pas valide
            
        Example:
            >>> gen = QuestionGenerator()
            >>> gen.add_true_false_question(
            ...     id=1,
            ...     section="1.1",
            ...     section_title="Faits",
            ...     difficulty="Easy",
            ...     question="La Terre est ronde.",
            ...     answer="True",
            ...     explanation="La Terre est approximativement sphérique."
            ... )
        """
        q = Question(
            id=id,
            section=section,
            section_title=section_title,
            difficulty=difficulty,
            type='True/False',
            question=question,
            options=['True', 'False'],
            answer=answer,
            explanation=explanation
        )
        
        is_valid, error = q.is_valid()
        if not is_valid:
            raise ValueError(f"Question invalide: {error}")
        
        self.questions.append(q)
    
    def add_short_answer_question(
        self,
        id: int,
        section: str,
        section_title: str,
        difficulty: str,
        question: str,
        answer: str,
        explanation: str
    ) -> None:
        """
        Ajoute une question à réponse courte (auto-évaluation).
        
        Args:
            id (int): Identifiant unique de la question
            section (str): Numéro de section (ex: "1.1")
            section_title (str): Titre de la section
            difficulty (str): "Easy", "Medium", ou "Hard"
            question (str): Texte de la question
            answer (str): Réponse attendue
            explanation (str): Explication de la réponse
            
        Example:
            >>> gen = QuestionGenerator()
            >>> gen.add_short_answer_question(
            ...     id=1,
            ...     section="1.1",
            ...     section_title="Concepts",
            ...     difficulty="Medium",
            ...     question="Expliquez le principe de séparation des responsabilités.",
            ...     answer="Chaque module doit avoir une seule responsabilité bien définie.",
            ...     explanation="Ce principe facilite la maintenance et les tests."
            ... )
        """
        q = Question(
            id=id,
            section=section,
            section_title=section_title,
            difficulty=difficulty,
            type='Short Answer',
            question=question,
            options=[],
            answer=answer,
            explanation=explanation
        )
        
        is_valid, error = q.is_valid()
        if not is_valid:
            raise ValueError(f"Question invalide: {error}")
        
        self.questions.append(q)
    
    def load_from_csv(self, filename: str) -> bool:
        """
        Charge des questions depuis un fichier CSV.
        
        Args:
            filename (str): Chemin du fichier CSV
            
        Returns:
            bool: True si le chargement a réussi
            
        Raises:
            FileNotFoundError: Si le fichier n'existe pas
            ValueError: Si le format CSV est invalide
        """
        try:
            df = pd.read_csv(filename)
            self.questions = []
            
            for _, row in df.iterrows():
                q = Question.from_dict(row.to_dict())
                is_valid, error = q.is_valid()
                if not is_valid:
                    print(f"⚠️  Question {q.id} invalide: {error}")
                    continue
                self.questions.append(q)
            
            print(f"✅ Chargé {len(self.questions)} questions depuis {filename}")
            return True
            
        except FileNotFoundError:
            print(f"❌ Fichier non trouvé: {filename}")
            return False
        except Exception as e:
            print(f"❌ Erreur lors du chargement: {e}")
            return False
    
    def save_to_csv(self, filename: str) -> bool:
        """
        Sauvegarde les questions dans un fichier CSV.
        
        Args:
            filename (str): Chemin du fichier CSV de destination
            
        Returns:
            bool: True si la sauvegarde a réussi
        """
        if not self.questions:
            print("❌ Aucune question à sauvegarder")
            return False
        
        try:
            data = [q.to_dict() for q in self.questions]
            df = pd.DataFrame(data)
            df.to_csv(filename, index=False)
            print(f"✅ Sauvegardé {len(self.questions)} questions dans {filename}")
            return True
        except Exception as e:
            print(f"❌ Erreur lors de la sauvegarde: {e}")
            return False
    
    def get_stats(self) -> Dict[str, Any]:
        """
        Calcule les statistiques de la base de questions.
        
        Returns:
            dict: Statistiques (total, par difficulté, par type, par section)
            
        Example:
            >>> gen = QuestionGenerator()
            >>> # ... ajouter des questions ...
            >>> stats = gen.get_stats()
            >>> print(f"Total: {stats['total']}")
        """
        if not self.questions:
            return {"total": 0}
        
        df = pd.DataFrame([q.to_dict() for q in self.questions])
        return {
            "total": len(self.questions),
            "by_difficulty": df['difficulty'].value_counts().to_dict(),
            "by_type": df['type'].value_counts().to_dict(),
            "by_section": df['section'].value_counts().to_dict()
        }
    
    def clear(self) -> None:
        """Efface toutes les questions de la mémoire."""
        self.questions.clear()
        print("🗑️  Toutes les questions ont été effacées")
    
    def preview(self, num_questions: int = 3) -> None:
        """
        Affiche un aperçu des premières questions.
        
        Args:
            num_questions (int): Nombre de questions à afficher (défaut: 3)
        """
        if not self.questions:
            print("❌ Aucune question à prévisualiser")
            return
        
        for i, q in enumerate(self.questions[:num_questions], 1):
            print(f"\n{'='*60}")
            print(f"Question {i}/{min(num_questions, len(self.questions))}")
            print(f"{'='*60}")
            print(f"ID: {q.id} | Section: {q.section} - {q.section_title}")
            print(f"Difficulté: {q.difficulty} | Type: {q.type}")
            print(f"\nQ: {q.question}")
            
            if q.type == 'Multiple Choice':
                print("\nOptions:")
                for opt in q.options:
                    print(f"  • {opt}")
            elif q.type == 'True/False':
                print("\nOptions: True / False")
            
            print(f"\n✓ Réponse: {q.answer}")
            print(f"💡 {q.explanation}")
    
    def validate_all(self) -> tuple[int, List[str]]:
        """
        Valide toutes les questions chargées.
        
        Returns:
            tuple[int, List[str]]: (nombre_invalides, liste_erreurs)
        """
        errors = []
        for q in self.questions:
            is_valid, error = q.is_valid()
            if not is_valid:
                errors.append(f"Question {q.id}: {error}")
        
        return len(errors), errors
    
    def get_question_by_id(self, question_id: int) -> Optional[Question]:
        """
        Récupère une question par son ID.
        
        Args:
            question_id (int): ID de la question recherchée
            
        Returns:
            Optional[Question]: La question si trouvée, None sinon
        """
        for q in self.questions:
            if q.id == question_id:
                return q
        return None
    
    def remove_question(self, question_id: int) -> bool:
        """
        Supprime une question par son ID.
        
        Args:
            question_id (int): ID de la question à supprimer
            
        Returns:
            bool: True si la question a été supprimée
        """
        for i, q in enumerate(self.questions):
            if q.id == question_id:
                self.questions.pop(i)
                print(f"✅ Question {question_id} supprimée")
                return True
        print(f"❌ Question {question_id} non trouvée")
        return False
