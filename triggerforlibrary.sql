#book_copies
DELIMITER //
CREATE DEFINER=`root`@`localhost` TRIGGER 
`book_copies_BEFORE_INSERT` BEFORE INSERT ON `book_copies` FOR EACH ROW BEGIN
Set new.users= current_user();
 set new.time_in = now();
END
##books
DELIMITER //
CREATE DEFINER=`root`@`localhost` TRIGGER `books_BEFORE_INSERT` BEFORE INSERT ON `books` FOR EACH ROW BEGIN
Set new.users= current_user();
 set new.time_in = now();
END
## publishers
DELIMITER //
CREATE DEFINER=`root`@`localhost` TRIGGER `publishers_BEFORE_INSERT` BEFORE INSERT ON `publishers` FOR EACH ROW BEGIN
Set new.users= current_user();
set new.time_in = now();
END
##book_loans
DELIMITER //
CREATE DEFINER=`root`@`localhost` TRIGGER `book_loans_BEFORE_INSERT` BEFORE INSERT ON `book_loans` FOR EACH ROW BEGIN
Set new.users= current_user();
 set new.time_in = now();
END
