n, k = map(int, input().split())
arr = list(map(int, input().split()))

visited = {}

for x in arr:
    visited[x] = visited.get(x, 0) + 1

count = 0

for key in list(visited.keys()):
    alter = k - key

    # 이미 사용됨
    if visited.get(key, 0) == 0:
        continue
    
    # 상대값이 없음
    if alter not in visited:
        continue

    # key == alter_key (같은 수 두 개로 쌍 만들기)
    if key == alter:
        count += visited[key] // 2
        visited[key] = 0
        continue

    # key < alter 일 때만 처리 (중복 방지)
    if key < alter:
        pairs = min(visited[key], visited[alter])
        count += pairs
        visited[key] -= pairs
        visited[alter] -= pairs

print(count)
