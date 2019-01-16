from tkinter import *


class GUIT():
    def __init__(self):
        self.tkhandler = Tk()
        self.tkhandler.geometry('500x500')
        self.tkhandler.title('패스트캠퍼스 자동화 프로그램')

        self.label_title = Label(self.tkhandler, text='안녕하세요. 자동화 프로그램입니다.')
        self.label_title.pack()
        
        self.btn = Button(self.tkhandler, text='11번가 조회', width=30, command=self.auto_11st)
        self.btn.pack()

        self.label_telegram = Label(self.tkhandler, text='텔레그램 ID')
        self.label_telegram.pack()

        self.text_telegram = Text(self.tkhandler, width=40, height=1, relief=RIDGE, bd=1)
        self.text_telegram.pack()

        self.scroll = Scrollbar(self.tkhandler, orient='vertical')
        self.lbox = Listbox(self.tkhandler, yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.lbox.yview)

        self.scroll.pack(side='right', fill='y')
        self.lbox.pack(side='left', fill='both', expand=True)

        self.append_log('프로그램을 시작했습니다')
    
    def auto_11st(self):
        self.append_log('11번가 예제를 시작합니다')
        from example11st import do_auto
        tid = self.text_telegram.get('1.0', END).strip()
        do_auto(tid)
        self.append_log('11번가 예제를 완료하였습니다')
    
    def append_log(self, msg):
        import datetime
        now = str(datetime.datetime.now())[11:-7]
        self.lbox.insert(END, "[%s] %s"%(now, msg))
        self.lbox.update()
        self.lbox.see(END)

    def run(self):
        self.tkhandler.mainloop()

g = GUIT()
g.run()