def findLength(length):
	# 가로 회문 찾기
	for row in arr:
		for col in range(0, 101-length):
			word = row[col:col+length]
			if word == word[::-1]:
				return length
	# 세로 회문 찾기
	for col in range(100):
		for r in range(0, 101-length):
			word = ''.join(arr[r+k][col] for k in range(length))
			if word == word[::-1]:
				return length

for tcase in range(10):
	num = int(input())
	arr = [input() for _ in range(100)]
	for i in range(100, 0, -1): # 회문 길이 (첫번째로 발견되는 i가 정답)
		maxLen = findLength(i)
		if maxLen == i:
			break
	print(f"#{num} {maxLen}")