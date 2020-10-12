class a:
    def __init__(self):
        print("you are in a")
class b(a):
    def __init__(self):
        print("init B")
        self.metb()
        super().__init__()
    def metb(self):
        print("you are in met b")
b()