while True:
	print("Enter single digits separated by one space: ",end="")
	L = input().split()
	m_digit = False
	for i in range(len(L)):
		L[i] = int(L[i])
		if L[i] > 9:
			m_digit = True
	if L[0]==0 or L[-1]==0 or m_digit:
		print("Invalid list, try again.")
		continue
	rev_L = L[::-1]
	N,rev_N = 0,0
	for i in range(len(L)):
		N = N*10 + L[i]
		rev_N = rev_N*10 + rev_L[i]
	
	print("The initial list is:",L)
	print("The reversed list is:",rev_L)
	break
