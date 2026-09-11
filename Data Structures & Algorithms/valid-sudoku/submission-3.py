class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        xlines = collections.defaultdict(set)
        ylines = collections.defaultdict(set)
        boxes = collections.defaultdict(set)
        high = int(len(board))
        long =  int(len(board[0]))
        for x in range(long):
            for y in range(high):
                num = board[x][y]
                if num == ".":
                    continue
                if (
                    num in xlines[x] or
                    num in ylines[y] or
                    num in boxes[(x//3,y//3)] 
                ):
                    return False
                xlines[x].add(num)
                ylines[y].add(num)
                boxes[(x//3,y//3)].add(num)
        return True
