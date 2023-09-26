def merge_sort(array):
    if len(array)<2:
        return array
    mid = len(array)//2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merg_e(left, right)

def merg_e(left, right):
    result = []
    i=j= 0
    while i<len(left) or j< len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
        if i == len(left) or j==len(right):
            result.extend(left[i:] or right[j:])
            break
    return result      
            
ls= [-11,12.34,-23,5,56,3,5,67,93,24,85]    #output : [-23, -11, 3, 5, 5, 12.34, 24, 56, 67, 85, 93]
merge_sort(ls)