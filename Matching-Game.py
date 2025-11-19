import random
import os

class VocabGame:
    def __init__(self):
        # Vocabulary data with levels
        self.words_data = [
            {"word": "ubiquitous", "definition": "present, appearing, or found everywhere", "level": "beginner"},
            {"word": "ephemeral", "definition": "lasting for a very short time", "level": "beginner"},
            {"word": "eloquent", "definition": "fluent or persuasive in speaking or writing", "level": "intermediate"},
            {"word": "meticulous", "definition": "showing great attention to detail", "level": "intermediate"},
            {"word": "benevolent", "definition": "well-meaning and kindly", "level": "intermediate"},
            {"word": "juxtapose", "definition": "place side by side for contrasting effect", "level": "advanced"},
            {"word": "verbose", "definition": "To speak in a vague way to mislead", "level": "advanced"},
            {"word": "Equivocate", "definition": "Sluggish or inactive", "level": "advanced"},
            {"word": "Lethargic", "definition": "persistent, determined", "level": "advanced"},
            {"word": "tenacious", "definition": "persistent, determined", "level": "advanced"},
        ]

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def start_game(self):
        self.clear_screen()
        print("===== VOCAB MATCHING GAME =====")
        print("Select a level:")
        print("1. Beginner")
        print("2. Intermediate")
        print("3. Advanced")

        level_choice = input("Enter choice (1-3): ")

        if level_choice == "1":
            chosen_level = "beginner"
        elif level_choice == "2":
            chosen_level = "intermediate"
        elif level_choice == "3":
            chosen_level = "advanced"
        else:
            print("Invalid choice. Defaulting to Beginner.")
            chosen_level = "beginner"

        # Filter words for the selected level
        word_list = [w for w in self.words_data if w["level"] == chosen_level]

        if not word_list:
            print("No words available for this level.")
            return

        random.shuffle(word_list)
        score = 0
        total_questions = min(len(word_list), 10)

        for i, word_data in enumerate(word_list[:total_questions]):
            self.clear_screen()
            print(f"Question {i + 1} of {total_questions}")
            print(f"Word: {word_data['word']}")
            
            # Generate multiple-choice options
            options = [word_data["definition"]]
            while len(options) < 4:
                # Randomly pick definitions from other words to fill options
                choice = random.choice(self.words_data)["definition"]
                if choice not in options:
                    options.append(choice)
            random.shuffle(options)
            
            for idx, option in enumerate(options):
                print(f"{idx + 1}. {option}")
            
            # Get user input
            while True:
                try:
                    answer = int(input("Enter your choice (1-4): "))
                    if 1 <= answer <= 4:
                        break
                    else:
                        print("Please enter a number between 1 and 4.")
                except ValueError:
                    print("Invalid input. Enter a number.")

            if options[answer - 1] == word_data["definition"]:
                print("✓ Correct!")
                score += 1
            else:
                print(f"✗ Incorrect! The correct definition is: {word_data['definition']}")
            
            input("Press Enter to continue...")

        self.clear_screen()
        print(f"Game Over! You scored {score}/{total_questions} ({score/total_questions*100:.1f}%)")

if __name__ == "__main__":
    game = VocabGame()
    game.start_game()

