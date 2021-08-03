"""
1657. Determine if Two Strings Are Close
Medium
"""

from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        # diff len -> False
        if len(word1) != len(word2):
            return False

        # contains same characters
        word_count1 = {}
        for chr in word1:
            if chr in word_count1:
                word_count1[chr] += 1
            else:
                word_count1[chr] = 1

        word_count2 = {}
        for chr in word2:
            if chr not in word_count1:
                return False
            else:
                if chr in word_count2:
                    word_count2[chr] += 1
                else:
                    word_count2[chr] = 1

        val_1 = sorted([chr for chr in word_count1.values()])
        val_2 = sorted([chr for chr in word_count2.values()])

        # Not containing the same count number list
        for i in range(len(val_1)):
            if val_1[i] != val_2[i]:
                return False

        return True



class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counter1 = Counter(word1)
        counter2 = Counter(word2)

        return counter1.keys() == counter2.keys() and Counter(counter1.values()) == Counter(counter2.values())



