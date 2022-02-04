from random import choice

# //////////////////////////////////////////////////////////////////
validation_memory = {
    'dp1': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    'dp2': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    'dp3': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    'dp4': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],

    'bulls1': [],
    'bulls2': [],
    'bulls3': []
}

all_guesses = []
current_guess = []
p1, p2, p3, p4 = 0, 0, 0, 0
S = ''

# //////////////////////////////////////////////////////////////////
# generate new guesses and over time these guesses choices will be
# reduced since we take and implement information from the user
def generate_new_guess():
    global current_guess, S, p1, p2, p3, p4

    p1 = choice(validation_memory['dp1'])
    p2 = choice(validation_memory['dp2'])
    p3 = choice(validation_memory['dp3'])
    p4 = choice(validation_memory['dp4'])

    current_guess = [p1, p2, p3, p4]

    if current_guess in all_guesses:
        generate_new_guess()
    else:
        all_guesses.append(current_guess)
        S = str(p1) + str(p2) + str(p3) + str(p4)


# //////////////////////////////////////////////////////////////////
# find_patterns function try to reduce every position choices
# based on information about bulls and cows it gets from the user
def find_patterns():
    for i in range(0, len(validation_memory['bulls1'])):
        fp1, fp2, fp3, fp4 = validation_memory['bulls1'][i]

        if (fp1 in validation_memory['dp1']
                and fp2 not in validation_memory['dp2']
                and fp3 not in validation_memory['dp3']
                and fp4 not in validation_memory['dp4']
        ):
            validation_memory['dp1'] = [fp1]

        if (fp2 in validation_memory['dp2']
                and fp1 not in validation_memory['dp1']
                and fp3 not in validation_memory['dp3']
                and fp4 not in validation_memory['dp4']
        ):
            validation_memory['dp2'] = [fp2]

        if (fp3 in validation_memory['dp3']
                and fp1 not in validation_memory['dp1']
                and fp2 not in validation_memory['dp2']
                and fp4 not in validation_memory['dp4']
        ):
            validation_memory['dp3'] = [fp3]

        if (fp4 in validation_memory['dp4']
                and fp1 not in validation_memory['dp1']
                and fp2 not in validation_memory['dp2']
                and fp3 not in validation_memory['dp3']
        ):
            validation_memory['dp4'] = [fp4]
    # ---------------------------------------------------------------
    for i in range(0, len(validation_memory['bulls2'])):
        fp1, fp2, fp3, fp4 = validation_memory['bulls2'][i]

        if (fp1 in validation_memory['dp1']
                and fp2 in validation_memory['dp2']
                and fp3 not in validation_memory['dp3']
                and fp4 not in validation_memory['dp4']
        ):
            validation_memory['dp1'] = [fp1]
            validation_memory['dp2'] = [fp2]
        # ---------------------------------------------------
        if (fp1 in validation_memory['dp1']
                and fp3 in validation_memory['dp3']
                and fp2 not in validation_memory['dp2']
                and fp4 not in validation_memory['dp4']
        ):
            validation_memory['dp1'] = [fp1]
            validation_memory['dp3'] = [fp3]
        # ---------------------------------------------------
        if (fp1 in validation_memory['dp1']
                and fp4 in validation_memory['dp4']
                and fp2 not in validation_memory['dp2']
                and fp3 not in validation_memory['dp3']
        ):
            validation_memory['dp1'] = [fp1]
            validation_memory['dp4'] = [fp4]
        # ---------------------------------------------------
        if (fp2 in validation_memory['dp2']
                and fp3 in validation_memory['dp3']
                and fp1 not in validation_memory['dp1']
                and fp4 not in validation_memory['dp4']
        ):
            validation_memory['dp2'] = [fp2]
            validation_memory['dp3'] = [fp3]
        # ---------------------------------------------------
        if (fp2 in validation_memory['dp2']
                and fp4 in validation_memory['dp4']
                and fp1 not in validation_memory['dp1']
                and fp3 not in validation_memory['dp3']
        ):
            validation_memory['dp2'] = [fp2]
            validation_memory['dp4'] = [fp4]
        # ---------------------------------------------------
        if (fp3 in validation_memory['dp3']
                and fp4 in validation_memory['dp4']
                and fp1 not in validation_memory['dp1']
                and fp2 not in validation_memory['dp2']
        ):
            validation_memory['dp3'] = [fp3]
            validation_memory['dp4'] = [fp4]
    # ---------------------------------------------------------------
    for i in range(0, len(validation_memory['bulls3'])):
        fp1, fp2, fp3, fp4 = validation_memory['bulls3'][i]

        if (fp1 not in validation_memory['dp1']
                and fp2 in validation_memory['dp2']
                and fp3 in validation_memory['dp3']
                and fp4 in validation_memory['dp4']
        ):
            validation_memory['dp2'] = [fp2]
            validation_memory['dp3'] = [fp3]
            validation_memory['dp4'] = [fp4]

        if (fp2 not in validation_memory['dp2']
                and fp1 in validation_memory['dp1']
                and fp3 in validation_memory['dp3']
                and fp4 in validation_memory['dp4']
        ):
            validation_memory['dp1'] = [fp1]
            validation_memory['dp3'] = [fp3]
            validation_memory['dp4'] = [fp4]

        if (fp3 not in validation_memory['dp3']
                and fp1 in validation_memory['dp1']
                and fp2 in validation_memory['dp2']
                and fp4 in validation_memory['dp4']
        ):
            validation_memory['dp1'] = [fp1]
            validation_memory['dp2'] = [fp2]
            validation_memory['dp4'] = [fp4]

        if (fp4 not in validation_memory['dp4']
                and fp1 in validation_memory['dp1']
                and fp2 in validation_memory['dp2']
                and fp3 in validation_memory['dp3']
        ):
            validation_memory['dp1'] = [fp1]
            validation_memory['dp2'] = [fp2]
            validation_memory['dp3'] = [fp3]


# //////////////////////////////////////////////////////////////////
for i in range(0, 50):
    # -----------------------------------------------------------------
    generate_new_guess()
    print(S)
    # -----------------------------------------------------------------
    try:
        bulls, cows = map(int, input().split(' '))
    except:
        break
    # -----------------------------------------------------------------
    if bulls + cows > 4:
        break
    if bulls == 4 and cows == 0:
        break
    # -----------------------------------------------------------------
    if bulls == 0:
        validation_memory['dp1'].remove(p1)
        validation_memory['dp2'].remove(p2)
        validation_memory['dp3'].remove(p3)
        validation_memory['dp4'].remove(p4)

    if all(cows == 0, bulls == 0):
        validation_memory['dp1'] = [
            n for n in validation_memory['dp1'] if n not in current_guess]
        validation_memory['dp2'] = [
            n for n in validation_memory['dp2'] if n not in current_guess]
        validation_memory['dp3'] = [
            n for n in validation_memory['dp3'] if n not in current_guess]
        validation_memory['dp4'] = [
            n for n in validation_memory['dp4'] if n not in current_guess]

    if (cows + bulls) == 4:
        validation_memory['dp1'] = [
            n for n in validation_memory['dp1'] if n in current_guess]
        validation_memory['dp2'] = [
            n for n in validation_memory['dp2'] if n in current_guess]
        validation_memory['dp3'] = [
            n for n in validation_memory['dp3'] if n in current_guess]
        validation_memory['dp4'] = [
            n for n in validation_memory['dp4'] if n in current_guess]
    # -----------------------------------------------------------------
    if bulls == 1:
        validation_memory['bulls1'].append(current_guess)
    if bulls == 2:
        validation_memory['bulls2'].append(current_guess)
    if bulls == 3:
        validation_memory['bulls3'].append(current_guess)
    # -----------------------------------------------------------------
    find_patterns()
# End of (0:50) loop
# //////////////////////////////////////////////////////////////////