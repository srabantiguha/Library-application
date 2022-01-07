DROP DATABASE IF EXISTS nlibrary;
CREATE DATABASE nlibrary;
use nlibrary;
CREATE TABLE Book_Copies (
	BookCopyId bigint NOT NULL DEFAULT 0 ,
	NoOfCopies smallint ,
	BookId bigint NOT NULL NULL DEFAULT 0  ,
	BranchId bigint NULL NULL DEFAULT 0,
    users varchar(20) , time_in timestamp) ;
CREATE TABLE Book_Loans (
	BookLoanId bigint NOT NULL DEFAULT 0 ,
    DateOut date,
	DueDate date,
	BranchId bigint not null DEFAULT 0,
	BookId bigint   not null  DEFAULT 0,
	CardNo bigint   not null    DEFAULT 0,
    users varchar(20) , 
  time_in timestamp) ;
CREATE TABLE Borrowers (
	CardNo bigint NOT NULL DEFAULT 0 ,
	Name varchar(50)   ,
	Address varchar (100),
	Phone    varchar(15)) ;
CREATE TABLE Library_Branches (
	BranchId bigint NOT NULL DEFAULT 0 ,
	BranchName varchar(50) ) ;
CREATE TABLE Books (
	BookId bigint NOT NULL DEFAULT 0 ,
	AuthorName varchar(50),
	Title varchar(100),
	Name varchar(50) NOT NULL DEFAULT 0,
    users varchar(20) ,  time_in timestamp);
CREATE TABLE Publishers (
	Name varchar(50) NOT NULL DEFAULT 0 ,
	Address Varchar(100),
	Phone varchar(15),
    users varchar(18),time_in timestamp
    );
create index BookId on Book_Copies(BookID);
create index BranchId  on Book_Copies(BranchId);
 ALTER TABLE Book_Copies ADD
	CONSTRAINT Book_Copies_PK PRIMARY KEY
	(
		BookCopyId
	) ;
create index BranchId on Book_Loans(BranchId);
create index BookId on Book_Loans(BookId);
create index CardNo on Book_Loans(CardNo);
ALTER TABLE Book_Loans ADD
	Constraint Book_Loans_PK PRIMARY KEY
    (
		BookLoanId
	);
create index Name on Books(Name);
ALTER TABLE Publishers ADD
	Constraint Publishers_PK PRIMARY KEY
    (
		Name
	);
ALTER TABLE Borrowers ADD
	Constraint Borrowers_PK PRIMARY KEY
    (
		CardNo
	);
ALTER TABLE Books ADD
	Constraint Books_PK PRIMARY KEY
    (
		BookId
	);
ALTER TABLE Library_Branches ADD
	Constraint Library_Branches PRIMARY KEY
    (
		BranchId
	);
ALTER TABLE Book_Copies ADD
	CONSTRAINT Book_Copies_FK00 FOREIGN KEY
	(
		BookId
	) REFERENCES Books(
		BookId
	),ADD
	CONSTRAINT Book_Copies_FK01 FOREIGN KEY
	(
		BranchId
	) REFERENCES Library_Branches (
		BranchId
	);
ALTER TABLE Book_Loans ADD
	CONSTRAINT Book_Loans_FK00 FOREIGN KEY
	(
		BookId
	) REFERENCES Books(
		BookId
	),ADD
	CONSTRAINT Book_Loans_FK01 FOREIGN KEY
	(
		BranchId
	) REFERENCES Library_Branches (
		BranchId
	), ADD CONSTRAINT Book_Loans_FK02 FOREIGN KEY
	(
		CardNo
	) REFERENCES Borrowers (
		CardNo);
	ALTER TABLE Books ADD
	CONSTRAINT Books_FK00 FOREIGN KEY
	(
		Name
	) REFERENCES Publishers (
		Name
	);
