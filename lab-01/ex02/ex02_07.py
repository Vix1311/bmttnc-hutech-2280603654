print("Nhập các dòng văn bản (Nhập done để kết thúc): ")
lines = []
while True:
    line =input()
    if line.lower() == 'done':
        break
    lines.append(line)
    # append() thêm các dòng văn bản vào danh sách lines
# chuyển tất cả các dòng văn bản thành chữ hoa
print("\nCác dòng văn bản đã nhập sau khi chuyển thành chữ hoa là: ")
for line in lines:
    print(line.upper())