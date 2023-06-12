## HANGMAN GAME ##
## IMPORTS
import random
## FUNCTION
def display_word(word, letters):
    displayed_word = ""
    for char in word:
        if char in letters:
            displayed_word += char + " "
        else:
            displayed_word += "_ "
    return displayed_word
## PRINTS
print("Welcome to Hangman!")
print("The computer will choose a word and you will have to guess it.")
print("You can guess one letter at a time.")
print("Choose yout theme: \n1. Animals \n2. Fruits \n3. Countries")
theme = int(input("Enter your choice: "))
print("Choose your difficulty level: \n1. Easy(15 Trys) \n2. Medium(10 Trys) \n3. Hard(5 Trys)")
difficulty = int(input("Enter your choice: "))
## IF ELSE STATEMENT FOR THE DIFFICULTY
if difficulty == 1:
    max_attempts = 15
elif difficulty == 2:
    max_attempts = 10
elif difficulty == 3:
    max_attempts = 5
else:
    print("Invalid choice. The game will be played on easy mode.")
    max_attempts = 15
## IF ELSE STATEMENT FOR THE THEME
if theme == 1:
    animals = ["cat", "dog", "elephant", "tiger", "lion", "monkey", "giraffe", "zebra", "bear", "wolf"]
    word = random.choice(animals)
elif theme == 2:
    fruits = ["apple", "banana", "orange", "grapes", "pineapple", "mango", "watermelon", "strawberry", "papaya", "cherry"]
    word = random.choice(fruits)
elif theme == 3:
    countries = ["india", "china", "usa", "russia", "japan", "germany", "france", "italy", "spain", "canada"]
    word = random.choice(countries)
else:
    print("Invalid choice. The game will be played on animals theme.")
    animals = ["cat", "dog", "elephant", "tiger", "lion", "monkey", "giraffe", "zebra", "bear", "wolf"]
    word = random.choice(animals)
## VARIEBLES
chosen_word = word
guessed_letters = []
## WHILE LOOP
while True:
    print("Guess the word:", display_word(chosen_word, guessed_letters))
    guess = input("Enter a letter: ").lower()
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)
    if guess in chosen_word:
        print("Correct guess!")
    else:
        print("Wrong guess!")
        if len(guessed_letters) == max_attempts:
            print("Game Over! You ran out of attempts.")
            print("The word was:", chosen_word)
            break
    if set(chosen_word).issubset(set(guessed_letters)):
        print("Congratulations! You won the game.")
        print("The word was:", chosen_word)
        break
## @suadob0y