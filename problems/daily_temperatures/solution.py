class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        array = []
        for i in range(len(temperatures)-1,-1,-1):
            if stack == []:
                stack.append(i)
                array.append(0)
            else:
                while stack != [] and temperatures[stack[-1]] <= temperatures[i]:
                    stack.pop()
                if stack == []:
                    stack.append(i)
                    array.append(0)
                else:
                    array.append(stack[-1] - i)
                    stack.append(i)
            # print(i,temperatures[i],stack)
        array.reverse()
        return array
                    
                    
                

            