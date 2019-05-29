# hoc python
'''def double(num):
	""" dong nay la comment ne"""
	return 2*num
# print(double.__doc__) # result: dong nay la comment ne 
# nhap tu ban phim, built: ctrl + alt + b
name = input("ban ten gi: ")
age = input("ban bao nhieu tuoi:")
print(name + " is " + str(age) + " years old")

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
# List
m = [1,'s',4.6]
print(m)

# Tupe : (10, 'h') const
# set a = {5,2,'s',4}  các phần tử trong set không có thứ tự. 
m = { 1, 'chao', 5, 2 }
m.update([2,3,4])
print(m) # {1, 2, 3, 4 ,5 ,'chao'}

# dictionary
dict1 ={ 'tên': 'Dong', 'age': 22}
print(dict1['tên'])

letter = ['a','b','c']
upletter = [ x.upper() for x in letter]
print(upletter)
'''
# hàm vô danh
tich= lambda s : s*2 
print(tich(4))


