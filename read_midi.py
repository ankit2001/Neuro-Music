

from imports import *

def read(file, head):
	midi_file = converter.parse(file)
	parsing_notes = midi_file.flat.notes
	if len(parsing_notes) > head:
		head = len(parsing_notes)
	for el in parsing_notes[:head]:
		print(el, el.offset)

"""
#Testing sources 
if __name__ == "__main__":
	read("dataset/aguado-op03n02.mid", 20)
"""


