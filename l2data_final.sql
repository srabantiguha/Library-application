
use nlibrary;
#select * from Book_Loans;
insert into publishers(name,address, phone)values('Packt Publishing','notKnown',null);
insert into publishers(name,address, phone)values('Poughkeepsie', ' NY : IBM Corporation', null);
insert into publishers(name,address, phone)values('O Reilly Media', 'unknown', null);
insert into publishers(name,address, phone)values('O Reilly Verlag','unknown',null);
insert into publishers(name,address, phone)values('Pearson', 'India',null);
#
insert into Library_Branches (BranchId , BranchName )values(1,'Publiclibrary');
insert into Library_Branches (BranchId , BranchName )values(2,'Hillcrest');
insert into Library_Branches (BranchId , BranchName )values(3,'Albertson_library');
#
insert into Borrowers (CardNo, Name  ,Address, phone)values(1,'Shom','Boise',null) ;
insert into Borrowers (CardNo, Name  ,Address, phone)values(2,'Srabanti','Boise',null) ;
insert into Borrowers (CardNo, Name  ,Address, phone)values(3,'Auntu','Numpa', null) ;
insert into Borrowers (CardNo, Name  ,Address, phone)values(4,'Nity','Numpa', null) ;
insert into Borrowers (CardNo, Name  ,Address, phone)values(5,'Mina','Numpa', null) ;
insert into Borrowers (CardNo, Name  ,Address, phone)values(6,'Janet','Numpa', null) ;
insert into Borrowers (CardNo, Name  ,Address, phone)values(7,'Milly','Numpa', null) ;
insert into Borrowers (CardNo, Name  ,Address, phone)values(8,'Sam','Numpa', null) ;
insert into Borrowers (CardNo, Name  ,Address, phone)values(9,'Sara','Numpa', null) ;
insert into Borrowers (CardNo, Name  ,Address, phone)values(10,'Mitu','Boise', null) ;
#
