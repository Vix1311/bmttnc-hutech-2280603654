def truyCapPhanTu(tupleData):
    firstElement = tupleData[0]
    lastElement = tupleData[-1]
    return firstElement, lastElement

inputTuple = eval(input("Nhập tuple, ví dụ (1, 2, 3): "))
first,last = truyCapPhanTu(inputTuple)

print("Phần tử đầu tiên: ",first)
print("Phần tử cuối cùng: ",last)