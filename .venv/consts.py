from enum import Enum

class Colour(Enum):
    White = "w"
    Yellow = "y"
    Red = "r"
    Orange = "o"
    Blue = "b"
    Green = "g"
    Any = "a"

class Direction(Enum):
    Clockwise = "Cw"
    Counterclockwise = "Ccw"

class Faces(Enum):
    Top = "To"
    Front = "Fr"
    Left = "Le"
    Right = "Ri"
    Back = "Ba"
    Bottom = "Bo"

class Sides(Enum):
    Top = 0
    Left = 1
    Right = 2
    Bottom = 3

class Blocks(Enum):
    TopTopLeftCorner = 0
    TopTopMiddleConnector = 1
    TopTopRightCorner = 2
    TopLeftMiddleConnector = 3
    TopCentre = 4
    TopRightMiddleConnector = 5
    TopBottomLeftCorner = 6
    TopBottomMiddleConnector = 7
    TopBottomRightCorner = 8
    BottomTopLeftCorner = 9
    BottomTopMiddleConnector = 10
    BottomTopRightCorner = 11
    BottomLeftMiddleConnector = 12
    BottomCentre = 13
    BottomRightMiddleConnector = 14
    BottomBottomLeftCorner = 15
    BottomBottomMiddleConnector = 16
    BottomBottomRightCorner = 17
    FrontLeftMiddleConnector = 18
    FrontCentre = 19
    FrontRightMiddleConnector = 20
    BackLeftMiddleConnector = 21
    BackCentre = 22
    BackRightMiddleConnector = 23
    LeftCentre = 24
    RightCentre = 25