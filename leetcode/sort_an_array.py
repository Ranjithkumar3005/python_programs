class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)
        gap = n // 2

        while gap > 0:
         for i in range(gap, n):
            new_element = nums[i]
            j = i

            while j >= gap and nums[j - gap] > new_element:
                nums[j] = nums[j - gap]
                j -= gap

            nums[j] = new_element

         gap //= 2
        
        print(nums)

s=Solution()
s.sortArray( nums = [5,2,3,1])




# for(int gap=intArray.length/2;gap>0;gap/=2){
#             for(int i=gap;i<intArray.length;i++){
#                 int newElement=intArray[i];
#                 int j=i;

#                 while(j>=gap && intArray[j-gap]>newElement){
#                     intArray[j]=intArray[j-gap];
#                     j-=gap;
#                 }
#                 intArray[j]=newElement;
#             }
#         }