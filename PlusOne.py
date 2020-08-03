"""
Given a non-empty array of digits representing a non-negative integer,
 increment one to the integer. The digits are stored such that the most
 significant digit is at the head of the list, and each element in the
 array contains a single digit. You may assume the integer does not
 contain any leading zero, except the number 0 itself.

Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""


def plus_one(digits):
    i = len(digits) - 1
    while 1:
        if digits[i] < 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0
            if i != 0:
                i -= 1
            else:
                return ([1] + digits)

if __name__ == "__main__":
    print(plus_one([9, 9, 9, 9]))