import random
import string
import sys
import time

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


def winning_possibilities(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def print_message(message):
    for char in message:
        print(char, end='', flush=True)
        if char in string.punctuation:
            time.sleep(.2)
        time.sleep(.03)


def print_wait(prompt, wait=0):
    print_message(prompt)
    print('')
    time.sleep(wait)


# check if an input is valid response
def is_valid_input(prompt, options=[]):
    while True:
        response = input(prompt).lower()
        if len(options) < 1 or response in options:
            return response
        print_wait(f"{response} is invalid, please enter a valid input.")


class Player:
    def __init__(self, greet):
        self.greet = print_wait("Hi, this is rock, paper, scissors game!")

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


# computer
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


# Human
class HumanPlayer(Player):
    def move(self):
        return is_valid_input("Rock, paper or scissors? ",
                              ["rock", "paper", "scissors"])


# Player thst remembers move
class ReflectPlayer(Player):
    def __init__(self):
        self.next_move = random.choice(moves)

    def move(self):
        return self.next_move

    def learn(self, my_move, their_move):
        self.next_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        # super().__init__()
        self.next_move = random.choice(moves)

    def move(self):
        return self.next_move

    def learn(self, my_move, their_move):
        i = 0
        while i < 3:
            if(my_move == moves[i]):
                i = (i+1) % 3
                self.next_move = moves[i]
                break
            i += 1


class Game:
    def __init__(self, p1=HumanPlayer("Player"), p2=RandomPlayer("Player 2")):
        self.score = {1: 0, 2: 0}
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        if(move1 != move2):
            self.score[1] += winning_possibilities(move1, move2)
            self.score[2] += winning_possibilities(move2, move1)
        print_wait(
            f"Player played {move1},  Computer played {move2}",
            1)
        print_wait(
            f"Player scored {self.score[1]}, "
            f"Computer scored {self.score[2]}\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        play_again = 'y'
        while play_again == 'y':
            self.score = {1: 0, 2: 0}
            print_wait("\nThe game has 3 rounds.", 2)
            for round in range(3):
                print_wait(f"Round {round}:", 1)
                self.play_round()

            if (self.score[1] > self.score[2]):
                print_wait("Congratulations, you won!!!", 1)
            elif (self.score[1] < self.score[2]):
                print_wait(
                    "You lost to the computer. ", 1)
            else:
                print_wait("Well done players, its a tie.", 1)

            print_wait(
                f"Score: Player {self.score[1]}, "
                f"Computer {self.score[2]}\n", )
            play_again = is_valid_input("Play again? Y or N: ", "y,n")

        print_wait("Game over!", 1)


if __name__ == '__main__':
    try:
        game = Game()
        game.play_game()
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
        print_wait("\nThe program was interrupted.", 1)
        print_wait("Goodbye!!!")
        sys.exit(1)
