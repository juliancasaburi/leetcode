class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row_map = {c: 1 for c in "qwertyuiop"}
        row_map.update({c: 2 for c in "asdfghjkl"})
        row_map.update({c: 3 for c in "zxcvbnm"})

        result = []

        for word in words:
            first_row = row_map[word[0].lower()]
            if all(row_map[c.lower()] == first_row for c in word):
                result.append(word)

        return result
