class Edge:
    def __init__(self, w, u, v):
        self.w = w
        self.u = u
        self.v = v

class Tree:
    def __init__(self, n, parent=None):
        self.data = n
        self.parent = parent # Tree
        self.rank = 0
        self.children = []

def init_set(n): #집합 트리로 관리
    tre = Tree(n)
    return tre

def find(my, sets): #loot 노드 체크로 같은 집합인지 확인
    if my.parent is None: #loot 노드에 도달하면 해당 노드 return
        return my
    else:
        my.parent = find(my.parent, sets) # 재귀 함수로 경로 압축. return 되는 loot 노드를 부모로 삼음.
        sets[my.data] = my
        return my.parent


def union(u, v, sets):
    if sets[u].rank >= sets[v].rank:
        king = sets[u] #Tree
        loot = None
        if sets[v].parent is not None:
            loot = find(sets[v].parent, sets) #sets[v]의 loot 노드
            loot = loot.data
            sets[loot].parent = king
            sets[u].children.append(sets[loot])

        else:
            sets[v].parent = king
            sets[u].children.append(sets[v])

        if sets[u].rank == sets[v].rank:
            sets[u].rank += 1

    elif sets[u].rank < sets[v].rank:
        king = sets[v]
        loot = None
        if sets[u].parent is not None:
            loot = find(sets[u].parent, sets)
            loot = loot.data
            sets[loot].parent = king
            sets[v].children.append(sets[loot])

        else:
            sets[u].parent = king
            sets[v].children.append(sets[u])

        if sets[u].rank == sets[v].rank:
            sets[v].rank += 1
    return sets

def kruskal(e, n):
    sort_cost_adjacency_matrix = [] #기존 비용인접행렬의 원소들은 가중치 뿐이므로 간선을 이루는 정점을 함께 저장하기 위한 배열
    for i in range(len(e)):
        for j in range(len(e[0])):
            if e[i][j] != 0 and e[i][j] != 99: #비용인접행렬에서 0과 99는 자기 자신이거나 간선이 없는 것을 의미함. 따라서 제거함.
                sort_cost_adjacency_matrix.append([e[i][j], i, j])

    sets = []
    sort_cost_adjacency_matrix.sort() # 오름차 정렬
    mst_e = [] # 목적!!!!
    for i in range(n): sets.append(init_set(i)) #n개의 집합(트리) 생성

    while len(mst_e) < n-1:
        mini = Edge(0, 0, 0)# 최소 가중치 간선
        mini.w = sort_cost_adjacency_matrix[0][0] # 오름차 정렬돼있으므로 인덱스 0이 최소 가중치 간선
        mini.u = sort_cost_adjacency_matrix[0][1]
        mini.v = sort_cost_adjacency_matrix[0][2]
        sort_cost_adjacency_matrix.pop(0) # E -= (u, v)

        if find(sets[mini.u], sets) != find(sets[mini.v], sets): #정점 u, v가 서로 다른 집합인지 확인
            mst_e.append([mini.u, mini.v])
            union(mini.u, mini.v, sets)
    return mst_e


#main
cost_adjacency_matrix = [  #비용인접행렬
    [0, 4, 99, 99, 99, 99, 99, 8, 99],
    [4, 0, 8, 99, 99, 99, 99, 11, 99],
    [99, 8, 0, 7, 99, 4, 99, 99, 2],
    [99, 99, 7, 0, 9, 14, 99, 99, 99],
    [99, 99, 99, 9, 0, 10, 99, 99, 99],
    [99, 99, 4, 14, 10, 0, 2, 0, 99],
    [99, 99, 99, 99, 99, 2, 0, 1, 6],
    [8, 11, 99, 99, 99, 99, 1, 0, 7],
    [99, 99, 2, 99, 99, 99, 6, 7, 0]
]
mm = kruskal(cost_adjacency_matrix, 9)
print(mm)