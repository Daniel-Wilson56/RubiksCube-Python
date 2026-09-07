import consts

class Face:
    
    def __init__ (self, centreColour, faceID):
        self.centreColour = centreColour
        self.colours = [[centreColour, centreColour, centreColour], [centreColour, centreColour, centreColour], [centreColour, centreColour, centreColour]]
        self.faceID = faceID
        if self.faceID == consts.Faces.Top:
            self.relationalTopFaceID = consts.Faces.Back
            self.relationalRightFaceID = consts.Faces.Right
            self.relationalBottomFaceID = consts.Faces.Front
            self.relationalLeftFaceID = consts.Faces.Left
        elif self.faceID == consts.Faces.Front:
            self.relationalTopFaceID = consts.Faces.Top
            self.relationalRightFaceID = consts.Faces.Right
            self.relationalBottomFaceID = consts.Faces.Bottom
            self.relationalLeftFaceID = consts.Faces.Left
        elif self.faceID == consts.Faces.Right:
            self.relationalTopFaceID = consts.Faces.Top
            self.relationalRightFaceID = consts.Faces.Back
            self.relationalBottomFaceID = consts.Faces.Bottom
            self.relationalLeftFaceID = consts.Faces.Front
        elif self.faceID == consts.Faces.Bottom:
            self.relationalTopFaceID = consts.Faces.Front
            self.relationalRightFaceID = consts.Faces.Right
            self.relationalBottomFaceID = consts.Faces.Back
            self.relationalLeftFaceID = consts.Faces.Left
        elif self.faceID == consts.Faces.Left:
            self.relationalTopFaceID = consts.Faces.Top
            self.relationalRightFaceID = consts.Faces.Front
            self.relationalBottomFaceID = consts.Faces.Bottom
            self.relationalLeftFaceID = consts.Faces.Back
        elif self.faceID == consts.Faces.Back:
            self.relationalTopFaceID = consts.Faces.Top
            self.relationalRightFaceID = consts.Faces.Left
            self.relationalBottomFaceID = consts.Faces.Bottom
            self.relationalLeftFaceID = consts.Faces.Right
        else:
            self.relationalTopFaceID = consts.Faces.Top
            self.relationalRightFaceID = consts.Faces.Top
            self.relationalBottomFaceID = consts.Faces.Top
            self.relationalLeftFaceID = consts.Faces.Top

    def GetFace(self):
        return self.colours
    
    def SetFace(self, data):
        self.colours = data

    def GetSide(self, side):
        if side == consts.Sides.Top:
            return [self.colours[0][0], self.colours[0][1], self.colours[0][2]]
        elif side == consts.Sides.Left:
            return [self.colours[0][0], self.colours[1][0], self.colours[2][0]]
        elif side == consts.Sides.Right:
            return [self.colours[0][2], self.colours[1][2], self.colours[2][2]]
        elif side == consts.Sides.Bottom:
            return [self.colours[2][0], self.colours[2][1], self.colours[2][2]]
        else:
            raise Exception("Invalid side")
        
    def SetSide(self, side, values):
        if side == consts.Sides.Top:
            self.colours[0][0] = values[0]
            self.colours[0][1] = values[1]
            self.colours[0][2] = values[2]
        elif side == consts.Sides.Left:
            self.colours[0][0] = values[0]
            self.colours[1][0] = values[1]
            self.colours[2][0] = values[2]
        elif side == consts.Sides.Right:
            self.colours[0][2] = values[0]
            self.colours[1][2] = values[1]
            self.colours[2][2] = values[2]
        elif side == consts.Sides.Bottom:
            self.colours[2][0] = values[0]
            self.colours[2][1] = values[1]
            self.colours[2][2] = values[2]

    def Turn(self, direction):
        top = self.GetSide(consts.Sides.Top)
        left = self.GetSide(consts.Sides.Left)
        right = self.GetSide(consts.Sides.Right)
        bottom = self.GetSide(consts.Sides.Bottom)
        if direction == consts.Direction.Clockwise:
            self.SetSide(consts.Sides.Top, left)
            self.SetSide(consts.Sides.Left, bottom)
            self.SetSide(consts.Sides.Bottom, [right[2], right[1], right[0]])
            self.SetSide(consts.Sides.Right, top)
        elif direction == consts.Direction.Counterclockwise:
            self.SetSide(consts.Sides.Top, right)
            self.SetSide(consts.Sides.Left, [top[2], top[1], top[0]])
            self.SetSide(consts.Sides.Bottom, left)
            self.SetSide(consts.Sides.Right, [bottom[2], bottom[1], bottom[0]])