def dao_nguoc_chuoi(chuoi):
    # đảo ngược chuỗi
    return chuoi[::-1]  
input_string = input("Nhập chuỗi cần đảo ngược: ")
print("Chuỗi sau khi đảo ngược là:", dao_nguoc_chuoi(input_string))