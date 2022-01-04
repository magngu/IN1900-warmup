# mult_table.py
# Author Magnus // Jan 2022
# ------------------------------------------------------------------------------

# Prints whole multiplication tabel form 1*1 to 10*10
for i in range(1,11):
    print(f'--- Multiples of {i} ---')
    for j in range(1,11):
        print(i*j)


'''
Test run:
>>>python3 mult_table.py
--- Multiples of 1 ---
1
2
3
4
5
6
7
8
9
10
--- Multiples of 2 ---
2
4
6
8
10
12
14
16
18
20
--- Multiples of 3 ---
3
6
9
12
15
18
21
24
27
30
--- Multiples of 4 ---
4
8
12
16
20
24
28
32
36
40
--- Multiples of 5 ---
5
10
15
20
25
30
35
40
45
50
--- Multiples of 6 ---
6
12
18
24
30
36
42
48
54
60
--- Multiples of 7 ---
7
14
21
28
35
42
49
56
63
70
--- Multiples of 8 ---
8
16
24
32
40
48
56
64
72
80
--- Multiples of 9 ---
9
18
27
36
45
54
63
72
81
90
--- Multiples of 10 ---
10
20
30
40
50
60
70
80
90
100
>>>
'''