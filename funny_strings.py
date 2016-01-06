"""
Problem Statement

Suppose you have a string S that has the length N. It is indexed from 0 to N−1. String R is the reverse of string S. The string S is funny if the condition |Si−Si−1|=|Ri−Ri−1| is true for every i from 1 to N−1.

Note: Given a string str, stri denotes the ascii value of the ith character (0-indexed) of str. Here, |x| denotes the absolute value of an integer x.

Input Format

The first line of input will contain an integer T, the number of test cases. Each of the next T lines contains one string S.

Constraints

1⩽T⩽10
2⩽length of S⩽10000
Output Format

For each string, print Funny or Not Funny on separate lines.

Sample Input

2
acxz
bcxz
Sample Output

Funny
Not Funny
Explanation

Consider the 1st test case: acxz

Here:

|c-a| = |x-z| = 2
|x-c| = |c-x| = 21
|z-x| = |a-c| = 2
Hence, the string is Funny.

Consider the 2nd test case: bcxz

Here:

|c-b| != |x-z|
Hence, the string is Not Funny.
"""

def check_funny(string):
    reversed_string = string[::-1]
    for first_index in range(len(string)-1):
        second_index = first_index+1
        first_string_diff = abs(ord(string[first_index]) - ord(string[second_index]))
        second_string_diff = abs(ord(reversed_string[first_index]) - ord(reversed_string[second_index]))
        if (first_string_diff != second_string_diff):
            return 'Not Funny'
    return 'Funny'


if __name__ == '__main__':
    n = input()
    output_array = []
    for i in range(n):
        input_string = raw_input()
        output = check_funny(input_string)
        output_array.append(output)
    print output_array
