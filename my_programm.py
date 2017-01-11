name = raw_input("Please enter yor name: ")

def parse_name(name):
	names = name.split("-")
	for i in range(len(names)):
		names_with_particles = names[i].split()
		if not all(n.isalpha() for n in names_with_particles):
			return 'world'
		names[i] = " ".join(n.lower().capitalize() for n in names_with_particles)
	return '-'.join(names)

print 'hello', parse_name(name)
