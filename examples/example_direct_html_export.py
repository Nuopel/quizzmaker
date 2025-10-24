#!/usr/bin/env python3
"""
Direct HTML Export Examples - No Interactive Menus

This example shows direct code to generate HTML quizzes with various options,
without interactive prompts. Perfect for automation or scripting.
"""

import sys
from pathlib import Path

# Add src directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from quizzmaker import QuizRunner


def example1_basic_html_export():
    """Example 1: Basic HTML export with all questions."""
    print("\n" + "="*60)
    print("Example 1: Basic HTML Export")
    print("="*60)

    runner = QuizRunner()
    runner.load_questions("example_python_questions.csv")

    # Create quiz with all questions
    runner.create_quiz(num_questions=10)

    # Export to HTML (all questions on one page)
    runner.export_html_quiz("basic_quiz.html")
    print("✅ Generated: basic_quiz.html")


def example2_paginated_export():
    """Example 2: HTML export with pagination."""
    print("\n" + "="*60)
    print("Example 2: Paginated HTML Export")
    print("="*60)

    runner = QuizRunner()
    runner.load_questions("example_python_questions.csv")

    # Create quiz with 20 questions
    runner.create_quiz(num_questions=20)

    # Export with 5 questions per page
    runner.export_html_quiz("paginated_quiz.html", questions_per_page=5)
    print("✅ Generated: paginated_quiz.html (5 questions per page)")


def example3_filter_by_difficulty():
    """Example 3: Export only Hard questions."""
    print("\n" + "="*60)
    print("Example 3: Filter by Difficulty")
    print("="*60)

    runner = QuizRunner()
    runner.load_questions("example_python_questions.csv")

    # Create quiz with only Hard questions
    runner.create_quiz(
        num_questions=10,
        difficulty_filter="Hard"
    )

    # Export to HTML
    runner.export_html_quiz("hard_questions_quiz.html")
    print("✅ Generated: hard_questions_quiz.html (Hard questions only)")


def example4_filter_by_section():
    """Example 4: Export questions from specific section."""
    print("\n" + "="*60)
    print("Example 4: Filter by Section")
    print("="*60)

    runner = QuizRunner()
    runner.load_questions("example_python_questions.csv")

    # Create quiz with only section 1.x questions
    runner.create_quiz(
        num_questions=10,
        section_filter="1"
    )

    # Export to HTML
    runner.export_html_quiz("section1_quiz.html")
    print("✅ Generated: section1_quiz.html (Section 1 only)")


def example5_filter_question_types():
    """Example 5: Export only Multiple Choice and True/False (exclude Short Answer)."""
    print("\n" + "="*60)
    print("Example 5: Filter by Question Type")
    print("="*60)

    runner = QuizRunner()
    runner.load_questions("example_python_questions.csv")

    # Filter out Short Answer questions by manually filtering the questions list
    # Keep only Multiple Choice and True/False
    runner.questions = [
        q for q in runner.questions
        if q.type in ["Multiple Choice", "True/False"]
    ]

    print(f"Filtered to {len(runner.questions)} questions (MC and T/F only)")

    # Create quiz with filtered questions
    runner.create_quiz(num_questions=len(runner.questions))

    # Export to HTML
    runner.export_html_quiz("mc_tf_only_quiz.html")
    print("✅ Generated: mc_tf_only_quiz.html (Multiple Choice & True/False only)")


def example6_only_multiple_choice():
    """Example 6: Export only Multiple Choice questions."""
    print("\n" + "="*60)
    print("Example 6: Multiple Choice Only")
    print("="*60)

    runner = QuizRunner()
    runner.load_questions("example_python_questions.csv")

    # Keep only Multiple Choice questions
    runner.questions = [q for q in runner.questions if q.type == "Multiple Choice"]

    print(f"Filtered to {len(runner.questions)} Multiple Choice questions")

    # Create quiz
    runner.create_quiz(num_questions=len(runner.questions))

    # Export to HTML with pagination
    runner.export_html_quiz("multiple_choice_only.html", questions_per_page=3)
    print("✅ Generated: multiple_choice_only.html (Multiple Choice only)")


def example7_combined_filters():
    """Example 7: Combine multiple filters."""
    print("\n" + "="*60)
    print("Example 7: Combined Filters")
    print("="*60)

    runner = QuizRunner()
    runner.load_questions("example_python_questions.csv")

    # Filter by question type first (no Short Answer)
    runner.questions = [
        q for q in runner.questions
        if q.type != "Short Answer"
    ]

    # Then create quiz with difficulty filter
    runner.create_quiz(
        num_questions=10,
        difficulty_filter="Medium",
        shuffle=True
    )

    # Export to HTML
    runner.export_html_quiz("medium_no_short_answer.html", questions_per_page=2)
    print("✅ Generated: medium_no_short_answer.html")
    print("   (Medium difficulty, no Short Answer, 2 per page)")


def example8_auto_generated_filename():
    """Example 8: Auto-generated filename with timestamp."""
    print("\n" + "="*60)
    print("Example 8: Auto-generated Filename")
    print("="*60)

    runner = QuizRunner()
    runner.load_questions("example_python_questions.csv")

    # Create quiz
    runner.create_quiz(num_questions=5)

    # Export without specifying filename (auto-generates with timestamp)
    html_path = runner.export_html_quiz()
    print(f"✅ Generated: {Path(html_path).name} (auto-generated)")


def example9_custom_question_selection():
    """Example 9: Custom question selection by IDs or criteria."""
    print("\n" + "="*60)
    print("Example 9: Custom Question Selection")
    print("="*60)

    runner = QuizRunner()
    runner.load_questions("example_python_questions.csv")

    # Custom filter: Medium OR Hard questions, and only MC/TF types
    runner.questions = [
        q for q in runner.questions
        if q.difficulty in ["Medium", "Hard"]
        and q.type in ["Multiple Choice", "True/False"]
    ]

    print(f"Custom filtered to {len(runner.questions)} questions")

    # Create quiz without shuffling to maintain order
    runner.create_quiz(num_questions=len(runner.questions), shuffle=False)

    # Export to HTML
    runner.export_html_quiz("custom_selection.html")
    print("✅ Generated: custom_selection.html")
    print("   (Medium/Hard difficulty, MC/TF only, ordered)")


def main():
    """Run all direct examples."""
    print("="*60)
    print("Direct HTML Export Examples (No Interactive Menus)")
    print("="*60)
    print("\nThese examples show direct code without user prompts.")
    print("Perfect for scripts, automation, or batch processing.\n")

    # Run all examples
    example1_basic_html_export()
    example2_paginated_export()
    example3_filter_by_difficulty()
    example4_filter_by_section()
    example5_filter_question_types()
    example6_only_multiple_choice()
    example7_combined_filters()
    example8_auto_generated_filename()
    example9_custom_question_selection()

    print("\n" + "="*60)
    print("✅ All examples completed!")
    print("="*60)
    print("\nGenerated HTML files:")
    print("  1. basic_quiz.html - All questions, one page")
    print("  2. paginated_quiz.html - 5 questions per page")
    print("  3. hard_questions_quiz.html - Hard difficulty only")
    print("  4. section1_quiz.html - Section 1 only")
    print("  5. mc_tf_only_quiz.html - Multiple Choice & True/False only")
    print("  6. multiple_choice_only.html - Multiple Choice only, paginated")
    print("  7. medium_no_short_answer.html - Medium, no Short Answer")
    print("  8. quiz_YYYYMMDD_HHMMSS.html - Auto-generated filename")
    print("  9. custom_selection.html - Custom filtered questions")
    print("\n💡 Open any file in your browser to test!")


if __name__ == "__main__":
    main()
