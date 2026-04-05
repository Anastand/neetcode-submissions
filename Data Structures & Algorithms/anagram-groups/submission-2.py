from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group=defaultdict(list)
        for val in strs:
            nval=tuple(sorted(val))
            group[nval].append(val) 
    
        return list(group.values())