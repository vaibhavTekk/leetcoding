class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            j = 0
            k = len(image) - 1
            while(k > j):
                temp = flip(image[i][j])
                image[i][j] = flip(image[i][k])
                image[i][k] = temp
                k -= 1
                j += 1
            if (k - j == 0):
                image[i][j] = flip(image[i][j])
        return image
def flip(n):
    if n == 0:
        return 1
    else:
        return 0