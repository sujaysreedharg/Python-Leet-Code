class UnionFindSet:
    def __init__(self,n):
        self.parent= {}
        self.rank = {}
        for i in range(n):
            self.add(i)
    def add(self,p):
        self.parent[p] = -1
        self.rank[p] = 0
    def find(self,u):
        if self.parent[u]==-1:
            return u
        else:
            self.parent[u] = self.find(self.parent[u])
            return self.parent[u]
    def union(self,u,v):
        pv,pu = self.find(u),self.find(v)
        if pv == pu:
            return False
        if self.rank[pv] > self.rank[pu]:
            self.parent[pu] = pv
        elif self.rank[pv] < self.rank[pu]:
            self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu]+=1
        return True
    
# UnionFind + Kruskal + Enumerate edges
# O(ElogE + E^2 + E^2)
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # sort edges in asc order based on weight
        edges = [(u,v,w,i) for i,(u,v,w) in enumerate(edges)]
        edges.sort(key= lambda x: x[2])
        # do not use this edge
        def find_mst_without_this_edge(edge_idx):
            union_find_set = UnionFindSet(n)
            ans = 0
            for i, (u, v, w, _) in enumerate(edges):
                # do not use this edge
                if i == edge_idx:
                    continue
                if union_find_set.union(u, v):
                    ans += w
            parent = union_find_set.find(0)
            return ans if all(union_find_set.find(i) == parent for i in range(n)) else inf
        
        # need to use this edge
        def find_mst_with_this_edge(edge_idx):
            union_find_set = UnionFindSet(n)
            # use this edge first
            u0, v0, w0, _ = edges[edge_idx]
            ans = w0
            union_find_set.union(u0, v0)
            for i, (u, v, w, _) in enumerate(edges):
                # do not use this edge
                if i == edge_idx:
                    continue
                if union_find_set.union(u, v):
                    ans += w
            parent = union_find_set.find(0)
            return ans if all(union_find_set.find(i) == parent for i in range(n)) else inf
        
        # normal MST total weight
        base = find_mst_without_this_edge(-1)
        cri, p_cri = [],[]
        for i in range(len(edges)):
            wgt_excl = find_mst_without_this_edge(i)
            # if not included, MST total weight would increase
            if wgt_excl > base:
                cri.append(edges[i][3])
            else:
                wgt_incl = find_mst_with_this_edge(i)
                # with this edge, MST total weight doesn't change
                if wgt_incl == base:
                    p_cri.append(edges[i][3])
    
        return [cri, p_cri]
