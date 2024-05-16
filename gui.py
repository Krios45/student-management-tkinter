from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from datetime import date

root = Tk()
root.title("Student Management")
root.geometry("900x600+300+80")

def add_window():
    add_window = Toplevel()
    add_window.title("Add Student")
    add_window.geometry("500x500+500+150")
    
    # Student infomation
    Label(add_window, text="Họ và tên:", font="Arial 13").place(x=30, y=20)
    Label(add_window, text="Tuổi:", font="Arial 13").place(x=30, y=70)
    Label(add_window, text="Giới tính:", font="Arial 13").place(x=30, y=120)
    Label(add_window, text="Mã số sinh viên:", font="Arial 13").place(x=30, y=170)
    Label(add_window, text="Chuyên ngành:", font="Arial 13").place(x=30, y=220)
    Label(add_window, text="Email:", font="Arial 13").place(x=30, y=270)
    Label(add_window, text="Địa chỉ:", font="Arial 13").place(x=30, y=320)

    # Entry
    Name = StringVar()
    name_entry = Entry(add_window, textvariable=Name, width=20, font="Arial 13").place(x=200, y=20)
    
    Age = StringVar()
    age_entry = Entry(add_window, textvariable=Age, width=20, font="Arial 13").place(x=200, y=70)
    
    Gender = IntVar()
    g1 = Radiobutton(add_window, text="Nam", variable=Gender, value=1, font="Arial 13").place(x=200, y=120)
    g2 = Radiobutton(add_window, text="Nữ", variable=Gender, value=2, font="Arial 13").place(x=320, y=120)
    
    Id = StringVar()
    id_entry = Entry(add_window, textvariable=Id, width=20, font="Arial 13").place(x=200, y=170)
    
    Major = Combobox(add_window, values=["BSCE", "BJS", "ECE", "ESAS", "FTH", "MJM"], font="Arial 13", width=18, state="r")
    Major.place(x=200, y=220)
    email_entry = Entry(add_window, textvariable=Major, width=20, font="Arial 13").place(x=200, y=270)
    
    Address = StringVar()
    address_entry = Entry(add_window, textvariable=Address, width=20, font="Arial 13").place(x=200, y=320)
    
    def add_window2_and_close():
        add_window.destroy()
        add_window2()

    Button(add_window, text="Tiếp tục", font="Arial 13", width=10, height=2, command=add_window2_and_close).place(x=200, y=370)

def add_window2():
    add_window2 = Toplevel()
    add_window2.title("Add Student")
    add_window2.geometry("580x250+500+250")
    
    def add_window3_and_close():
        add_window2.destroy()
        add_window3()
    
    def add_window4_and_close():
        add_window2.destroy()
        add_window4()

    def add_window5_and_close():
        add_window2.destroy()
        add_window5()

    def add_window6_and_close():
        add_window2.destroy()
        add_window6()

    Button(add_window2, text="Sinh viên năm nhất", width=20, height=2, font="Arial 13", command=add_window3_and_close).place(x=50, y=50)
    Button(add_window2, text="Sinh viên năm hai", width=20, height=2, font="Arial 13", command=add_window4_and_close).place(x=320, y=50)
    Button(add_window2, text="Sinh viên năm ba", width=20, height=2, font="Arial 13", command=add_window5_and_close).place(x=50, y=150)
    Button(add_window2, text="Sinh viên năm bốn", width=20, height=2, font="Arial 13", command=add_window6_and_close).place(x=320, y=150)

# SINH VIÊN NĂM NHẤT
def add_window3():
    add_window3 = Toplevel()
    add_window3.title("Add Student")
    add_window3.geometry("500x250+500+150")

    Label(add_window3, text="Trường cấp 3 theo học:", font="Arial 13").place(x=30, y=20)
    Label(add_window3, text="Điểm thi THPT:", font="Arial 13").place(x=30, y=70)

    School = StringVar()
    school_entry = Entry(add_window3, textvariable=School, width=20, font="Arial 13").place(x=250, y=20)

    Point = StringVar()
    point_entry = Entry(add_window3, textvariable=Point, width=20, font="Arial 13").place(x=250, y=70)
    
    def show_mb():
        messagebox.showinfo("Thông báo", "Thêm sinh viên thành công!!... (^_^)")
        add_window3.after(0, add_window3.destroy)
        

    Button(add_window3, text="Xác nhận", font="Arial 13", width=10, height=2, command=show_mb).place(x=200, y=120)

# SINH VIÊN NĂM HAI
def add_window4():
    add_window4 = Toplevel()
    add_window4.title("Add Student")
    add_window4.geometry("500x250+500+150")

    Label(add_window4, text="Điểm GPA:", font="Arial 13").place(x=30, y=20)
    Label(add_window4, text="Học bổng loại:", font="Arial 13").place(x=30, y=70)

    GPA = StringVar()
    gpa_entry = Entry(add_window4, textvariable=GPA, width=20, font="Arial 13").place(x=250, y=20)

    Scholarship = StringVar()
    scholarship_entry = Entry(add_window4, textvariable=Scholarship, width=20, font="Arial 13").place(x=250, y=70)

    def show_mb():
        messagebox.showinfo("Thông báo", "Thêm sinh viên thành công!!... (^_^)")
        add_window4.after(0, add_window4.destroy)

    Button(add_window4, text="Xác nhận", font="Arial 13", width=10, height=2, command=show_mb).place(x=200, y=120)

# SINH VIÊN NĂM BA
def add_window5():
    add_window5 = Toplevel()
    add_window5.title("Add Student")
    add_window5.geometry("500x250+500+150")

    Label(add_window5, text="Điểm GPA:", font="Arial 13").place(x=30, y=20)
    Label(add_window5, text="Học bổng loại:", font="Arial 13").place(x=30, y=70)
    Label(add_window5, text="Công ty thực tập:", font="Arial 13").place(x=30, y=120)

    Gpa = StringVar()
    gpa_entry = Entry(add_window5, textvariable=Gpa, width=20, font="Arial 13").place(x=250, y=20)

    Scholarship = StringVar()
    scholarship_entry = Entry(add_window5, textvariable=Scholarship, width=20, font="Arial 13").place(x=250, y=70)

    Company = StringVar()
    company_entry = Entry(add_window5, textvariable=Company, width=20, font="Arial 13").place(x=250, y=120)
    
    def show_mb():
        messagebox.showinfo("Thông báo", "Thêm sinh viên thành công!!... (^_^)")
        add_window5.after(0, add_window5.destroy)
        

    Button(add_window5, text="Xác nhận", font="Arial 13", width=10, height=2, command=show_mb).place(x=200, y=170)

# SINH VIÊN NĂM BỐN
def add_window6():
    add_window6 = Toplevel()
    add_window6.title("Add Student")
    add_window6.geometry("500x300+500+150")

    Label(add_window6, text="Điểm GPA:", font="Arial 13").place(x=30, y=20)
    Label(add_window6, text="Học bổng loại:", font="Arial 13").place(x=30, y=70)
    Label(add_window6, text="Công ty thực tập:", font="Arial 13").place(x=30, y=120)
    Label(add_window6, text="Đề tài nghiên cứu", font="Arial 13").place(x=30, y=170)

    Gpa = StringVar()
    gpa_entry = Entry(add_window6, textvariable=Gpa, width=20, font="Arial 13").place(x=250, y=20)

    Scholarship = StringVar()
    scholarship_entry = Entry(add_window6, textvariable=Scholarship, width=20, font="Arial 13").place(x=250, y=70)

    Company = StringVar()
    company_entry = Entry(add_window6, textvariable=Company, width=20, font="Arial 13").place(x=250, y=120)

    Project = StringVar()
    project_entry = Entry(add_window6, textvariable=Project, width=20, font="Arial 13").place(x=250, y=170)
    
    def show_mb():
        messagebox.showinfo("Thông báo", "Thêm sinh viên thành công!!... (^_^)")
        add_window6.after(0, add_window6.destroy)
        

    Button(add_window6, text="Xác nhận", font="Arial 13", width=10, height=2, command=show_mb).place(x=200, y=220)

def show_window():
    show_window = Toplevel()
    show_window.title("List of students")
    show_window.geometry("500x500+500+150")

    Label(show_window, text="Danh sách sinh viên", font="Arial 13").pack(side=TOP, fill=X)

def delete_window():
    delete_window = Toplevel()
    delete_window.title("Delete student")
    delete_window.geometry("500x200+500+250")

    Label(delete_window, text="Nhập mã số sinh viên:", font="Arial 13").place(x=30, y=20)
    Delete = StringVar()
    delete_entry = Entry(delete_window, textvariable=Delete, width=20, font="Arial 13").place(x=250, y=20)

    def show_mb():
        messagebox.showinfo("Thông báo", "Xoá sinh viên thành công!!... (^_^)")
        delete_window.after(0, delete_window.destroy)

    Button(delete_window, text="Xác nhận", font="Arial 13", width=10, height=2, command=show_mb).place(x=200, y=70)

def exit():
    root.destroy()

# Main 
Label(root, text = "Quản lí sinh viên", width=10, height=2, bg="white", fg="black", font="Arial 20 ").pack(side=TOP, fill=X)

image = PhotoImage(file="C:/Users/KIEN/Downloads/student.png")
image = image.subsample(2, 2)
Label(root, image=image,).place(x=30, y=150)

Button(root, text = "Thêm sinh viên", width=20, height=3, font="Arial 12", command=add_window).place(x=620,y=130)
Button(root, text = "Hiển thị sinh viên", width=20, height=3, font="Arial 12", command=show_window).place(x=620,y=230)
Button(root, text = "Xoá sinh viên", width=20, height=3, font="Arial 12", command=delete_window).place(x=620,y=330)
Button(root, text = "Thoát", width=20, height=3, font="Arial 12", command=exit).place(x=620,y=430)

root.mainloop()

