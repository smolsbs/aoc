#!/usr/bin/python
from hashlib import md5

def hashMyId(doorID, part2=False):
	code = ['-' for _ in range(8)]
	i = 1
	runs = 0
	while runs != 8:
		a = doorID + str(i).encode("utf-8")
		aHashed = md5(a).hexdigest()
		if aHashed[:5] == '00000':
			if part2:
				pos = int(aHashed[5], 16)
				if pos < 8:
					if code[pos] is '-':
						code[pos] = aHashed[6]
						runs += 1
			else:
				code[runs] = aHashed[5]
				runs += 1
		i += 1

	return ''.join(code)



def main():
	with open('input', 'r') as fp:
		doorID = fp.read().strip().encode("utf-8")

	print("Part 1: {}".format(hashMyId(doorID)))
	print("Part 2: {}".format(hashMyId(doorID, True)))


			

if __name__ == '__main__':
	main()