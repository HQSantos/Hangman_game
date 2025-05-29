class Print():
    def head():
        print(r'''     NVVVV    ''')
        print(r'''    (o , o)   ''')
        print(r'''     \ - /    ''')
    def body():
        print(r'''       |      ''')
        print(r'''       |      ''')
        print(r'''       |      ''')
        print(r'''      _A_     ''')
    def bodyleftarm():
        print(r'''     __|__    ''')
        print(r'''       |  \   ''')
        print(r'''       |   \  ''')
        print(r'''      _A_   \ ''')
    def bodyarms():
        print(r'''     __|__    ''')
        print(r'''    /  |  \   ''')
        print(r'''   /   |   \  ''')
        print(r'''  /   _A_   \ ''')
    def leftleg():
        print(r'''         \    ''')
        print(r'''          \   ''')
        print(r'''           \  ''')
    def legs():
        print(r'''     /   \    ''')
        print(r'''    /     \   ''')
        print(r'''   /       \  ''')
    def dead_head():
        print(r'''     NVVVV    ''')
        print(r'''    (X , X)   ''')
        print(r'''     \ _ /    ''')

    def print_hanger(self,tries):
        if tries == 1:
            self.head()
        if tries == 2:
            self.head()
            self.body()
        if tries == 3:
            self.head()
            self.bodyleftarm()
        if tries == 4:
            self.head()
            self.bodyarms()
        if tries == 5:
            self.head()
            self.bodyarms()
            self.leftleg()
        if tries == 6:
            self.head()
            self.bodyarms()
            self.legs()
        if tries == 7:
            self.dead_head()
            self.bodyarms()
            self.legs()