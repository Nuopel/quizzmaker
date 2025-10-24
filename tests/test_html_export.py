#!/usr/bin/env python3
"""Quick test script for HTML export functionality."""

import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from quizzmaker import QuizRunner


def test_html_export():
    """Test HTML export with different configurations."""
    print("="*60)
    print("Testing HTML Export Functionality")
    print("="*60)

    runner = QuizRunner()

    # Load questions
    csv_file = "examples/example_python_questions.csv"
    print(f"\n1. Loading questions from {csv_file}...")
    if not runner.load_questions(csv_file):
        print("❌ Failed to load questions")
        return False

    print(f"✅ Loaded {len(runner.questions)} questions")

    # Test 1: Export all questions on one page
    print("\n2. Test 1: Export all questions on one page...")
    runner.create_quiz(num_questions=5)
    html_path = runner.export_html_quiz("test_all_in_one.html")
    if html_path:
        print(f"✅ Test 1 passed: {html_path}")
    else:
        print("❌ Test 1 failed")
        return False

    # Test 2: Export with pagination (2 questions per page)
    print("\n3. Test 2: Export with 2 questions per page...")
    runner.create_quiz(num_questions=5)
    html_path = runner.export_html_quiz("test_paginated.html", questions_per_page=2)
    if html_path:
        print(f"✅ Test 2 passed: {html_path}")
    else:
        print("❌ Test 2 failed")
        return False

    # Test 3: Auto-generated filename
    print("\n4. Test 3: Auto-generated filename...")
    runner.create_quiz(num_questions=3)
    html_path = runner.export_html_quiz()
    if html_path:
        print(f"✅ Test 3 passed: {html_path}")
    else:
        print("❌ Test 3 failed")
        return False

    # Test 4: Export with filters (difficulty)
    print("\n5. Test 4: Export filtered quiz (Hard questions)...")
    if runner.create_quiz(num_questions=5, difficulty_filter="Hard"):
        html_path = runner.export_html_quiz("test_hard_questions.html")
        if html_path:
            print(f"✅ Test 4 passed: {html_path}")
        else:
            print("❌ Test 4 failed")
            return False
    else:
        print("⚠️  Test 4 skipped: No hard questions available")

    print("\n" + "="*60)
    print("✅ All tests passed!")
    print("="*60)
    print("\nGenerated HTML files:")
    print("  - test_all_in_one.html (all questions on one page)")
    print("  - test_paginated.html (2 questions per page)")
    print("  - quiz_*.html (auto-generated filename)")
    print("  - test_hard_questions.html (filtered by difficulty)")
    print("\n💡 Open any of these files in your web browser to test the interactive quiz!")

    return True


if __name__ == "__main__":
    success = test_html_export()
    sys.exit(0 if success else 1)
