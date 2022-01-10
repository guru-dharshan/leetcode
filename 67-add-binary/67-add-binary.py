class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            d=len(a)-len(b)
            b=("0"*d)+b
        elif len(b) > len(a):
            d=len(b)-len(a)
            a=("0"*d) +a
        ans=""
        c="0"
        for i in range(len(a)-1,-1,-1):
            if a[i]=="0" and b[i]=="0":
                if c=="1":
                    ans=ans+"1"
                    c="0"
                elif c=="0":
                    ans=ans+"0"
            elif a[i]=="1" and b[i]=="1":
                if c=="0":
                    ans=ans+"0"
                    c="1"
                elif c=="1":
                    ans=ans+"1"
                    c="1"
            elif (a[i]=="0" and b[i]=="1") or (a[i]=="1" and b[i]=="0"):
                if c=="0":
                    ans=ans+"1"
                elif c=="1":
                    ans=ans+"0"
                    c="1"
           
                
        if c=="1":
            ans=ans+"1"
        return ans[::-1]
            
            