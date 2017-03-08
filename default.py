#===============================================================================
# Sean Corrigan 2017
# ICS 3U1
# Game of 31
#===============================================================================

# import libraries
import os  # Needed for clearing the terminal in a clear manner
import sys  # Needed for seemless restarts
import random
import time
import shelve # Needed for saving highscore
#########
#Set a few variables so eveything doesnt explode
highscore = 0
highname = "N/A"



os.system("clear")
d = shelve.open('highscore')
try: # Just in case the file doesn't exist 
	highscore = d['percent']
	highname = d['name']
except:
	lo = 1
	
print ("Welcome to the python name sorting program")
print "Highscore is %", highscore, "by", highname.title()
name = raw_input("What is your name? ")
os.system("clear")


while 1 == 1:
	def test():
		os.system("clear")
		wins = 0
		print "How many times would you like to roll", name.title(),"?" # ask how many rolls to perform
		rolls = raw_input("")
		os.system("clear")
		try:  # Try to convert to a int. if not restart
	  		rolls = int(rolls)  # Define as interger
		except ValueError:  # If it isn't a whole number then
			raw_input("WAIT A MINUTE, WHOOOOO ARE YOUUU (PRESS ENTER TO RESTART)")
			del rolls
			test()
		
		
		print "Shuffling", rolls, "Times"
		time.sleep(1)
		
		x = 0
		while x < rolls:
			random1 = random.randrange(7, 13, 1)
			random2 = random.randrange(7, 13, 1)
			random3 = random.randrange(7, 13, 1)
			total = random1 + random2 + random3
			print random1, random2, random3
			print "Total:", total
			print ""
			x = x + 1
			if total == 31:
				wins = wins + 1
		
		percent = 1. * wins / rolls
		percent = percent * 100
		
		if highscore < percent: #If the highscore is lower then current roll then write to file
			d = shelve.open('highscore') # here you will save details of the Highscore
			d['percent'] = percent       # thats all, now ;ercentit is saved on disk.
			d['name'] = name       	# thats all, now it is saved on disk.
			d.close()
		
		
		print "You rolled 31,", wins,"/", rolls, "times. Or %",percent, "of the time"
		
		
		wait = raw_input("PRESS ENTER TO CONTINUE")
		test()
	test()