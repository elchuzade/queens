# making an action state
def make_action_state(general_state, action_state):
    action_state = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for entry in general_state:
        index = general_state.index(entry)
        action_state[index] = entry[2]
    return action_state
# finding if there is any value on the right of the curent step
def row_E(variable, action_state):
    status = 0
    i = variable[0]
    j = variable[1]
    while j < 3:
        j += 1
        index = i*4 + j
        if action_state[index] == 1:
            status = 1
            return status
    return status
# finding if there is any value on the left of the curent step
def row_W(variable, action_state):
    status = 0
    i = variable[0]
    j = variable[1]
    while j > 0:
        j -= 1
        index = i*4 + j
        if action_state[index] == 1:
            status = 1
            return status
    return status
# finding if there is any value above of the curent step
def col_N(variable, action_state):
    status = 0
    i = variable[0]
    j = variable[1]
    while i > 0:
        i -= 1
        index = i*4 + j
        if action_state[index] == 1:
            status = 1
            return status
    return status
# finding if there is any value below of the curent step
def col_S(variable, action_state):
    status = 0
    i = variable[0]
    j = variable[1]
    while i < 3:
        i += 1
        index = i*4 + j
        if action_state[index] == 1:
            status = 1
            return status
    return status
# finding if there is any value right above diagonal of the curent step
def diag_NE(variable, action_state):
    status = 0
    i = variable[0]
    j = variable[1]
    while i>0 and j<3:
        i -= 1
        j += 1
        index = i*4 + j
        if action_state[index] == 1:
            status = 1
            return status
    return status
# finding if there is any value left below diagonal of the curent step
def diag_SW(variable, action_state):
    status = 0
    i = variable[0]
    j = variable[1]
    while i<3 and j>0:
        i += 1
        j -= 1
        index = i*4 + j
        if action_state[index] == 1:
            status = 1
            return status
            print('i and j', i)
    return status
# finding if there is any value right below diagonal of the curent step
def diag_SE(variable, action_state):
    status = 0
    i = variable[0]
    j = variable[1]
    while i<3 and j<3:
        i += 1
        j += 1
        index = i*4 + j
        if action_state[index] == 1:
            status = 1
            return status
    return status
# finding if there is any value left above diagonal of the curent step
def diag_NW(variable, action_state):
    status = 0
    i = variable[0]
    j = variable[1]
    while i>0 and j>0:
        i -= 1
        j -= 1
        index = i*4 + j
        if action_state[index] == 1:
            status = 1
            return status
    return status
# checking all of the constrains in a single function
def constrains(variable, action_state, general_state):
    row_e,row_w,col_n,col_s,diag_ne,diag_sw,diag_se,diag_nw = 0,0,0,0,0,0,0,0
    row_e = row_E(variable, action_state)
    row_w = row_W(variable, action_state)
    col_n = col_N(variable, action_state)
    col_s = col_S(variable, action_state)
    diag_ne = diag_NE(variable, action_state)
    diag_sw = diag_SW(variable, action_state)
    diag_se = diag_SE(variable, action_state)
    diag_nw = diag_NW(variable, action_state)
    if row_e==0 and row_w==0 and col_n==0 and col_s==0 and diag_ne==0 and diag_nw==0 and diag_se==0 and diag_sw==0:
        ind = general_state.index(variable)
        variable[2] = 1
        general_state[ind] = variable
        action_state = make_action_state(general_state, action_state)
        return action_state
    return action_state
# checking if there is any row left without a queen during iteration to force stop the program
def row_check(variable, action_state):
    x = 1
    i = variable[0]
    j = variable[1]
    ij = i*4 + j
    if ij == 3:
        x = sum(action_state[0:4])
        return x
    elif ij == 7:
        x = sum(action_state[4:8])
        return x
    elif ij == 11:
        x = sum(action_state[8:12])
        return x
    elif ij == 15:
        x = sum(action_state[12:16])
        return x
    else:
        return x
# checking if at each state I have reached the goal or not
def check_result(action_state):
    status = 0
    result = sum(action_state)
    if result == 4:
        status = 1
        return status
# printing out the board in a more easier to read way
def fancy_output(action_state):
    print(action_state[0],action_state[1],action_state[2],action_state[3])
    print(action_state[4],action_state[5],action_state[6],action_state[7])
    print(action_state[8],action_state[9],action_state[10],action_state[11])
    print(action_state[12],action_state[13],action_state[14],action_state[15])

def main():
    result = 0
    general_state = []
    variable = []
    answer = 0
    action_state = []
    action_state = make_action_state(general_state, action_state)
    jump = 0
    while jump < 4:
        general_state = [[0,0,0],[0,1,0],[0,2,0],[0,3,0],[1,0,0],[1,1,0],[1,2,0],
        [1,3,0],[2,0,0],[2,1,0],[2,2,0],[2,3,0],[3,0,0],[3,1,0],[3,2,0],[3,3,0]]
        for variable in general_state[jump:]:
            checkup = 0
            action_state = make_action_state(general_state, action_state)
            action_state = constrains(variable, action_state, general_state)
            i = variable[0]
            j = variable[1]
            ij = i*4 + j
            checkup = row_check(variable, action_state)
            if checkup == 0:
                print("Sorry, I couldn't fit 4 Queens in 4x4 board")
                print('\n')
                break
        result = check_result(action_state)
        if result == 1:
            print('congratulations', action_state)
            print('\n')
            fancy_output(action_state)
            print('\n')
        jump += 1


main()
