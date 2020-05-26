import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 400,  relief = 'raised')
canvas1.pack()
canvas1.config(bg='skyblue')

label1 = tk.Label(root, text='Automatic TimeTable Generation')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='No.of Subjects:')
label2.config(font=('helvetica', 10))
canvas1.create_window(50, 50, window=label2)
label3 = tk.Label(root, text='No.of Default Periods:')
label3.config(font=('helvetica', 10))
canvas1.create_window(68, 70, window=label3)
label4 = tk.Label(root, text='No.of Labs:')
label4.config(font=('helvetica', 10))
canvas1.create_window(38, 90, window=label4)
label5 = tk.Label(root, text='No.of Free Periods:')
label5.config(font=('helvetica', 10))
canvas1.create_window(60, 110, window=label5)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 50, window=entry1)
entry2 = tk.Entry (root) 
canvas1.create_window(200, 70, window=entry2)
entry3 = tk.Entry (root) 
canvas1.create_window(200, 90, window=entry3)
entry4 = tk.Entry (root) 
canvas1.create_window(200, 110, window=entry4)

def show():
	x1=entry1.get()
	label6 = tk.Label(root, text='Enter names of '+x1+'subjects: ',font=('helvetica', 10))
	canvas1.create_window(70, 200, window=label6)
	for i in range(0,int(x1)):
		print_data()
def print_data():		
	label7=label(text='subject: ')
	label7.grid(row=7,column=0)
button1 = tk.Button(text='Next', command=show, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)
    
root.mainloop()
