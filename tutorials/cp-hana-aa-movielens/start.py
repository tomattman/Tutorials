import shutil

for i in range(50):
	#shutil.copy(r'cp-hana-aa-movielens-' + str(i) + '.md', r'cp-hana-aa-movielensC-' + str(i) + '.md')
	r = open('cp-hana-aa-movielensC-' + str(i) + '.md', 'r')
	w = open('cp-hana-aa-movielens-' + str(i) + '.md', 'w')
	index = 0
	for line in r:
		if index == 1:
			w.write(line + '  ' + str(i))
		else:
			w.write(line)
	r.close()
	w.close()
#l = [line.strip() for line in f]
#print(l[1])