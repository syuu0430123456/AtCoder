def binary_search(data, value):
    left = 0
    right = len(data) -1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == value: #中央の値と一致した場合->位置を返す
            return mid
        elif data[mid] < value:
            left = mid + 1
        else:
            right = mid -1
    return -1

data = [50, 30, 90, 10, 20,70, 60, 40, 80]
data.sort()
print(binary_search(data,40))
