def generate(ind,curr_subset,ans,nums):
    if(ind==len(nums)):
        ans.append(curr_subset.copy())
        return
    curr_subset.append(nums[ind])
    generate(ind+1,curr_subset,ans,nums)
    curr_subset.pop()
    generate(ind+1,curr_subset,ans,nums)
def subset(nums):
    curr_subset=[]
    ans=[]
    ind=0
    generate(ind,curr_subset,ans,nums)
    return ans
arr=[1,2,3]
print(subset(arr))