class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        x_l = collections.defaultdict(set)
        y_l = collections.defaultdict(set)
        boxes = collections.defaultdict(set)
        H=len(board)
        L=len(board[0])
        for x in range(H):
            for y in range(L):
                val = board[x][y]
                if val == ".":
                    continue
                if (val in x_l[x] or
                    val in y_l[y] or
                    val in boxes[(x//3, y//3)]):
                    return False
                x_l[x].add(val)
                y_l[y].add(val)
                boxes[(x//3, y//3)].add(val)
        return True