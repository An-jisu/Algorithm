def solution(nums):
    #중복 제거해서, 뽑는 수보다 적으면 중복제거한 것의 길이 return/많으면 뽑는 수 return
    nums2 = set(nums)
    if len(nums2)<=len(nums)//2:
        return len(nums2)
    else:
        return len(nums)//2