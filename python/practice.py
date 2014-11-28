def rest_of_string(s)
	return s[1:]

print rest_of_string('audacity')

def square(n):
	return n*n
x = 37
print square(x)

def sum3(a, b, c):
	return a+b+c

def abbaize(a, b):
	return a+b+b+a

def find_second(search, target):
	first = search.find(target)
	second = search.find(target, first+1)
	return second

def absolute(x):
	if x < 0:
		x = -x
	return x

def bigger(a, b):
	if a > b:
		return a
	return b

def bigger(a, b):
	if a > b:
		return a
	else:
		return b

def is_friend(name):
	if name[0] == 'D':
		return True
	else:
		return False

def is_friend(name)
	return name[0] == 'D'


def is_friend(name):
	if name[0] == 'D':
		return True
	if name[0] == 'N':
		return True
	return False

def is_friend(name):
	if name[0] == 'D':
		return True
	else:
		if name[0] == 'N':
			return True
		return False

def is_friend(name):
	if name[0] == 'D':
		return True
	else:
		if name[0] == 'N':
			return True
		else:
			return False

def is_friend(name)
	return name[0] == 'D' or name[0] == 'N'


def biggest(a, b, c):
	if a > b:
		if a > c:
			return a
		else:
			return c
	else:
		if b > c:
			return b
		else:
			return c 

def biggest(a, b, c):
	return bigger(bigger(a,b), c)

def print_numbers(n):
	i = 1
	while i <= n:
		print i
		i = i + 1

def print_numbers(n):
	i = 0
	while i < n:
		i = i + 1
		print i

def factorial(n):
	result = 1
	while n >= 1:
		result = result * n
		n = n - 1
	return result

def print_number(n):
	i = 1
	while True:
		if i > n:
			break
		print i
		i = i + 1

while <T>:
	<S>

while True:
	if not <T>:
		break
	<S>

while <T>:
	<S>
	if <T>:
		<S>
	else:
		break

def udacify(s):
    return 'U'+ s

def median(a, b, c):
    x = biggest(a, b, c)
    if a == x:
        return bigger(b, c)
    else:
        if b == x:
            return bigger(a, c)
        else:
            return bigger(a, b)

def median(a, b, c):
	big = biggest(a,b,c)
	if big == a
		return bigger(b,c)
	if big == b
		return bigger(a,c)
	else:
		return bigger(a,b)

def countdown(n):
    while n > 0:
        print n
        n = n-1
    print 'Blastoff!'

n = any positive integer
while n != 1:
	if n % 2 == 0: #n is even
		n = n/2
	else:
		n = 3 * n + 1

def find_last(s, t):
	last_pos = -1
	while True:
		pos = s.find(t, last_pos+1)
		if pos == -1:
			return last_pos
		last_pos = pos
	return last_pos

stooges = ['Moe', 'Larry', 'Curly']
#mutation
stooges[2]='Shemp'
stooges.append('Shemp')

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
def how_many_days(n):
    return days_in_month[n-1]

mixed_up = ['apple', 3, 'oranges', 27, [1, 2, ['alpha', 'beta']]]
beatles = [['John', 1940], ['Paul', 1942], ['George', 1943], ['Ringo', 1940]]

countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]
print countries[1][1]
print countries[0][2]/countries[2][2]

def print_all_elements(p):
	i = 0
	while i < len(p):
		print p[i]
		i = i + 1

def print_all_elements(p):
	for e in p:
		print e

def sum_list(list):
    sum = 0
    for e in list:
        sum = sum + e
    return sum

def measure_udacity(list):
    count = 0
    for e in list:
        if e[0] == 'U':
            count = count + 1
    return count


def find_element(list, target):
    i = 0
    while i < len(list):
        if list[i] == target:
            return i
        i = i + 1
    return -1

def find_element(list, target):
    i = 0
    for e in list:
		if e == target:
			return i
		i = i + 1
    return -1


def find_element(list, target):
    if target in list:
        return list.index(target)
    else:
        return -1

def product_list(list):
    ret = 1
    for e in list:
        ret = ret * e
    return ret

def greatest(list):
    ret = 0
    for e in list:
        if e > ret:
            ret = e
    return ret

udacious_univs = [['Udacity',90000,0]]

usa_univs = [ ['California Institute of Technology',2175,37704],
              ['Harvard',19627,39849],
              ['Massachusetts Institute of Technology',10566,40732],
              ['Princeton',7802,37000],
              ['Rice',5879,35551],
              ['Stanford',19535,40569],
              ['Yale',11701,40500]  ]

def total_enrollment(list):
    ret1 = 0
    ret2 = 0
    for e in list:
        ret1 = ret1 + e[1]
        ret2 = ret2 + e[2]*e[1]
    return ret1, ret2

def total_enrollment(list):
    ret1 = 0
    ret2 = 0
    for a, b, c in list:
        ret1 = ret1 + b
        ret2 = ret2 + b*c
    return ret1, ret2

def check_sudoku(p):
	n = len(p)
	digit = 1
	while digit <= n:
		i =0
		while i < n:
			row_count = 0
			col_count = 0
			j = 0
			while j < n:
				if p[i][j] == digit:
					row_count = row_count + 1
				if p[j][i] == digit:
					col_count = col_count + 1
				j = j + 1
			if row_count != 1 or col_count != 1:
				return False
			i = i + 1
		digit = digit + 1
	return True

