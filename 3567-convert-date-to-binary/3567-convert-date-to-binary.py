class Solution:
    def convertDateToBinary(self, date: str) -> str:
        date=date.split("-")
        y=date[0]
        m=date[1]
        d=date[2]
        return bin(int(y))[2:]+"-"+bin(int(m))[2:]+"-"+bin(int(d))[2:]
        
        