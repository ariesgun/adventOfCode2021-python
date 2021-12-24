import os

# Day One
def run_day_one():
  with open('dayone.txt', 'r') as fi:
    nums = fi.readlines()
    measurements = [int(depth.strip()) for depth in nums]
    inc = 0
    
    prev = measurements[0]
    for num in measurements[1:]:
      if num > prev:
        #print(num + " vs " + prev)
        inc += 1
      prev = num
    
    print(inc)

def run_day_one_b():
  with open("dayone.txt", 'r') as fi:
    nums = fi.readlines()
    measurements = [int(depth.strip()) for depth in nums]
    inc = 0

    prev = measurements[0] + measurements[1] + measurements[2]
    for idx in range(len(measurements[:len(measurements)-2])):
      cur = measurements[idx] + measurements[idx+1] + measurements[idx+2]
      if cur > prev:
        inc += 1
      prev = cur

    print(inc)


# Day Two
def run_day_two():
  with open('daytwo.txt', 'r') as fi:
    lines = fi.readlines()
    cmds = [line.strip() for line in lines]

    horizontal = 0
    vertical = 0

    for cmd in cmds:
      (a, b) = cmd.split()
      if a == 'forward':
        horizontal += int(b)
      elif a == 'down':
        vertical += int(b)
      elif a == 'up':
        vertical -= int(b)

    print(horizontal * vertical)

    # Part B
    horizontal = 0
    vertical = 0
    aim = 0
    for cmd in cmds:
      (a, b) = cmd.split()
      if a == 'forward':
        horizontal += int(b)
        vertical += (aim * int(b))
      elif a == 'down':
        aim += int(b)
      elif a == 'up':
        aim -= int(b)

    print(horizontal * vertical)

# Day Three

def calculate_common(nums, i, oxygen):
  output = [0 for i in range(len(nums[0]))]

  for bin in nums:
    for idx in range(len(bin)):
      if bin[idx] == '0':
        output[idx] -= 1
      elif bin[idx] == '1':
        output[idx] += 1

  val = ''
  for out in output:
    print(out)
    if oxygen:
      val += '1' if out >= 0 else '0'
    else:
      val += '0' if out >= 0 else  '1'

  print("coommon ", val, i, val[i])
  return val[i]


def run_day_three():

  # Part A
  with open('daythree.txt', 'r') as fi:
    lines = fi.readlines()
    binaries = [line.strip() for line in lines]

    output = [0 for i in range(len(binaries[0]))]

    for bin in binaries:
      for idx in range(len(bin)):
        if bin[idx] == '0':
          output[idx] -= 1
        elif bin[idx] == '1':
          output[idx] += 1

    gamma = ''
    epsilon = ''
    for out in output:
      gamma += '1' if out >= 0 else '0'
      epsilon += '0' if out >= 0 else  '1'
    
    print ("Part one")
    print(gamma)
    print(epsilon)
    print(int(gamma, 2) * int(epsilon, 2))
    
  # Part B
  with open('daythree.txt', 'r') as fi:
    lines = fi.readlines()
    binaries = [line.strip() for line in lines]

    currents = binaries.copy()
    for i in range(len(gamma)):
      print("checkL: ", i, currents)
      common = calculate_common(currents, i, True)
      temps = []
      print(currents, common)
      for j in range(len(currents)):
        if currents[j][i] == common:
          temps.append(currents[j])

      currents = []
      currents = temps.copy()

      if (len(currents) <= 1):
        break

    oxygen = currents[-1]
    print(oxygen)
    
    currents = binaries.copy()
    for i in range(len(epsilon)):
      common = calculate_common(currents, i, False)
      temps = []
      for j in range(len(currents)):
        if currents[j][i] == common:
          temps.append(currents[j])

      currents = []
      currents = temps.copy()

      if (len(currents) <= 1):
        break

    print(currents)
    carbon = currents[-1]

    print(int(oxygen,2) * int(carbon,2))


#Day Four
def run_day_four():
  with open('dayfour.txt', 'r') as fi:
    lines = fi.readlines()
    binaries = [line.strip() for line in lines if len(line.strip()) > 0]

    input_bingo = list(map(int, binaries[0].split(',')))
    original_input = input_bingo.copy()

    #boards
    boards = []
    for n in range(1, len(binaries), 5):
      board = []
      for j in range(0, 5):
        row = list(map(int, binaries[n+j].rstrip().split()))
        board.append(row)
      print(board)
      boards.append(board)

    # Do the bingo
    row_count = [[0] * 5 for _ in range(len(boards))]
    col_count = [[0] * 5 for _ in range(len(boards))]

    for num in input_bingo:
      for idx, board in enumerate(boards):
        for r in range(len(board)):
          for c in range(len(board[0])):
            if board[r][c] == num:
              row_count[idx][r] += 1
              col_count[idx][c] += 1
              board[r][c] = 0
              if row_count[idx][r] == 5 or col_count[idx][c] == 5:
                # We got a bingo
                print(idx)
                print(boards[idx])

                rem = 0
                for r in range(len(board)):
                  for c in range(len(board[0])):
                    rem += board[r][c]

                print(rem)
                print(rem * num)
                break

    # Part B
    input_bingo = original_input
    boards = []
    for n in range(1, len(binaries), 5):
      board = []
      for j in range(0, 5):
        row = list(map(int, binaries[n+j].rstrip().split()))
        board.append(row)
      print(board)
      boards.append(board)
    print(boards)

    row_count = [[0] * 5 for _ in range(len(boards))]
    col_count = [[0] * 5 for _ in range(len(boards))]
    win_board = []

    for num in input_bingo:
        for idx, board in enumerate(boards):
          if idx not in win_board:
            for r in range(len(board)):
              for c in range(len(board[0])):
                if board[r][c] == num:
                  row_count[idx][r] += 1
                  col_count[idx][c] += 1
                  board[r][c] = -1
                  
                  if row_count[idx][r] == 5 or col_count[idx][c] == 5:
                    # We got a bingo
                    print("----", num)
                    print(idx, r, c, row_count[idx][r], col_count[idx][r])
                    print(boards[idx])

                    rem = 0
                    for r in range(len(board)):
                      for c in range(len(board[0])):
                        if board[r][c] != -1:
                          rem += board[r][c]

                    print(rem)
                    print(rem * num)
                    win_board.append(idx)
                    break
              
              if idx in win_board:
                break

    print(len(win_board))
    print("Last one is ", win_board[-1])


# Day Five
def run_day_five():
  with open('dayfive.txt', 'r') as fi:
    lines = fi.readlines()
    coordinates = [line.strip() for line in lines]

    #print(coordinates)
    lines = []
    min_global_x = 0
    max_global_x = 0
    min_global_y = 0
    max_global_y = 0
    for coord in coordinates:
      coors = coord.split(' -> ')
      line = []
      for coor in coors:
        coordinate = list(map(int, coor.split(',')))
        min_global_x = min(min_global_x, coordinate[0])
        max_global_x = max(max_global_x, coordinate[0])
        min_global_y = min(min_global_y, coordinate[1])
        max_global_y = max(max_global_y, coordinate[1])
        line.append(coordinate)

      if line[0][0] == line[1][0]:
        # Vertical Line
        min_y = min(line[0][1], line[1][1])
        max_y = max(line[0][1], line[1][1])
        #print(line[0][0], min_y, max_y)
        for y in range(min_y, max_y+1):
          lines.append([line[0][0], y])
      elif line[0][1] == line[1][1]:
        # Horizontal Line
        min_x = min(line[0][0], line[1][0])
        max_x = max(line[0][0], line[1][0])
        #print(line[0][0], min_x, max_x)
        for x in range(min_x, max_x+1):
          lines.append([x, line[0][1]])
      else:
        # Diagonal
        lc = 0 if line[0][0] < line[1][0] else 1 # Left X coordinate
        rc = 1 if line[0][0] < line[1][0] else 0 # Left X coordinate
        der = int((line[rc][1] - line[lc][1]) / (line[rc][0] - line[lc][0]))
        print(der, line[lc], line[rc])
        for coo in range(line[rc][0]-line[lc][0]+1):
          #print([line[lc][0] + coo, line[lc][1] + coo * der  ])
          lines.append([line[lc][0] + coo, line[lc][1] + coo * der  ])
        #print(lines)

    maps = [[0] * (max_global_x + 1) for _ in range(max_global_y + 1)]
    print(min_global_x, max_global_x, min_global_y, max_global_y)
    print(len(maps), len(maps[0]))
    
    for line in lines:
      maps[line[1]][line[0]] += 1

    rem = 0
    for i in maps:
      for j in i:
        if j > 1:
          rem += 1
    print(rem)


# Day Six
def dp(day, count):
  pass

def run_day_six():
  with open('daysix.txt', 'r') as fi:
    lines = fi.readlines()
    fishes = lines[0].split(',')
    fishes = list(map(int, fishes))

    print(fishes)

    caches = [0 for _ in range(6)]

    result = 0

    for idx, fish in enumerate(fishes):
      if caches[fish] == 0:
        # Calculate
        temp = 1
        cur = [fish]

        for i in range(256):
          for idx, cu in enumerate(cur):
            if cur[idx] == 0:
              cur[idx] = 6
              cur.append(9)
              temp += 1
            else:
              cur[idx] -= 1

          print("temp", temp, cur)

        caches[fish] = temp
        result += temp
      else:
        result += caches[fish]

    print(result)

# Day Seven
def run_day_seven():
  with open('dayseven.txt', 'r') as fi:
    lines = fi.readlines()
    nums = list(map(int, lines[0].split(',')))

    # Part 1
    temp = {}
    for position in range(min(nums), max(nums)+1):
      temp[position] = sum(abs(position - crab_pos) for crab_pos in nums)
    print(temp)

    print(min(temp.items(), key=lambda item: item[1]))

    # Part 2
    temp = {}
    for position in range(min(nums), max(nums) + 1):
      temp[position] = sum( ((abs(position - crab_pos) * (abs(position - crab_pos) + 1) ) / 2) for crab_pos in nums)

    print(min(temp.items(), key=lambda item: item[1]))

#run_day_one()
#run_day_one_b()
#run_day_two()
#run_day_three()
#run_day_four()
#run_day_five()
#run_day_six()
run_day_seven()