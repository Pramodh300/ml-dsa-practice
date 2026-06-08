#Network Delay Time
import heapq

class Solution:
    def networkDelayTime(self, times, n, k):

        graph = {}

        for u, v, w in times:

            if u not in graph:
                graph[u] = []

            graph[u].append((v, w))

        distances = {
            i: float('inf')
            for i in range(1, n + 1)
        }

        distances[k] = 0

        pq = [(0, k)]

        while pq:

            current_distance, node = heapq.heappop(pq)

            if current_distance > distances[node]:
                continue

            for neighbor, weight in graph.get(node, []):

                distance = current_distance + weight

                if distance < distances[neighbor]:

                    distances[neighbor] = distance

                    heapq.heappush(
                        pq,
                        (distance, neighbor)
                    )

        max_time = max(distances.values())

        return max_time if max_time != float('inf') else -1



#Cheapest Flights Within K Stops
import heapq

class Solution:
    def findCheapestPrice(
        self,
        n,
        flights,
        src,
        dst,
        k
    ):

        graph = {}

        for u, v, price in flights:

            if u not in graph:
                graph[u] = []

            graph[u].append((v, price))

        pq = [(0, src, 0)]

        while pq:

            cost, node, stops = heapq.heappop(pq)

            if node == dst:
                return cost

            if stops > k:
                continue

            for neighbor, price in graph.get(node, []):

                heapq.heappush(
                    pq,
                    (
                        cost + price,
                        neighbor,
                        stops + 1
                    )
                )

        return -1



#Path With Minimum Effort
import heapq

class Solution:
    def minimumEffortPath(self, heights):

        rows = len(heights)
        cols = len(heights[0])

        efforts = [
            [float('inf')] * cols
            for _ in range(rows)
        ]

        efforts[0][0] = 0

        pq = [(0, 0, 0)]

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while pq:

            effort, r, c = heapq.heappop(pq)

            if r == rows - 1 and c == cols - 1:
                return effort

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < rows and
                    0 <= nc < cols
                ):

                    new_effort = max(
                        effort,
                        abs(
                            heights[r][c]
                            - heights[nr][nc]
                        )
                    )

                    if new_effort < efforts[nr][nc]:

                        efforts[nr][nc] = new_effort

                        heapq.heappush(
                            pq,
                            (
                                new_effort,
                                nr,
                                nc
                            )
                        )

                        