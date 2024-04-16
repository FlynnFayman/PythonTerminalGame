


#The Starting Game Screen Grid
NoWin = True
winFor0 = False
winForX = False 
Draw = False

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
        ("else Has Occord")



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

def Didwinn(Grid):
    TotalGrid = ""
    #For Statment to check if there is a draw
    for value in Grid.values():
        TotalGrid += value
    #checks wheather or not a row is complete
    condation10 = (Grid['RowOne'] == "0|0|0" or Grid['RowTwo'] == "0|0|0", Grid['Rowthree'] == "0|0|0")
    #these condation 1 Checks if a colummn is compelet
    condationCol10 = (Grid['RowOne'][0] + Grid['RowTwo'][0] + Grid['RowThree'][0]) == "000"
    condationCol20 = (Grid['RowOne'][2] + Grid['RowTwo'][2] + Grid['RowThree'][2]) == "000"
    condationCol30 = (Grid['RowOne'][-1] + Grid['RowTwo'][-1] + Grid['RowThree'][-1]) == "000"
    #Dieaganal Condations
    condationDie10 = (Grid['RowOne'][0] + Grid['RowTwo'][2] + Grid['RowThree'][-1]) == "000"
    condationDie20 = (Grid['RowOne'][-1] + Grid['RowTwo'][2] + Grid['RowThree'][0]) == "000"
    #Checking the X options for victory
    #checks wheather or not a row is complete
    condation1x = (Grid['RowOne'] == "X|X|X" or Grid['RowTwo'] == "X|X|X", Grid['Rowthree'] == "X|X|X")
    #these condation 1 Checks if a colummn is compelet
    condationCol1X = (Grid['RowOne'][0] + Grid['RowTwo'][0] + Grid['RowThree'][0]) == "XXX"
    condationCol2X = (Grid['RowOne'][2] + Grid['RowTwo'][2] + Grid['RowThree'][2]) == "XXX"
    condationCol3X = (Grid['RowOne'][-1] + Grid['RowTwo'][-1] + Grid['RowThree'][-1]) == "XXX"
    #Dieaganal 
    condationDie1X = (Grid['RowOne'][0] + Grid['RowTwo'][2] + Grid['RowThree'][-1]) == "XXX"
    condationDie2X = (Grid['RowOne'][-1] + Grid['RowTwo'][2] + Grid['RowThree'][0]) == "XXX"
    # If statment for o's condations victory being met 
    if(condation10 or condationCol10 or condationCol20 or condationCol30 or condationDie10 or condationDie20):
        winFor0 = True
        return winFor0,winForX,Draw, NoWin
    elif(condation1x or condationCol1X or condationCol2X or condationCol3X or condationDie1X or condationDie2X):
        winForX = True
        return winFor0,winForX,Draw, NoWin
    elif("_" in TotalGrid):
        return winFor0,winForX,Draw, NoWin
    else:
        Draw = True
        return winFor0,winForX,Draw, NoWin

#Function To display Grid for Tick Tac Toe
def DisplayFunction(DGrid):
    Display = ""
    for value in DGrid.values():
        Display += value + '\n'
    return Display


TikTackToe = """                                (
-------       *     | /    -------       /\       (       -------      (  )
   |          |     |/        |         /  \     (           |        (    )
   |          |     |\        |        /----\     (          |        (    )
   |          |     | \       |       /      \      (        |         (  )
     

                            """
                            
   
print(TikTackToe)

while NoWin == True:
    print(DisplayFunction(GridToGrid()))
    Player1Row = int(input("Player One: Wich Row do you want. Enter A number 1-3!"))
    Player1Col = int(input("Wich Column. Enter a Number 1-3!"))
    Alpha,Row = NumToAlpha(Player1Row,Player1Col)
    ChangeGrid(Alpha,'Player0',Row)
    print(DisplayFunction(GridToGrid()))
    Player2Row = int(input("Player Two: Wich Row do you want. Enter A number 1-3!"))
    Player2Col = int(input("Wich Column. Enter a Number 1-3!"))
    Alpha,Row = NumToAlpha(Player2Row,Player2Col)
    ChangeGrid(Alpha,'PlayerX',Row)
    Didwinn(GridForInput)
    if (winFor0):
        print("Player One has won. Good For you!")
        break
    elif(winForX):
        print("Player Two has won. Good For you!")
        break
    elif(Draw):
        print("No one has won. What a pair of losers!")
        break
    
    

    
    