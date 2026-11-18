# 가위바위보
def rps(p1, p2):
    num1, card1 = p1
    num2, card2 = p2
    if card1==card2:
        return p1 if num1<num2 else p2
    # p1이 이기는 경우
    if (card1 ==1 and card2 ==3) or (card1 ==2 and card2==1) or (card1 ==3 and card2 ==2):
        return p1
    return p2

# 그룹 나누기 (len이 2 이하이면 더 이상 안쪼개고-> 가위바위보-> 진 사람 user에서 제거)
def tournament(group):
    if len(group) == 1:
        return group[0]

    mid = (len(group)+1) // 2
    group1 = group[:mid]
    group2 = group[mid:]

    winner1 = tournament(group1)
    winner2 = tournament(group2)

    return rps(winner1, winner2)


t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    nums = list(map(int, input().split()))
    user = [(i+1, nums[i]) for i in range(n)]
    result = []
    # print(nums, user)

    winner = tournament(user)

    print(f"#{test_case} {winner[0]}")