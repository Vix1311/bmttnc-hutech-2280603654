def xoaPhanTu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False
    
myDict = {'a':1,'b':2,'c':3,'d':4}
keyToDelete ='e'
result = xoaPhanTu(myDict, keyToDelete)
if result:
    print("Phần tử đã được xóa từ Dictionary: ",myDict)
else:
    print("Không tìm thấy phần tử cần xóa trong Dictionary.")