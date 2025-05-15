ban_kinh = float(input("Nhập bán kính hình tròn: "))
dientich = 3.14 * (ban_kinh**2)
# sử dụng .format() để chèn giá trị thông qua dấu {} 
print ('Diện tích hình tròn với bán kính {} là: {}'.format(ban_kinh, dientich))
# sử dụng f-string (formatted string literal) giúp biến được chèn trực tiếp vào trong chuỗi thông qua {}
print (f'Diện tích hình tròn với bán kính {ban_kinh} là: {dientich}')

