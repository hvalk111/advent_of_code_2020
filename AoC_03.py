import numpy as np

input = """..#.......#..##...#...#..#.#...
..##..#..#.....#.........#....#
...#.##..#.#......#.#....#.....
...#.....#......#...#..........
.......#.#..#..#....##....##...
.#......#......#.#..#....#.#...
.#..........#.....###.##..#.#..
....#...##...........#.........
##......#.#...#...#....##.#...#
.....#.....#.#..#....###...#..#
.#....#.........#...#.......#.#
.##......#.#.........#....#.#..
...#........###..#......##....#
.#.....###..........#...#....##
............#......#...#...#..#
.....#.#....#.#.#...........#.#
....#.....#...##.##.....###..#.
.....#.##......#.##.#...#.#.#..
##.....#.##.##....#..##......#.
.....#.....#........#........##
#..#...#.#.#..##....#....##..#.
.#......................##..#..
#.#.#................#.....#...
..#....#.#.#..##..#..#.....##..
.....###..#.............#....##
..#....#.#...#......###..#.....
.......####.....##......#......
..##...#..#...#.#..#......#....
..##..#..#.....#......##.##....
.#......#................#..#.#
...............#....#.......#..
#...........#.#.#........#.#...
...#...#..#.....##..#.##...#.#.
.#.#..#.#.....#...#..##....#.##
.........#...#.#.#....#.......#
............##.#..#.#........#.
#..#..#........#......####.....
..#.#...#...#...#.#...#..#..#..
#....................#.#.#....#
.......#.....#....#....##..#...
.......#.............##.....#..
..##..#.......#..#.........#..#
..##.#........#...#...#..#..#..
..##.#...#................#..#.
..#.....##...##......###.....#.
.....#.....#......#......#.....
....##.#.#....#.....#..........
...#...#.#.....#.###.....#....#
......##....#..##...##.#.......
......................##......#
.##......#...#...#...##.#.##.#.
#.......#...#.....#........#.#.
...............#......#.......#
.#..##...#....#.....###....##..
...#..###...#..#....#.#..#.....
.#...#....#.................#..
.......##....#..##......#.#....
....#.....#.....###...#....#...
..##..#..##........#...........
....#..#.#............#........
####.....##.........#....#.....
........#.....#......#......##.
#..........#........#....#...##
#..#...###.....##.....#.##...#.
......#....##.............#..#.
..#......###...#...#..##.....#.
#.##...#......##.###....#....#.
...............#....#.....###.#
#......#........#.#..##.#.....#
#..............#..##.#....#....
.##....###...#...#.#....#....#.
.......#...#.......#....#..##..
..##.#.....#..#...............#
.##..............#.......#...#.
.....#...#.#..#.........#..#...
........#.#.###......#..#......
..#.......###..#...#...........
............#.#.....#....#...#.
#...#..#......#..#......#......
..##..#......#..#.......#.....#
............#.##.....#.#...#...
....#.#...#.#...#........##....
........##...#...##.....#.#..#.
.#..........#.##...............
###.#..#...###..###..#........#
....#..#............#...#.#.#..
.#....###........#.......#...#.
..........#..#.....#......#....
..##..#.#....#..#.....##....#..
...#...............#......#....
......#.#.#...###.....##.#.....
.#...#.#.#.#....#.....#..#..#.#
..#.....#..##....#......#.#.#..
##.#....#.......#.#.#.......#..
.#.#.#........##.#....#........
...#..#...#.#.........#..#....#
#.#......#.#.#..#.#............
......#.....#.....#.......#..#.
.........#..#.##..#..###....#.#
.......#..........#..#.........
......#.#.##...#.#...##........
...........##..##.##....#......
..#..#...#.###...##.....#..#..#
.#...##.......#.#..........#..#
##......#...........#.#........
..#..#.....##..#.#.......#...#.
.#....#..#.....###.......#...#.
...#..#...#...###.#.###..#.....
.......#...#.##......#.#.#.#...
.#.......#...#...#...##........
...#........#....#..#.#...#.#..
..#............#.....#.#....#..
#.....#.#..#.#....#...#.#.#....
#......#......##.#...........#.
.#..#.........##.#........#....
.#....#.#...#........#......#..
....#..#..#....#..#.#.....#..#.
.##.#.....#..#.#...#.....#..###
#..#......#..##....##..#.......
.......#..##....#.###..........
.#......#..........#........#..
.........#.....#......#.#......
.....#..#.......#...#.#....#...
.#......#...#..#......#.....#.#
#.#.#..#.........#.......##....
...#..#.....#.#..#......#...#..
.##...#...#.#....#.....#.#...#.
..#......##......#....#.#..#...
....#.#.....#..#...........#...
.#........#....#....#...#......
..#.#.....#.......#.#.#.##..##.
...#..#.##.......#...#.........
....##.#.#..#.#..#.#.#..#.#.#.#
......#.......#.....#...##.#...
..#.##.....#....#...#...##.##.#
..##.........##.........#..#...
.....###......####..#.#...#....
...#....#....##.............#.#
.#.........#.......##..#.#.....
...#..#........#...............
........#........##......#.#...
##...#......#.....#.##........#
.............#.#........#......
.......##.........#.......#....
....#.......#......#..###....#.
.#.##........#.....#......#....
#...........##...#..##.........
.....#.#........#........##...#
#.........#..##.....#...#....#.
.........#...####..#....###....
###.#..##.......#....#....#.##.
...........#.....#.#...#..#....
.##......###.#.#.#....#........
....#..................#.###.#.
#..##...#......#...#......###..
.#.....#..##......#.#.#.#......
..##...#..#.......##.#.......#.
...#..#..##..##..##.#..####....
......#..#..............#.#####
....#....#..#...#...#.#........
.###...#.......#..#........#...
........#.#......##...#........
.#..#.......##.......#.....##..
...##..........##...........#..
......................#..#.#.#.
#..#.....#......#.....#....#.##
..#......#.....#....#...#.##.#.
............#...#...#......#.##
........##.......#......##.....
..#.##.....#....#..##...#......
........#.#...##.#..#...#....#.
...##............##.....#..#...
...###.##....#....#.#.#.#..#...
............#..#....#..#.....##
...#......##.......#......##..#
.......#......#........#.....#.
.#....#.##..........#..........
..###.........#..#...##.....#..
##....##..#.......###....#.#.#.
#.......#.#.##.................
..#..........#................#
....#.#....#...###...#......#..
.#..........#..#..##.....#...##
.#.....###....#.#...#.#........
.........##.........#..#.#.....
.#.....##....#......##.#....#..
###..#...#..#.........#......#.
..##.....#....#............#...
.....##.##....#.....#..#..#....
.......###...#..........#......
...#........#....#.##.#........
........###....##........##.#..
....#....#........#.....##.....
.#........#.#........#...#..#..
#..#..#......#....##.#..###....
...........#...#...#....#.#...#
.#..#.....#.##..#......##......
..#.#...............##..##.###.
...#.#...#............##.#..#..
.#.#....#....#................#
...#..#.#.##.#.#....#......#...
.........#..#.......##.##.#....
..............#..##.#.....#....
......#.........#...#...##.#..#
....##.....#.#...#.#.####.#....
#..#.#....#.##.......#....#....
...##....#...................##
##.#.......#....#.#.........#.#
.##.#..###...#.#.........#.....
...#.#.#..#...#...#.##....#..#.
....#.....###...#....##........
.............#....#....#....#..
#...#.....#.#...#.#............
#.#....#...........##.......#..
..#..#.........#....###.......#
....###..................##...#
.#........#.....##...#......#..
#..#......#..#.....#.##..#...#.
....#........#.##.#......#.....
#.#...#...............####...##
#.#.....##..#.####.............
##...##..#.##........#.#...#...
...#...........#............#..
...#..#..#........##...........
..#.##..#.#...#...#..#......#..
.....##......#...##.....##.....
.......##.....##....#..........
..........#.#...............#.#
#.#..........#..#..##..#...#..#
.#.#..#.###................#...
#...#...#....#...#....#.##.##..
.#................###.....##...
.....##.#.....##.#.....#.....##
.......#.......#......#.#......
..#....#......#.....#.....#..#.
#......#..##..####.....#.#..#..
.......#...###..#...#.....#....
#.#.#......#.............#..###
.#.#.......#..#.#..#..#...#.#..
..#.#......#......#.#....#.....
..#..###..#.#.....#....#.......
..........#........#......#..#.
##..........##....##..###.##...
...#....#.......#..##.......#..
##...#............##...#.#.#.#.
...........#...#.#....#.....##.
.#................#.......#...#
....##.#..#.#.........###.###.#
#..#...###..#...#......#..##...
..##........#.#..##.#..........
...#..#...#...............#.#..
##.##....#...#........#...#....
#..#......#.##.................
.....#..##.##.......#..........
...#.....#........#......#.....
.....#..#......#.....##...#....
#......#...###....#....###.....
................###..#..#..#.##
......#.......#..........#.#..#
###..#..#.##.............#.#...
....##.#.......#...#..##.......
..#.....##..#..#..#.#..........
.#.......#.#..#........##......
..............#.........#......
..#........##....#.#.#......##.
.#.#.........#.#...#.#.........
..........#..#.##.#....#...#.#.
............##....#.....###...#
#....#..#...#.#...#.....#....#.
.#...##.....#......#..#........
.#..#...###.#..##........#...#.
#..#...##.####.......#.....#...
#.##..#...#......#.#.......#.#.
#.#.....##...#.#...............
#...........##.##.#.........#..
...#...........#.#.#.#....#..#.
..#......#.#.#....##..#.#.....#
.........#.#.##...##...#.#.#...
...........#..#.####.#..#.#.###
#........#.#......#..#...#.....
...#....#......##...#.#........
......#.#....#.##....#....#..##
.......###......#.#.....#......
#..........##..................
.###.......##..#..##...##......
##.#..............#....#....##.
#....#.....#.##.....#..#....#.#
.......#.......#..#..#..##..#..
......#...........#..##....#...
.....#.......#..#......#..#..##
.##...#......#........#....#...
.....#..#....#...............##
..#.....#....#..#.##....#.#....
#.#......####...#..#.........#.
#.#........#..#........#...#...
..#..............#.......###.#.
...#.#....##.#......#........#.
....###.......##.#.....##.....#
.........#......#.#.......##.##
.......#.#....#.#...#...#....#.
....#....#....#.#.......##.....
#...#.....#..#.....#...........
#...#..#...#.#..#.............#
........###..#........#........
.............#....#..###..#.#.#
#...............#..#.#.........
##.....###..#......#...#....#..
.#...................##.#.##...
#..#........#.#...#..#...#.....
................#.#.........#..
#.....##.#.#...#..#.........##.
...#.....#....#..####.#........
....#.#...........#............
.....#........##..........#....
..#.......#.#.#.####..#......#.
#.......#...##.#.#..#.#.#......
##........#.#...###............
..##........#........#...#.#.#.
#.#..#.#.......#....#........#.
..............#....#.........#.
#....#.#........#.............#
..##...#..........#........#...
..#..#..#....#....#............"""

input_array = np.array([i*300 for i in input.split("\n")])

column_pos = 0
tree_hit_01 = 0
for i in input_array:
    if i[column_pos] == "#":
        tree_hit_01 += 1
    column_pos += 1

column_pos = 0
tree_hit_02 = 0
for i in input_array:
    if i[column_pos] == "#":
        tree_hit_02 += 1
    column_pos += 3

column_pos = 0
tree_hit_03 = 0
for i in input_array:
    if i[column_pos] == "#":
        tree_hit_03 += 1
    column_pos += 5

column_pos = 0
tree_hit_04 = 0
for i in input_array:
    if i[column_pos] == "#":
        tree_hit_04 += 1
    column_pos += 7

column_pos = 0
tree_hit_05 = 0
for i in range(0, len(input_array)+1, 2):
    if input_array[i][column_pos] == "#":
        tree_hit_05 += 1
    column_pos += 1

print(tree_hit_01*tree_hit_02*tree_hit_03*tree_hit_04*tree_hit_05)
