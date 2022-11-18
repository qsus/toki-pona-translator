#!/usr/bin/python3

import json
dictionary = json.load(open('toki-pona.json'))

print("\n\nProgram can be stopped at any time by entering nothing.")

def printDef(word):
	print(f"\n{c.G}{c.BOLD}{word}{c.NOBD}: {dictionary[word]}")

def printOther(word):
	print(f"{c.O}{word}{c.END} ", end="")

class c:
	G = '\033[92m'
	O = '\033[93m'
	R = '\033[91m'
	B = '\033[94m'
	BOLD = '\033[1m'
	NOBD = '\033[22m'
	END = '\033[0m'

while True:
	try:
		phrase = input(f"{c.B}Enter toki pona phrase: {c.END}")
	except KeyboardInterrupt:
		break

	# exit
	if phrase == '':
		break

	for word in phrase.split():
		wordNoPunc = word.strip('.,!?:;')
		if wordNoPunc in dictionary:
			printDef(wordNoPunc)
		else:
			printOther(word)

	print() # newline


# on exit
print(f"{c.B}Goodbye!{c.END}")
