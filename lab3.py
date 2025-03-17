import random

def generate_secret_code():
    """Генерує 4-цифровий секретний код з унікальними цифрами."""
    digits = list(range(10))
    random.shuffle(digits)
    return ''.join(map(str, digits[:4]))

def analyze_guess(secret_code, user_guess):
    """Аналізує спробу користувача та підраховує "биків" і "корів"."""
    bulls = sum(1 for i in range(4) if user_guess[i] == secret_code[i])
    cows = sum(1 for digit in user_guess if digit in secret_code) - bulls
    return bulls, cows

def play_game():
    """Основна функція для гри в консолі."""
    secret_code = generate_secret_code()
    attempts = 0
    print("Гра 'Таємний код'! Спробуйте вгадати 4-цифровий код.")
    
    while True:
        user_guess = input("Введіть 4-цифрове число: ")
        
        if not user_guess.isdigit() or len(user_guess) != 4:
            print("Некоректний ввід! Введіть рівно 4 цифри.")
            continue
        
        attempts += 1
        bulls, cows = analyze_guess(secret_code, user_guess)
        print(f"Бики: {bulls}, Корови: {cows}")
        
        if bulls == 4:
            print(f"Вітаємо! Ви вгадали код {secret_code} за {attempts} спроб.")
            break

if __name__ == "__main__":
    play_game()
