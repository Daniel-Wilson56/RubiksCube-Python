import consts
from cube import Cube
from face import Face
from operations import Operations

class CubeSolver:

    def __init__(self, cube: Cube):
        self.cube = cube

    def SolveCube(self):
        whiteCrossInstructions, whiteCrossCube = self.CreateWhiteCross(self.cube)

        return whiteCrossInstructions, whiteCrossCube

    def CreateWhiteCross(self, cube: Cube):
        instrucions = []
        blockValues =[
            [consts.Colour.White, consts.Colour.Orange],
            [consts.Colour.White, consts.Colour.Blue],
            [consts.Colour.White, consts.Colour.Red],
            [consts.Colour.White, consts.Colour.Green]
        ]
        middleConnectors = [
            consts.Blocks.TopTopMiddleConnector,
            consts.Blocks.TopRightMiddleConnector,
            consts.Blocks.TopBottomMiddleConnector,
            consts.Blocks.TopLeftMiddleConnector,
            consts.Blocks.BottomTopMiddleConnector,
            consts.Blocks.BottomRightMiddleConnector,
            consts.Blocks.BottomBottomMiddleConnector,
            consts.Blocks.BottomLeftMiddleConnector,
            consts.Blocks.FrontLeftMiddleConnector,
            consts.Blocks.FrontRightMiddleConnector,
            consts.Blocks.BackLeftMiddleConnector,
            consts.Blocks.BackRightMiddleConnector
            ]
        topSideConnectors = [
            consts.Blocks.TopTopMiddleConnector,
            consts.Blocks.TopRightMiddleConnector,
            consts.Blocks.TopBottomMiddleConnector,
            consts.Blocks.TopLeftMiddleConnector
        ]
        target = [
            [
                [consts.Colour.Any, consts.Colour.White, consts.Colour.Any],
                [consts.Colour.White, consts.Colour.White, consts.Colour.White],
                [consts.Colour.Any, consts.Colour.White, consts.Colour.Any]
            ],
            [
                [consts.Colour.Any, consts.Colour.Any, consts.Colour.Any],
                [consts.Colour.Any, consts.Colour.Any, consts.Colour.Any],
                [consts.Colour.Any, consts.Colour.Any, consts.Colour.Any]
            ],
            [
                [consts.Colour.Any, consts.Colour.Red, consts.Colour.Any],
                [consts.Colour.Any, consts.Colour.Red, consts.Colour.Any],
                [consts.Colour.Any, consts.Colour.Any, consts.Colour.Any]
            ],
            [
                [consts.Colour.Any, consts.Colour.Orange, consts.Colour.Any],
                [consts.Colour.Any, consts.Colour.Orange, consts.Colour.Any],
                [consts.Colour.Any, consts.Colour.Any, consts.Colour.Any]
            ],
            [
                [consts.Colour.Any, consts.Colour.Green, consts.Colour.Any],
                [consts.Colour.Any, consts.Colour.Green, consts.Colour.Any],
                [consts.Colour.Any, consts.Colour.Any, consts.Colour.Any]
            ],
            [
                [consts.Colour.Any, consts.Colour.Blue, consts.Colour.Any],
                [consts.Colour.Any, consts.Colour.Blue, consts.Colour.Any],
                [consts.Colour.Any, consts.Colour.Any, consts.Colour.Any]
            ]
        ]
        bigTableOfTrues = [
            [
                [True, True, True],
                [True, True, True],
                [True, True, True]
            ],
            [
                [True, True, True],
                [True, True, True],
                [True, True, True]
            ],
            [
                [True, True, True],
                [True, True, True],
                [True, True, True]
            ],
            [
                [True, True, True],
                [True, True, True],
                [True, True, True]
            ],
            [
                [True, True, True],
                [True, True, True],
                [True, True, True]
            ],
            [
                [True, True, True],
                [True, True, True],
                [True, True, True]
            ],
        ]
        initialComparison = self.CompareCubeToTarget(cube.GetCube(), target)
        if initialComparison == bigTableOfTrues:
            return [], cube
        else:
            loops = 0
            while bigTableOfTrues != self.CompareCubeToTarget(cube.GetCube(), target):
                #random turn to avoid any infinite loops from complicated interplay between different blocks' algorithms that I couldn't notice
                if loops >= 10:
                    loops = 0
                    instrucions.append(cube.RandomTurn())
                #will do this for each top connector, needs the while because the algorithms might interact with each other
                for i in range(4):
                    nonWhiteColour = blockValues[i][1]
                    #Due to the order GetBlockValues() returns in, this will always work without worrying about permutations
                    while cube.GetBlockValues(topSideConnectors[i]) != blockValues[i]:
                        cubeData = cube.GetCube()
                        permutations = Operations.GetPermutationsOfList(blockValues[i])
                        #issue is in here
                        for connector in middleConnectors:
                            connectorBlockValues = cube.GetBlockValues(connector)
                            if connectorBlockValues in permutations:
                                print(connectorBlockValues)
                                print(permutations)
                                print(connector)
                                if connector in topSideConnectors and connectorBlockValues[0] == consts.Colour.White:
                                    done = True
                                else:
                                    done = False
                                    connectorLocation = connector
                        if done:
                            continue
                        print(connectorLocation)
                        cube.PrintCube()
                        #make sure the non-white colour on the white connector block is on the face with the centre of that colour
                        #then just rotate that face until the white is on top
                        #do this by checking if the non-white is on the top or bottom face
                        #and if not, check the side it's on and rotate the connected face (e.g. top side = rotate relational top face)
                        #until it's right
                        #if it is on the top or bottom, flip edge
                        match connectorLocation:
                            case consts.Blocks.TopTopMiddleConnector:
                                if cubeData[0][0][1] == nonWhiteColour:
                                    nonWhiteFaceCentreColour = cube.GetBlockValues(consts.Blocks.TopCentre)
                                    nonWhiteFaceID = consts.Faces.Top
                                    nonWhiteSide = consts.Sides.Top
                                else:
                                    nonWhiteFaceCentreColour = cube.GetBlockValues(consts.Blocks.BackCentre)
                                    nonWhiteFaceID = consts.Faces.Back
                                    nonWhiteSide = consts.Sides.Top
                            case consts.Blocks.TopLeftMiddleConnector:
                                if cubeData[0][1][0] == nonWhiteColour:
                                    nonWhiteFaceCentreColour = cube.GetBlockValues(consts.Blocks.TopCentre)
                                    nonWhiteFaceID = consts.Faces.Top
                                    nonWhiteSide = consts.Sides.Left
                                else:
                                    nonWhiteFaceCentreColour = cube.GetBlockValues(consts.Blocks.LeftCentre)
                                    nonWhiteFaceID = consts.Faces.Left
                                    nonWhiteSide = consts.Sides.Top
                            case consts.Blocks.TopRightMiddleConnector:
                                if cubeData[0][1][2] == nonWhiteColour:
                                    nonWhiteFaceCentreColour = cube.GetBlockValues(consts.Blocks.TopCentre)
                                    nonWhiteFaceID = consts.Faces.Top
                                    nonWhiteSide = consts.Sides.Right
                                else:
                                    nonWhiteFaceCentreColour = cube.GetBlockValues(consts.Blocks.RightCentre)
                                    nonWhiteFaceID = consts.Faces.Right
                                    nonWhiteSide = consts.Sides.Top
                            case consts.Blocks.TopBottomMiddleConnector:
                                if cubeData[0][2][1] == nonWhiteColour:
                                    nonWhiteFaceCentreColour = cube.GetBlockValues(consts.Blocks.TopCentre)
                                    nonWhiteFaceID = consts.Faces.Top
                                    nonWhiteSide = consts.Sides.Bottom
                                else:
                                    nonWhiteFaceCentreColour = cube.GetBlockValues(consts.Blocks.FrontCentre)
                                    nonWhiteFaceID = consts.Faces.Front
                                    nonWhiteSide = consts.Sides.Top
                            case consts.Blocks.BottomTopMiddleConnector:
                                if cubeData[1][0][1] == nonWhiteColour:
                                    nonWhiteFaceCentreColour = cube.GetBlockValues(consts.Blocks.BottomCentre)
                                    nonWhiteFaceID = consts.Faces.Bottom
                                    nonWhiteSide = consts.Sides.Top
                                else:
                                    nonWhiteFaceCentreColour = cube.GetBlockValues(consts.Blocks.FrontCentre)
                                    nonWhiteFaceID = consts.Faces.Front
                                    nonWhiteSide = consts.Sides.Bottom
                            case consts.Blocks.BottomLeftMiddleConnector:
                                if cubeData[1][1][0] == nonWhiteColour:
                                    nonWhiteFaceCentreColour = cube.GetBlockValues(consts.Blocks.BottomCentre)
                                    nonWhiteFaceID = consts.Faces.Bottom
                                    nonWhiteSide = consts.Sides.Left
                                else:
                                    nonWhiteFaceCentreColour = cube.GetBlockValues(consts.Blocks.LeftCentre)
                                    nonWhiteFaceID = consts.Faces.Left
                                    nonWhiteSide = consts.Sides.Bottom
                            case consts.Blocks.BottomRightMiddleConnector:
                                if cubeData[1][1][2] == nonWhiteColour:
                                    nonWhiteFaceCentreColour = cube.GetBlockValues(consts.Blocks.BottomCentre)
                                    nonWhiteFaceID = consts.Faces.Bottom
                                    nonWhiteSide = consts.Sides.Right
                                else:
                                    nonWhiteFaceCentreColour = cube.GetBlockValues(consts.Blocks.RightCentre)
                                    nonWhiteFaceID = consts.Faces.Right
                                    nonWhiteSide = consts.Sides.Bottom
                            case consts.Blocks.BottomBottomMiddleConnector:
                                if cubeData[1][2][1] == nonWhiteColour:
                                    nonWhiteFaceCentreColour = cube.GetBlockValues(consts.Blocks.BottomCentre)
                                    nonWhiteFaceID = consts.Faces.Bottom
                                    nonWhiteSide = consts.Sides.Bottom
                                else:
                                    nonWhiteFaceCentreColour = cube.GetBlockValues(consts.Blocks.BackCentre)
                                    nonWhiteFaceID = consts.Faces.Back
                                    nonWhiteSide = consts.Sides.Bottom
                            case consts.Blocks.FrontLeftMiddleConnector:
                                if cubeData[2][1][0] == nonWhiteColour:
                                    nonWhiteFaceCentreColour = cube.GetBlockValues(consts.Blocks.FrontCentre)
                                    nonWhiteFaceID = consts.Faces.Front
                                    nonWhiteSide = consts.Sides.Left
                                else:
                                    nonWhiteFaceCentreColour = cube.GetBlockValues(consts.Blocks.LeftCentre)
                                    nonWhiteFaceID = consts.Faces.Left
                                    nonWhiteSide = consts.Sides.Right
                            case consts.Blocks.FrontRightMiddleConnector:
                                if cubeData[2][1][2] == nonWhiteColour:
                                    nonWhiteFaceCentreColour = cube.GetBlockValues(consts.Blocks.FrontCentre)
                                    nonWhiteFaceID = consts.Faces.Front
                                    nonWhiteSide = consts.Sides.Right
                                else:
                                    nonWhiteFaceCentreColour = cube.GetBlockValues(consts.Blocks.RightCentre)
                                    nonWhiteFaceID = consts.Faces.Right
                                    nonWhiteSide = consts.Sides.Left
                            case consts.Blocks.BackLeftMiddleConnector:
                                if cubeData[3][1][0] == nonWhiteColour:
                                    nonWhiteFaceCentreColour = cube.GetBlockValues(consts.Blocks.BackCentre)
                                    nonWhiteFaceID = consts.Faces.Back
                                    nonWhiteSide = consts.Sides.Left
                                else:
                                    nonWhiteFaceCentreColour = cube.GetBlockValues(consts.Blocks.RightCentre)
                                    nonWhiteFaceID = consts.Faces.Right
                                    nonWhiteSide = consts.Sides.Right
                            case consts.Blocks.BackRightMiddleConnector:
                                if cubeData[2][1][2] == nonWhiteColour:
                                    nonWhiteFaceCentreColour = cube.GetBlockValues(consts.Blocks.BackCentre)
                                    nonWhiteFaceID = consts.Faces.Back
                                    nonWhiteSide = consts.Sides.Right
                                else:
                                    nonWhiteFaceCentreColour = cube.GetBlockValues(consts.Blocks.LeftCentre)
                                    nonWhiteFaceID = consts.Faces.Left
                                    nonWhiteSide = consts.Sides.Left
                        nonWhiteFace = cube.GetFace(nonWhiteFaceID)
                        if nonWhiteFaceCentreColour == nonWhiteColour:
                            while cube.GetBlockValues(topSideConnectors[i]) != blockValues[i]:
                                instrucions.append(cube.TurnSide(nonWhiteFace, consts.Direction.Clockwise, 1))
                        else:
                            if nonWhiteFaceID != consts.Faces.Top and nonWhiteFaceID != consts.Faces.Bottom:
                                connectedFaces = cube.GetAdjacentFaces(nonWhiteFace)
                                if nonWhiteSide == consts.Sides.Top:
                                    instrucions.append(cube.TurnSide(connectedFaces[0].faceID, consts.Direction.Clockwise, 1))
                                elif nonWhiteSide == consts.Sides.Right:
                                    instrucions.append(cube.TurnSide(connectedFaces[1].faceID, consts.Direction.Clockwise, 1))
                                elif nonWhiteSide == consts.Sides.Bottom:
                                    instrucions.append(cube.TurnSide(connectedFaces[2].faceID, consts.Direction.Clockwise, 1))
                                else:
                                    instrucions.append(cube.TurnSide(connectedFaces[3].faceID, consts.Direction.Clockwise, 1))
                            else:
                                returnInstructions, cube = self.FlipEdge(cube, nonWhiteFace, nonWhiteSide)
                                for instruction in returnInstructions:
                                    instrucions.append(instruction)
                loops += 1
        whiteCrossCube = Cube()
        whiteCrossCube.SetCube(cube.GetCube())
        return instrucions, whiteCrossCube

    def CompareCubeToTarget(self, cubeData, target):
        output = [
            [
                [False, False, False],
                [False, False, False],
                [False, False, False]
            ],
            [
                [False, False, False],
                [False, False, False],
                [False, False, False]
            ],
            [
                [False, False, False],
                [False, False, False],
                [False, False, False]
            ],
            [
                [False, False, False],
                [False, False, False],
                [False, False, False]
            ],
            [
                [False, False, False],
                [False, False, False],
                [False, False, False]
            ],
            [
                [False, False, False],
                [False, False, False],
                [False, False, False]
            ],
        ]
        for i in range(len(output)):
            for j in range(len(output[i])):
                for k in range(len(output[i][j])):
                    if cubeData[i][j][k] == target[i][j][k] or target[i][j][k] == consts.Colour.Any:
                        output[i][j][k] = True
        return output
    
    def FlipEdge(self, cube: Cube, face: Face, side: consts.Sides):
        instructions = []
        faces = cube.GetAdjacentFaces(face)
        if side == consts.Sides.Top:
            secondFaceToTurn = faces[0]
            thirdFaceToTurn = faces[1]
        elif side == consts.Sides.Right:
            secondFaceToTurn = faces[1]
            thirdFaceToTurn = faces[2]
        elif side == consts.Sides.Bottom:
            secondFaceToTurn = faces[2]
            thirdFaceToTurn = faces[3]
        else:
            secondFaceToTurn = faces[3]
            thirdFaceToTurn = faces[0]
        instructions.append(cube.TurnSide(face.faceID, consts.Direction.Clockwise, 1))
        instructions.append(cube.TurnSide(secondFaceToTurn.faceID, consts.Direction.Counterclockwise, 1))
        instructions.append(cube.TurnSide(thirdFaceToTurn.faceID, consts.Direction.Clockwise, 1))
        instructions.append(cube.TurnSide(secondFaceToTurn.faceID, consts.Direction.Clockwise, 1))
        return instructions, cube