LARGE_FONT= ("Verdana", 12)
class Container(TabbedPanel):
    def calculate(self):

        try:
            speed_of_learning, deadline, number_of_iterations = float(self.speed_of_learning.text), int(self.deadline.text), int(
                self.number_of_iterations.text)
        except:
            speed_of_learning, deadline, number_of_iterations = 0.001, 5, 10000

        first, second, count = perceptron(speed_of_learning, deadline, number_of_iterations)
        self.w1.text, self.w2.text = str(first), str(second)
        def popupmsg():
            popup = tk.Tk()
            popup.wm_title("Iterations")
            label = ttk.Label(popup, text="Iterations:"+str(count), font=LARGE_FONT)
            label.pack(side=    "top", fill="x", pady=10)
            B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
            B1.pack()
            popup.mainloop()
        app = popupmsg()
