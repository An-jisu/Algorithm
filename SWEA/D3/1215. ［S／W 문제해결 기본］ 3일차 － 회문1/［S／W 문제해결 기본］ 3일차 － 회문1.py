for tcase in range(1, 11):
	n = int(input())
	arr = [list(input()) for _ in range(8)]
	count = 0
    
	for i in range(8):
		for j in range(8-n+1):
			# 가로 회문
			word = ''.join(arr[i][j:j+n])
			if word == word[::-1]: 
					count += 1
            
 			# 세로 회문
			word = ''.join(arr[j+k][i] for k in range(n))
			if word == word[::-1]: 
				count += 1
    
	print(f"#{tcase} {count}")