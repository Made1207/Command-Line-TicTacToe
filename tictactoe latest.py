def tictactoe():
    player1 = input('Player 1, enter your name: ')
    player2 = input('Player 2, enter your name: ')

    print('1', '|', '2','|', '3')
    print('-', '+', '-', '+', '-')
    print('4','|', '5', '|', '6')
    print('-', '+', '-', '+', '-')
    print('7','|', '8', '|', '9')

    list1 = ['1', '2', '3']
    list2 = ['4', '5', '6']
    list3 = ['7', '8', '9']
    list4 = ['1', '4', '7']
    list5 = ['2', '5', '8']
    list6 = ['3', '6', '9']
    list7 = ['1', '5', '9']
    list8 = ['3', '5', '7']

    row1 = ['1', '2', '3']
    row2 = ['4', '5', '6']
    row3 = ['7', '8', '9']

    loop01 = 60 < 120
    loop02 = 60 < 3
    condition = 90 < 50
    index = 1
    p1 = []
    p2 = []
    options = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    while loop01 == True:
        index = index + 1
        print(p1)
        print(p2)
        if index % 2 == 0:
            condition = True
            player = player1
        else:
            condition = False
            player = player2

        print(player + ', it is your turn')
        user_input = input('Pick a number to play in that positon: ')
        loop02 = True

        if loop02 == True:
            if condition == True:
                p1.append(user_input)
            elif condition == False:
                p2.append(user_input)

        if len(p1) + len(p2) == 9:
            print('It is a draw.')
            loop01 = False

        if condition == True:
            for item in p2:
                if item in p1:
                    user_input = input('This position is taken. Try again: ')
                    p1.remove(item)
                    loop02 = False
                    loop02 = True
                else:
                    loop02 = False
        elif condition == False:
            for item in p1:
                if item in p2:
                    user_input = input('This position is taken. Try again: ')
                    p2.remove(item)
                    loop02 = False
                    loop02 = True
                else:
                    loop02 = False

        if user_input in options:
            pos = options.index(user_input)
            if pos == 6 or pos < 9 and pos > 5:
                if condition == True:
                    row3[pos - 6] = 'X'
                elif condition == False:
                    row3[pos - 6] = 'O'
            elif pos == 2 or pos < 2:
                if condition == True:
                    row1[pos] = 'X'
                elif condition == False:
                    row1[pos] = 'O'
            elif pos == 5 or pos < 5 and pos > 2:
                if condition == True:
                    row2[pos - 3] = 'X'
                elif condition == False:
                    row2[pos - 3] = 'O'

        print(' | '.join(row1))
        print('-', '+', '-', '+', '-')
        print(' | '.join(row2))
        print('-', '+', '-', '+', '-')
        print(' | '.join(row3))

        if list1[0] in p1 and list1[1] in p1 and list1[2] in p1:
            print(player1, 'won')
            loop01 = False
        if list1[0] in p2 and list1[1] in p2 and list1[2] in p2:
            print(player2, 'won!')
            loop01 = False
        if list2[0] in p1 and list2[1] in p1 and list2[2] in p1:
            print(player1, 'won')
            loop01 = False
        if list2[0] in p2 and list2[1] in p2 and list2[2] in p2:
            print(player2, 'won!')
            loop01 = False
        if list3[0] in p1 and list3[1] in p1 and list3[2] in p1:
            print(player1, 'won')
            loop01 = False
        if list3[0] in p1 and list3[1] in p2 and list3[2] in p2:
            print(player2, 'won!')
            loop01 = False
        if list4[0] in p1 and list4[1] in p1 and list4[2] in p1:
            print(player1, 'won')
            loop01 = False
        if list4[0] in p2 and list4[1] in p2 and list4[2] in p2:
            print(player2, 'won!')
            loop01 = False
        if list5[0] in p1 and list5[1] in p1 and list5[2] in p1:
            print(player1, 'won')
            loop01 = False
        if list5[0] in p2 and list5[1] in p2 and list5[2] in p2:
            print(player2, 'won!')
            loop01 = False
        if list6[0] in p1 and list6[1] in p1 and list6[2] in p1:
            print(player1, 'won')
            loop01 = False
        if list6[0] in p2 and list6[1] in p2 and list6[2] in p2:
            print(player2, 'won!')
            loop01 = False
        if list7[0] in p1 and list7[1] in p1 and list7[2] in p1:
            print(player1, 'won')
            loop01 = False
        if list7[0] in p2 and list7[1] in p2 and list7[2] in p2:
            print(player2, 'won!')
            loop01 = False
        if list8[0] in p1 and list8[1] in p1 and list8[2] in p1:
            print(player1, 'won')
            loop01 = False
        if list8[0] in p2 and list8[1] in p2 and list8[2] in p2:
            print(player2, 'won!')
            loop01 = False

tictactoe()