from typing import List


def get_index_of_seven(nums: List[int]) -> int:
    for i, n in enumerate(nums):
        if n==7:
            return i
    return -1


def get_dist_between_sevens(nums: List[int]) -> int:
    count_idx = 0
    dist = 0
    for i,n in enumerate(nums):
        if n==7 and count_idx!=2:
            dist = i - dist
            count_idx+=1
    return dist


# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))
