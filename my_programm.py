# https://en.wikipedia.org/wiki/Nobiliary_particle
NOBILIARY_PARTICLES = set([
	# Denmark and Norway
	'af', 'von', 'de', 'der', 'dit', 'la',
	# France
	'de', 'du', 'd\'', 'des',
	# Spain
	'de', 'la',
	# Germany and Austria
	'von', 'zu', 'und',
	# England and Wales
	'de', 'of',
	# Scotland
	'of',
	# Switzerland
	'de', 'von',
	# Portugal
	'de', 'do', 'dos', 'da', 'das', 'e',
	# Italy
	'de', 'di', 'de\'', 'dei',
	# Netherlands
	'van', 'tot', 'thoe',
	# Somalia
	# 'Aw',
	# Belgium
	'de', 'der', 'van',
	# Sweden
	'af', 'von', 'de',
	# Finland
	'af', 'von',
	# Thailand
	'na'
])

name = raw_input("Please enter yor name: ")

def parse_name(name):
	barrelled_names = name.split("-")
	for i in range(len(barrelled_names)):
		particle_names = barrelled_names[i].split()
		if not all(n.isalpha() for n in particle_names):
			return 'world'
		barrelled_names[i] = " ".join(n.lower().capitalize() 
			if n not in NOBILIARY_PARTICLES else n.lower()
			for n in particle_names)
	return '-'.join(barrelled_names)

print 'hello', parse_name(name)
