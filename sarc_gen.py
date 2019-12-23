"""Test Project to randomize letters based
on an inputed message."""

import random

def sarcasm_gen(phrase):
	for i in range(phrase):
		if round(random.random()):
			phrase[i].upper()
		else:
			phrase[i].lower()
	return phrase

message = input()