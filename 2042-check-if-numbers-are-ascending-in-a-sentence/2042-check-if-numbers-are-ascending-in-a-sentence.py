class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        arr=s.split(" ")
        n=0
        flag=True
        for i in arr:
            if i.isnumeric():
                k=int(i)
                if k>n:
                    n=k
                else:
                    flag=False
                    break
        return flag
        