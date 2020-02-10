# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 18:04:37 2020

@author: mzly903
"""

matches = []

len_mat = []
n_gaps = 0
all_points = []
for i in range(3):
    l = int(input())
    r = int(input())
    
    matches.append(l)
    matches.append(r)
    
    len_mat.append(r-l)
    for j in range(l, r):
        
        all_points.append(j)


all_points = list(set(all_points))

min_value = min(all_points)
max_value = max(all_points)


gap = []
check = 0
for t in range(min_value, max_value + 1):
    if t not in all_points:
        
        check = 1
        
        gap.append(t+0.5)
    

        
        

gap = list(set(gap))
where = []
if len(gap) >= 1:
    
    min_gap = int(min(gap)-0.5)
    max_gap = int(max(gap)+0.5)

    n_gaps = 1
    
    for r in range(min_gap, max_gap):
        
        if (r + 0.5) not in gap:
            n_gaps = 2
            where.append(r - min_gap)
        

    
#     dist = []
#     for r in range(1, len(gap)):
#         if gap[r] != (gap[r-1] + 1):
#             gap_dist =  gap[r] - gap[r-1]
#             dist.append(gap_dist)

        
print ("Numb of gaps ",n_gaps, "Gaps ", gap, "WHere ", min(where))
       
for y in range(3):
    if n_gaps == 1:
    
    


# 1
# l1, r1 = matches[1], matches[0]
# l2, r2 = matches[3], matches[2]
# l3, r3 = matches[5], matches[4]
# len1 = r1 - l1
# len2 = r2 - l2
# len3 = r3 - l3

# m1 = [l1, r1]
# m2 = [l2, r2]
# m3 = [l3, r3]

# lefts = [l1, l2, l3]

# rigths = [r1, r2, r3]

# sort_left = sorted(lefts)

# sort_rigth = sorted(rigths)


# if max(matches) - min(matches) <= (len1 + len2 + len3):
    
#     if len(set(matches)) <= 4:
        
#         print(0)
#     else:
#         print(2)
# else:
    
#     print (-1)
    
