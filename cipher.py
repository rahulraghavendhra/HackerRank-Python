"""
Alice has taken up cryptography course. She recently learnt the interesting topic

of transposition ciphers. In transposition ciphers, the cipher is keyed by a word or

phrase not containing any repeated letters. The purpose of the key is to order the

columns, with column 1 being under the lexicographically smallest key letter and

so on. The plaintext is written horizontally, in rows, padded to fill the matrix if need

be(with abcdef....). The ciphertext* is read out by columns, starting with the

column whose key letter is the lowest. Help her convert

Note: Lexicographical ordering is same as the roman alphabetical ordering i.e. A

is smallest and B is greater than A and Z is the greatest.

Input format:

First line contains the key, a single word with all uppercase alphabets without any

white spaces in between.

Second line contains an integer N

N lines follow, each containing a single plaintext, a word with all uppercase

alphabets without any white spaces in between.

Output format:

Output is N lines each containing the ciphertext for the corresponding plaintext,

with all uppercase roman alphabets.

Constraints:

1<=N<=1000

1<=Key length<=10

1<=Plaintext length<=1000

Sample Input

DELHI

1

thankyouforyourcooperation

https://www.hackerrank.com/tests/eoihki03k1o/questions/fn23ecjcs87 1/3

1/3/2016 VISA Coding Challenge 2015-2016 :: powered by HackerRank

Sample Output

TYRCRNHOYOAANFUPICKOREODAUOOTB

Explanation

key: DELHI

Plaintext: thankyouforyourcooperation

1 2 5 3 4

t h a n k

y o u f o

r y o u r

c o o p e

r a t i o

n a b c d ­> last row is having only 1 character, so we pad it with abcd.

As you read the columns vertically, based on the key, you will arrive at the

ciphertext: TYRCRNHOYOAANFUPICKOREOD

"""


def encode(txt,key):
	sz = len(key)  # how big are the columns 
	cols = list(map("".join,zip(*zip(*[iter(txt)]*sz)))) # list partitioned into columns
	return "".join([cols[key.index(str(c))] for c in range(1,sz+1)])


if __name__ == '__main__':
	key = raw_input()
	n = raw_input()
	output_array = []
	sorted_key = sorted(key)
	final_key = []
	for char in key:
		final_key.append(str(sorted_key.index(char) + 1))
	key_string = ''.join(final_key)
	padding_text = "abcdefghijklmnopqrstuvwxyz"
	for i in range(int(n)):
		plain_text = raw_input()
		pad_no = len(plain_text)%len(key_string)
		if pad_no != 0:
			pad_length = len(key_string) - pad_no
			plain_text = plain_text + padding_text[:pad_length]
		encoded = encode(plain_text,key_string)
		output_array.append(encoded)
	for output in output_array:
		print output.upper()
