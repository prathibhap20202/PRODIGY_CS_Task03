"""
Password Complexity Checker Tool
--------------------------------
This tool evaluates the strength of a password based on standard
security requirements and provides improvement suggestions.
"""

import re
import sys


class PasswordChecker:
    """
    Class to validate and evaluate password strength.
    """

    def __init__(self, password: str):
        self.password = password
        self.feedback = []
        self.valid = True
        self.score = 0  # scoring to define strength

    def check_length(self):
        if len(self.password) >= 8:
            self.score += 1
        else:
            self.valid = False
            self.feedback.append("Minimum 8 characters required.")

    def check_uppercase(self):
        if re.search(r"[A-Z]", self.password):
            self.score += 1
        else:
            self.valid = False
            self.feedback.append("At least one uppercase letter required (A-Z).")

    def check_lowercase(self):
        if re.search(r"[a-z]", self.password):
            self.score += 1
        else:
            self.valid = False
            self.feedback.append("At least one lowercase letter required (a-z).")

    def check_digit(self):
        if re.search(r"\d", self.password):
            self.score += 1
        else:
            self.valid = False
            self.feedback.append("At least one numeric digit required (0-9).")

    def check_special_char(self):
        if re.search(r"[@$!%*?&#]", self.password):
            self.score += 1
        else:
            self.valid = False
            self.feedback.append("At least one special character required (@$!%*?&#).")

    def evaluate_strength(self):
        """Return strength label based on score."""
        if self.score == 5:
            return "Very Strong"
        elif self.score == 4:
            return "Strong"
        elif self.score == 3:
            return "Moderate"
        else:
            return "Weak"

    def evaluate(self):
        """Run all checks and return result with feedback."""
        self.check_length()
        self.check_uppercase()
        self.check_lowercase()
        self.check_digit()
        self.check_special_char()

        strength = self.evaluate_strength()

        if self.valid:
            return f"Password meets all security requirements. Strength: {strength}", []
        else:
            return f"Password does not meet security requirements. Strength: {strength}", self.feedback


def display_requirements():
    """Print password rules."""
    print("\nPassword Requirements:")
    print(" - Minimum 8 characters")
    print(" - At least one uppercase letter (A-Z)")
    print(" - At least one lowercase letter (a-z)")
    print(" - At least one digit (0-9)")
    print(" - At least one special character (@$!%*?&#)\n")


def run_tool():
    """Main CLI loop for the tool."""
    
    
    print("        Password Complexity Tool        ")

    display_requirements()

    while True:
        password = input("Enter password to check (or type 'exit'): ").strip()

        if password.lower() == "exit":
            print("\nExiting tool. Goodbye.")
            sys.exit()

        checker = PasswordChecker(password)
        result, improvements = checker.evaluate()

        print("\nResult:", result)

        if improvements:
            print("\nSuggestions:")
            for suggestion in improvements:
                print(" -", suggestion)

        print("\n")


# Execute tool
run_tool()
