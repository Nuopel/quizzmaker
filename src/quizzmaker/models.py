"""
Module de modèles de données pour le système de quiz.

Ce module contient les classes de données représentant les questions
et les résultats de quiz.
"""

from dataclasses import dataclass
from typing import List, Optional
import json


@dataclass
class Question:
    """
    Représente une question de quiz.
    
    Attributs:
        id (int): Identifiant unique de la question
        section (str): Numéro de section (ex: "1.1", "2.3")
        section_title (str): Titre de la section
        difficulty (str): Niveau de difficulté ("Easy", "Medium", "Hard")
        type (str): Type de question ("Multiple Choice", "True/False", "Short Answer")
        question (str): Texte de la question
        options (List[str]): Liste des options de réponse (vide pour Short Answer)
        answer (str): Réponse correcte
        explanation (str): Explication de la réponse
    """
    id: int
    section: str
    section_title: str
    difficulty: str
    type: str
    question: str
    options: List[str]
    answer: str
    explanation: str
    
    def to_dict(self) -> dict:
        """
        Convertit la question en dictionnaire pour sauvegarde CSV.
        
        Returns:
            dict: Dictionnaire avec options en format JSON string
        """
        return {
            'id': self.id,
            'section': self.section,
            'section_title': self.section_title,
            'difficulty': self.difficulty,
            'type': self.type,
            'question': self.question,
            'options': json.dumps(self.options),
            'answer': self.answer,
            'explanation': self.explanation
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Question':
        """
        Crée une Question à partir d'un dictionnaire (lecture CSV).
        
        Args:
            data (dict): Dictionnaire contenant les données de la question
            
        Returns:
            Question: Instance de Question créée
        """
        return cls(
            id=int(data['id']),
            section=str(data['section']),  # Convertir en string pour gérer les nombres
            section_title=str(data['section_title']),
            difficulty=str(data['difficulty']),
            type=str(data['type']),
            question=str(data['question']),
            options=json.loads(data['options']) if data['options'] else [],
            answer=str(data['answer']),
            explanation=str(data['explanation'])
        )
    
    def is_valid(self) -> tuple[bool, Optional[str]]:
        """
        Vérifie si la question est valide.
        
        Returns:
            tuple[bool, Optional[str]]: (est_valide, message_erreur)
        """
        # Vérifier le type
        if self.type not in ['Multiple Choice', 'True/False', 'Short Answer']:
            return False, f"Type invalide: {self.type}"
        
        # Vérifier la difficulté
        if self.difficulty not in ['Easy', 'Medium', 'Hard']:
            return False, f"Difficulté invalide: {self.difficulty}"
        
        # Vérifier les options pour Multiple Choice
        if self.type == 'Multiple Choice':
            if len(self.options) < 2:
                return False, "Multiple Choice doit avoir au moins 2 options"
            if self.answer not in self.options:
                return False, f"La réponse '{self.answer}' n'est pas dans les options"
        
        # Vérifier les options pour True/False
        if self.type == 'True/False':
            if self.answer not in ['True', 'False']:
                return False, "True/False doit avoir comme réponse 'True' ou 'False'"
        
        return True, None


@dataclass
class QuizResult:
    """
    Représente le résultat d'une question dans un quiz.
    
    Attributs:
        question_id (int): ID de la question
        question (str): Texte de la question
        user_answer (str): Réponse de l'utilisateur
        correct_answer (str): Réponse correcte
        is_correct (bool): Si la réponse est correcte
        difficulty (str): Difficulté de la question
    """
    question_id: int
    question: str
    user_answer: str
    correct_answer: str
    is_correct: bool
    difficulty: str
    
    def to_dict(self) -> dict:
        """Convertit le résultat en dictionnaire."""
        return {
            'question_id': self.question_id,
            'question': self.question,
            'user_answer': self.user_answer,
            'correct_answer': self.correct_answer,
            'is_correct': self.is_correct,
            'difficulty': self.difficulty
        }


@dataclass
class QuizSummary:
    """
    Résumé complet d'un quiz terminé.
    
    Attributs:
        score (int): Nombre de bonnes réponses
        total (int): Nombre total de questions
        percentage (float): Pourcentage de réussite
        results (List[QuizResult]): Liste des résultats par question
    """
    score: int
    total: int
    percentage: float
    results: List[QuizResult]
    
    def to_dict(self) -> dict:
        """Convertit le résumé en dictionnaire pour sauvegarde JSON."""
        return {
            'score': self.score,
            'total': self.total,
            'percentage': self.percentage,
            'results': [r.to_dict() for r in self.results]
        }
    
    def get_performance_by_difficulty(self) -> dict:
        """
        Calcule les performances par niveau de difficulté.
        
        Returns:
            dict: Dictionnaire avec stats par difficulté
        """
        difficulty_stats = {}
        for result in self.results:
            diff = result.difficulty
            if diff not in difficulty_stats:
                difficulty_stats[diff] = {'correct': 0, 'total': 0}
            difficulty_stats[diff]['total'] += 1
            if result.is_correct:
                difficulty_stats[diff]['correct'] += 1
        
        return difficulty_stats
