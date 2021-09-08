from tkinter import *
from tkinter import filedialog as fd


class FileManager(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background='white')
        self.parent = parent
        self.parent.title('File Manager')
        self.pack(fill=BOTH, expand=1)
        self.center_window()
        self.initUI()

    def initUI(self):
        choose_directory_btn = Button(
            self, text='Выберите каталог', command=self.directory_choose, width=16)
        self.text_window = Text(width=100, height=100)

        choose_directory_btn.grid(row=0, column=0)
        self.text_window.pack()

    def directory_choose(self):
        file_name = fd.askopenfilename()
        file = open(file_name)
        file_text = file.read()
        self.text_window.insert(1.0, file_text)

    def center_window(self):
        w = 488
        h = 100
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))


def main():
    root = Tk()
    ex = FileManager(root)
    root.mainloop()


if __name__ == '__main__':
    main()
