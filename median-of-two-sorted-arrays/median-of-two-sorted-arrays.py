class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr=nums1+nums2
        arr.sort()
        n=len(arr)//2
        print(n)
        if len(arr)%2==0:
            ans=float((arr[n]+arr[n-1])/2)
        else:
            s=arr[n]
            ans=float(s)
            
        return ans        