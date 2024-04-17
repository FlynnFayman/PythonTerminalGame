
#The function change Grid
GridForInput = {'RowOne' : "A|B|C", 'Rowtwo' : "D|E|F",'Rowthree' : "G|H|I"}

#Function to accept Players input and change GridForInput
def ChangeGrid(Alpha,Stats,Row):
    if Stats == "Player0":
        GridForInput[Row] = GridForInput[Row].replace(Alpha,"0")
    else:
        GridForInput[Row] = GridForInput[Row].replace(Alpha,"X")

#A function to Translate Row number into letters

def NumToAlpha(PR,PC):
    if PR == 1 and PC == 1:
        return ("A", "RowOne")
    elif(PR == 1 and PC == 2):
        return ("B", "RowOne")
    elif(PR == 1 and PC == 3):
        return ("C", "RowOne")
    elif(PR == 2 and PC == 1):
        return ("D", "Rowtwo")
    elif(PR == 2 and PC == 2):
        return ("E", "Rowtwo")
    elif(PR == 2 and PC == 3):
        return ("F", "Rowtwo")
    elif(PR == 3 and PC == 1):
        return ("G", "Rowthree")
    elif(PR == 3 and PC == 2):
        return ("H", "Rowthree")
    elif(PR == 3 and PC == 3):
        return ("I", "Rowthree")
    else:
        print("Enter a worng number the program has stop")
        exit()



#Draw Condtion
def GridToGrid():
    DGrid = GridForInput.copy()
    for key in DGrid.keys():
        DGrid[key] = DGrid[key].replace("A","_")
        DGrid[key] = DGrid[key].replace("B","_")
        DGrid[key] = DGrid[key].replace("C","_")
        DGrid[key] = DGrid[key].replace("D","_")
        DGrid[key] = DGrid[key].replace("E","_")
        DGrid[key] = DGrid[key].replace("F","_")
        DGrid[key] = DGrid[key].replace("G","_")
        DGrid[key] = DGrid[key].replace("H","_")
        DGrid[key] = DGrid[key].replace("I","_")
    return DGrid


#Function To display Grid for Tick Tac Toe

def WinSat(IGrid):
    winForO = ['0|0|0','000']
    winForX = ['X|X|X','XXX']
    #rows of the Tick Tac Toe grid
    row1 = IGrid['RowOne']
    row2 = IGrid['Rowtwo']
    row3 = IGrid['Rowthree']
    #The columns of the tick tack toe Grid
    col1 = IGrid['RowOne'][0] + IGrid['Rowtwo'][0] + IGrid['Rowthree'][0]
    col2 = IGrid['RowOne'][2] + IGrid['Rowtwo'][2] + IGrid['Rowthree'][2] 
    col3 = IGrid['RowOne'][-1] + IGrid['Rowtwo'][-1] + IGrid['Rowthree'][-1]
    #Dieangelo
    die1 = IGrid['RowOne'][-1] + IGrid['Rowtwo'][2] + IGrid['Rowthree'][0]
    die2 = IGrid['RowOne'][0] + IGrid['Rowtwo'][2] + IGrid['Rowthree'][-1]
    #All  Sum of copy grid
    Dgrid = GridToGrid()
    SumAll = Dgrid['RowOne'] + Dgrid['Rowtwo'] + Dgrid['Rowthree']
    if((row1 in winForO) or (row2 in winForO) or (row3 in winForO) or (col1 in winForO) or (col2 in winForO) or (col3 in winForO) or (die1 in winForO) or (die2 in winForO)):
        return [False,"0Win"]
    elif((row1 in winForX) or (row2 in winForX) or (row3 in winForX) or (col1 in winForX) or (col2 in winForX) or (col3 in winForX) or (die1 in winForX) or (die2 in winForX)):
        return [False,"XWin"]
    elif("_" in SumAll):
        return [True, "GameOn"]
    else:
        return [False, "Draw"]
    
#Function to check wheather or not game is over:

def EndWord(stats):
    if stats == "0Win":
        return print("Player 1 has won the game. Good for you!")
    elif stats == "XWin":
        return print("Player 2 has won the game. Good for you!")
    elif stats == "Draw":
        return print("It's a draw. You both lose.")
    
    
            


def DisplayFunction(DGrid):
    Display = ""
    for value in DGrid.values():
        Display += value + '\n'
    return Display


TikTackToe = """                                                    (
-------       *     | /    -------       /\       (       -------      (  )     |------
   |          |     |/        |         /  \     (           |        (    )    |
   |          |     |\        |        /----\     (          |        (    )    |------
   |          |     | \       |       /      \      (        |         (  )     |
                                                                                |------                                                       

                            """
                            
   
print(TikTackToe)

NoWin = True

while NoWin:
    #Frist Round For player One
    print(DisplayFunction(GridToGrid()))
    Player1Row = int(input("Player One: Wich Row do you want. Enter A number 1-3!"))
    Player1Col = int(input("Wich Column. Enter a Number 1-3!"))
    Alpha,Row = NumToAlpha(Player1Row,Player1Col)
    ChangeGrid(Alpha,'Player0',Row)
    list1 = WinSat(GridForInput)
    NoWin = list1[0]
    stats = list1[1]
    EndWord(stats)
    #Seconed Round For player Two
    print(DisplayFunction(GridToGrid()))
    Player2Row = int(input("Player Two: Wich Row do you want. Enter A number 1-3!"))
    Player2Col = int(input("Wich Column. Enter a Number 1-3!"))
    Alpha,Row = NumToAlpha(Player2Row,Player2Col)
    ChangeGrid(Alpha,'PlayerX',Row)
    list1 = WinSat(GridForInput)
    NoWin = list1[0]
    stats = list1[1]
    EndWord(stats)
    

    
    