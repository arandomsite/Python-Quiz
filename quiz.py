#!/usr/bin/env python3

import os

done = False

while not done:
	os.system('cls' if os.name == 'nt' else 'clear')

	answers = {1:2, 2:4, 3:1}

	print("Python Quiz!\n")
	print("============\n")
	# Question 1
	print("Question 1: Who made the programming language Python?\n")
	print("1. Brendan Eich\n")
	print("2. Guido van Rossum\n")
	print("3. Tim Berners-Lee\n")
	print("4. Rasmus Lerdorf\n")
	questionOneInput = int(input(":"))
	if answers[1] == questionOneInput:
		questionOneScore = 1
	else:
		questionOneScore = 0
	
	# Question 2
	print("Question 2: Which entity started the Internet?\n")
	print("1. NASA\n")
	print("2. CIA\n")
	print("3. AT&T\n")
	print("4. CERN\n")
	questionTwoInput = int(input(":"))
	if answers[2] == questionTwoInput:
		questionTwoScore = 1
	else:
		questionTwoScore = 0
	
	# Question 3
	print("Question 3: Who created Linux?\n")
	print("1. Linus Torvalds\n")
	print("2. Mark Shuttleworth\n")
	print("3. Dennis Ritchie and Ken Thompson\n")
	print("4. Ian Murdock\n")
	questionThreeInput = int(input(":"))
	if answers[3] == questionThreeInput:
		questionThreeScore = 1
	else:
		questionTwoScore = 0
		
	# Score
	quizScore = questionOneScore + questionTwoScore + questionThreeScore
	quizScoreStr = str(quizScore)
	quizPercentage = quizScore * 33.3333333333;
	if quizScore == 3:
		quizPercentage = 100;
	quizPercentageInt = int(quizPercentage)
	quizPercentageStr = str(quizPercentageInt)
	print("You got " + quizScoreStr + " questions out of 3 correct!\n")
	print("You scored a " + quizPercentageStr + "%!\n")
	
	
	# Redo
	redo = input("Would you like to redo the quiz? (y/n): \n")
	if redo.lower() != 'y':
			done = True