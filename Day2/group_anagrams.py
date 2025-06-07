class Solution:
    def groupAnagrams(self,strs):
        d=defaultdict(list)
        for word in strs:
            key=tuple(sorted(word))
            d[key].append(word)
        return list(d.values())