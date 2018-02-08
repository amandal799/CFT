'''
	This is a terminal based application which mostly uses API
	provided by codeForces for filtering problems with tags , types,
	and users too.
	
	It is still in the state of development. so , on regular basis new 
	features are added.
	

	Important points :-
	
	1. KeyWords for writing commands on the terminal:-
	
	-h | -u :-  handle(s)  
	
	-tags :- problem tag(s)
	
	-type :- type (A B C D E F G H...)
	
	-pid :- problem id
	

	Demonstration:-
	
	** For Handles:-
	one or many handles can be given through command:-
	

	for one handle:-
		{-h|-u} {handle}  
	eg :-   -h tourist
	 	-u rajat1603
	
	for many handles:

	*	{-h|-u} {handle1} {handle2} ..... {handlen}
	eg:-	{-h|-u} tourist rajat1603 vicennil

	2. Any command must start with following :-
	
	* plist	{for problem List}
	* pstmt {for problem statement}
	
	3.
	*	plist can be followed by {-u|-h} , {-tags} , {-type}
	eg:- plist {it will give all the problems available on codeforces} 
	eg:- plist -tags dp greedy dfs		:- (for filtering with tags)
	eg:- plist -tags dp -type {A|B|C|D|E|F|G|H} or any combination of ABCDEFGH 		:-(for filtering with tags and type)
	eg:- plist {-u|-h} tourist -tags combinatorics math   	:-(for getting only those questions solved by user specified)

	*	pstmt must be followed by -pid and then problem id
	eg:- pstmt -pid 917D
'''

# importing important modules
import os
import sys
import readline
sys.path.append('objects/')
sys.path.append('methods/')
sys.path.append('/home/amandal799/Desktop/codeForces/')

from command import *

def main():
	cmd = command()
	while True:
		try:
			query = input("codeforces $ ")
			cmd.execute(query)
		except KeyboardInterrupt :
			print("Good Bye")
			sys.exit(0)
main()

