"""
A palindrome is a word, phrase, number, or other sequence of characters which
reads the same forward and backwards . For example :"madam" "dad" are
palindromes but "sir", "sad" are not.
You are given a string s. You have to select exactly two non-
overlapping palindromic subsequences A and B from the string to maximize the
fun score.
The fun score, for selecting two subsequences, is the product of their
respective lengths. There can be many ways to choose A and B, but your goal is
to maximize the score.
There can't be any overlap or crossover between the subsequences.
Constraints:
1 < |s| <= 3000
Only lower­case English characters.
Input Format:
You need to complete a function called funPal which takes a single string s as a
parameter.
Output Format:
Return a single integer denoting the maximum score you can get from s.
Sample Input #00:
acdapmpomp
Sample Output #00:
15
Explanation #00:
You can select A="aca" and B="pmpmp". The product is 3*5=15.
Sample Input #01:
axbawbaseksqke
Sample Output #01:
25
Explanation #01:
You can select A="ababa" and B="ekske". The product is 5*5=25. Another
possible solution is A="ababa" and B="ekqke" which also gives 25.
"""
from itertools import combinations
def funPal(string):
	C=1
	for j in range(len(string)+1):
		str1=string[j:]
		str2=string[:j]
		c1=1
		c2=1
		for i in range(len(str1)+1,1,-1):
			if c1==1:
				for x in combinations(str1,i):
					if x==x[::-1]:
						c1=max(c1,len(x))
						break
		for i in range(len(str2)+1,1,-1):
			if c2==1:
				for x in combinations(str2,i):
					if x==x[::-1]:
						c2=max(c2,len(x))
						break
		if C<c1*c2:
			C=c1*c2
	return C
_s = raw_input()
res = funPal(_s);
print res
