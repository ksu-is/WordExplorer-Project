import random
import os
import time
from datetime import datetime

class VocabGame:
    def __init__(self):
        # Default built-in vocab
        self.words_data = [
            {"word": "ubiquitous", "definition": "present, appearing, or found everywhere", "level": "beginner"},
            {"word": "ephemeral", "definition": "lasting for a very short time", "level": "beginner"},
            {"word": "touche", "definition": "acknowledging someone's good point during an argument", "level": "beginner"},
            {"word": "accolade", "definition": "a tangible symbol signifying approval or distinction", "level": "beginner"},
            {"word": "acrimony", "definition": "a rough and bitter manner", "level": "beginner"},
            {"word": "fiasco", "definition": "can be used to describe something that failed miserably", "level": "beginner"},
            {"word": "baroque", "definition": "relating to an elaborately ornamted style of art and music", "level": "intermediate"},
            {"word": "eloquent", "definition": "fluent or persuasive in speaking or writing", "level": "intermediate"},
            {"word": "meticulous", "definition": "showing great attention to detail", "level": "intermediate"},
            {"word": "benevolent", "definition": "well-meaning and kindly", "level": "intermediate"},
            {"word": "tranquil", "definition": "the state of being relaxed/calm", "level": "intermediate"},
            {"word": "capricious", "definition": "sudden changes in mood or behavior", "level": "intermediate"},
            {"word": "Exacerbate", "definition": "To worsen a situation that is already bad", "level": "intermediate"},
            {"word": "repertoire", "definition": "a person's list of talents and skills", "level": "intermediate"},
            {"word": "juxtapose", "definition": "place side by side for contrasting effect", "level": "advanced"},
            {"word": "Flummoxed", "definition": "Extreme confusion or bewilderment", "level": "advanced"},
            {"word": "quintessential", "definition": "being the best example of something/someone", "level": "advanced"},
            {"word": "Ostentatious", "definition": "An act which is done to obviously seek attention", "level": "advanced"},
            {"word": "Quid Pro Quo", "definition": "A material or favor recieved for doing or giving something else", "level": "advanced"},
            {"word": "verbose", "definition": "using or expressed in more words than necessary", "level": "advanced"},
            {"word": "Rendezvous", "definition": "A meeting place and date agreed upon by two parties", "level": "advanced"},
            {"word": "equivocate", "definition": "use ambiguous language to conceal truth or avoid commitment", "level": "advanced"},
            {"word": "lethargic", "definition": "sluggish or inactive", "level": "advanced"},
            {"word": "tenacious", "definition": "persistent, determined", "level": "advanced"},
        ]

        self.custom_file = "vocab_custom.txt"
        self.score_file = "scores.txt"

        self.load_custom_words()

    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")

    # -------------------------
    # Load custom words from file
    # -------------------------
    def load_custom_words(self):
        if not os.path.exists(self.custom_file):
            return

        with open(self.custom_file, "r") as f:
            for line in f:
                if "|" in line:
                    word, definition, level = line.strip().split("|")
                    self.words_data.append({
                        "word": word,
                        "definition": definition,
                        "level": level
                    })

    # -------------------------
    # Save newly added word
    # -------------------------
    def save_custom_word(self, word, definition, level):
        with open(self.custom_file, "a") as f:
            f.write(f"{word}|{definition}|{level}\n")

    # -------------------------
    # Save score
    # -------------------------
    def save_score(self, level, score, total):
        percent = (score / total) * 100
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        with open(self.score_file, "a") as f:
            f.write(f"Level: {level} | Score: {score}/{total} | Percent: {percent:.1f}% | Date: {timestamp}\n")

    # -------------------------
    # View saved scores
    # -------------------------
    def view_scores(self):
        self.clear()
        print("====== SCORE HISTORY ======\n")
        if not os.path.exists(self.score_file):
            print("No scores saved yet.\n")
        else:
            with open(self.score_file, "r") as f:
                print(f.read())
        input("Press Enter to return to menu...")

    # -------------------------
    # Add new word interactively
    # -------------------------
    def add_word(self):
        self.clear()
        print("====== ADD NEW WORD ======\n")

        word = input("Enter the new word: ").strip()
        definition = input("Enter its definition: ").strip()
        level = input("Enter level (beginner / intermediate / advanced): ").strip().lower()

        if level not in ["beginner", "intermediate", "advanced"]:
            print("Invalid level. Defaulting to beginner.")
            level = "beginner"

        self.save_custom_word(word, definition, level)

        print("\nWord added successfully!")
        input("Press Enter to return to menu...")

    # -------------------------
    # START REAL GAME
    # -------------------------
    def start_vocab_game(self):
        self.clear()
        print("====== VOCAB GAME ======")
        print("Choose level:")
        print("1. Beginner")
        print("2. Intermediate")
        print("3. Advanced")
        print("-----------------------------------")
        print("💡 Type 'hint' for a hint")
        print("⏳ Each question has a 10-second timer\n")

        choice = input("Enter choice (1-3): ")

        levels = {"1":"beginner", "2":"intermediate", "3":"advanced"}
        chosen_level = levels.get(choice, "beginner")

        word_list = [w for w in self.words_data if w["level"] == chosen_level]
        random.shuffle(word_list)

        score = 0
        total = len(word_list)
        time_limit = 10

        for i, item in enumerate(word_list, start=1):
            self.clear()
            print(f"Question {i}/{total}")
            print("Definition:", item["definition"])
            print(f"⏳ Time limit: {time_limit} seconds")

            start = time.time()
            hint_used = False

            while True:
                if time.time() - start > time_limit:
                    print("\n⏳ Time ran out!")
                    print(f"Correct answer: {item['word']}")
                    break

                answer = input("> ").strip().lower()

                if answer == "hint":
                    hint_used = True
                    print(f"Hint: starts with '{item['word'][0]}' ({len(item['word'])} letters)")
                    continue

                if answer == item["word"].lower():
                    print("✓ Correct!")
                    if not hint_used:
                        score += 1
                    else:
                        print("(Hint used — no point)")
                    break
                else:
                    print("Try again or type 'hint'")

            input("Press Enter to continue...")

        # Save score
        self.save_score(chosen_level, score, total)

        self.clear()
        print("====== GAME OVER ======")
        print(f"Score: {score}/{total} ({score/total*100:.1f}%)")
        input("\nPress Enter to return to menu...")

    # -------------------------
    # MAIN MENU
    # -------------------------
    def main_menu(self):
        while True:
            self.clear()
            print("====== VOCAB GAME MENU ======")
            print("1. Play Game")
            print("2. Add New Word")
            print("3. View Saved Scores")
            print("4. Exit")
            choice = input("\nEnter your choice: ")

            if choice == "1":
                self.start_vocab_game()
            elif choice == "2":
                self.add_word()
            elif choice == "3":
                self.view_scores()
            elif choice == "4":
                self.clear()
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")
                time.sleep(1)

if __name__ == "__main__":
    VocabGame().main_menu()

