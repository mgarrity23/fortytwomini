from play_board import PlayBoard

play = True
while(play):
    print('Welcome to my command line adventure game!')
    start_input = input('Enter \"Start\" to begin: ')
    start_input = start_input.lower()
    if start_input == 'start':
        rooms = PlayBoard()
        print('\n\nThe goal is to visit every room\nThere are 9 rooms total')
        print('Use the commands \"Up\", \"Down\", \"Right\", and \"Left\" to move through the rooms')
        print(rooms.room_description(rooms.get_position()))
        visited = []
        visited.append(rooms.get_position)
        while (len(visited) < 9):
            direction = input('Enter a command: ').lower()
            if (direction == 'up'):
                rooms.move_up()
                print(rooms.room_description(rooms.get_position()))
                if rooms.get_position() not in visited:
                    visited.append(rooms.get_position())
            elif (direction == 'down'):
                rooms.move_down()
                print(rooms.room_description(rooms.get_position()))
                if rooms.get_position() not in visited:
                    visited.append(rooms.get_position())
            elif (direction == 'left'):
                rooms.move_left()
                print(rooms.room_description(rooms.get_position()))
                if rooms.get_position() not in visited:
                    visited.append(rooms.get_position())
            elif (direction == 'right'):
                rooms.move_right()
                print(rooms.room_description(rooms.get_position()))
                if rooms.get_position() not in visited:
                    visited.append(rooms.get_position())
            else:
                print('Not a valid command. Please enter: up, down, left, right')
        print('Congrats! You visited every room!')
        again = input('Enter yes to play again: ').lower()
        if again != 'yes':
            play = False
    else:
        break
    play = False
