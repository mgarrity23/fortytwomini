import numpy as np

play = True
while(play):
    print('Welcome to my command line adventure game!')
    start_input = input('Enter \'Start\' to begin: ')
    start_input = start_input.lower()
    if start_input == 'start':
        rooms = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        print(rooms)
        pass
    else:
        break
