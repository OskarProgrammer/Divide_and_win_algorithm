#find the dimensions of the largest squares that can fit in the given rectangle
def divide_and_win(x: int, y: int)->int:
    return min(x,y) if (max(x,y) % min(x,y) == 0) else (divide_and_win(max(x,y) % min(x,y), min(x,y)))

print(divide_and_win(1680, 640))
print(divide_and_win(480, 640))
print(divide_and_win(240, 160))
print(divide_and_win(240, 240))
print(divide_and_win(123210, 3210312))