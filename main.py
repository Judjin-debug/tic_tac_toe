import os
import re


def tic_tac_toe():

    def cls():
        os.system('cls||clear')

    def display_field():
        print(f"\n  0 1 2\n"
              f"0 {field[0][0]} {field[0][1]} {field[0][2]}\n"
              f"1 {field[1][0]} {field[1][1]} {field[1][2]}\n"
              f"2 {field[2][0]} {field[2][1]} {field[2][2]}")

    def game_info(extra_info):
        display_field()
        print('\n', extra_info)
        print(f"\nGame {game}, turn {turn}")

    def input_check(input_text):

        if not re.search("[0-2]{1}\s+[0-2]{1}", input_text):
            return False
        return True

    def input_processing(input_text):
        return re.findall("\d{1}", input_text)

    def check_cell(x, y, player):
        nonlocal field
        if field[int(x)][int(y)] != '-':
            return False
        return True

    def condition_check(pl):
        nonlocal field
        return any([field[0][0] == pl and field[0][1] == pl and field[0][2] == pl,
                    field[1][0] == pl and field[1][1] == pl and field[1][2] == pl,
                    field[2][0] == pl and field[2][1] == pl and field[2][2] == pl,
                    field[0][0] == pl and field[1][0] == pl and field[2][0] == pl,
                    field[0][1] == pl and field[1][1] == pl and field[2][1] == pl,
                    field[0][2] == pl and field[1][2] == pl and field[2][2] == pl,
                    field[0][0] == pl and field[1][1] == pl and field[2][2] == pl,
                    field[2][0] == pl and field[1][1] == pl and field[0][2] == pl])

    field = [['-' for i in range(3)] for j in range(3)]
    turn = 1
    players = ['X', 'O']
    current_player = 0
    score = [0, 0]
    game = 1
    game_extra_info = "Welcome to the game of tic-tac-toe."

    while True:
        while True:
            cls()
            game_info(game_extra_info)
            print("You can type 'exit' to leave the game prematurely")
            input_coordinates = input("Enter the coordinates separated by a whitespace (e.g. '0 1', row-column):")
            if input_coordinates.lower() == 'exit':
                print("Exiting the current game...")
                break
            if not input_check(input_coordinates):
                game_extra_info = "Input is not correct"
                continue
            coordinate_list = input_processing(input_coordinates)
            if not check_cell(*coordinate_list, players[current_player]):
                game_extra_info = "The field is busy"
                continue
            field[int(coordinate_list[0])][int(coordinate_list[1])] = players[current_player]
            if turn >= 5:
                if condition_check(players[current_player]):
                    score[current_player] += 1
                    cls()
                    display_field()
                    print(f"Player {players[current_player]} won! The score is {score[0]} : {score[1]}")
                    break
            if turn >= 9:
                cls()
                display_field()
                print(f"The game ends in a draw! The score is {score[0]} : {score[1]}")
                break
            turn += 1
            current_player = (current_player + 1) % 2
        choice = input("Another game?[y/N]")
        if not choice.lower() == 'y':
            break
        field = [['-' for i in range(3)] for j in range(3)]
        turn = 1
        current_player = 0
        game += 1


tic_tac_toe()