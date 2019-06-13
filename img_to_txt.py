# imports
import os
from subprocess import call

# defines
def main(_input, _output):
	if os.path.exists(_input) == True:
		count = 0
		files = 0

		for f in os.listdir(_input):
			ext = os.path.splitext(f)[1]

			count += 1
			image_file_name = os.path.join(_input, f)
			filename = os.path.splitext(f)[0]
			filename = ''.join(e for e in filename if e.isalnum() or e == '-')
			text_file_path = os.path.join(_output, filename)

			call(["tesseract", image_file_name, text_file_path], stdout = open(os.devnull, 'w'))
			print("Complete")
	else:
		print("No directory found")

if __name__ == "__main__":
	_input = os.path.abspath("input")
	main(_input, "output")
