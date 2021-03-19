from tkinter import*
root = Tk()
root.title("When we will do something intresting in pythonnnnnnnnnnnnnnnnNNNNNN")
root.geometry("1000x1000")

Entry2 = Entry(root)
Entry3 = Entry(root)
Entry4 = Entry(root)

label = Label(root)
label1 = Label(root)
label2 = Label(root)



class Pointy:
    def gy():
        pointy3001= Entry2.get()
        label['text'] = str(pointy3001)
    def gy2():
        pointy3002= Entry3.get()
        label1['text'] = str(pointy3002)
    def gy3():
        pointy3003= Entry4.get()
        label2['text'] = str(pointy3003)
        
class qwerty(Pointy):
    def gy(self):
        Pointy.gy()
    def gy2(self):
        Pointy.gy2()
    def gy3(self):
        Pointy.gy3()
        
obj1 = qwerty()
btn = Button(root,text = "Man1",command = obj1.gy)
btn2 = Button(root,text = "Man2",command = obj1.gy2)
btn3 = Button(root,text = "Man3",command = obj1.gy3)

btn.pack()
btn2.pack()
btn3.pack()
label.pack()
label1.pack()
label2.pack()
Entry2.pack()
Entry3.pack()
Entry4.pack()

root.mainloop()