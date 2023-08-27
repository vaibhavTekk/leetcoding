class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        Lcount, Rcount = 0,0
        total = len(moves)
        for i in moves:
            if i == 'L':
                Lcount += 1
            elif i == 'R':
                Rcount += 1
        blanks = total - (Lcount + Rcount)
        # print(Lcount, Rcount, blanks)
        return blanks + abs(Lcount - Rcount)