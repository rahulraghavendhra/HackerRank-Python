"""
Roy loves to play with numbers and digits. His lucky numbers are 3 and 5 for that
he believes that the numbers containing 3 and 5 are also lucky numbers for him.
For example 335, 355, 533 are lucky but 435, 137 etc. aren’t lucky. Now Roy is
interested in some extra­lucky numbers.
Extra lucky numbers are those which contains 3 and 5 and removing some but not
all digits you can covert that into a lucky number. Like 37455 is extra lucky as you
can convert that to a lucky number by removing 7 and 4.
Now Roy wants to develop an algorithm which will help him to calculate the
number of positive dividers of a given number (n) which are extra lucky. Help him
to develop that algorithm.
Input
Output
Constraints
1 ≤ T ≤ 10
1 ≤ n ≤ 10^9
Time Limit : 1 second.
Sample Input :
10
1
2
3
4
5
6
7
8
9
10
Sample Output :
0
0
1
0
1
1
0
0
2
1
"""
def prime_factors(n):
	i = 2
	factors = []
	while i * i <= n:
		if n % i:
			i += 1
		else:
			n //= i
			factors.append(i)
	if n > 1:
		factors.append(n)
	return factors

output_array = []
test_case = input()
for i in xrange(0,test_case):
	n = input()
	factors_n = prime_factors(n)
	count = 0
	for factor in factors_n:
		if factor == 3 or factor == 5:
			count += 1
	output_array.append(count)
for element in output_array:
	print element
