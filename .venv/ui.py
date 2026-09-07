import consts
from operations import Operations
from cube import Cube

class UI:

    def GetOptionFromList(self, list):
        print("Select an option: ")
        for i in range(len(list)):
            print(f"{i + 1}: {list[i]}")
        userInput = input("")
        inputAsInt, successfulConversion = Operations.AttemptToConvertToInt(userInput)
        if successfulConversion and 1 <= inputAsInt and len(list) + 1 >= inputAsInt:
            return inputAsInt - 1
        else:
            print("Invalid response, please try again")
            return self.GetOptionFromList(list)
        
    def TurnFaceOfCube(self, cube: Cube):
        faces = [consts.Faces.Top, consts.Faces.Bottom, consts.Faces.Front, consts.Faces.Back, consts.Faces.Left, consts.Faces.Right]
        directions = [consts.Direction.Clockwise, consts.Direction.Counterclockwise]
        print("Which face do you want to turn?")
        faceToTurn = faces[self.GetOptionFromList(["Top", "Bottom", "Front", "Back", "Left", "Right"])]
        print("Which direction?")
        directionToTurn = directions[self.GetOptionFromList(["Clockwise", "Counterclockwise"])]
        successfulConversion = False
        while not successfulConversion:
            print("How many times?")
            numberOfTurns, successfulConversion = Operations.AttemptToConvertToInt(input())
            if not successfulConversion:
                print("Invalid response, please try again")
        cube.TurnSide(faceToTurn, directionToTurn, numberOfTurns)
        if cube.CheckIfCubeIsSolved():
            print("Cube is now solved.")
        print("")
        cube.PrintCube()

    def ShuffleCube(self, cube: Cube):
        cube.ShuffleCube()
        cube.PrintCube()

    def MainLoop(self):
        mainCube = Cube()
        mainCube.PrintCube()
        options = ["Turn a side", "Shuffle the cube", "Quit"]
        userInput = ""
        while userInput != 3:
            userInput = self.GetOptionFromList(options)
            print("")
            if userInput == 0:
                self.TurnFaceOfCube(mainCube)
            elif userInput == 1:
                self.ShuffleCube(mainCube)
        print("Quitting...")