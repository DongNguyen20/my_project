# hoc python
'''def double(num):
	""" dong nay la comment ne"""
	return 2*num
# print(double.__doc__) # result: dong nay la comment ne 
# nhap tu ban phim, built: ctrl + alt + b
name = input("ban ten gi: ")
age = input("ban bao nhieu tuoi:")
print(name + " is " + str(age) + " years old")
print("toi {}".format(name))
print("Kia %s nang %d kg" %('ban', 55))
b = 8 + 2j
print(isinstance(b, complex))

# Phân số 
import fractions
print(fractions.Fraction(4.5))# chuyển thập phân thành phân số

# for:
count = 0
for i in " Nguoi da doi thay":
	if(i == 'o'):
		count += 1
print(count)
for i in range(10):
	print(i)

# hàm enumerate() trả về liệt kê
a = 'Python'
b = list(enumerate(a))
print(b) #[(0, 'P'), (1, 'y'), (2, 't'), (3, 'h'), (4, 'o'), (5, 'n')]

print('toi ga lam'.split())
# LIST
m = [1,'s',4.6]
print(m)

# TUPLE : (10, 'h') const
# set a = {5,2,'s',4}  các phần tử trong set không có thứ tự. 
m = { 1, 'chao', 5, 2 }
m.update([2,3,4])
print(m) # {1, 2, 3, 4 ,5 ,'chao'}

# DICTIONARY
dict1 ={ 'tên': 'Dong', 'age': 22}
print(dict1['tên'])

letter = ['a','b','c']
upletter = [ x.upper() for x in letter]
print(upletter)

# hàm vô danh
tich= lambda s : s*2 
print(tich(4))

# iterator : __iter__(), __next__()
# file 
a = open('C:/Users/admin/Desktop/abc.txt',mode= 'r') 
# read
f= a.readline()
print(f)
a.close()

# thu muc
import os
print(os.getcwd())

# class
class Person:
	def __init__(self, name, age):
		self.name=name
		self.age= age
	def myFunc(self):
		print("My name is "+ self.name, "age:"+ str(self.age))
p1 = Person("Hary", 22)
p1.myFunc()

def BangCuuChuong():
	n = input('Nhap so luong: ')
	print('-------------------------------------Bang Cuu Chuong-----------------------------------------------')
	if(int(n) <= 5):
		XuatBangCon(1,n)
	else:
		XuatBangCon(1,5)
		print()
		XuatBangCon(6,n)
	
def XuatBangCon(a,b):
		for j in range(10):
			for i in range(int(a),int(b)+1):
				line =" {0} x {1} = {2}". format(i,j,i*j)
				print(line, end = '\t')
			print()

if __name__ == '__main__':
	BangCuuChuong()
'''

class Nguoi:
	#Lop cha
	def __int__(self):
		self.ten
		self.tuoi
		self.Cao
	
	def nhap(self):
		self.ten = input('Nhap ten: ')
		self.tuoi = input('Nhap tuoi: ')
		self.Cao = input('Chieu cao: ')
	def Xuat(self):
		print(" ten la: {} ,tuoi la {} ".format(self.ten, self.tuoi))
	def __del__(self):
		#print('deconstructor duoc goi!')
		del self.ten, self.tuoi, self.Cao
# Ke thua
class TreEm(Nguoi):
	# Lop con
	def IsBaby(self):
		if(int(self.tuoi) <= 12):
			print('La tre em!')
		else:
			print('Khong phai tre em!')
# Da Ke Thua
class First:
	def getClass(self):
		print('Lop 1')
		#super().getClass() muon in them class Second thi them dong nay 
class Second:
	def getClass(self):
		print('Lop 2')
class Third(First, Second):
	def getClass(self):
		print('Lop 3')
		super().getClass()

m = Third()
m.getClass()

