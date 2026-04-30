for tcase in range (1, 11):
	n = int(input())
	arr = [list(map(int, input().split())) for _ in range(100)]
	count = 0
	# 하나의 열마다 교착 상태 확인
	for i in range(0, 100):
		col = [arr[j][i] for j in range(100) if arr[j][i]!=0] 
		# 교착 상태 확인: 1,2 세트인 경우에만 (last 값이랑 그 다음 값 확인)
		last = 0
		for j in col:
			if last==1 and j==2:
				count+=1
			last = j
     
	print(f"#{tcase} {count}")