import tkinter as tk
root = tk.Tk()
root.title("Thẻ Sinh Viên Số")
root.geometry("400x300")

# 1. Nhãn tiêu đề với Phông chữ và Màu sắc
nhan_truong = tk.Label(
    root, 
    text="ĐẠI HỌC HẠ LONG", 
    font=("Arial", 14, "bold"), 
    fg="green", 
    bg="#43b3b9" # Màu xanh thương hiệu
)
nhan_truong.pack(fill="x", pady=10) # fill="x" để màu nền trải rộng hết chiều ngang
# 2. Nhãn hiển thị họ tên
nhan_ten = tk.Label(root, text="Khoa công nghệ thông tin", font=("Arial", 16))
nhan_ten.pack(pady=5)
nhan_ten = tk.Label(root, text="Họ tên: Nguyễn Văn A", font=("Arial", 12))
nhan_ten.pack(pady=5)

# 3. Nhãn hiển thị MSSV với màu đỏ nổi bật
nhan_msv = tk.Label(root, text="MSSV: 22010001", font=("Arial", 12), fg="red")
nhan_msv.pack(pady=5)

# 4. Tạo nút bấm để thoát chương trình
nut_thoat = tk.Button(
    root, 
    text="Đóng ứng dụng", 
    command=root.destroy, 
    bg="#dc3535", # Màu đỏ cảnh báo
    fg="white"
)
nut_thoat.pack(pady=60)

root.mainloop()

