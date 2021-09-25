import numpy as np


# Example 1:

# Input: image = [[1,1,0],[1,0,1],[0,0,0]]

# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].

# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]


# Example 2:

# Input: image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]

# Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].

# Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

i = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
rev_list = []
pix_rev = []
f_l = []

for pix in i:
    rev_list.append(pix[::-1])
for pix in rev_list:
    for num in pix:

        if num == 0:
            pix_rev.append(1)
        else:
            pix_rev.append(0)
    f_l.append(pix_rev)
    pix_rev = []

print(f_l)


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        rev_list = []
        pix_rev = []
        f_l = []

        for pix in image:
            rev_list.append(pix[::-1])
        for pix in rev_list:
            for num in pix:

                if num == 0:
                    pix_rev.append(1)
                else:
                    pix_rev.append(0)
            f_l.append(pix_rev)
            pix_rev = []

        return f_l