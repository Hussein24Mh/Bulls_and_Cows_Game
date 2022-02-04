from random import choice
# //////////////////////////////////////////////////////////////////
Ap1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Ap2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Ap3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Ap4 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Bulls_1 = []
Bulls_2 = []
Bulls_3 = []

All_Guesses = []
Current_Guess = []
p1, p2, p3, p4 = 0, 0, 0, 0
S = ''
loop_flag = 1
# //////////////////////////////////////////////////////////////////
def Generate_New_Guess():
    """
    generate new guesses and over time these guesses choices will be
    reduced since we take and implement information from the user
    :rtype: list
    """
    global Current_Guess, S, p1, p2, p3, p4

    p1 = choice(Ap1)
    p2 = choice(Ap2)
    p3 = choice(Ap3)
    p4 = choice(Ap4)

    Current_Guess = [p1, p2, p3, p4]

    if Current_Guess in All_Guesses:
        Generate_New_Guess()
    else:
        All_Guesses.append(Current_Guess)
        S = str(p1) + str(p2) + str(p3) + str(p4)
# //////////////////////////////////////////////////////////////////
def Try_Reduce_Choices():
    """
    # find_patterns function try to reduce every position choices
    # based on information about bulls and cows it gets from the user
    :return: Nothing
    """
    global Ap1, Ap2, Ap3, Ap4

    for i1 in range(0, len(Bulls_1)):
        fp1, fp2, fp3, fp4 = Bulls_1[i1]
# ------------------------------------------ 1
        if all([fp1 in Ap1,
                fp2 not in Ap2,
                fp3 not in Ap3,
                fp4 not in Ap4
                ]):
            Ap1 = [fp1]
# ------------------------------------------ 2
        elif all([fp2 in Ap2,
                  fp1 not in Ap1,
                  fp3 not in Ap3,
                  fp4 not in Ap4
                  ]):
            Ap2 = [fp2]
# ------------------------------------------ 3
        elif all([fp3 in Ap3,
                  fp1 not in Ap1,
                  fp2 not in Ap2,
                  fp4 not in Ap4
                  ]):
           Ap3 = [fp3]
# ------------------------------------------ 4
        elif all([fp4 in Ap4,
                  fp1 not in Ap1,
                  fp2 not in Ap2,
                  fp3 not in Ap3
                  ]):
            Ap4 = [fp4]
# ---------------------------------------------------------------
    for i2 in range(0, len(Bulls_2)):
        fp1, fp2, fp3, fp4 = Bulls_2[i2]
# ------------------------------------------ 1&2
        if all([fp1 in Ap1,
                fp2 in Ap2,
                fp3 not in Ap3,
                fp4 not in Ap4
                ]):
            Ap1 = [fp1]
            Ap2 = [fp2]
# ------------------------------------------ 1&3
        elif all([fp1 in Ap1,
                  fp3 in Ap3,
                  fp2 not in Ap2,
                  fp4 not in Ap4
                  ]):
            Ap1 = [fp1]
            Ap3 = [fp3]
# ------------------------------------------ 1&4
        elif all([fp1 in Ap1,
                  fp4 in Ap4,
                  fp2 not in Ap2,
                  fp3 not in Ap3
                  ]):
            Ap1 = [fp1]
            Ap4 = [fp4]
# ------------------------------------------ 2&3
        elif all([fp2 in Ap2,
                  fp3 in Ap3,
                  fp1 not in Ap1,
                  fp4 not in Ap4
                  ]):
            Ap2 = [fp2]
            Ap3 = [fp3]
# ------------------------------------------ 2&4
        elif all([fp2 in Ap2,
                  fp4 in Ap4,
                  fp1 not in Ap1,
                  fp3 not in Ap3
                  ]):
            Ap2 = [fp2]
            Ap4 = [fp4]
# ------------------------------------------ 3&4
        elif all([fp3 in Ap3,
                  fp4 in Ap4,
                  fp1 not in Ap1,
                  fp2 not in Ap2
                  ]):
            Ap3 = [fp3]
            Ap4 = [fp4]
# ---------------------------------------------------------------
    for i3 in range(0, len(Bulls_3)):
        fp1, fp2, fp3, fp4 = Bulls_3[i3]
# ------------------------------------------ 2&3&4
        if all([fp1 not in Ap1,
                fp2 in Ap2,
                fp3 in Ap3,
                fp4 in Ap4
                ]):
            Ap2 = [fp2]
            Ap3 = [fp3]
            Ap4 = [fp4]
# ------------------------------------------ 1&3&4
        elif all([fp2 not in Ap2,
                  fp1 in Ap1,
                  fp3 in Ap3,
                  fp4 in Ap4
                  ]):
            Ap1 = [fp1]
            Ap3 = [fp3]
            Ap4 = [fp4]
# ------------------------------------------ 1&2&4
        elif all([fp3 not in Ap3,
                  fp1 in Ap1,
                  fp2 in Ap2,
                  fp4 in Ap4
                  ]):
            Ap1 = [fp1]
            Ap2 = [fp2]
            Ap4 = [fp4]
# ------------------------------------------ 1&2&3
        elif all([fp4 not in Ap4,
                  fp1 in Ap1,
                  fp2 in Ap2,
                  fp3 in Ap3
                  ]):
            Ap1 = [fp1]
            Ap2 = [fp2]
            Ap3 = [fp3]
# //////////////////////////////////////////////////////////////////
while True:
    # -----------------------------------------------------------------
    Generate_New_Guess()
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
    # -----------------------------------------------------------------
    Try_Reduce_Choices()
    loop_flag += 1
# End of while loop
# ///////////////////////////////////////////////////////////////////////////
