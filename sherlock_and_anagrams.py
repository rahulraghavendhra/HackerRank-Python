"""
Problem Statement
Given a string S, find the number of "unordered anagrammatic pairs" of substrings.
Input Format
First line contains T, the number of testcases. Each testcase consists of string S in one line.
Constraints 
1≤T≤10 
2≤length(S)≤100 
String S contains only the lowercase letters of the English alphabet.
Output Format
For each testcase, print the required answer in one line.
Sample Input
2
abba
abcd
Sample Output
4
0
Explanation
Let's say S[i,j] denotes the substring Si,Si+1,⋯,Sj.
testcase 1: 
For S=abba, anagrammatic pairs are: {S[1,1],S[4,4]}, {S[1,2],S[3,4]}, {S[2,2],S[3,3]} and {S[1,3],S[2,4]}.
testcase 2: 
No anagrammatic pairs.
"""
def find_sub_string(string):
	temp_array = []
	for i in range(0, len(string)):
		for j in range(i, len(string)):
			temp_array.append(string[i:j+1])
	return temp_array

def check_for_anagrams(string):
	count = 0
	substring_array = find_sub_string(string)
	sorted_str_array = []
	for substring in substring_array:
		sorted_str_array.append(''.join(sorted(substring)))
#		sorted_str_array.append(sorted(substring))
	final_sorted =  sorted(sorted_str_array)
	seen = set()
	for i in range(len(final_sorted)):
		for j in range(i+1, len(final_sorted)):
			if final_sorted[i] == final_sorted[j]:
				count  = count + 1
	
		
"""
	for n in sorted_str_array:
		if n in seen:
			print n
			count = count + 1
		else:
			seen.add(n)
	print seen
"""
	return count

if __name__ == '__main__':
	n = input()
	n = int(n)
	string_array = []
	for i in range(n):
		input_string = raw_input()
		string_array.append(input_string)
	for i in range(n):
		val = check_for_anagrams(string_array[i])
		print val
