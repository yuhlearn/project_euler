from time import time

class disjoint_set:
  _ds = list()

  def __init__(self, initial_ds=[]):
    self._ds = [[elem] for elem in list(set(initial_ds))]

  def find_set(self, elem):
    for i, subset in enumerate(self._ds):
      if elem in subset:
        return i
    return None

  def union(self, elem1, elem2):
    i = self.find_set(elem1)
    j = self.find_set(elem2)
    if i != j and i is not None and j is not None: 
      self._ds[i] = self._ds[i]+self._ds[j]
      del self._ds[j]
      return True
    return False
       

def mst_kruskal(G):
  V = range(len(G))
  E = sorted([(u,v) for u in V for v in V[u+1:] if G[u][v] > 0], key=lambda (u,v): G[u][v])
  S = disjoint_set(V)
  A = [(u,v) for u,v in E if S.union(u,v)]
  return A


with open('p107_network.txt', 'r') as fp:
   G = [map(int, line.replace('-', '0').split(',')) for line in fp]

start = time()

A = mst_kruskal(G)

total_sum = sum([sum(line[:i+1]) for i, line in enumerate(G)])
minimum_sum = sum([G[u][v] for u, v in A])

print total_sum-minimum_sum, time()-start
