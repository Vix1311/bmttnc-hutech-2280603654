def taoTuppleTuList(lst):
    return tuple(lst)

inputList = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int,inputList.split(',')))

myTupple = taoTuppleTuList(numbers)
print("List: ", numbers)
print("tuple: ",myTupple)