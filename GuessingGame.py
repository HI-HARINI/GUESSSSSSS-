from tkinter import*
import random
root=Tk()
root.geometry("500x500")
root.title("MultiD Array")
label1=Label(root)
label1.place(relx=0.5, rely=0.5, anchor=CENTER)
inputbox=Entry(root)
inputbox.place(relx=0.5,rely=0.2,anchor=CENTER)
label2=Label(root)
label2.place(relx=0.5, rely=0.3, anchor=CENTER)
array_3d=[[['1','2','3','4','5','6'],['A','B','C','D','E','F','G','H'],['Head','Tails'],['!','@','#','$','%','^','&','*']]]
def key():
    rn1=random.randint(0, 5)
    rn2=random.randint(0, 6)
    rn3=random.randint(0, 1)
    rn4=random.randint(0, 7)
    
    letter1=str(array_3d[0][0][rn1])
    letter2=array_3d[0][1][rn2]
    letter3=array_3d[0][2][rn3]
    letter4=array_3d[0][3][rn4]
    label1["text"]=letter1+letter2+letter3+letter4
    label2["text"]=inputbox.get()

button=Button(root, text="key", command=key)
button.place(relx=0.5, rely=0.4, anchor =CENTER)
root.mainloop()