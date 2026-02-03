class Solution:
    def rearrangeArray(self, nums):
        pos=[]
        neg=[]
        for num in nums:
            if num >= 0:
                pos.append(num)
            else:
                neg.append(num)
        pos_size=len(pos)
        neg_size=len(neg)
        if pos_size>neg_size:
            for i in range(neg_size):
                nums[2*i]=pos[i]
                nums[2*i+1]=neg[i]
            index=neg_size*2
            for i in range(neg_size,pos_size):
                nums[index]=pos[i]
                index+=1
            else:
                for i in range(pos_size):
                    nums[2*i]=pos[i]
                    nums[2*i+1]=neg[i]
                index=pos_size*2
                for i in range(pos_size,neg_size):
                 nums[index]=neg[i]
                index+=1
        return nums
arr=[2,4,5,-1,-3,-4]
sol=Solution()
print("result is:",sol.rearrangeArray(arr))