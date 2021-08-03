"""
Given a non-empty string, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
Test cases:
Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.

Input: "aba"
Output: False

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

"""

def multi_substring(s):
    # too be copied, the string should not be over half of the substring
    print(f"string:{s}")
    for i in range(0, int(len(s)/2) + 1):
        sub_str = s[:i+1]
        step_size = len(sub_str)
        print(f"sub_str :{sub_str} / step_size:{step_size}")

        # mod over 0, definitely False
        if len(s) % step_size > 0:
            continue
        else:
            # check the copying
            passed = True
            for j in range(i+1, len(s), step_size):
                if s[j:(j+step_size)] != sub_str:
                    passed = False
                    break
            if passed:
                return True
    return False

"""

Implement a function str_compression(string) to perform basic string compression using the counts of repeated characters. 
For example, the string “aabcccccaaa” would become “a2b1c5a3”. 
If the "compressed" string would not become smaller than the original string your method should return the original string.
Test cases:
Input: "aabcccccaaa"
Output: “a2b1c5a3”
"""


def str_compression(s):
    ans = ""
    i = 0
    while i < len(s):
        print(f"len(ans) + 2 >= len(s): {len(ans) + 2 >= len(s)}")
        if len(ans) + 2 >= len(s):
            return s

        print(f"i: {i}")
        count = 1
        j = i+1
        while j < len(s):
            if s[i] == s[j]:
                count += 1
                j += 1
            else:
                break
        print(f"count:{count} / j: {j}")
        ans = ans + s[i] + str(count)
        i = j
        print(ans)

    print(f"ans:{ans}")
    return ans

