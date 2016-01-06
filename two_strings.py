"""
Problem Statement
You are given two strings, A and B. Find if there is a substring that appears in both A and B.
Input Format
Several test cases will be given to you in a single file. The first line of the input will contain a single integer T, the number of test cases
Then there will be T descriptions of the test cases. Each description contains two lines. The first line contains the string A and the second line contains the string B.
Output Format
For each test case, display YES (in a newline), if there is a common substring. Otherwise, display NO.
Constraints
All the strings contain only lowercase Latin letters.
1<=T<=10
1<=|A|,|B|<=105
Sample Input
2
hello
world
hi
world
Sample Output
YES
NO
Explanation
For the 1st test case, the letter o is common between both strings, hence the answer YES. (Furthermore, the letter l is also common, but you only need to find one common substring.) 
For the 2nd test case, hi and world do not have a common substring, hence the answer NO.
"""
def common_start(sa, sb):
	""" returns the longest common substring from the beginning of sa and sb """
	def _iter():
		for a, b in zip(sa, sb):
			if a == b:
				yield a
			else:
			   	return

	return ''.join(_iter())


def find_sub_string(string):
	temp_array = []
	for i in range(0, len(string)):
		for j in range(i, len(string)):
			temp_array.append(string[i:j+1])
	return set(temp_array)

def check_for_substrings(string1, string2):
	for character in string1:
		if character in string2:
			return True
	return False

if __name__ == '__main__':
	n = input()
	n = int(n)*2
	string_array = []
	for i in range(n):
		input_string = input()
		string_array.append(input_string)
	for i in range(0, n, 2):
		val = check_for_substrings(string_array[i], string_array[i+1])
		if val == True:
			print "YES"
		else:
			print "NO"


"""
t = input()
assert t<=10 and t>=1
for _ in range(t):
s = list(raw_input())
	assert len(s) >=1 and len(s)<= 10000
	su = 0
	for i in range(0,len(s)/2):
		su+= abs(ord(s[i]) - ord(s[-1-i]))
	print su



"""
