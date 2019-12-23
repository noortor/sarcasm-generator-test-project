"""Test Project to randomize letters based
on an inputed message."""

import random

def sarcasm_gen(phrase):
	for i in range(phrase):
		if round(random.random()):
			phrase[i].upper()
	return phrase

message = input()