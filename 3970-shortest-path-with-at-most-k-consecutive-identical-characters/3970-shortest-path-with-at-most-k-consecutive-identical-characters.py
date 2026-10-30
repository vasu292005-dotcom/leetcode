class Solution(object):
    def shortestPath(self, n, edges, labels, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :type k: int
        :rtype: int
        """
        import heapq
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
        pq = [(0, 0, 1)]
        dist = {}
        while pq:
            cost, u, cnt = heapq.heappop(pq)
            if u == n - 1:
                return cost
            if (u, cnt) in dist and dist[(u, cnt)] <= cost:
                continue
            dist[(u, cnt)] = cost
            for v, w in adj[u]:
                nc = cnt + 1 if labels[u] == labels[v] else 1
                if nc <= k:
                    if (v, nc) not in dist or cost + w < dist[(v, nc)]:
                        heapq.heappush(pq, (cost + w, v, nc))
        return -1