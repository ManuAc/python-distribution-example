import sys


def main():
	n = len(sys.argv)

	if(n > 3):
		print("Error")

	command = sys.argv[1]
	value = int(sys.argv[2])

	if(command == "ABC"):
		print(2*value)

	if(command == "XYZ"):
		print(5*value)

	if(command == "FOO"):
		print(10*value)

	sys.exit(0)


if __name__ == '__main__':
	main()
