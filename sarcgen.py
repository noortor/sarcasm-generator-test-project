"""Test Project to randomize letters based
on an inputed message."""

from random import randint

def sarcasm_gen(phrase):
	if phrase == '':
		return ''
	elif randint(0,1):
		return phrase[0].upper() + sarcasm_gen(phrase[1:])
	return phrase[0].lower() + sarcasm_gen(phrase[1:])

message = input("Type in any phrase ")
print(sarcasm_gen(message))