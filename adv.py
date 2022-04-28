import time
import random
import sys


def print_sleep(prompt, sleep_time=0):
    print(prompt)
    time.sleep(sleep_time)


def valid_input(prompt, options):
    while True:
        response = input(prompt).lower().strip()
        if response in options:
            return response


def play_again():
    user_choice = valid_input(
        "Play again? Y or N: ", ["y", "n"])
    if user_choice == "y":
        print_sleep("Welcome back", 1)
        return True
    elif user_choice == "n":
        print_sleep("Hey!!! Go take a glass of water", 2)
        print_sleep("Good Bye", 1)
        exit(0)


def sango_new_car(location):
    user_choice_two = valid_input(
        "Do you want to take the new car? Y or N ", ["y", "n"])
    if user_choice_two == 'y':
        print_sleep("The car takes another 5 minutes before it"
                    " is filled up. The driver takes a longer"
                    f" route. You are 7 minutes walk from {location}"
                    " however there is a terrible traffic.", 2)
        final_choice = valid_input("Do you want to (1) walk (2)"
                                   "run or (3) stay in the car? ",
                                   ['1', '2', '3'])
        if final_choice == "1":
            print_sleep("You got there late. Game over!", 1)
        elif final_choice == "2":
            print_sleep("You got there early enough and had a good drink."
                        " Congratulations, you survived and won the game!", 1)
        elif final_choice == "3":
            print_sleep("You got there late. Game over!", 1)
    elif user_choice_two == "n":
        print_sleep("You got there late. Game over!", 1)


def sango(location):
    print_sleep("You are stuck in traffic for 15 minutes as"
                " others want to get to the tap too. Your car"
                " seems to be slow however there is another car option.", 2)

    sango_new_car(location)
    return True


def ojoo(location):
    print_sleep("Your car is fast, very fast. You seem to have"
                " made the right choice. However, you see a road"
                " block, one that has been caused by angry protesters", 2)
    user_choice_three = valid_input(" Do you want to (1) go back to Sango or"
                                    " (2) join the protest? ", ['1', '2'])
    if user_choice_three == '1':
        print_sleep(f"You missed the last car going to {location}."
                    " You die of thirst... Game over", 1)
    elif user_choice_three == '2':
        print_sleep("You become so engrossed in the"
                    " protest before you realize what is happening"
                    " you die of thirst... Game over", 1)


def about_game(location):
    print_sleep("You are hanging out with friends. Suddenly the"
                " environment becomes dark, everyone is running helter,"
                " skelter.", 1)
    print_sleep("The only source of water supply in your"
                " current environment is dried up. You are thirsty however"
                " you have 30 minutes to get to the water "
                f"supply in {location}.", 1)
    print_sleep("You have 2 options, go through", 1)
    user_choice_three = valid_input(" (1) Sango or (2) Ojoo? ", ['1', '2'])
    if user_choice_three == "1":
        sango(location)
        return True
    elif user_choice_three == '2':
        ojoo(location)
        return True


def start_game():
    game_location = ['Iwo Road', 'Oja Oba', 'Bodija']
    while True:
        location = random.choice(game_location)
        about_game(location)
        play_again()


if __name__ == '__main__':
    try:
        start_game()
    except TypeError as e:
        print(e)
        sys.exit(1)
    except NameError as e:
        print(e)
        sys.exit(1)
    except IndexError as e:
        print(e)
        sys.exit(1)
    except KeyboardInterrupt:
        print_sleep("\nThe program was interrupted.", 1)
        print_sleep("Goodbye!!!")
        sys.exit(1)
