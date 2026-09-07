class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words={}
        for w in strs:
            key = "".join(sorted(w))
            if key in words:
                words[key].append(w)
            else:
                words[key] = [w]
        return list(words.values())