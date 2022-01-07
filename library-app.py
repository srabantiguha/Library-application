import mysql.connector
from datetime import date
from prettytable import PrettyTable
import pandas as pd
from datetime import datetime
import time    
time.strftime('%Y-%m-%d')
def clear():
    for _ in range(65):
        print()

def add_books():
  conn = mysql.connector.connect(host='localhost', database='nlibrary', user='root', password='root')
  cursor = conn.cursor()

  BookId = input('Enter Book ID:')
  AuthorName = input('Enter Book AuthorName : ')
  Title = input('Enter Book Title : ')
  Name = input('Enter Book Publisher name  : ')
  
  sql = 'insert into books(BookId, AuthorName,  Title , Name) values ( "' + \
      BookId + '","' +  AuthorName+'","'+Title+ \
        '","'+ Name+'");'
        
  cursor.execute(sql)
  conn.commit()
  conn.close()
  print('\n\nNew Book added successfully')

def add_bookcopies():
      
  conn = mysql.connector.connect(host='localhost', database='nlibrary', user='root', password='root')
  cursor = conn.cursor()

  BookCopyId = input('Enter BookCopyId:')
  NoOfCopies = input('Enter Book NoOfCopies : ')
  BookId  = input('Enter BookId   : ')
  BranchId = input('Enter BranchId   : ')
  
  sql = 'insert into Book_copies(BookCopyId, NoOfCopies, BookId , BranchId )values( "' + \
        BookCopyId  + '","' + NoOfCopies+'","'+BookId  + \
        '","'+BranchId +'");'
        
  cursor.execute(sql)
  conn.commit()
  conn.close()
  print('\nNew Book added successfully to bookcopy')
  wait = input('\33[34m''\n Press any key to continue....')
  
#  books to show at each library branch
  
def Library_branch1():    
    conn = mysql.connector.connect( host='localhost', database='nlibrary', user='root', password='root')
    cursor = conn.cursor() 
      
    sql = '''
    SELECT Library_Branches.BranchId, Library_Branches.BranchName,
    Books.Title, Books.Name, Books.AuthorName
    from Library_Branches
    INNER JOIN Book_copies 
    ON Library_Branches.BranchId  = Book_copies.BranchId INNER JOIN Books on 
    Books.BookId = Book_copies.BookId where Library_Branches.BranchId = 1
    '''
    
    cursor.execute(sql)
    names = [ x[0] for x in cursor.description]
    result = cursor.fetchall()
    p = pd.DataFrame(result, columns=names)
    print(p)
    conn.close()
    wait = input('\33[34m''\n Press any key to continue....')
    
def Library_branch2():    
    conn = mysql.connector.connect(
       host='localhost', database='nlibrary', user='root', password='root')
    cursor = conn.cursor()      
    sql = '''
    SELECT Library_Branches.BranchId, Library_Branches.BranchName,
    Books.Title, Books.Name, Books.AuthorName
    from Library_Branches
    INNER JOIN Book_copies 
    ON Library_Branches.BranchId  = Book_copies.BranchId INNER JOIN Books on 
    Books.BookId = Book_copies.BookId where Library_Branches.BranchId = 2
    '''
    cursor.execute(sql)
    names = [ x[0] for x in cursor.description]
    result = cursor.fetchall()
    p = pd.DataFrame(result, columns=names)
    print(p)
    conn.close()
   
    wait = input('\33[34m''\n Press any key to continue....')

def Library_branch3():    
    conn = mysql.connector.connect(
       host='localhost', database='nlibrary', user='root', password='root')
    cursor = conn.cursor() 
      
    sql = '''
    SELECT Library_Branches.BranchId, Library_Branches.BranchName,
    Books.Title, Books.Name, Books.AuthorName
    from Library_Branches
    INNER JOIN Book_copies 
    ON Library_Branches.BranchId  = Book_copies.BranchId INNER JOIN Books on 
    Books.BookId = Book_copies.BookId where Library_Branches.BranchId = 3
    '''   
    cursor.execute(sql)
    names = [ x[0] for x in cursor.description]
    result = cursor.fetchall()
    p = pd.DataFrame(result, columns=names)
    print(p)
    conn.close()
    wait = input('\33[34m''\n Press any key to continue....')

def Library_branch():
    while True:
      clear()
      print(' Books at library branch ')
      print("\n1.   Publiclibrary ")
      print('\n2.   Hillcrest')
      print('\n3.   Albertson_library')
      #print('\n')
      choice = int(input('Enter your choice ...: '))      
      if choice == 1:
        Library_branch1()
      if choice == 2:
        Library_branch2()
      if choice == 3:
        Library_branch3()
      if choice == 0:
          break
#show book count checked out from library branch    
def check_out_book_count():
    
    conn = mysql.connector.connect(host='localhost', database='nlibrary', user='root', password='root')
    cursor = conn.cursor()
    print('\n Total checked out from branch ')
    sql ='''select Book_loans.BranchId, Book_loans.BookId,
    books.Title,
count(Book_loans.BookId) as total_check_out from Book_loans 
join books on books.BookId = Book_loans.BookId
group by Book_loans.BranchId, Book_loans.BookId'''
    
    cursor.execute(sql)
    names = [ x[0] for x in cursor.description]
    result = cursor.fetchall()  
    p = pd.DataFrame(result, columns=names)
 #   print(p)   
    l = int(input('Enter bookid ...: '))
    j= p[(p['BookId'] == l) ]
    k = j.loc[:,['BranchId', 'total_check_out']] 
    print(k)
    wait = input('\33[34m''\n Press any key to continue....')   
    
# add book and bookcopies for multiple branch  
def mul():
    conn = mysql.connector.connect(host='localhost', database='nlibrary', user='root', password='root')
    cursor = conn.cursor()
    add_books()
    print('mutiple branch insert')
    l = int(input('number of branch'))
    for i in range(l):    
        add_bookcopies()    
# add to book_loans and issue book and display the borrowed books details

def add_loan():
  conn = mysql.connector.connect(
       host='localhost', database='nlibrary', user='root', password='root')
  cursor = conn.cursor() 
  print('add loan to book_loans')
  BookLoanId   = input('Enter BookLoanId :')                              
  DateOut  =input  (time.strftime('DateOut : '))                       
  DueDate  = input (time.strftime('Datedue :'))
  BranchId= input('Enter BranchId : ')
  BookId= input('Enter BookId  : ')
  CardNo = input('EnterCardNo  : ')
  
  sql = 'insert into Book_Loans(BookLoanId,DateOut , DueDate ,  BranchId , BookId,CardNo ) values ( "' + \
      BookLoanId  + '","' + DateOut +'","'+ DueDate +'","'+BranchId+ '","'+ BookId+\
        '","'+ CardNo +'");'       
  cursor.execute(sql)
  conn.commit()  
  print('\n Book issued successfully')
  conn.close()
#we will check if student borrowed book before
#check if book is available at library branch
def issue_book():
      
  conn = mysql.connector.connect(host='localhost', database='nlibrary', user='root', password='root')
  cursor = conn.cursor()  
  sql ='''SELECT  books.BookId, book_loans.Cardno from book_loans left join books on books.BookId = book_loans.BookId '''
    
  cursor.execute(sql)
  names = [ x[0] for x in cursor.description]
  result = cursor.fetchall()
  p = pd.DataFrame(result, columns=names)
  #print(p)
  a = int(input('Enter bookid ...: '))
  b = int(input("Enter cardno:..."))
  c = p[(p['BookId'] == a) & (p['Cardno'] == b) ]
  d = len(c) 
  print('\33[30m''\n ------CHECK IF USER BORROW BOOK BEFORE------')
  if d==0:
     print('\33[32m''\n    BOOK IS NOT BORROWED BEFORE')
     print('\33[30m''\n ------CHECK BOOK AVAILABILITY------')    
     book_give_avialability()   
     #add_loan() 
 #    display()   
  else: 
    print( '\33[31m''   Already Issued   ')
    wait = input('\33[34m''\nPress any key to continue....')
    
 # display the borrowed book   
def display():   
    conn = mysql.connector.connect(
       host='localhost', database='nlibrary', user='root', password='root')
    cursor = conn.cursor()  
    print('display book that borrowed')
    b = int(input("Enter bookid:...")) 
    cursor.execute("select BookId, Title,AuthorName,Name FROM `books` WHERE BookId = %s", (b,))
    r = cursor.fetchall()
    print(r)
    conn.commit()
    conn.close()
    wait = input('\33[34m''\n Press any key to continue....')           
# return book      
def returns_book():
  conn = mysql.connector.connect(
       host='localhost', database='nlibrary', user='root', password='root')
  cursor = conn.cursor()
  BookLoanId  = input('Enter BookLoanId :')
  sql =cursor.execute("DELETE FROM `Book_Loans` WHERE  BookLoanId = %s", (BookLoanId,)) 
  cursor.execute(sql)
  conn.commit()
  conn.close() 
  print('\nBook deleted successfully')  
  wait = input('\33[34m''\n Press any key to continue....') 
##
  
def book_give_avialability():
      
  conn = mysql.connector.connect(host='localhost', database='nlibrary', user='root', password='root')
  cursor = conn.cursor()
  
  sql ='''select  Library_Branches.BranchId,book_copies.BookId,
  book_copies.NoOfCopies from 
Library_Branches left join book_copies on
book_copies.BranchId =   Library_Branches. BranchId'''
    
  cursor.execute(sql)
  names = [ x[0] for x in cursor.description]
  result = cursor.fetchall()
  p = pd.DataFrame(result, columns=names)
 # print('p',p)
  b = int(input("Enter branchid:..."))
  a = int(input('Enter bookid ...: '))
  c = p[(p['BookId'] == a) & (p['BranchId'] == b) ]  
#  print('c is',c)
  d = len(c)  
  if d==0:
      print('\n')
      print('\33[31m''BOOK IS NOT AVAILABLE IN THAT BRANCH')
  else:
      print('\n')
      print('\33[32m''BOOK IS AVAILABLE IN THAT BRANCH')
      add_loan()
      display()   
  wait = input('\33[34m''\n Press any key to continue....')                 
# menu function
def main_menu():
    while True:
      clear()
      print('\33[34m''------L I B R A R Y    M E N U------')
      
      print('\33[34m' "\n1.  Add Books and bookcopies one branch")
      
      print('\33[34m'"\n2.  Add Books  and bookcopies for multiple library branch")
 
      print('\33[34m'"\n3.  Books at library branch")
      
      print('\33[34m'"\n4.  Issue book & display borrowed book")
      
      print('\33[34m'"\n5.  Total copies check out for a book")
  
      print('\33[34m'"\n6.  Return book")
      
      choice = int(input('Enter your choice ...: '))
      
      if choice == 1:
        add_books()
        add_bookcopies()
        
      if choice== 2:
          mul()
        
      if choice== 3:
         Library_branch()
         
      if choice== 4:
         issue_book()
    
      if choice== 5:
         check_out_book_count()

         
      if choice ==  6:
         returns_book()
 
         
      if choice == 0:
        break


if __name__ == "__main__":
    main_menu()




