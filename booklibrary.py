#create a library class
#displaybook
#lendbook(who owns the book if not present)
#add book
#return book
#lovely library(listof books,library_name)
#dictionary (book-name of person)
#create a main function and run an infinity while loop asking users for there  input

# from platformdirs import user_runtime_dir


class library:
    def __init__(self,list,name):
        self.booklist=list
        self.name=name
        self.landdict={}
    
    def displaybook(self):
        
        print(f"we have following books in our library: {self.name}")
        for book in self.booklist:
            print(book)

    def landbook(self,user,book):
        if book not in self.landdict.keys():
            self.landdict.update({book:user})
            print("lander_book database has been updated you can take the book now")
        else:
            print(f"Sorry! Book is already being used by  {self.landdict[book]} ")
            print("you can take any other book ")
            

    def addbook(self,book):
        self.booklist.append(book)
        print("book has been added in the booklist! Now you can take the book ")
        print("thanku ")

    def returnbook(self,book):
        self.booklist.remove(book)

if __name__=='__main__':
    lovely=library(['python','c++','harry_poter','java','nodejs'],"bookstock")
    while(True):
        print(f"welcome to the {lovely.name} library.enter your choice to continue")
        print("1. display a book")
        print("2. lend a book")
        print("3. add a book")
        print("4. return a book" )
        user_choice=int(input("enter your choice: "))
        if user_choice==1:
            lovely.displaybook()
        
        elif user_choice==2:
            book=input("enter the book name you want to land: " )
            user=input("enter your name: ")
            lovely.landbook(user,book)
        
        elif user_choice==3:
            book=input("enter the book name you want to add: ")
            lovely.addbook(book)
        elif user_choice==4:
            book=input("enter the name of the book you want to return: ")
            lovely.returnbook(book)

        user_choice=input()
        if user_choice not in ['1','2','3','4']:
            print("please inter a valid option")
            continue
        else:
            user_choice=int(user_choice)

        print("press q to quit and c to continue")
        while(user_choice!="q" and user_choice!="c"):
            user_choice=input()
            if user_choice=="q":
                exit()
            if user_choice=='c':
                continue







