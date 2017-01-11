name = raw_input("Please enter yor name: ")

def parse_name(name):
	if name.isalpha():
		return name.lower().capitalize()
	else:
		return 'world'


print 'hello', parse_name(name)
