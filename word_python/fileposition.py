

class FilePosition:
    line: int
    column: int

    def __init__(self):
        self. line = 1
        self. column = 1

    def advance(self, i: int):
        self. column += i

    def nextLine(self):
        self. line += 1
        self. column = 1

    def __repr__(self) -> str:
        return "( {}, {} )". format(self. line, self. column)

    def __str__(self) -> str:
        return "line " + str(self. line) + ", column " + str(self. column)

    def __hash__(self) -> int:
        return hash(self.column + self.line)          # return the hash

    def __eq__(self, other) -> bool:
        # if other object has not same type
        if not isinstance(other, FilePosition):
            return False
        else:
            if self.line == other.line:
                if self.column == other.column:
                    # if and only if lines are same and columns are same
                    return True
                else:
                    return False                           # otherwise return False
            else:
                return False

    def __lt__(self, other) -> bool:
        if self.line < other.line:                   # firstly checks lines
            return True
        elif self.line > other.line:
            return False
        else:
            if self.column > other.column:            # then looks to columns of two objects
                return False
            else:
                return True
