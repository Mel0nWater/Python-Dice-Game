import random

#SETUP

#usernames
p1 = input('Enter Player one name ')
p2 = input('Enter Player two name ')

#dies

p1d1 = None
p1d2 = None

p2d1 = None
p2d2 = None


#constant randomise
#if p1d1 != 0 and p1d2 != 0 and p2d1 != 0 and p2d2 != 0:
#		p1d1, p1d2, p2d1, p2d2 = random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)

#scores
p1s = 0
p2s = 0

#round tracker
cap = 5
cround = 0

#RULES
print('This is a 2 player Dice game')
input()
print('the rules are simple:')
input()
print('there are five rounds')
input()
print('each round, you will both roll two die')
input()
print('get an even total and your score increases by 10. Get an odd total and your score gets taken away by five. ')
input()
print('roll a double, and you get to have another roll')
input()
print('at the end, whoever has the most points wins')
input()
print('If the points are the same, the game keeps going')
input()
print('game starts in 3...')
input()
print('2...')
input()
print('1...')
input()
print('go!')
input()

#GAME
while cround < cap:


	print(f'ROUND {cround + 1}')

	#roll
	
	if p1d1 != 0 and p1d2 != 0 and p2d1 != 0 and p2d2 != 0:
		p1d1, p1d2, p2d1, p2d2 = random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)


	print(f'{p1} dice rolls: {p1d1} and {p1d2}')
	input()
	print(f'{p2} dice rolls: {p2d1} and {p2d2}')
	
	#add scores
	p1s += p1d1 + p1d2
	p2s += p2d1 + p2d2
	
	input()
	
	#double checking
	
	if p1d1 == p1d2:
		
		#keep giving chances if double is true

		while p1d1 == p1d2:

			print(f'{p1} got a double! Roll another!')

			#reset the dies
			p1d1, p1d2 = random.randint(1,6), random.randint(1,6)

			input()

			print(f'{p1} dice rolls: {p1d1} and {p1d2}')

			input()
		

	#player 2	
	if p2d1 == p2d2:

		while p2d1 == p2d2:

			print(f'{p2} got a double! Roll another!')

			#reset dies
			p2d1, p2d2 = random.randint(1,6), random.randint(1,6)


			input()

			print(f'{p2} dice rolls: {p2d1} and {p2d2}')

			input()

	#even or odd

	#player 1

	if (p1d1+p1d2) % 2 == 0:
		print(f"{p1}'s total is even! + 10 points!")
		p1s += 10

	elif (p1d1+p1d2) % 2 != 0 and p1s >= 5:
		print(f"{p1}'s total is odd! No points!")


	else:
		print(f"{p1}'s total is odd! -5 points!")
		p1s -= 5

	#player 2
	if (p2d1+p2d2) % 2 == 0:
		print(f"{p2}'s total is even! + 10 points!")
		p2s += 10

	elif (p2d1+p2d2) % 2 != 0 and p2s >= 5:
		print(f"{p2}'s total is odd! No points!")


	else:
		print(f"{p2}'s total is odd! -5 points!")
		p1s -= 5

	input()

	#increase
	cround +=1

#RESULTS
print('(ﾉ◕ヮ◕)ﾉ*:・ﾟ✧RESULTS')
input()

#p1 scores
print(f'{p1} results:')
input()
print(p1s)
input()

#p2 scores
print(f'{p2} results:')
input()
print(p2s)
input()

#measurements

#p1 wins
if p1s > p2s:
	print(f'{p1} wins!')
	input()
	print('Game end')

#p2 wins
elif p2s > p1s:
	print(f'{p2} wins!')
	input()
	print('Game end')

#tie
else:

	print('(͡ ° ͜ʖ ͡ °)... tie...')
	input()
	print('REMATCH')
	input()