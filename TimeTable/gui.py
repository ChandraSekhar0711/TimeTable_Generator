import tkinter as tk
root= tk.Tk()
canvas1 = tk.Canvas(root, width = 1300, height = 1300,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Automatic TimeTable Generation')
label1.config(font=('helvetica', 14))
canvas1.create_window(450, 25, window=label1)

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
label16=tk.Label(root,text=f'No.of Sections: ')
label16.config(font=('helvetica', 10))
canvas1.create_window(50, 600 , window=label16)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 50, window=entry1)
entry2 = tk.Entry (root) 
canvas1.create_window(200, 70, window=entry2)
entry3 = tk.Entry (root) 
canvas1.create_window(200, 90, window=entry3)
entry4 = tk.Entry (root) 
canvas1.create_window(200, 110, window=entry4)
entry5 = tk.Entry (root) 
canvas1.create_window(200,600, window=entry5)


sublabels = None
subfaculty= None
subdefault= None
sublabs=None
sublabfac=None
sublabfac1=None
freePeriods=None
lst1=[]
lst2=[]
lst3=[]
lst4=[]
def display():
    for i in sublabels:
        lst1.append(i.get()) 
    print(lst1)              
    for i in subdefault:
        lst2.append(i.get())
    print(lst2)      
    for i in sublabs:
        lst3.append(i.get())
    print(lst3)    
        
    for i in freePeriods:
        lst4.append(i.get())
    print(lst4)    
    #no_sec()
def show():
    global sublabels,subfaculty,subfaculty1,subdefault,sublabs,sublabfac,sublabfac1,freePeriods,no_of_section
    global x1,x2,x3,x4,x5
    x1=entry1.get()
    x2=entry2.get()
    x3=entry3.get()
    x4=entry4.get()
    x5=entry5.get()
    sublabels = [0] * int(x1)
    subfaculty= [0] * int(x1)
    subfaculty1= [0] * int(x1)
    subdefault= [0] * int(x2)
    sublabs=[0] * int(x3)
    sublabfac=[0] *int(x3)
    sublabfac1=[0] *int(x3)
    freePeriods=[0]*int(x4)
    no_of_section=int(x5)
    label6 = tk.Label(root, text=f'Enter names of {x1} subjects: ',font=('helvetica', 10))
    canvas1.create_window(85,140, window=label6)
    for i in range(0,int(x1)):
        print_sub(i)
        print_fac(i)
    label7 = tk.Label(root, text=f'Enter {x2} default periods: ',font=('helvetica', 10))
    canvas1.create_window(70, 320, window=label7)
    for i in range(0,int(x2)):
        print_def(i)     
    label8 = tk.Label(root, text=f'Enter names of {x3} labs: ',font=('helvetica', 10))
    canvas1.create_window(70, 420, window=label8)
    for i in range(0,int(x3)):
        print_labs(i)
        print_labfac(i)   
    label9 = tk.Label(root, text=f'Enter names of {x3} Free Periods: ',font=('helvetica', 10))
    canvas1.create_window(93, 500, window=label9)
    for i in range(0,int(x4)):
        print_freePeriods(i)          
    button2 = tk.Button(text='Submit', command=display, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
    canvas1.create_window(450,560 , window=button2)



def print_sub(i):
    global sublabels
    # print(i,sublabels[i])
    label10 = tk.Label(root, text=f'Name of subject{i+1}: ')
    label10.config(font=('helvetica', 10))
    canvas1.create_window(60, 160 + i*20, window=label10)
    sublabels[i] = tk.Entry (root) 
    canvas1.create_window(200, 160+ i*20, window=sublabels[i])
    # label7=tk.Label(text='subject: ')
    # tk.Entry (root)
    # label7.pack()
def print_fac(i):   
    global subfaculty  
    label11 = tk.Label(root, text=f'Faculty of subject{i+1}: ')
    label11.config(font=('helvetica', 10))
    canvas1.create_window(350, 160 +i*20, window=label11)
    subfaculty[i] = tk.Entry (root) 
    canvas1.create_window(500,160+ i*20, window=subfaculty[i])    
    subfaculty1[i] = tk.Entry (root) 
    canvas1.create_window(650,160+ i*20, window=subfaculty1[i])
    
def print_def(i):    
    global subdefault
    # print(i,subdefault[i])
    label12 = tk.Label(root, text=f'Default period{i+1}: ')
    label12.config(font=('helvetica', 10),)
    canvas1.create_window(50,  340+ i*20, window=label12)
    subdefault[i] = tk.Entry (root) 
    canvas1.create_window(200, 340+ i*20, window=subdefault[i])
def print_labs(i):
    global sublabs
    label13 = tk.Label(root, text=f'Name of Lab{i+1}: ')
    label13.config(font=('helvetica', 10))
    canvas1.create_window(50, 440 + i*20, window=label13)
    sublabs[i] = tk.Entry (root) 
    canvas1.create_window(200, 440+ i*20, window=sublabs[i])

def print_labfac(i):
    global sublabfac
    label14 = tk.Label(root, text=f'Faculty of labs{i+1}: ')
    label14.config(font=('helvetica', 10))
    canvas1.create_window(350, 440 + i*20, window=label14)
    sublabfac[i] = tk.Entry (root) 
    canvas1.create_window(500, 440+ i*20, window=sublabfac[i])
    sublabfac1[i] = tk.Entry (root) 
    canvas1.create_window(650, 440+ i*20, window=sublabfac1[i])
def print_freePeriods(i):
    global freePeriods
    label15 = tk.Label(root, text=f'Free Period{i+1}: ')
    label15.config(font=('helvetica', 10))
    canvas1.create_window(50, 520 + i*20, window=label15)
    freePeriods[i] = tk.Entry (root) 
    canvas1.create_window(200, 520+ i*20, window=freePeriods[i])

button1 = tk.Button(text='Next', command=show, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(450, 90, window=button1)

root.mainloop()