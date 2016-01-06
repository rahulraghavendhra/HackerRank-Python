"""
Problem Statement

Your teacher has given you the task of drawing a staircase structure. Being an expert programmer, you decided to make a program to draw it for you instead. Given the required height, can you print a staircase as shown in the example?

Input 
You are given an integer N depicting the height of the staircase.

Output 
Print a staircase of height N that consists of # symbols and spaces. For example for N=6, here's a staircase of that height:

     #
    ##
   ###
  ####
 #####
######
Note: The last line has 0 spaces before it.
"""
# Complete the function below.


def StairCase(n):
	for i in range(1,n+1):
		stair_array = []
		j = 1
		while(j <= n):
			if(j <= i):
				stair_array.append('#')
			else:
				stair_array.append(' ')
			j = j + 1
		
		reversed_array = list(reversed(stair_array))
		for element in reversed_array:
			print(element),
		print
_n = int(raw_input().strip("\n"))
StairCase(_n)
