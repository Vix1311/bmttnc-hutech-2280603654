def chia_het_cho_5(so_nhi_phan):
    # chuyển đổi số nhị phân thành số thập phân
    so_thap_phan = int(so_nhi_phan, 2)
    # kiểm tra xem số thập phân có chia hết cho 5 hay không
    if so_thap_phan % 5 == 0:
        return True
    else:
        return False
# nhập số nhị phân từ bàn phím
chuoi_nhi_phan = input("Nhập chuỗi số nhị phân (phân cách nhau bởi dấu phẩy): ")
# tách chuỗi thành danh sách các số nhị phân và kiểm tra chia hết cho 5
so_nhi_phan_list = chuoi_nhi_phan.split(", ")
so_chia_het_cho_5 = [so for so in so_nhi_phan_list if chia_het_cho_5(so)]
# in ra danh sách các số nhị phân chia hết cho 5
if len(so_chia_het_cho_5) > 0:
    ketqua = ','.join(so_chia_het_cho_5)
    print("Các số nhị phân chia hết cho 5 là: ", ketqua)
    # print("Các số nhị phân chia hết cho 5 là: ", ", ".join(so_chia_het_cho_5))
else:
    print("Không có số nhị phân nào chia hết cho 5.")