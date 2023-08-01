class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for i in points:
            dist = sqrt(i[0]*i[0] + i[1]*i[1])
            distances += [{"p":i, "d":dist}]
        distances = sorted(distances,key =lambda c: c["d"])
        result = [i["p"] for i in distances]
        return result[:k]
            