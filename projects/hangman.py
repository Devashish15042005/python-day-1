import random
word = ["elephant","lion","bat","cat","python","velocity","friction","temprature","liverpool","football","cricket","macdonald","domino","melon","bird"]
hints = {
    "elephant": ["A very large animal 🐘", "It has a trunk 🤏", "Largest land mammal 🌍"],
    "lion": ["King of the jungle 🦁", "Lives in pride", "Big cat"],
    "bat": ["A flying mammal 🦇", "Active at night", "Uses echo to move"],
    "cat": ["Says meow 😺", "Loves milk", "Domestic animal"],
    "python": ["A snake 🐍", "Also a programming language 💻", "Popular for beginners"],
    "velocity": ["Speed in a direction", "Physics term", "Measured in m/s"],
    "friction": ["Opposes motion", "Force between surfaces", "Generates heat"],
    "temprature": ["Hot or cold measure 🌡️", "Measured in °C", "Weather term"],
    "liverpool": ["Football club ⚽", "Premier League team", "Color = Red"],
    "football": ["Played with feet ⚽", "11 players each side", "Goal to win"],
    "cricket": ["Bat and ball sport 🏏", "Played in India", "Has wickets"],
    "macdonald": ["Fast-food brand 🍔", "Yellow logo", "Burgers"],
    "domino": ["Pizza brand 🍕", "Blue and red logo", "Delivery fast"],
    "melon": ["A juicy fruit 🍉", "Green outside", "Red inside"],
    "bird": ["Can fly 🐦", "Has feathers", "Builds nests"]
}
hint_given = False
secret_word = random.choice(word)
guessed = ["_"]*len(secret_word)
hint_index = 0
lives = 6
wrong_guesses = []
#photu of hangman
HANGMAN_PICS = [
    """
       _______
      |/      |
      |      ( )
      |     ==|==
      |       |
      |      / \\
     |__
    """,
    """
       _______
      |/      |
      |      ( )
      |     ==|==
      |       |
      |      /
     |__
    """,
    """
       _______
      |/      |
      |      ( )
      |     ==|==
      |       |
      |
     |__
    """,
    """
       _______
      |/      |
      |      ( )
      |     ==|
      |       |
      |
     |__
    """,
    """
       _______
      |/      |
      |      ( )
      |       |
      |       |
      |
     |__
    """,
    """
       _______
      |/      |
      |      ( )
      |
      |
      |
     |__
    """,
    """
       _______
      |/      |
      |
      |
      |
      |
     |__
    """
]
#loop yaha se chalu ho raha hai
while lives > 0:
    print("Word" , " " .join(guessed))
    print("Lives:",lives)
    print(HANGMAN_PICS[lives])
    guess = input("Enter Your Guess 💁🏻‍♂️: ").lower()
#check if it is valid or not
    if len(guess) != 1 or not guess.isalpha():
        print("\n Invalid input! Please enter you guess again ❌\n")
        continue
#check if it is already used
    if guess in guessed or guess in wrong_guesses:
        print("Already guessed! Please guess another word 🙂‍↔️\n")
        continue
#check and reveal if the word is the secret word
    if guess in secret_word:
        for i,ch in enumerate(secret_word):
            if ch == guess:
                guessed[i] = guess
        print("Good Guess ✅ 😎\n")
    else:
#agar guess galat hai to hangman ke hath pair laga do
        wrong_guesses.append(guess)
        lives -= 1
        print("Wrong Guess 🤨 🙁")
        if len(wrong_guesses) % 2 == 0:
            if(hint_index) < len(hints[secret_word]):
             print("\n💡HINT:",hints[secret_word][hint_index])
             hint_index += 1
            else:
             print("\n no more hint available!")
        hint_given = True
#dekhte hai ki guess bhe kar paya player ya nahi
    if "_" not in guessed:
        print("You Win! Your Guess Was Right 🥳 🤩 ✅ :",secret_word)
        break
# jab player ka dimmag na chaale 
if lives == 0:
    print(HANGMAN_PICS[lives])
    print("You Lost! The Word Was ❌ 🫠 🤪:",secret_word)