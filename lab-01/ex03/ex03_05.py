def demSoLanXuatHien(lst):
    countDist ={}
    for item in lst:
        if item in countDist:
            countDist[item] +=1
        else:
            countDist[item] =1
    return countDist

inputString = input ("Nhập vào danh sách các từ, cách nhau  bằng dấu cách: ")
wordList = inputString.split()

soLanXuatHien = demSoLanXuatHien(wordList)
print("Số lần xuất hiện của các phần tử: ", soLanXuatHien)