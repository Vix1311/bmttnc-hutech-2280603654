# tạo 1 danh sách rỗng
j = []
# duyệt qua từng phần tử trong đoạn từ 2000 đến 3200, kiểm tra xem nó có chia hết cho 7 và không chia hết cho 5 hay không
for i in range(2000, 3200):
    if (i % 7 == 0) and (i % 5 != 0):
        j.append(str(i))
print(" ,".join(j))
