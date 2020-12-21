input = """111
56
160
128
25
182
131
174
87
52
23
30
93
157
36
155
183
167
130
50
71
98
42
129
18
13
99
146
81
184
1
51
137
8
9
43
115
121
171
77
97
149
83
89
2
38
139
152
29
180
10
165
114
75
82
104
108
156
96
150
105
44
100
69
72
143
32
172
84
161
118
47
17
177
7
61
4
103
66
76
138
53
88
122
22
123
37
90
134
41
64
127
166
173
168
58
26
24
33
151
57
181
31
124
140
3
19
16
80
164
70
65"""

input_list = [int(i) for i in input.split("\n")]

adapters = sorted(input_list)
print(adapters)

one_count = 0
three_count = 0

for num in range(1, len(adapters)):
    if adapters[num] - adapters[num-1] == 1:
        one_count += 1
    elif adapters[num] - adapters[num-1] == 3:
        three_count += 1
    else:
        pass

#print((one_count+1) * (three_count+1))

test = sorted([16, 10, 15, 5, 1 ,11, 7, 19, 6, 12, 4])

print(test)
