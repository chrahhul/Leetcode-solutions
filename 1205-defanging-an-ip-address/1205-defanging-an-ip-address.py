class Solution:
    def defangIPaddr(self, add: str) -> str:
        add=add.replace(".","[.]")
        return add

        