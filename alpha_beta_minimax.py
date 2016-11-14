

def alpha_beta(node, depth, alpha, beta, maximizer):

    options = get_next(node, maximizer)
    
    if options == []:
        return get_value(node)*(1/(depth+1))
    
    if maximizer==True:
        v = -10000
        for option in options:
            v = max(v, alpha_beta(option, depth + 1, alpha, beta, False))
            alpha = max(alpha, v)
            if beta <= alpha:
                break
        return v
    else:
        v = 100000
        for option in options:
            v = min(v, alpha_beta(option, depth+1, alpha, beta, True))
            beta = min(beta, v)
            if beta <= alpha:
                break
        return v


def print_board(state):
    print(state[0], '|', state[1], '|', state[2])
    print('----------')
    print(state[3], '|', state[4], '|', state[5])
    print('----------')
    print(state[6], '|', state[7], '|', state[8])



def get_next(state, is_o):
    
    if is_o:
        player = 'o'
    else: player = 'x'

    if abs(get_value(state)) == 100:
        return []
    
    #Game Code
    possible_states = []
    for i in range(len(state)):
        if state[i] == ' ':
            new_state = list(state)
            new_state[i] = player
            possible_states.append(new_state)
    
    return(possible_states)

def get_value(state):
    #horizontal win
    i = 0
    for _ in range(3):
        if state[i] == state[i+1] and state[i+1] == state[i+2] and state[i] != ' ':
            if state[i] == 'x':
                return -100
            else: return 100
        i += 3

    #vertical win
    i = 0
    for _ in range(3):
        if state[i] == state[i+3] and state[i] == state[i+6] and state[i] != ' ':
            if state[i] == 'x':
                return -100
            else: return 100
        i += 1

    #diagonal win
    if (state[0] == state[4] and state[0] == state[8] and state[0] != ' ') or (state[2] == state[4] and state[4] == state[6] and state[4] != ' '):
            if state[4] == 'x':
                return -100
            else: return 100

    #else a draw
    return 0
        
def play_game():

    game_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    while True:
        # human move
        print ('########################\n')
        print_board(game_board)
        game_board[int(input("\n Player One Enter Move: \n"))] = 'x'

        # computer move
        options = get_next(game_board, True)
        best_option_score = -10000
        for option in options:
            option_score = alpha_beta(option,0,-1000,1000,False)
            print('alpha-beta: '+str(option_score))
            if option_score > best_option_score:
                game_board = list(option)
                best_option_score = option_score
        if abs(get_value(game_board)) == 100:
            break

keep_playing = True
while keep_playing:
    play_game()
    
    if input(print('########################\n Play Again? y/n \n')) == 'n':
        break

