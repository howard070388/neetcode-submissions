class Solution:
    def isValid(self, s: str) -> bool:
        save = []
        for word in s:
            if word == "(" or word == "{" or word == "[":
                save.append(word)
            elif len(save) > 0 and ( word == ")" and save[len(save)-1] == "("
            or word == "}" and save[len(save)-1] == "{"
            or word == "]" and save[len(save)-1] == "[" ):
                save.pop()
            else:
                return False
        return save == []