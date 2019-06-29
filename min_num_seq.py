# Python3 program of above approach

# Returns minimum number made from
# given sequence without repeating digits
def getMinNumberForPattern(seq):
	n = len(seq)

	if (n >= 9):
		return "-1"

	result = [None] * (n + 1)

	count = 1

	# The loop runs for each input character
	# as well as one additional time for
	# assigning rank to remaining characters
	for i in range(n + 1):
		if (i == n or seq[i] == 'I'):
			for j in range(i - 1, -2, -1):
				result[j + 1] = int('0' + str(count))
				count += 1
				if(j >= 0 and seq[j] == 'I'):
					break
	return result

# Driver Code
if __name__ == '__main__':
	inputs = ["IDID", "I", "DD", "II",
			"DIDI", "IIDDD", "DDIDDIID"]
	for Input in inputs:
		print(*(getMinNumberForPattern(Input))) 
