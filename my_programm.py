name = raw_input("Please enter yor name: ")

def parse_name(name):
	names = [n.strip() for n in name.split("-")]
	if all(n.isalpha() for n in names):
		return '-'.join(n.lower().capitalize() for n in names)
	else:
		return 'world'


print 'hello', parse_name(name)
