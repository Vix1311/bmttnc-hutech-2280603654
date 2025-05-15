def tinhTongSoChan(lst):
    tong=0
    for num in lst:
        if num %2 == 0:
            tong += num
    return tong

inputList = input("Nhập danh sách các số cách nhau bằng dấu phẩy: ")
numbers = list(map(int, inputList.split(',')))

tongChan = tinhTongSoChan(numbers)
print("Tổng số chẳn là ", tongChan)