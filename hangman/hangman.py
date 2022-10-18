import random

win = 0
lost = 0
print("H A N G M A N\n")


def results():
    global win
    global lost
    print(f"""You won: {win} times.
You lost: {lost} times.""")


def possible_errors(guess_):
    if len(guess_) != 1:
        print("Please, input a single letter.")
        return False
    elif not guess_.islower():
        print("Please, enter a lowercase letter from the English alphabet.")
        return False
    elif type(guess_) != str:
        print("Please, enter a lowercase letter from the English alphabet.")
        return False
    else:
        return True


def menu():
    while True:
        start = 'Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: '
        print(start)
        y = input()
        if y == 'play':
            play_the_game()
        elif y == 'results':
            results()
        elif y == 'exit':
            exit()
        else:
            continue


def play_the_game():
    global win
    global lost
    playing_list = ['python', 'java', 'swift', 'javascript']
    playing_word = random.choice(playing_list)
    word_set = set(playing_word)
    guess_set = set()
    hidden_word = str("-" * len(playing_word))
    hidden_list = list(hidden_word)
    repeat_error_msg = "You've already guessed this letter."
    wrong_set = set()
    attempt = 0
    while True:
        if attempt == 8:
            print("You lost!")
            lost += 1
            break
        elif word_set == guess_set:
            print(f"You guessed the word {playing_word}! \nYou survived!")
            win += 1
            break
        print(hidden_word)
        guess = input('Input a letter: ')
        x = 0
        if possible_errors(guess) is True:
            if guess in word_set and guess not in guess_set:
                for j in playing_word:
                    if j == guess:
                        hidden_list[x] = guess
                        hidden_word = "".join(hidden_list)
                        x += 1
                        guess_set.add(guess)
                    else:
                        x += 1
            elif guess in word_set and guess in guess_set:
                print(repeat_error_msg)
            elif guess in wrong_set:
                print(repeat_error_msg)
            else:
                print("That letter doesn't appear in the word.")
                attempt += 1
                wrong_set.add(guess)


menu()
