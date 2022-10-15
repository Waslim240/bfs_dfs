maps = {'B.Aceh':set(['Sabang', 'Calang', 'Jantho', 'Sigli']),
        'Sabang':set(['B.Aceh']),
        'Calang':set(['B.Aceh','Meulaboh']),
        'Jantho':set(['B.Aceh']),
        'Sigli':set(['B.Aceh', 'Bireun']),
        'Meulaboh':set(['Calang', 'Bl.pidie','Simuelue']),
        'Bireun':set(['Sigli','Takengon', 'Lhokseumawe']),
        'Bl.pidie':set(['Meulaboh','Tapaktuan','Singkil']),
        'Takengon':set(['Bireun', 'Bl.kejren','Kutacane']),
        'Lhokseumawe':set(['Bireun', 'Langsa', 'Perlak']),
        'Tapaktuan':set(['Bl.pidie']),
        'Singkil':set(['Bl.pidie']),
        'Bl.kejren':set(['Takengon']),
        'Kutacane':set(['Takengon']),
        'Langsa':set(['Lhokseumawe']),
        'Perlak':set(['Lhokseumawe'])}


def bfs(graph, start, finish):
    explored = []
    queue = [[start]]

    if start == finish:
        return "Awal adalah Tujuan"

    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = graph[node] 
            for neighbour in neighbours: 
                new_path = list(path) 
                new_path.append(neighbour) 
                queue.append(new_path) 
                if neighbour == finish:
                    return new_path 

            explored.append(node) 

    return "Mohon maaf node yang dipilh tidak ada"


awal = input("Masukan awal: ")
tujuan = input("Masukan tujuan: ")

print(bfs(maps, awal, tujuan)) 