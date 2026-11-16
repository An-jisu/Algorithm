def count_nodes(n):
    global cnt
    cnt+=1
    if tree[n][0]:
        count_nodes(tree[n][0])
    if tree[n][1]:
        count_nodes(tree[n][1])


t = int(input())
for test_case in range(1, t+1):
    e, n = map(int, input().split())
    edges = list(map(int, input().split()))
    tree = [[0,0] for _ in range(e+2)] # 노드 갯수는 e+1개

    # 트리 구성
    for i in range(e):
        parent = edges[i*2]
        child = edges[i*2+1]
        if tree[parent][0] == 0:
            tree[parent][0] = child
        else:
            tree[parent][1] = child
    
    cnt = 0
    count_nodes(n)

    print(f"#{test_case} {cnt}")