import consts
from face import Face
from numpy import random
from operations import Operations

class Cube:

    def __init__(self):
        self.faces = [
            Face(consts.Colour.White, consts.Faces.Top), 
            Face(consts.Colour.Yellow, consts.Faces.Bottom), 
            Face(consts.Colour.Red, consts.Faces.Front), 
            Face(consts.Colour.Orange, consts.Faces.Back), 
            Face(consts.Colour.Green, consts.Faces.Left), 
            Face(consts.Colour.Blue, consts.Faces.Right)
            ]
    #faces in format Top, Bottom, Front, Back, Left, Right

    def GetCube(self):
        output = []
        for face in self.faces:
            output.append(face.GetFace())
        return output

    def SetCube(self, data):
        i = 0
        for face in self.faces:
            face.SetFace(data[i])
            i+=1

    def GetFace(self, faceID):
        if faceID == consts.Faces.Top:
            return self.faces[0]
        elif faceID == consts.Faces.Bottom:
            return self.faces[1]
        elif faceID == consts.Faces.Front:
            return self.faces[2]
        elif faceID == consts.Faces.Back:
            return self.faces[3]
        elif faceID == consts.Faces.Left:
            return self.faces[4]
        else:
            return self.faces[5]

    def TurnFace(self, faceToTurn, direction, numTimes):
        for face in self.faces:
            if face.faceID == faceToTurn:
                mainFace = face
        for i in range(numTimes % 4):
            mainFace.Turn(direction)
            adjacentSides = self.GetAndReverseAdjacentSidesOfFace(mainFace, direction)
            topSide = adjacentSides[0]
            rightSide = adjacentSides[1]
            bottomSide = adjacentSides[2]
            leftSide = adjacentSides[3]
            if direction == consts.Direction.Clockwise:
                self.SetAdjacentSidesOfFace(mainFace, [leftSide, topSide, rightSide, bottomSide])
                #array is in format newTopSide, newRightSide, newBottomSide, newLeftSide
            elif direction == consts.Direction.Counterclockwise:
                self.SetAdjacentSidesOfFace(mainFace, [rightSide, bottomSide, leftSide, topSide])

    def GetBlockValues(self, blockToGet):
        cubeData = self.GetCube()
        match blockToGet:
            case consts.Blocks.TopTopLeftCorner:
                return ([cubeData[0][0][0], cubeData[4][0][0], cubeData[3][0][2]])
            case consts.Blocks.TopTopMiddleConnector:
                return ([cubeData[0][0][1], cubeData[3][0][1]])
            case consts.Blocks.TopTopRightCorner:
                return ([cubeData[0][0][2], cubeData[5][0][2], cubeData[3][0][0]])
            case consts.Blocks.TopLeftMiddleConnector:
                return ([cubeData[0][1][0], cubeData[4][0][1]])
            case consts.Blocks.TopCentre:
                return ([cubeData[0][1][1]])
            case consts.Blocks.TopRightMiddleConnector:
                return ([cubeData[0][1][2], cubeData[5][0][1]])
            case consts.Blocks.TopBottomLeftCorner:
                return ([cubeData[0][2][0], cubeData[4][0][2], cubeData[2][0][0]])
            case consts.Blocks.TopBottomMiddleConnector:
                return ([cubeData[0][2][1], cubeData[2][0][1]])
            case consts.Blocks.TopBottomRightCorner:
                return ([cubeData[0][2][2], cubeData[5][0][0], cubeData[2][0][2]])
            case consts.Blocks.BottomTopLeftCorner:
                return ([cubeData[1][0][0], cubeData[4][2][2], cubeData[2][2][0]])
            case consts.Blocks.BottomTopMiddleConnector:
                return ([cubeData[1][0][1], cubeData[2][2][1]])
            case consts.Blocks.BottomTopRightCorner:
                return ([cubeData[1][0][2], cubeData[5][2][0], cubeData[2][2][2]])
            case consts.Blocks.BottomLeftMiddleConnector:
                return ([cubeData[1][1][0], cubeData[4][2][1]])
            case consts.Blocks.BottomCentre:
                return ([cubeData[1][1][1]])
            case consts.Blocks.BottomRightMiddleConnector:
                return ([cubeData[1][1][2], cubeData[5][2][1]])
            case consts.Blocks.BottomBottomLeftCorner:
                return ([cubeData[1][2][0], cubeData[4][2][0], cubeData[3][2][2]])
            case consts.Blocks.BottomBottomMiddleConnector:
                return ([cubeData[1][2][1], cubeData[3][2][1]])
            case consts.Blocks.BottomBottomRightCorner:
                return ([cubeData[1][2][2], cubeData[5][2][2], cubeData[3][2][0]])
            case consts.Blocks.FrontLeftMiddleConnector:
                return ([cubeData[2][1][0], cubeData[4][1][2]])
            case consts.Blocks.FrontCentre:
                return ([cubeData[2][1][1]])
            case consts.Blocks.FrontRightMiddleConnector:
                return ([cubeData[2][1][2], cubeData[5][1][0]])
            case consts.Blocks.BackLeftMiddleConnector:
                return ([cubeData[3][1][0], cubeData[5][1][2]])
            case consts.Blocks.BackCentre:
                return ([cubeData[3][1][1]])
            case consts.Blocks.BackRightMiddleConnector:
                return ([cubeData[3][1][2], cubeData[4][1][0]])
            case consts.Blocks.LeftCentre:
                return ([cubeData[4][1][1]])
            case consts.Blocks.RightCentre:
                return ([cubeData[5][1][1]])

    #returns IDs in format top, right, bottom, left
    def GetAdjacentFaces(self, centreFace: Face):
        for face in self.faces:
            if face.faceID == centreFace.relationalTopFaceID:
                topFace = face
            elif face.faceID == centreFace.relationalRightFaceID:
                rightFace = face
            elif face.faceID == centreFace.relationalBottomFaceID:
                bottomFace = face
            elif face.faceID == centreFace.relationalLeftFaceID:
                leftFace = face
        adjacentFaces = [topFace, rightFace, bottomFace, leftFace]
        return adjacentFaces

    #returns in format [
    # [topfacesidevalues, sidelocation], 
    # [rightfacesidevalues, sidelocation], 
    # [bottomfacesidevalues, sidelocation], 
    # [leftfacesidevalues, sidelocation]
    #]
    def GetAdjacentSidesOfFace(self, centreFace: Face):
        adjacentFaces = self.GetAdjacentFaces(centreFace)
        adjacentSides = []
        for face in adjacentFaces:
            if face.relationalTopFaceID == centreFace.faceID:
                adjacentSides.append([face.GetSide(consts.Sides.Top), consts.Sides.Top])
            elif face.relationalRightFaceID == centreFace.faceID:
                adjacentSides.append([face.GetSide(consts.Sides.Right), consts.Sides.Right])
            elif face.relationalBottomFaceID == centreFace.faceID:
                adjacentSides.append([face.GetSide(consts.Sides.Bottom), consts.Sides.Bottom])
            else:
                adjacentSides.append([face.GetSide(consts.Sides.Left), consts.Sides.Left])
        return adjacentSides

    #because of how some sides connect to each other, they end up being set backwards
    #this is just a list of all the connections that lead to being backwards
    #and then pre-emptively reversing sides that have those connections
    def DealWithSidesThatNeedReversing(self, direction, adjacentSides):
        correctedAdjacentSides = []
        unsafeSideConnections = [
            [consts.Sides.Top, consts.Sides.Left],
            [consts.Sides.Left, consts.Sides.Top],
            [consts.Sides.Bottom, consts.Sides.Right],
            [consts.Sides.Right, consts.Sides.Bottom],
            [consts.Sides.Right, consts.Sides.Left],
            [consts.Sides.Left, consts.Sides.Right],
            [consts.Sides.Top, consts.Sides.Bottom],
            [consts.Sides.Bottom, consts.Sides.Top]
        ]
        if direction == consts.Direction.Clockwise:
            for i in range(len(adjacentSides)):
                if [adjacentSides[i][1], adjacentSides[(i + 1) % 4][1]] not in unsafeSideConnections:
                    correctedAdjacentSides.append(adjacentSides[i][0])
                else:
                    temp = ["", "", ""]
                    temp[0] = adjacentSides[i][0][2]
                    temp[1] = adjacentSides[i][0][1]
                    temp[2] = adjacentSides[i][0][0]
                    correctedAdjacentSides.append(temp)
        elif direction == consts.Direction.Counterclockwise:
            for i in range(len(adjacentSides)):
                if [adjacentSides[i][1], adjacentSides[(i - 1) % 4][1]] not in unsafeSideConnections:
                    correctedAdjacentSides.append(adjacentSides[i][0])
                else:
                    temp = ["", "", ""]
                    temp[0] = adjacentSides[i][0][2]
                    temp[1] = adjacentSides[i][0][1]
                    temp[2] = adjacentSides[i][0][0]
                    correctedAdjacentSides.append(temp)
        return correctedAdjacentSides

    def GetAndReverseAdjacentSidesOfFace(self, centreFace: Face, direction):
        adjacentSides = self.GetAdjacentSidesOfFace(centreFace)
        return self.DealWithSidesThatNeedReversing(direction, adjacentSides)

    def SetAdjacentSidesOfFace(self, centreFace: Face, newSides):
        adjacentFaces = self.GetAdjacentFaces(centreFace)
        i = 0
        for face in adjacentFaces:
            if face.relationalTopFaceID == centreFace.faceID:
                face.SetSide(consts.Sides.Top, newSides[i])
            elif face.relationalRightFaceID == centreFace.faceID:
                face.SetSide(consts.Sides.Right, newSides[i])
            elif face.relationalBottomFaceID == centreFace.faceID:
                face.SetSide(consts.Sides.Bottom, newSides[i])
            else:
                face.SetSide(consts.Sides.Left, newSides[i])
            i += 1
    
    def PrintCube(self):
        cubeData = self.GetCube()
        sides = ["Top side: ", "Bottom side:", "Front side:", "Back side:", "Left side:", "Right side:"]
        for i in range(len(cubeData)):
            print(sides[i])
            for j in range(len(cubeData[i])):
                row = ""
                for k in range(len(cubeData[i][j])):
                    row += f"{cubeData[i][j][k].value} "
                print(row)
            print("")

    def TurnSide(self, faceToTurn: consts.Faces, direction: consts.Direction, numTurns):
        self.TurnFace(faceToTurn, direction, numTurns)
        return f"{faceToTurn.value}{direction.value}{numTurns}"

    def ShuffleCube(self):
        numTurns = random.randint(1000, 10000)
        for i in range(numTurns):
            self.RandomTurn()

    def RandomTurn(self):
        faces = [consts.Faces.Top, consts.Faces.Bottom, consts.Faces.Front, consts.Faces.Back, consts.Faces.Left, consts.Faces.Right]
        directions = [consts.Direction.Clockwise, consts.Direction.Counterclockwise]
        randFace = faces[random.randint(0, len(faces))]
        randDirection = directions[random.randint(0, len(directions))]
        randTurnNum = random.randint(0, 4)
        self.TurnFace(randFace, randDirection, randTurnNum)
        return f"{randFace.value}{randDirection.value}{randTurnNum}"

    def TestIfCubeIsValid(self):
        valid = []
        validCorners = [
            [consts.Colour.White, consts.Colour.Blue, consts.Colour.Orange],
            [consts.Colour.White, consts.Colour.Green, consts.Colour.Orange],
            [consts.Colour.White, consts.Colour.Green, consts.Colour.Red],
            [consts.Colour.White, consts.Colour.Blue, consts.Colour.Red],
            [consts.Colour.Yellow, consts.Colour.Blue, consts.Colour.Red],
            [consts.Colour.Yellow, consts.Colour.Blue, consts.Colour.Orange],
            [consts.Colour.Yellow, consts.Colour.Green, consts.Colour.Orange],
            [consts.Colour.Yellow, consts.Colour.Green, consts.Colour.Red]
        ]
        corners = [
            self.GetBlockValues(consts.Blocks.TopTopLeftCorner),
            self.GetBlockValues(consts.Blocks.TopTopRightCorner),
            self.GetBlockValues(consts.Blocks.TopBottomLeftCorner),
            self.GetBlockValues(consts.Blocks.TopBottomRightCorner),
            self.GetBlockValues(consts.Blocks.BottomTopLeftCorner),
            self.GetBlockValues(consts.Blocks.BottomTopRightCorner),
            self.GetBlockValues(consts.Blocks.BottomBottomLeftCorner),
            self.GetBlockValues(consts.Blocks.BottomBottomRightCorner)
        ]
        for corner in corners:
            cornerPermutations = Operations.GetPermutationsOfList(corner)
            for validCorner in validCorners:
                if validCorner in cornerPermutations:
                    valid.append(True)
        if valid == [True, True, True, True, True, True, True, True]:
            return True
        else:
            return False
        
    def CheckIfCubeIsSolved(self):
        cubeData = self.GetCube()
        solvedCube =[
            [
                [consts.Colour.White, consts.Colour.White, consts.Colour.White],
                [consts.Colour.White, consts.Colour.White, consts.Colour.White],
                [consts.Colour.White, consts.Colour.White, consts.Colour.White]
            ],
            [
                [consts.Colour.Yellow, consts.Colour.Yellow, consts.Colour.Yellow],
                [consts.Colour.Yellow, consts.Colour.Yellow, consts.Colour.Yellow],
                [consts.Colour.Yellow, consts.Colour.Yellow, consts.Colour.Yellow]
            ],
            [
                [consts.Colour.Red, consts.Colour.Red, consts.Colour.Red],
                [consts.Colour.Red, consts.Colour.Red, consts.Colour.Red],
                [consts.Colour.Red, consts.Colour.Red, consts.Colour.Red]
            ],
            [
                [consts.Colour.Orange, consts.Colour.Orange, consts.Colour.Orange],
                [consts.Colour.Orange, consts.Colour.Orange, consts.Colour.Orange],
                [consts.Colour.Orange, consts.Colour.Orange, consts.Colour.Orange]
            ],
            [
                [consts.Colour.Green, consts.Colour.Green, consts.Colour.Green],
                [consts.Colour.Green, consts.Colour.Green, consts.Colour.Green],
                [consts.Colour.Green, consts.Colour.Green, consts.Colour.Green]
            ],
            [
                [consts.Colour.Blue, consts.Colour.Blue, consts.Colour.Blue],
                [consts.Colour.Blue, consts.Colour.Blue, consts.Colour.Blue],
                [consts.Colour.Blue, consts.Colour.Blue, consts.Colour.Blue]
            ]
        ]
        if cubeData == solvedCube:
            return True
        else:
            return False