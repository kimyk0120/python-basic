from tkinter import *


class GUIT():

    def __init__(self):
        self.tkhandler = Tk()
        self.tkhandler.geometry('500x500')
        self.tkhandler.title('facam online program')

        self.label_title = Label(self.tkhandler, text='Hello World')
        self.label_title.pack()

        self.btn = Button(self.tkhandler, text='11st search', width=30, command=self.auto_11st)
        self.btn.pack()

        self.label_telegram = Label(self.tkhandler, text='telegram ID')
        self.label_telegram.pack()

        self.text_telegram = Text(self.tkhandler, width=40, height=1, relief=RIDGE, bd=1)
        self.text_telegram.pack()

        self.scroll = Scrollbar(self.tkhandler, orient='vertical')
        self.lbox = Listbox(self.tkhandler, yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.lbox.yview)

        self.scroll.pack(side='right', fill='y')
        self.lbox.pack(side='left', fill='both',expand=True)

        self.append_log("init")

    def auto_11st(self):
        self.append_log("11st example start")
        import example11st
        tid = self.text_telegram.get('1.0', END).strip()
        example11st.do_auto(tid)
        self.append_log('11st example end')

    def append_log(self, msg):
        import datetime
        now = str(datetime.datetime.now())[11:-7]
        self.lbox.insert(END, "[%s] %s" % (now, msg))
        self.lbox.update()
        self.lbox.see(END)

    def run(self):
        self.tkhandler.mainloop()


g = GUIT()
g.run()


