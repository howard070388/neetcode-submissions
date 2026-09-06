class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mem={}
        for w in strs:
            key="".join(sorted(w))
            if key in mem:
                mem[key].append(w)
            else:    
                mem[key] = [w]
        return list(mem.values())