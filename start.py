import shutil

for i in range(50):
	shutil.copy(r'cp-hana-aa-movielens-06.md', r'cp-hana-aa-movielens-' + str(i) + '.md')