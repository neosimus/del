name = raw_input("Please enter yor name: ")

def parse_name(name):
	if all(n.strip().isalpha() for n in name.split('-')):
		return name.lower().capitalize()
	else:
		return 'world'


print 'hello', parse_name(name)
