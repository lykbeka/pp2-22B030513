line=input()
strs=line.split()
nums=[int(i) for i in strs]
def spy_game(nums):
    for i in range(0,len(nums)):
        if nums[i]==0 and nums[i+1]==0 and nums[i+2]==7:
            return True
        else:
            continue
        if i==len(nums)-2:
            return False
print(spy_game(nums))