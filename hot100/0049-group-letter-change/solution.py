class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        match_dict = {}
        final_ans = []
        for i in range(len(strs)):
            ele = tuple(sorted(strs[i]))
            if ele not in match_dict:
                match_dict[ele] = {i} 
            else:
                match_dict[ele].add(i)
        for ele in match_dict:
            words = [] # 同一组字母异位词构成的列表。
            for word_index in match_dict[ele]:
                words.append(strs[word_index])
            final_ans.append(words)
        return final_ans

