name = raw_input("Please enter yor name: ")

def is_valid(name):
	if name.isalpha():
		return True
	return False


if is_valid(name):
	print 'hello', name
else:
	print 'hello world'
