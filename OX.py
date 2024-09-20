# ox array
arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
arr3 = [7, 8, 9]
player = 'x'


#check x
def checkgridX(arr1, arr2, arr3):
    x = "x"
    if ((arr1[0] == x and arr2[0] == x and arr3[0] == x) or # Column 1
        (arr1[1] == x and arr2[1] == x and arr3[1] == x) or # Column 2
        (arr1[2] == x and arr2[2] == x and arr3[2] == x) or # Column 3
        (arr1[0] == x and arr1[1] == x and arr1[2] == x) or # Row 1
        (arr2[0] == x and arr2[1] == x and arr2[2] == x) or # Row 2
        (arr3[0] == x and arr3[1] == x and arr3[2] == x) or # Row 3
        (arr1[0] == x and arr2[1] == x and arr3[2] == x) or # Diagonal 1
        (arr1[2] == x and arr2[1] == x and arr3[0] == x)):    # Diagonal 2
        return True
    else:
        return False
    
#check o
def checkgridO(arr1, arr2, arr3):
    o = "o"
    if ((arr1[0] == o and arr2[0] == o and arr3[0] == o) or # Column 1
        (arr1[1] == o and arr2[1] == o and arr3[1] == o) or # Column 2
        (arr1[2] == o and arr2[2] == o and arr3[2] == o) or # Column 3
        (arr1[0] == o and arr1[1] == o and arr1[2] == o) or # Row 1
        (arr2[0] == o and arr2[1] == o and arr2[2] == o) or # Row 2
        (arr3[0] == o and arr3[1] == o and arr3[2] == o) or # Row 3
        (arr1[0] == o and arr2[1] == o and arr3[2] == o) or # Diagonal 1
        (arr1[2] == o and arr2[1] == o and arr3[0] == o)):    # Diagonal 2
        return True
    else:
        return False
#check game complete
def gameComplete(arr1, arr2 ,arr3):
    if ((arr1[0] != 1) and (arr1[1] != 2) and (arr1[2] != 3) and
        (arr2[0] != 4) and (arr2[1] != 5) and (arr2[2] != 6) and
        (arr3[0] != 7) and (arr3[1] != 8) and (arr3[2] != 9)):
        return True
    else: 
        return False
    
#tie check
def checkTie(arr1, arr2, arr3):
    if (checkgridX(arr1, arr2, arr3) == False) and (checkgridX(arr1, arr2, arr3) == False) and (gameComplete(arr1, arr2, arr3) == True):
        return True
    else:
        return False

    
#print(checkgridX(arr1, arr2, arr3))
#print(checkgridO(arr1, arr2, arr3))


input("PRESS ENTER TO START:    ")


# user input value and check
def arrValueCheck():
    playerInput = False
    while playerInput == False:
        gameInput = int(input("player " + player + " pick number between 1-9: "))
        
        if gameInput in [ 1, 2, 3]:
            arrCheck = gameInput - 1
            if arr1[arrCheck] in ["x", "o"]:
                print("That has is already occupied by " + str(arr1[arrCheck])+ " please try again")
            else:
                arrValueChange(gameInput)
                playerInput = True
        elif gameInput in [ 4, 5, 6]:
            arrCheck = gameInput - 4
            if arr2[arrCheck] in ["x", "o"]:
                print("That has is already occupied by " + str(arr2[arrCheck])+ " please try again")
            else:
                arrValueChange(gameInput)
                playerInput = True
        elif gameInput in [ 7, 8, 9]:
            arrCheck = gameInput - 7
            if arr3[arrCheck] in ["x", "o"]:
                print("That has is already occupied by " + str(arr3[arrCheck])+ " please try again")
            else:
                arrValueChange(gameInput)
                playerInput = True
        else:
            print("error")

#Change value to user input
def arrValueChange(gameInput):
    if gameInput in [ 1, 2, 3]:
        arrChange = gameInput - 1
        arr1[arrChange] = player
    elif gameInput in [ 4, 5, 6]:
        arrChange = gameInput - 4
        arr2[arrChange] = player
    elif gameInput in [ 7, 8, 9]:
        arrChange = gameInput - 7
        arr3[arrChange] = player
    else:
        print("error")


#start game user input
i = 0
while i < 2:
    print(i)
    # player check
    if i == 0:
        player = "x"
    elif i == 1:
        player = "o"
    else: 
        break
    print(arr1)
    print(arr2)
    print(arr3)

    #gameInput = int(input("player " + player + "pick number between 1-9: "))
    arrValueCheck()
    #if wins stop else contine
    if player == "x":
         if checkgridX(arr1, arr2, arr3) == True:
            print("X wins")
            i = 2
         elif checkTie(arr1, arr2, arr3) == True:
            print("The game is a tie")
            i = 2
         else:
            i = 1
    elif player == "o":
         if checkgridO(arr1, arr2, arr3) == True:
            print("O wins")
            i = 2
         elif checkTie(arr1, arr2, arr3) == True:
            print("The game is a tie")
            i = 2
         else:
            i = 0
    else:
        i = 2




    