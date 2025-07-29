import requests

BASE_URL = "https://mastermind.darkube.app"

def start_game():
    response = requests.post(f"{BASE_URL}/game")
    response.raise_for_status()
    return response.json()["game_id"]

def send_guess(game_id, guess):
    response = requests.post(
        f"{BASE_URL}/guess",
        json={"game_id": game_id, "guess": guess}
    )
    response.raise_for_status()
    return response.json()

def is_valid_guess(guess):
    return (
        len(guess) == 4
        and guess.isdigit()
        and all(c in '123456' for c in guess)
        and len(set(guess)) == 4
    )

def prompt_guess(game_id):
    while True:
        guess = input("Enter your guess (4 unique digits from 1-6): ").strip()
        if not is_valid_guess(guess):
            print("❌ Invalid guess. Please enter 4 unique digits from 1 to 6.")
            continue
        
        result = send_guess(game_id, guess)
        print(f"✅ Guess: {guess}")
        print(f"🎯 Correct positions: {result['correct_place']}, "
              f"Correct digits (wrong place): {result['correct_digit']}")
        
        if result["win"]:
            print("🎉 Congratulations! You won the game!")
            break

def run_game():
    print("🎮 Welcome to Mastermind!")
    print("Guess the 4-digit code (digits 1–6, no repeats).")
    game_id = start_game()
    prompt_guess(game_id)

if __name__ == "__main__":
    run_game()