import random
import time
import os

cell_types = [1, 2, 3, 0]
# 1 - рыба, 2 - креветка ,3 - скала, 0 - ничего
print("Ширина океана: ")
width = int(input())
print("Высота океана: ")
height = int(input())
ocean = [[random.randint(0, 3) for i in range(width)] for j in range(height)]
ocean_copy = [[random.randint(0, 3) for i in range(width + 2)] for j in range(height + 2)]
for i in range(width + 2):
    ocean_copy[0][i] = 0
    ocean_copy[height + 1][i] = 0
for i in range(height + 2):
    ocean_copy[i][0] = 0
    ocean_copy[i][width + 1] = 0
while True:
    for i in range(height):
        print(*ocean[i])
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(height):
        for j in range(width):
            ocean_copy[i + 1][j + 1] = ocean[i][j]
    for i in range(height):
        for j in range(width):
            if ocean_copy[i + 1][j + 1] == 1:
                cnt = 0
                if ocean_copy[i][j] == 1: cnt += 1
                if ocean_copy[i + 1][j] == 1: cnt += 1
                if ocean_copy[i][j + 1] == 1: cnt += 1
                if ocean_copy[i][j + 2] == 1: cnt += 1
                if ocean_copy[i + 2][j] == 1: cnt += 1
                if ocean_copy[i + 1][j + 2] == 1: cnt += 1
                if ocean_copy[i + 2][j + 1] == 1: cnt += 1
                if ocean_copy[i + 2][j + 2] == 1: cnt += 1
                if cnt > 3 or cnt < 2:
                    ocean[i][j] = 0
            elif ocean_copy[i + 1][j + 1] == 2:
                cnt = 0
                if ocean_copy[i][j] == 2: cnt += 1
                if ocean_copy[i + 1][j] == 2: cnt += 1
                if ocean_copy[i][j + 1] == 2: cnt += 1
                if ocean_copy[i][j + 2] == 2: cnt += 1
                if ocean_copy[i + 2][j] == 2: cnt += 1
                if ocean_copy[i + 1][j + 2] == 2: cnt += 1
                if ocean_copy[i + 2][j + 1] == 2: cnt += 1
                if ocean_copy[i + 2][j + 2] == 2: cnt += 1
                if cnt > 3 or cnt < 2:
                    ocean[i][j] = 0
            elif ocean_copy[i + 1][j + 1] == 0:
                cnt = 0
                if ocean_copy[i][j] == 1: cnt += 1
                if ocean_copy[i + 1][j] == 1: cnt += 1
                if ocean_copy[i][j + 1] == 1: cnt += 1
                if ocean_copy[i][j + 2] == 1: cnt += 1
                if ocean_copy[i + 2][j] == 1: cnt += 1
                if ocean_copy[i + 1][j + 2] == 1: cnt += 1
                if ocean_copy[i + 2][j + 1] == 1: cnt += 1
                if ocean_copy[i + 2][j + 2] == 1: cnt += 1
                if cnt == 3:
                    ocean[i][j] = 1
                else:
                    cnt = 0
                    if ocean_copy[i][j] == 2: cnt += 1
                    if ocean_copy[i + 1][j] == 2: cnt += 1
                    if ocean_copy[i][j + 1] == 2: cnt += 1
                    if ocean_copy[i][j + 2] == 2: cnt += 1
                    if ocean_copy[i + 2][j] == 2: cnt += 1
                    if ocean_copy[i + 1][j + 2] == 2: cnt += 1
                    if ocean_copy[i + 2][j + 1] == 2: cnt += 1
                    if ocean_copy[i + 2][j + 2] == 2: cnt += 1
                    if cnt == 3:
                        ocean[i][j] = 2




