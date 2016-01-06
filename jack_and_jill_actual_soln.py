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

n = input()
for test in xrange(0,n):
    num_cakes = input()
    rem = num_cakes % 6
    if rem == 0:
        print("Jill")
    else:
        print("Jack "+str(rem))
