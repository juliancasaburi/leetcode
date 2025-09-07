class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_codes = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]

        seen = set()

        for word in words:
            transformation = ""
            for c in word:
                index = ord(c) - ord("a")
                transformation += morse_codes[index]

            seen.add(transformation)

        return len(seen)
