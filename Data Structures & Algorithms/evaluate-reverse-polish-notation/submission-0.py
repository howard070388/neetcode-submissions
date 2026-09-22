class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        save=[]
        for smth in tokens:
            if smth != '+' and smth != '-' and smth != '*' and smth != '/':
                smth = int(smth)
                save.append(smth)
            else:
                right = save.pop()
                left = save.pop()
                if smth == "+":
                    new_num = left + right
                    save.append(new_num)

                if smth == "-":
                    new_num = left - right
                    save.append(new_num)

                if smth == "*":
                    new_num = left * right
                    save.append(new_num)

                if smth == "/":
                    new_num = int(left / right)
                    save.append(new_num)
        return save[0]