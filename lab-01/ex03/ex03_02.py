def daoNguocList(lst):
    return lst[::-1]

input_list = input("Nhập danh sách các số, cách nhau bởi dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))

listDaoNguoc = daoNguocList(numbers)
print("List sau khi được đảo ngược: ",listDaoNguoc)