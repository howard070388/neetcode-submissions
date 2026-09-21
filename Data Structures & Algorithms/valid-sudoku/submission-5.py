class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        xl = collections.defaultdict(set)
        yl = collections.defaultdict(set)
        boxes = collections.defaultdict(set)
        for x in range(len(board)):
            for y in range(len(board)):
                num = board[x][y]
                if num == '.':
                    continue
                elif (num in xl[x]
                    or num in yl[y]
                    or num in boxes[(x//3, y//3)]):
                    return False
                xl[x].add(num)
                yl[y].add(num)
                boxes[(x//3, y//3)].add(num)
        return True