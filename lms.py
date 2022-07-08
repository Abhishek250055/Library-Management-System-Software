class Books:
    def __init__(self, list, name):
        self.listm = list
        self.name = name
        self.dict = {}

    def show(self):
        for i in self.listm:
            print(i)

    def add(self, bookn):
        self.listm.append(bookn)

    def remove(self, bookn):
        self.dict.pop(bookn)
        print("Your this book is removed in list ")

    def issue(self, name, bookn):
        if bookn not in self.dict.keys():
            self.dict.update({bookn: name})
            print(f"your book {bookn} is issue")
        else:
            print(f"Book is not issue because this book ({bookn}) is also issue by other user ")
Abhishek = Books(["pyhton,org" ,"hello world.c","let c","let c++","java"],"makeABji")
while (True):
        print("prees 1 to add boooks:")
        print("prees 2 to delete boooks:")
        print("prees 3 to show  boooks:")
        print("prees 4 to issue student :")
        print("If you wand to exit the program so pree -1 and exit ")
        #print("prees 5 to issue boooks:")
        str = int(input("Enter one key:>>>"))
        if str == 1:
            t1 = input("Enter title:>>>")
            a1 = input("Enter auther:>>>")
            id1 = int(input("Enter id:>>>"))
            Abhishek.add(t1)
            print("Your book is add in list:")
        elif str == 2:
            bookn = input("Enter remove book name:>>")
            Abhishek.remove(bookn)
        elif str == 3:
            Abhishek.show()
        elif str == 4:
            name = input("Enter your namev>>")
            bookn = input("Enter which book want to issue :>>")
            Abhishek.issue(name, bookn)
        elif str == -1:
            print(" <<<< Thanks For Visit This Program >>>>  ")
            exit()
        else:
            print("Only 1,2,3,4 key press")
            print("*try again*")