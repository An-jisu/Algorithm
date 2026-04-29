t = int(input())
for tcase in range(1, t+1):
	n = int(input())
	arr = []
	total = 0
    # 2차원 배열에 농장 저장
	for i in range(0, n):
		arr.append(list(map(int, input())))
	# 농작물의 합
	mid = n//2
	for j in range(n):
		if j <=mid:
			start = mid-j
			end = mid+j
		else:
			start = j-mid
			end = n-(j-mid)-1
		for k in range(start, end+1):
			total+=arr[j][k]
    
	print(f"#{tcase} {total}")