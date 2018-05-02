#!/usr/bin/python

zifu = '!@#$%&abcdefghijklmnopqrstuvwxyz0123456789'
'''
c = 0
while c<zifulen:
	print zifu[c],
	c +=1
'''
pwdstr = ''
a = 0
b = 0
c = 0
fd = open("passwd.txt", 'w')
zifujz = [0,0,0,0,0,0]
while zifujz[0] < len(zifu):
	while zifujz[len(zifujz)-1] < len(zifu):
		while c < len(zifujz):
			pwdstr += zifu[zifujz[c]]
			c += 1
		c = 0
		pwdstr += '\n'
		#print pwdstr
		fd.write(pwdstr)
		pwdstr = ''
		zifujz[len(zifujz)-1] += 1
	b = len(zifujz)-2
	while b >= 0:
		if zifujz[b] == len(zifu)-1:
			if b == 0:
				break
			else:
				b -= 1
		else:
			zifujz[b] +=1
			c = b + 1
			while c < len(zifujz):
				zifujz[c] = 0
				c += 1
			break
'''
pwdstr = zifu[zifujz[0]] + zifu[zifujz[1]] 

zifulen = len(zifu)
zifuposition=0
offset = 0
'''
#while zifuposition<zifulen
#	zif
	
fd.close()
