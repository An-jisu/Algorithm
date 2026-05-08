t = int(input())
for tcase in range(1, t+1):
	n, m, k = map(int, input().split())
	clients = sorted(list(map(int, input().split())))
	poss = 'Possible'
	total = 0
	sold = 0
	# 손님 한 명 올 때마다 붕어빵 수 업데이트, 붕어빵 있으면 -1, 없으면 즉시 for문 벗어남
	for clientTime in clients:
		if clientTime ==0:
			poss = 'Impossible'
			break;
		# 현재 붕어빵 수 (그 손님시간의 붕어빵 수-현재까지 나간 붕어빵 수)
		total = ((clientTime//m)*k)-sold
		if total <= 0:
			poss = 'Impossible'
			break;
		else:
			sold+=1
	
	print(f"#{tcase} {poss}")