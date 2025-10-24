#!/usr/bin/env python3
"""
Example: Exporting Quizzes to Interactive HTML

This example demonstrates how to export quizzes to interactive HTML pages
that can be opened in any web browser.
"""

import sys
from pathlib import Path

# Add src directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from quizzmaker import QuizRunner


def main():
    """Run examples of HTML quiz export."""
    print("="*60)
    print("HTML Quiz Export Examples")
    print("="*60)

    # Initialize runner
    runner = QuizRunner()

    # Load questions from CSV
    csv_path = Path(__file__).parent.parent / "questions.csv"

    if not csv_path.exists():
        print(f"\n❌ File not found: {csv_path}")
        print("Please create questions first using example_create_questions.py")
        return

    if not runner.load_questions(str(csv_path)):
        return

    # Display available options
    print("\n" + "="*60)
    print("HTML Export Options")
    print("="*60)
    print("\n1. Export ALL questions on ONE page (default)")
    print("2. Export with 5 questions per page")
    print("3. Export with 10 questions per page")
    print("4. Export filtered quiz (Hard questions only)")
    print("5. Custom export")
    print("0. Exit")

    while True:
        choice = input("\nYour choice: ").strip()

        if choice == '0':
            print("\nGoodbye!")
            break

        elif choice == '1':
            # Example 1: All questions on one page (default)
            print("\n" + "-"*60)
            print("Example 1: All questions on one page")
            print("-"*60)

            runner.create_quiz(num_questions=len(runner.questions))
            html_path = runner.export_html_quiz(
                filename="quiz_all_in_one.html"
            )

            if html_path:
                print(f"\n✅ Open this file in your browser: {html_path}")

        elif choice == '2':
            # Example 2: 5 questions per page
            print("\n" + "-"*60)
            print("Example 2: 5 questions per page")
            print("-"*60)

            runner.create_quiz(num_questions=20)
            html_path = runner.export_html_quiz(
                filename="quiz_5_per_page.html",
                questions_per_page=5
            )

            if html_path:
                print(f"\n✅ Open this file in your browser: {html_path}")

        elif choice == '3':
            # Example 3: 10 questions per page
            print("\n" + "-"*60)
            print("Example 3: 10 questions per page")
            print("-"*60)

            runner.create_quiz(num_questions=30)
            html_path = runner.export_html_quiz(
                filename="quiz_10_per_page.html",
                questions_per_page=10
            )

            if html_path:
                print(f"\n✅ Open this file in your browser: {html_path}")

        elif choice == '4':
            # Example 4: Filtered quiz (Hard questions)
            print("\n" + "-"*60)
            print("Example 4: Hard questions only")
            print("-"*60)

            runner.create_quiz(
                num_questions=10,
                difficulty_filter="Hard"
            )
            html_path = runner.export_html_quiz(
                filename="quiz_hard_only.html"
            )

            if html_path:
                print(f"\n✅ Open this file in your browser: {html_path}")

        elif choice == '5':
            # Example 5: Custom export
            print("\n" + "-"*60)
            print("Example 5: Custom export")
            print("-"*60)

            # Get custom parameters
            num_q = input("Number of questions (or 'all'): ").strip()
            if num_q.lower() == 'all':
                num_questions = len(runner.questions)
            else:
                num_questions = int(num_q)

            # Section filter
            sections = runner.get_available_sections()
            print(f"\nAvailable sections: {', '.join(sections)}")
            section = input("Filter by section (or press Enter for all): ").strip()
            section_filter = section if section else None

            # Difficulty filter
            difficulties = runner.get_available_difficulties()
            print(f"\nAvailable difficulties: {', '.join(difficulties)}")
            difficulty = input("Filter by difficulty (or press Enter for all): ").strip()
            difficulty_filter = difficulty if difficulty else None

            # Questions per page
            per_page = input("\nQuestions per page (or 'all' for single page): ").strip()
            if per_page.lower() != 'all':
                per_page = int(per_page)

            # Filename
            filename = input("HTML filename (press Enter for auto-generated): ").strip()
            if not filename:
                filename = None

            # Create and export
            runner.create_quiz(
                num_questions=num_questions,
                section_filter=section_filter,
                difficulty_filter=difficulty_filter
            )

            html_path = runner.export_html_quiz(
                filename=filename,
                questions_per_page=per_page
            )

            if html_path:
                print(f"\n✅ Open this file in your browser: {html_path}")

        else:
            print("⚠️  Invalid choice. Please select 0-5.")


if __name__ == "__main__":
    main()
