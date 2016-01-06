""" 
Jack and Jill are two friends. They both are hungry but they have only a few cakes with them. So they started playing a game to grab those cakes. Initially they  have N number of cakes with them. Jack starts the game by making the first move. The game is such that in each turn one has to choose a move from a set of moves which consists of all the possible moves for removing p cakes from the table, where p is any prime and k is any non­negative integer. The winner is the one who takes the last cake. Identify who will win the game, assuming both the players follow a perfect strategy? If Jack wins, what will be the smallest possible number that he can remove in his first move? 
Input
An integer T, denoting the number of test cases.
Each test case contains one integer N, the number of chips on the table.
Output
Print "Jack" if Jack wins or "Jill" if Jill wins. Print the output for each test case on a
new line (without quotes).
Constraints
1 <= T <= 100000
1 <= N <= 100000
Sample Input :
3
1
5
6
Sample Output:
Jack 1
Jack 5
Jill
"""
def get_prime(n):
	prime_nos = []
	for x in range(2,n+1):
		prime = True
		for i in range(2,x):
			if (x%i==0):
				prime = False
		if prime == True:
		   prime_nos.append(x)
	return get_moves(prime_nos, n)

def get_moves(prime_nos, n):
	moves_array = []
	for no in prime_nos:
		i = 0
		while True:
			if (no ** i <= n):
				moves_array.append(no ** i)
				i = i+1
			else:
				break
	return list(set(moves_array))

def get_small_move(moves, n):
	print moves
	if n == 0:
		return 0
	for move in moves:
		if (n-move) not in moves:
			small_move = move
			return small_move
		else:
			get_small_move(moves, n-move)
	return 0
		

		

if __name__ == '__main__':
	n = raw_input()
	n = int(n)
	moves  = []
	moves = get_prime(n)
	if n == 1:
		small_move = 1
	else:
		small_move = 0
	small_move = get_small_move(moves, n)
	if small_move == 0 and n != 1:
		print "Jill"
	else:
		print "Jack ", small_move
		
