import random

score = 0

print("====== HANGMAN GAME ======")

topic_no = 1

while True:

    play = input("\nDo you want to play? (yes/no): ").lower()

    if play != "yes":
        print("\nThanks for playing!")
        print("Final Score:", score)
        print("Come again! Let's have fun next time.")
        break

    # Selecting topic using if-elif-else
    if topic_no == 1:
        topic = "Kitchen Tools"
        words = ["BOWL", "FORK", "KNIFE", "SPOON"]

    elif topic_no == 2:
        topic = "Birds"
        words = ["CROW", "EAGLE", "PARROT", "PIGEON"]

    elif topic_no == 3:
        topic = "Fruits"
        words = ["APPLE", "MANGO", "ORANGE", "GRAPES"]

    elif topic_no == 4:
        topic = "Animals"
        words = ["TIGER", "HORSE", "RABBIT", "MONKEY"]

    # Reset to first topic after last topic
    topic_no += 1
    if topic_no > 4:
        topic_no = 1

    word = random.choice(words)

    guessed_word = ["_"] * len(word)
    guessed_letters = []

    wrong_guesses = 0
    max_wrong = 6

    print("\nTopic :", topic)
    print("Word Length :", len(word))
    print("Word :", " ".join(guessed_word))

    while wrong_guesses < max_wrong and "_" in guessed_word:

        guess = input("\nEnter a letter: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in word:

            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess

            print("Correct Guess!")

        else:
            wrong_guesses += 1
            print("Wrong Guess!")

        print("Word :", " ".join(guessed_word))
        print("Remaining Chances :", max_wrong - wrong_guesses)

    if "_" not in guessed_word:
        print("Congratulations!")
        print("You guessed the word:", word)
        score += 10
    else:
        print("Better Luck Next Time!")
        print("The correct word was:", word)

    print("Current Score:", score)