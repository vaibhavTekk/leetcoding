class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for i in range(len(points)):
            point = points[i]
            dist = sqrt(point[0]*point[0] + point[1]*point[1])
            heappush(distances,(dist,i))
        res = []
        for _ in range(k):
            dist, point = heappop(distances)
            res.append(points[point])
        return res
            