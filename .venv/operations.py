class Operations:
    
    def GetPermutationsOfList(list):
        length = len(list)
        if length == 2:
            permutationsOfList = [[list[0], list[1]], [list[1], list[0]]]
        elif length == 3:
            permutationsOfList = [
                [list[0], list[1], list[2]],
                [list[0], list[2], list[1]],
                [list[1], list[0], list[2]],
                [list[1], list[2], list[0]],
                [list[2], list[0], list[1]],
                [list[2], list[1], list[0]]
            ]
        return permutationsOfList
    
    def AttemptToConvertToInt(item):
        try:
            output = int(item)
            return (output, True)
        except:
            return (item, False)