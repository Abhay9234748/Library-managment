import json
from datetime import datetime
def log():
    username= input(" Enter  a username:-")
    password=int(input("Enter a password:-"))
    if(username =="Abhay" and password == 1803):
        print("Login")
        return True
    else:
        print("Worng ID/Password")    
        return False
if not log(): 
        exit()      
def save_data():
    with open("Library.json","w") as f:
        json.dump(books,f,indent=4)
try:
    with open("Library.json","r") as f:
        books=json.load(f)
except:
    books=[]

while True:
    print("1.Add Book")
    print("2.Author wise count Book")
    print("3.Search Book")
    print("4.Remove Book")
    print("5.Clear All data")
    print("6.Issue Book")
    print("7.Return Book")
    print("8.Exit")
    choise=input(" Enter Your Choice 1 to 5:-")
    if choise=="1":
        while True:
            book_name=input("Enter a Book name:-")
            author_name=input("Enter a Book Author:-")
            book={
            "Book Name":book_name,
            "Author name":author_name,
            "status":"available",
            "isued_to":None,
            "isued_date":None,
            "return":None
         }
            print("---------------")
            books.append(book)
            save_data()
            print(books)
            print("Book Added Successfully")
            choise=input("add more book y/n:-")
            if choise=="n":
                break
# count book by author
    elif choise=="2":
        author_count={}
        for book in books:
            author=book["Author name"]
            if author in author_count:
                author_count[author]+=1
            else:
                author_count[author]=1
        print("\n Author wise book count:")
        print("-------------------")
        for author in author_count:
            print(author,"=",author_count[author],"books")

# search yes or not
    elif(choise=="3"):
        print("1.search by Author name")
        print("2.search by book name")
        search_type=input("Enter a choice 1 or 2:-")
    
# Search a book by a Author:-
        if(search_type=="1"):
            search_author = input("Enter a Author Name:-")
            found= False
            for book in books:
        
                if search_author.lower()==book["Author name"].lower():
                    print(book)
                    found=True
        
            if found==False:
                print("Sorry Not found...")
# search by book name
        elif(search_type=="2"):
            
            search_book_name=input("Enter a book name:-")
            found=False
            for book in books:
                if(search_book_name.lower()==book["Book Name"].lower()):
                    print(book)
                    found=True
            if found==False:
                print("Sorry not found...")    
        else:
            print("plz choise 1 or 2 only")
# book remove 
    elif(choise=="4"):
            print("1.Remove book")
            print("2.Remove Author  all book")
            remove_type=input("Enter a type:-")
            if(remove_type=="1"):
                remove_book=input("Enter a book name:-")
                found=False
                for book in books.copy():
                    if remove_book.lower()==book["Book Name"].lower():
                        books.remove(book)
                        save_data()
                        found=True
                if found==False:
                    print("Not found.....")
                else:
                    print("Book Removed Successfully")
            elif(remove_type=="2"):
                remove_book=input("Enter a Author name:-")
                found=False
                for book in books.copy():# .copy is liye q ki mutiplue remove me dikat a sakta ha kv kv or 1ya 2 v skip ho skat ha is liye
                    if remove_book.lower()==book["Author name"].lower():
                        books.remove(book)
                        save_data()
                        found=True
                    
                if found==False:
                    print("Not found.....")
                else:
                    print("Author All Books Removed")
            else:
                print("choise only 1 or 2")
    elif choise=="5":
        choise = input("Are you sure y/n:-")
        if choise=="y":
            books.clear()
            save_data()
            print("Clerared Successfully")
    elif(choise=="6"):
        issue_book=input("Enter a book name")
        student_name=input("Enter a student name:- ")
        found=False
        for book in books:
            if issue_book.lower()==book["Book Name"].lower():
                if book["status"]=="available":
                    current_time =datetime.now()
                    book["status"]="issued"
                    book["isued_to"]=student_name
                    book["isued_date"]= current_time.strftime("%d-%m-%Y  %I:%M  %p")
                    save_data()
                    print("Book issued")
                else:
                    print("Book already issued to",book["isued_to"])
                found=True
                break
    elif(choise=="7"):
        pass
    elif choise=="8":
        print("Program closed")
        break
    
    else:
        print("Invalid Choice")

        
