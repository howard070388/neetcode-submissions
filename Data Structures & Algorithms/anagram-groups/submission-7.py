class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        save={}
        for w in strs:
            key = "".join(sorted(w))
            if key in save:
                save[key].append(w)
            else:
                save[key] = [w]
        return list(save.values())