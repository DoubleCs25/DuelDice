from random import randrange
print("We are going to play Dice Duels, there will be three rounds")

win=3
plyr1roll=0
plyr2roll=0

plyr2win=0
plyr1win=0

while(plyr1win != win and plyr2win != win):
	plyr1roll=randrange(1,6)
	print(plyr1roll)
	plyr2roll=randrange(1,6)
	print(plyr2roll)
	if(plyr1roll>plyr2roll):
		plyr1win+= 1
		print("plyr1, you win this one")

	if(plyr2roll>plyr1roll):
		plyr2win+= 1
		print("plyr2, you win this one")

	if(plyr1win==3):
		print("plyr1, you win bud")
	if(plyr2win==3):
		print("plyr2, you win bud")