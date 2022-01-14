class Solution:
    def myAtoi(self, s: str) -> int:
        arr=list(s)
        ans=[]
        negative=False
        sign =0
        for i in range(0,len(arr)):
            if " "==arr[i] and i>0:
                if (arr[i-1]>="0" and arr[i-1]<="9") and (arr[i-1]>="0" and arr[i-1]<="9") or arr[i-1]=="-" or arr[i-1]=="+":
                    
                    print("yes")
                    #ans=[]
                    break
            elif " "==arr[i]:
                a=0
            elif "-"==arr[i]:
                if i>0 and (arr[i-1]=="-" or arr[i-1]=="+" or arr[i-1].isnumeric()):
                    break
                negative=True    
            elif "+"==arr[i]:
                if i>0 and (arr[i-1]=="-" or arr[i-1]=="+" or arr[i-1].isnumeric()):
                    break       
                negative=False
            elif arr[i]>="0" and arr[i]<="9":
                ans.append(arr[i])
            else:
                break 
        if len(ans)==0 :
            return 0 
        listToStr = ''.join(map(str, ans))
        ansint=int(listToStr)
            
        if negative:
            ansint=ansint*-1
        limit = (2**31)-1
        if limit < ansint:
            return limit
        if -(limit+1) > ansint:
            return -(limit+1)
        return ansint
            
                
            
        