class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_count = {}

        for magazine_letter in magazine:
            letter_count[magazine_letter] = letter_count.get(magazine_letter, 0) + 1
        
        for ransom_note_letter in ransomNote:
            if (ransom_note_letter not in letter_count or letter_count[ransom_note_letter] == 0):
                return False

            letter_count[ransom_note_letter] -= 1
        
        return True
        