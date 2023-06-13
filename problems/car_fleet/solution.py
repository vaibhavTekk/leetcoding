class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[position[i],speed[i]] for i in range(len(position))]
        pairs.sort()
        pairs.reverse()
        stack = []
        # print(pairs)
        for p,s in pairs:
            eta = (target - p)/s
            stack.append(eta)
            while(len(stack) >= 2 and stack[-1] <= stack[-2]):
                stack.pop()
            # print(stack)  
        return len(stack)