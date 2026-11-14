from words import get_random_word

NUM_ATTEMPTS = 6

def main():
    print("Welcome to Wordle!")
    secret_word = get_random_word()
    tries = 0

    for attempt in range(NUM_ATTEMPTS):

        while True:
            guess = input("Enter your guess: ").lower()

            if len(guess) == 5:
                break

            print("Please enter a 5-letter word.")

        remaining_letters = list(secret_word)
        result = []
        formatted_result = []

        tries += 1

        for i in range(5):
            if secret_word[i] == guess[i]:
                remaining_letters.remove(guess[i])
                result.append("G")
            else:
                result.append("B")

        for i in range(5):
            if result[i] == "B" and guess[i] in remaining_letters:
                result[i] = "Y"
                remaining_letters.remove(guess[i])

        for i in range(5):
            if result[i] == "G":
                formatted_result.append(f"[{guess[i]}]")
            elif result[i] == "B":
                formatted_result.append(guess[i])
            else:
                formatted_result.append(f"({guess[i]})")

        print("Result:", " ".join(formatted_result))

        if guess == secret_word:
            print(f"Congratulations! You guessed the word in {tries} tries!")
            break

    else:
        print(f"Better luck next time! The correct word was '{secret_word}'.")


if __name__ == "__main__":
    main()