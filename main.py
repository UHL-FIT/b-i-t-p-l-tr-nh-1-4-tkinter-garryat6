import tkinter as tk
root = tk.Tk()
root.title("Họ tên sinh viên")
root.geometry("400x200")
nhan_truong = tk.Label(
    root, 
    text="TRƯỜNG ĐẠI HỌC HẠ LONG", 
    font=("Arial", 14, "bold"), 
    fg="white", 
    bg="#0056b3"  
)

nhan_truong.pack(fill="x", pady=10) 
nhan_ten = tk.Label(root, text="Họ tên: Nguyễn Văn A", font=("Arial", 12))
nhan_ten.pack(pady=5)
nhan_msv = tk.Label(root, text="MSSV: 22010001", font=("Arial", 12), fg="red")
nhan_msv.pack(pady=5)
nut_thoat = tk.Button(
    root, 
    text="Đóng ứng dụng", 
    command=root.destroy, 
    bg="#dc3545", 
    fg="white"
)
nut_thoat.pack(pady=20)

root.mainloop()