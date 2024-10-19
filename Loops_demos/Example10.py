# how to write infinite loop

"""while 1:
	i=(int)(input("Enter number\n"))
	if(i==0):
		break
	print(i)"""

sum = 0
for i in range(1, 5):
    sum += i
print("Sum of first 5 numbers is", sum)

"""for i in range(ord('A'), ord('K')+1):
    print(chr(i))"""

"""i = 1
sum=0
while i<6:
    sum+=i
    i = i + 1
print("Sum of first 5 numbers is", sum)"""

for i in range(1, 5):
    for j in range(1, 3):
        print(i, j)


