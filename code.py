from random import choice

Ap1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # All current choices in position 1
Ap2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # All current choices in position 2
Ap3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # All current choices in position 3
Ap4 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # All current choices in position 4

Bulls_1 = []  # All guesses with 1 Bull
Bulls_2 = []  # All guesses with 2 Bull
Bulls_3 = []  # All guesses with 3 Bull

Bulls_1_Cows_0 = []  # All guesses with 1 Bull and 0 Cows
Bulls_2_Cows_0 = []  # All guesses with 2 Bull and 0 Cows
Bulls_3_Cows_0 = []  # All guesses with 3 Bull and 0 Cows

All_Guesses = []  # All guesses over time to prevent generate the same Guess
Current_Guess = []  # current generated guess
p1, p2, p3, p4 = 0, 0, 0, 0  # each position guess
S = ''  # the guess as string variable to print it
loop_flag = 1  # loop counter

Len_Ap1 = 10  # len(Ap1)
Len_Ap2 = 10  # len(Ap2)
Len_Ap3 = 10  # len(Ap3)
Len_Ap4 = 10  # len(Ap4)

Final_Ap1 = False  # True only if len(Ap1) == 1
Final_Ap2 = False  # True only if len(Ap2) == 1
Final_Ap3 = False  # True only if len(Ap3) == 1
Final_Ap4 = False  # True only if len(Ap4) == 1


def update_lens():
    global Len_Ap1, Len_Ap2, Len_Ap3, Len_Ap4
    global Final_Ap1, Final_Ap2, Final_Ap3, Final_Ap4
    Len_Ap1 = len(Ap1)
    Len_Ap2 = len(Ap2)
    Len_Ap3 = len(Ap3)
    Len_Ap4 = len(Ap4)

    Final_Ap1 = True if Len_Ap1 == 1 else False
    Final_Ap2 = True if Len_Ap2 == 1 else False
    Final_Ap3 = True if Len_Ap3 == 1 else False
    Final_Ap4 = True if Len_Ap4 == 1 else False


def any_update_happen():
    local_len_ap1 = len(Ap1)
    local_len_ap2 = len(Ap2)
    local_len_ap3 = len(Ap3)
    local_len_ap4 = len(Ap4)

    if any([
        local_len_ap1 < Len_Ap1,
        local_len_ap2 < Len_Ap2,
        local_len_ap3 < Len_Ap3,
        local_len_ap4 < Len_Ap4
    ]):
        return True


def generate_new_guess():
    """
    generate new guesses and over time these guesses choices will be
    reduced since we take information from the user and make implementation
    on them
    """
    global Current_Guess, S, p1, p2, p3, p4

    p1 = choice(Ap1)
    p2 = choice(Ap2)
    p3 = choice(Ap3)
    p4 = choice(Ap4)

    Current_Guess = [p1, p2, p3, p4]

    if Current_Guess in All_Guesses:
        generate_new_guess()
    else:
        All_Guesses.append(Current_Guess)
        S = str(p1) + str(p2) + str(p3) + str(p4)


def try_reduce_choices_if_final_true():
    update_lens()
    if Final_Ap1:
        if Ap1[0] in Ap2: Ap2.remove(Ap1[0])
        if Ap1[0] in Ap3: Ap3.remove(Ap1[0])
        if Ap1[0] in Ap4: Ap4.remove(Ap1[0])
    if Final_Ap2:
        if Ap2[0] in Ap1: Ap1.remove(Ap2[0])
        if Ap2[0] in Ap3: Ap3.remove(Ap2[0])
        if Ap2[0] in Ap4: Ap4.remove(Ap2[0])
    if Final_Ap3:
        if Ap3[0] in Ap1: Ap1.remove(Ap3[0])
        if Ap3[0] in Ap2: Ap2.remove(Ap3[0])
        if Ap3[0] in Ap4: Ap4.remove(Ap3[0])
    if Final_Ap4:
        if Ap4[0] in Ap1: Ap1.remove(Ap4[0])
        if Ap4[0] in Ap2: Ap2.remove(Ap4[0])
        if Ap4[0] in Ap3: Ap3.remove(Ap4[0])
    return any_update_happen()


def try_reduce_choices_if_cows_0():
    update_lens()
    for b1 in range(0, len(Bulls_1_Cows_0)):
        fp1, fp2, fp3, fp4 = Bulls_1_Cows_0[b1]
        if Final_Ap1 and Ap1[0] == fp1:
            if fp2 in Ap2: Ap2.remove(fp2)
            if fp3 in Ap3: Ap3.remove(fp3)
            if fp4 in Ap4: Ap4.remove(fp4)
        if Final_Ap2 and Ap2[0] == fp2:
            if fp1 in Ap1: Ap1.remove(fp1)
            if fp3 in Ap3: Ap3.remove(fp3)
            if fp4 in Ap4: Ap4.remove(fp4)
        if Final_Ap3 and Ap3[0] == fp3:
            if fp1 in Ap1: Ap1.remove(fp1)
            if fp2 in Ap2: Ap2.remove(fp2)
            if fp4 in Ap4: Ap4.remove(fp4)
        if Final_Ap4 and Ap4[0] == fp4:
            if fp1 in Ap1: Ap1.remove(fp1)
            if fp2 in Ap2: Ap2.remove(fp2)
            if fp3 in Ap3: Ap3.remove(fp3)

    for b2 in range(0, len(Bulls_2_Cows_0)):
        fp1, fp2, fp3, fp4 = Bulls_2_Cows_0[b2]
        if all([Final_Ap1, Final_Ap2, Ap1[0] == fp1, Ap2[0] == fp2]):
            if fp3 in Ap3: Ap3.remove(fp3)
            if fp4 in Ap4: Ap4.remove(fp4)
        if all([Final_Ap1, Final_Ap3, Ap1[0] == fp1, Ap3[0] == fp3]):
            if fp2 in Ap2: Ap2.remove(fp2)
            if fp4 in Ap4: Ap4.remove(fp4)
        if all([Final_Ap1, Final_Ap4, Ap1[0] == fp1, Ap4[0] == fp4]):
            if fp2 in Ap2: Ap2.remove(fp2)
            if fp3 in Ap3: Ap3.remove(fp3)
        if all([Final_Ap2, Final_Ap3, Ap2[0] == fp2, Ap3[0] == fp3]):
            if fp1 in Ap1: Ap1.remove(fp1)
            if fp4 in Ap4: Ap4.remove(fp4)
        if all([Final_Ap2, Final_Ap4, Ap2[0] == fp2, Ap4[0] == fp4]):
            if fp1 in Ap1: Ap1.remove(fp1)
            if fp3 in Ap3: Ap3.remove(fp3)
        if all([Final_Ap3, Final_Ap4, Ap3[0] == fp3, Ap4[0] == fp4]):
            if fp1 in Ap1: Ap1.remove(fp1)
            if fp2 in Ap2: Ap2.remove(fp2)

    for b3 in range(0, len(Bulls_3_Cows_0)):
        fp1, fp2, fp3, fp4 = Bulls_3_Cows_0[b3]
        if all([Final_Ap1, Final_Ap2, Final_Ap3,
                Ap1[0] == fp1, Ap2[0] == fp2, Ap3[0] == fp3
                ]):
            if fp4 in Ap4: Ap4.remove(fp4)
        if all([Final_Ap1, Final_Ap2, Final_Ap4,
                Ap1[0] == fp1, Ap2[0] == fp2, Ap4[0] == fp4
                ]):
            if fp3 in Ap3: Ap3.remove(fp3)
        if all([Final_Ap1, Final_Ap3, Final_Ap4,
                Ap1[0] == fp1, Ap3[0] == fp3, Ap4[0] == fp4
                ]):
            if fp2 in Ap2: Ap2.remove(fp2)
        if all([Final_Ap2, Final_Ap3, Final_Ap4,
                Ap2[0] == fp2, Ap3[0] == fp3, Ap4[0] == fp4
                ]):
            if fp1 in Ap1: Ap1.remove(fp1)

    return any_update_happen()


def try_reduce_choices():
    """
    find_patterns function try to reduce every position choices
    based on information about bulls and cows it gets from the user
    """
    update_lens()
    global Ap1, Ap2, Ap3, Ap4

    for i1 in range(0, len(Bulls_1)):  # Bulls_1
        fp1, fp2, fp3, fp4 = Bulls_1[i1]

        if all([fp1 in Ap1,
                fp2 not in Ap2,
                fp3 not in Ap3,
                fp4 not in Ap4
                ]):
            Ap1 = [fp1]  # 1

        elif all([fp2 in Ap2,
                  fp1 not in Ap1,
                  fp3 not in Ap3,
                  fp4 not in Ap4
                  ]):
            Ap2 = [fp2]  # 2

        elif all([fp3 in Ap3,
                  fp1 not in Ap1,
                  fp2 not in Ap2,
                  fp4 not in Ap4
                  ]):
            Ap3 = [fp3]  # 3

        elif all([fp4 in Ap4,
                  fp1 not in Ap1,
                  fp2 not in Ap2,
                  fp3 not in Ap3
                  ]):
            Ap4 = [fp4]  # 4

    for i2 in range(0, len(Bulls_2)):  # Bulls_2
        fp1, fp2, fp3, fp4 = Bulls_2[i2]

        if all([fp1 in Ap1,
                fp2 in Ap2,
                fp3 not in Ap3,
                fp4 not in Ap4
                ]):
            Ap1 = [fp1]
            Ap2 = [fp2]  # 1&2

        elif all([fp1 in Ap1,
                  fp3 in Ap3,
                  fp2 not in Ap2,
                  fp4 not in Ap4
                  ]):
            Ap1 = [fp1]
            Ap3 = [fp3]  # 1&3

        elif all([fp1 in Ap1,
                  fp4 in Ap4,
                  fp2 not in Ap2,
                  fp3 not in Ap3
                  ]):
            Ap1 = [fp1]
            Ap4 = [fp4]  # 1&4

        elif all([fp2 in Ap2,
                  fp3 in Ap3,
                  fp1 not in Ap1,
                  fp4 not in Ap4
                  ]):
            Ap2 = [fp2]
            Ap3 = [fp3]  # 2&3

        elif all([fp2 in Ap2,
                  fp4 in Ap4,
                  fp1 not in Ap1,
                  fp3 not in Ap3
                  ]):
            Ap2 = [fp2]
            Ap4 = [fp4]  # 2&4

        elif all([fp3 in Ap3,
                  fp4 in Ap4,
                  fp1 not in Ap1,
                  fp2 not in Ap2
                  ]):
            Ap3 = [fp3]
            Ap4 = [fp4]  # 3&4

    for i3 in range(0, len(Bulls_3)):  # Bulls_3
        fp1, fp2, fp3, fp4 = Bulls_3[i3]

        if all([fp1 not in Ap1,
                fp2 in Ap2,
                fp3 in Ap3,
                fp4 in Ap4
                ]):
            Ap2 = [fp2]
            Ap3 = [fp3]
            Ap4 = [fp4]  # 2&3&4

        elif all([fp2 not in Ap2,
                  fp1 in Ap1,
                  fp3 in Ap3,
                  fp4 in Ap4
                  ]):
            Ap1 = [fp1]
            Ap3 = [fp3]
            Ap4 = [fp4]  # 1&3&4

        elif all([fp3 not in Ap3,
                  fp1 in Ap1,
                  fp2 in Ap2,
                  fp4 in Ap4
                  ]):
            Ap1 = [fp1]
            Ap2 = [fp2]
            Ap4 = [fp4]  # 1&2&4

        elif all([fp4 not in Ap4,
                  fp1 in Ap1,
                  fp2 in Ap2,
                  fp3 in Ap3
                  ]):
            Ap1 = [fp1]
            Ap2 = [fp2]
            Ap3 = [fp3]  # 1&2&3
    return any_update_happen()


while True:

    generate_new_guess()
    bulls, cows = 0, 0
    print(f'Guess -> {loop_flag} is {S}')

    print(f'Enter Bulls Number ->>>', end=" ")
    while True:
        try:
            x = int(input())
            if not (0 <= x <= 4):
                print("Please enter integer between 0 and 4")
                continue
        except:
            print("please enter integer")
        else:
            bulls = x
            break

    print(f'Enter Cows Number ->>>', end=" ")
    while True:
        try:
            x = int(input())
            if not (0 <= x + bulls <= 4):
                print(
                    "Please enter integer between 0 and 4 and bulls "
                    "and cows together between 0 and 4"
                )
                continue
        except:
            print("please enter integer")
        else:
            cows = x
            break

    if bulls == 4:
        print("End Of Game :GG")
        print('press any to exit')
        input()
        break
    # -----------------------------------------------------------------
    if bulls == 0:
        Ap1.remove(p1)
        Ap2.remove(p2)
        Ap3.remove(p3)
        Ap4.remove(p4)

    if cows == 0 and bulls == 0:
        Ap1 = [n for n in Ap1 if n not in Current_Guess]
        Ap2 = [n for n in Ap2 if n not in Current_Guess]
        Ap3 = [n for n in Ap3 if n not in Current_Guess]
        Ap4 = [n for n in Ap4 if n not in Current_Guess]

    if (cows + bulls) == 4:
        Ap1 = [n for n in Ap1 if n in Current_Guess]
        Ap2 = [n for n in Ap2 if n in Current_Guess]
        Ap3 = [n for n in Ap3 if n in Current_Guess]
        Ap4 = [n for n in Ap4 if n in Current_Guess]
    # -----------------------------------------------------------------
    if bulls == 1:
        Bulls_1.append(Current_Guess)
    elif bulls == 2:
        Bulls_2.append(Current_Guess)
    elif bulls == 3:
        Bulls_3.append(Current_Guess)

    if bulls == 1 and cows == 0:
        Bulls_1_Cows_0.append(Current_Guess)
    elif bulls == 2 and cows == 0:
        Bulls_2_Cows_0.append(Current_Guess)
    elif bulls == 3 and cows == 0:
        Bulls_3_Cows_0.append(Current_Guess)
    # -----------------------------------------------------------------
    while any([try_reduce_choices_if_final_true(),
               try_reduce_choices_if_cows_0(),
               try_reduce_choices()
               ]):
        pass
    loop_flag += 1
# End of while loop
