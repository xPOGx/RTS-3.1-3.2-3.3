LARGE_FONT= ("Verdana", 12)
if __name__ == '__main__':
    start_tt = time.time()
    MyApp().run()
    tt = time.time() - start_tt
    def popupmsg():
        popup = tk.Tk()
        popup.wm_title("Exe Time")
        label = ttk.Label(popup, text="Time:"+str(tt), font=LARGE_FONT)
        label.pack(side=    "top", fill="x", pady=10)
        B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
        B1.pack()
        popup.mainloop()
    app = popupmsg()
