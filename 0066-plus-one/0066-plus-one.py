class Solution:
    def plusOne(self, dig: List[int]) -> List[int]:
        arr=""
        r=[]
        for i in range(len(dig)):
            arr+=str(dig[i])
        f=int(arr)+1
        for i in str(f):
            r.append(int(i))
        return r
        

        