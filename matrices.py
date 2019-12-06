# Matrices en Python
# 
# Exemples d'utilisation :
# python3 matrices.py -g 1 3 3 0 5 -d
# python3 matrices.py -g 3 3 3 0 5 -a
# python3 matrices.py -g 2 3 3 0 5 -cf x 2
# python3 matrices.py -g 1 3 3 0 5 -c
# 
# Reste à faire : multiplication de matrices
#
# [[3, 2, 0, 5, 2, 4, 2, 0, 5, 1], [5, 4, 2, 5, 5, 5, 5, 1, 3, 5], [2, 0, 3, 3, 2, 4, 5, 1, 0, 1], [1, 1, 2, 3, 0, 1, 2, 2, 4, 2], [0, 3, 0, 2, 4, 0, 2, 2, 2, 4], [4, 2, 0, 1, 2, 5, 4, 3, 5, 5], [3, 5, 2, 2, 5, 2, 1, 3, 0, 4], [4, 4, 1, 3, 4, 0, 3, 2, 5, 1], [3, 2, 3, 2, 3, 2, 2, 3, 4, 2], [3, 5, 1, 4, 5, 1, 3, 0, 4, 0]]

import random, sys
from copy import deepcopy
from fractions import Fraction

def genmat(n,m,mn,mx):
	mat = list()
	for i in range(0,n):
		ln = list()
		for j in range(0,m):
			ln.append(random.randint(mn,mx))
		mat.append(ln)
	return mat

def affmat(mat):
	if mat != False:
		for i in mat:
			for j in i:
				if not "-F" in sys.argv:
					print(str(j)+" ", end='')
				else:
					print(str(Fraction(j))+" ", end='')
			print("")

def veriflen(mat1,mat2):
	if len(mat1) == len(mat2):
		n = 0
		m = 0
		for i in mat1:
			n += len(i)
		for i in mat2:
			m += len(i)
		if m == n:
			return True
	return False

def verifcaree(mat):
	n = len(mat)
	m = 0
	for i in mat:
		m += len(i)
	m /= len(mat)
	if n == m:
		return True
	return False

def addorsub(t,mat1,mat2):
	if veriflen(mat1,mat2):
		mat = list()
		for i in range(0,len(mat1)):
			ln = list()
			for j in range(0,len(mat1[0])):
				ln.append(mat1[i][j]+mat2[i][j]*pow(-1,t))
			mat.append(ln)
		return mat
	return False

def mult(mat1,mat2):
	return mat1

def radius(mat,n,m):
	matr = deepcopy(mat)
	matr.pop(n-1)
	for i in matr:
		i.pop(m-1)
	return matr

def det(mat):
	if len(mat) == 2:
		return mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]
	else:
		dt = 0
		for i in range(0,len(mat)):
			if mat[i][0] != 0:
				dt += det(radius(mat,i+1,1))*pow(-1,i)*mat[i][0]
		return dt

def comm(mat):
	matr = deepcopy(mat)
	for i in range(0,len(matr)):
		for j in range(0,len(matr[i])):
			matr[i][j] = det(radius(mat,i+1,j+1))*pow(-1,i+j)
	return matr

def transp(mat):
	matr = list()
	for i in range(0,len(mat[0])):
		matr.append(list())
		for j in range(0,len(mat)):
			matr[i].append(mat[j][i])
	return matr

def coeff(t,mat,cf):
	matr = deepcopy(mat)
	for i in range(0,len(matr)):
		for j in range(0,len(matr[i])):
			if t != 2:
				matr[i][j] += cf*pow(-1,t)
			else:
				matr[i][j] *= cf
	return matr

def inv(mat):
	dt = det(mat)
	if dt != 0: return coeff(2,transp(comm(mat)),1/dt)
	return False

matrices = list()
n = random.randint(-5,5)
mn = -5
mx = 5
op = 0
nb = 1

i = -1
for arg in sys.argv:
	i += 1
	if arg == "-g":
		nb = int(sys.argv[i+1])
		n = int(sys.argv[i+2])
		m = int(sys.argv[i+3])
		mn = int(sys.argv[i+4])
		mx = int(sys.argv[i+5])
	if arg == "-a":
		op = 1
	if arg == "-s":
		op = 2
	if arg == "-cf":
		cfop = str(sys.argv[i+1])
		cf = int(sys.argv[i+2])
		op = 3
	if arg == "-m":
		op = 4
	if arg == "-d":
		op = 5
	if arg == "-t":
		op = 6
	if arg == "-c":
		op = 7
	if arg == "-i":
		op = 8

for i in range(0,nb):
	matrices.append(genmat(n,m,mn,mx))
	# matrices.append([[3, 2, 0, 5, 2, 4, 2, 0, 5, 1], [5, 4, 2, 5, 5, 5, 5, 1, 3, 5], [2, 0, 3, 3, 2, 4, 5, 1, 0, 1], [1, 1, 2, 3, 0, 1, 2, 2, 4, 2], [0, 3, 0, 2, 4, 0, 2, 2, 2, 4], [4, 2, 0, 1, 2, 5, 4, 3, 5, 5], [3, 5, 2, 2, 5, 2, 1, 3, 0, 4], [4, 4, 1, 3, 4, 0, 3, 2, 5, 1], [3, 2, 3, 2, 3, 2, 2, 3, 4, 2], [3, 5, 1, 4, 5, 1, 3, 0, 4, 0]])
	print("Matrice",i+1,":",matrices[i])
	affmat(matrices[i])

if nb > 1 and (op == 1 or op == 2 or op == 4):
	if op == 1:
		print("Addition des matrices :")
	if op == 2:
		print("Soustraction des matrices :")
	if op == 4:
		print("Multiplication des matrices :")
		print("Là C compliqué, savoir faire des inverses de matrices n'est pas supplicant.")
	matr = matrices[0]
	for i in range(1,nb):
		if op == 1:
			matr = addorsub(0,matr,matrices[i])
		if op == 2:
			matr = addorsub(1,matr,matrices[i])
		if op == 4:
			if len(matr[0]) == len(matrices[i]):
				matr = mult(matr,matrices[i])
	affmat(matr)
else:
	for i in range(0,nb):
		if op == 3:
			if cfop == "+":
				print("Addition par",cf," pour la matrice ",i+1,":")
				affmat(coeff(0,matrices[i],cf))
			if cfop == "-":
				print("Soustraction par",cf," pour la matrice ",i+1,":")
				affmat(coeff(1,matrices[i],cf))
			if cfop == "x":
				print("Multiplication par",cf," pour la matrice ",i+1,":")
				affmat(coeff(2,matrices[i],cf))
		if op == 5:
			if verifcaree(matrices[i]):
				print("Déterminant de la matrice",i+1,":",det(matrices[i]))
			else:
				print("Déterminant de la matrice",i+1,": 0")
		if op == 6:
			print("Transposée de la matrice",i+1,":")
			affmat(transp(matrices[i]))
		if op == 7:
			print("Commatrice de la matrice",i+1,":")
			if verifcaree(matrices[i]):
				affmat(comm(matrices[i]))
		if op == 8:
			print("Inverse de la matrice",i+1,":")
			if verifcaree(matrices[i]):
				affmat(inv(matrices[i]))
