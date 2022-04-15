import os
import tkinter.filedialog as fd

a = fd.askdirectory()
open('output.txt','w').close()
o = open('output.txt','a')
def search(a, b):
	for file in os.listdir(a):
		if os.path.isfile(a + '\\' + file):
			if b in file:
				print('/> ', a + '\\' + file, ' collected')
				o.write(open(a + '\\' + file).read())
		else:
			search(a + '\\' + file, b)
search(a,'Tokens.txt')
o.close()
tk = len(open('output.txt').read().split('\n'))
input(f'{tk-1} tokens found.')