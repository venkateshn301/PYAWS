import sys
n=len(sys.argv)
print("number of args:",n)

print("\nArgs passed:",end = " ")
sum=0
for i in range(1,n):
	sum+= int(sys.argv[i])
print(sum)

print("\nargs passed in new line:",end=" ")
for i in range(1,n):
	print(sys.argv[i], end= " ")
print("\n\nheelo")
print("Hello Welcome")

