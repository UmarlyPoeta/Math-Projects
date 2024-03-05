from palindrome import check_if_palindrome

def test_palindrome_detection():
    test_cases = [
        ("level", True),
        ("A man a plan a canal Panama", True),
        ("hello", False),
        ("", True),
        ("a", True),
        ("Racecar", True),
        ("12321", True),
        ("!@#$%^&*()", False),
        ("A man, a plan, a canal, Panama!", True),
    ]

    for word, expected_result in test_cases:
        result = check_if_palindrome(word)
        assert result == expected_result, f"Failed for word: {word}. Expected {expected_result}, got {result}"

    print("All test cases passed successfully!")


if __name__ == "__main__":
    test_palindrome_detection()
