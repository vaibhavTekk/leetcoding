class TimeMap:
    def __init__(self):
        self.timemap = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timemap:
            self.timemap[key] += [[timestamp,value]]
        else:
            self.timemap[key] = [[timestamp,value]]
        # print(self.timemap)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap or timestamp < self.timemap[key][0][0]:
            return ""
        else:
            left = 0
            right = len(self.timemap[key]) - 1
            pos = -1
            mid = (left + right) // 2
            while(left <= right):
                mid = (left + right) // 2
                if (self.timemap[key][mid][0] > timestamp):
                    right = mid - 1
                elif (self.timemap[key][mid][0] < timestamp):
                    left = mid + 1
                else:
                    break
            mid = (left+right)// 2
            return self.timemap[key][mid][1]
            # print(timestamp,mid,pos)
            # if pos == -1 and self.timemap[key][mid][0] < timestamp:
            #     return self.timemap[key][mid][1]
            # # elif pos == -1 and self.timemap[key][mid-1][0] < timestamp:
            # #     return self.timemap[key][mid-1][1]
            # elif pos > -1:
            #     return self.timemap[key][pos][1]
            # else:
            #     return ""
        return ""


        # for j in range(len(self.timemap[key])-1,-1,-1):
        #     if timestamp >= self.timemap[key][j][0]:
        #         return (self.timemap[key][j][1])
        # return ""
                
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)