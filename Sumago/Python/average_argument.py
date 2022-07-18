# write a program to return the average of its argument

# function that takes arbitrary
# number of inputs
def avg_argument(*n):
	sums = 0

	for t in n:
		sums = sums + t

	avg = sums / len(n)
	return avg
	

# Driver Code
result1 = avg_argument(1, 2, 3)
result2 = avg_argument(2, 6, 4, 8)

# Printing average of the list
print(round(result1, 2))
print(round(result2, 2))
