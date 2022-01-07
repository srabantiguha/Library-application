use nlibrary;
CREATE TABLE Book_Loans_archive (
	BookLoanId bigint NOT NULL DEFAULT 0 ,
    DateOut date,
	DueDate date,
	BranchId bigint not null DEFAULT 0,
	BookId bigint   not null  DEFAULT 0,
	CardNo bigint   not null    DEFAULT 0,  deletedAt TIMESTAMP DEFAULT NOW()
);
##
DELIMITER //
CREATE TRIGGER before_book_loans_delete
BEFORE DELETE
ON book_loans FOR EACH ROW
BEGIN
    INSERT INTO  Book_Loans_archive (BookLoanId ,   DateOut,	DueDate ,BranchId,	BookId , CardNo)
    VALUES(OLD.BookLoanId ,OLD.DateOut,	OLD.DueDate ,OLD.BranchId,	OLD.BookId , OLD.CardNo);

END
##