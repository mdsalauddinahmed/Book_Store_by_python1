class Book:
    def __init__(self,id,name,quantity):
        self.id=id
        self.name=name
        
        self.quantity=quantity



class User:
    def __init__(self,id,name,password):
        self.id=id
        self.name=name
        self.password=password
        self.borrowBooks =[]
        self.returnBooks=[]



class Library:
    def __init__(self,name):
        self.name=name
        self.users=[]
        self.books=[]
    def addBook(self,id,name,quantity):
        book=Book(id,name,quantity)
        self.books.append(book)
        print(f'{book.name} added successfully')
        
    def addUsers(self,id,name,password):
        for user in self.users:
            if user.id==id:
                print(f"\n\t---> !! User Id {book.id} already exists")
                return
        user=User(id,name,password)
        self.users.append(user)
        return user

    def borrowBook(self,user,token):
        for book in self.books:
            if book.name== token:
                if book in user.borrowBooks:
                    print("you have already borrowd ")
                    return
                elif book.quantity == 0:
                    print("There is No Copy here ! \n")
                    return

            user.borrowBooks.append(book)
            book.quantity -=1
            print(f'{token} is borrowed successfully')
            return
        print(f"Sorry {token} this book is not avilable here \n")

    def returnBook(self,user,token):
         for book in self.books:
            if book.name== token:
                if book in user.borrowBooks:
                   book.quantity +=1
                   user.returnBooks.append(book)
                   user.borrowBooks.remove(book)
                   print("Return Book successfully ! \n")
                elif book.quantity == 0:
                    print("There is No Copy here ! \n")
                    return

            user.borrowBooks.append(book)
            book.quantity -=1
            return
         print(f"Sorry {token} this book is not avilable here")




library=Library("Amir library")
admin=library.addUsers(100,'admin','admin')
Amir=library.addUsers(102,"amir","12344")
cpBook=library.addBook(11,"cp",5)

stry_book=library.addBook(1234,"amir_book",5)


current_user=admin
changeOfUser=True
while True:
    if current_user == None:
        print("there is no user.Please login first\n")

        option=input("Login or Register : (L\\R) :")

        if option == "L":
            id=int(input("ENter Your Id :"))
            password=input("Enter your password :")
            match=False
            for user in library.users:
                user.id == id and user.password== password
                current_user = user
                changeOfUser=True
                match = True
                break
            if match == False:
                print("There is No any user ")


        elif option == "R":
          id=int(input("ENter Your Id :"))
          name=input("ENter Name :")
          password=input("Enter your password :")
                 
          for user in library.users:
              if user.id == id:
                  print("User already exists!\n")

          user=library.addUsers(id,name,password)
          current_user=user
        

    else:
        if changeOfUser:
            print("\n------------------------------------")
            print(f"\tWelcome Back {current_user.name} !")
            print("------------------------------------")
            changeOfUser=False
        else:
            print("\n\t<---------------------------->")
        if current_user.name =="admin":
            print("Option:\n")
            print("1:Add Book")
            print("2: Add User")
            print("3:Show All Book")
            print("4:Logout")
            

            ch=int(input("Enter your Option"))
            if ch==1:
                id= int(input("enter your Book id:"))
                name=input("Enter  Book name")
                quanti =int(input("No of quantity :"))

                library.addBook(id,name,quanti)

            elif ch ==3:
                for book in library.books:
                    print(f'Book list {book.name}\t {book.quantity}')
                print("\n")
            
            elif ch ==4:
                current_user=None
        else:
            print("Option:\n")
            print("1:Borrow Book")
            print("2: return book")
            print("3: Show borrowed Book")
            print("4: show all History :")
            print("5:All books")
            print("5:Logout")

            ch=int(input("Enter Your Option :"))

            if ch ==1:
                name=input(" Enter book name :")
                library.borrowBook(current_user,name)

            elif ch ==2:
                name=input("Enter book name:")
                library.returnBook(current_user,name)
            elif ch==3:
                print("\n Borrowed Books:\n")
                for book in library.books:
                    print(f'{book.id}\t{book.name}\t {book.quantity}')
                    print("\n")
            elif ch ==4:
                print("\n Historty \n")
                for book in current_user.returnBooks:
                    print(f'{book.id}\t{book.name}\t {book.quantity}')
                print("\n")
            elif ch==5:
                print("\n\tAll Books:\n")
                for book in library.books:
                    if book in current_user.borrowedBooks:
                        print(f'\t{book.id}\t{book.name}\t{book.quantity}\tReading Now..')
                    elif book in current_user.returnBooks:
                        print(f'\t{book.id}\t{book.name}\t{book.quantity}\tAlready Read')
                    else:
                        print(f'\t{book.id}\t{book.name}\t{book.quantity}\tDid not Read')
            
            elif ch ==6:
                current_user=None


print(library)