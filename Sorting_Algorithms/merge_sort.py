# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

def merge_sort(in_list):
    if len(in_list)>1:
        mid = len(in_list)//2
        return merge(merge_sort(in_list[:mid]), merge_sort(in_list[mid:]))
    return in_list   
def merge(l1, l2):
    len1 = len(l1)
    len2 = len(l2)
    m_result = []
    while len1 and len2:
        if l1[-len1] <= l2[-len2]:
            m_result.append(l1[-len1])
            len1 -= 1
        else:
            m_result.append(l2[-len2])
            len2 -= 1

    if len1:
        m_result.extend(l1[-len1:])
    if len2:
        m_result.extend(l2[-len2:])
    
    return m_result


user_list = [int(x) for x in input("Enter elements separated by space:").split()]

result = merge_sort(user_list)
print("input list", user_list)
print("sorted list", result)
