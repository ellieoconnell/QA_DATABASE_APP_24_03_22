-- creating a database table
CREATE TABLE IF NOT EXISTS lookuptool (
    user_id_no INTEGER PRIMARY KEY AUTOINCREMENT,
    alias VARCHAR(10) NOT NULL,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    email_address VARCHAR(25) NOT NULL,
    employee_level INT NOT NULL,
    years_of_employment INT NOT NULL, 
    in_the_learning_program BOOLEAN NOT NULL
);

-- inserting data entires into the table from phonetool database
INSERT INTO lookuptool (alias, first_name, last_name, email_address, employee_level, years_of_employment, in_the_learning_program) VALUES ("nelszak", "Zakaria", "Nelson", "nelszak@amazon.co.uk", 4, 2, True);
INSERT INTO lookuptool (alias, first_name, last_name, email_address, employee_level, years_of_employment, in_the_learning_program) VALUES ("vachon", "Cohen", "Vasquez", "vachon@amazon.co.uk", 4, 2, True);
INSERT INTO lookuptool (alias, first_name, last_name, email_address, employee_level, years_of_employment, in_the_learning_program) VALUES ("budeaco", "Deacon", "Butler", "budeaco@amazon.co.uk", 4, 5, True);
INSERT INTO lookuptool (alias, first_name, last_name, email_address, employee_level, years_of_employment, in_the_learning_program) VALUES ("bradcarl", "Carlo", "Bradshaw", "bradcarl@amazon.co.uk", 6, 7, False);
INSERT INTO lookuptool (alias, first_name, last_name, email_address, employee_level, years_of_employment, in_the_learning_program) VALUES ("mcdhas", "Hasan", "McDaniel", "mcdhas@amazon.co.uk", 5, 5, False);
INSERT INTO lookuptool (alias, first_name, last_name, email_address, employee_level, years_of_employment, in_the_learning_program) VALUES ("sanchch", "Charles", "Sanchez", "sanchch@amazon.co.uk", 6, 1, True);
INSERT INTO lookuptool (alias, first_name, last_name, email_address, employee_level, years_of_employment, in_the_learning_program) VALUES ("thorzac", "Zachery", "Thorton", "thorzac@amazon.co.uk", 4, 1, True);
INSERT INTO lookuptool (alias, first_name, last_name, email_address, employee_level, years_of_employment, in_the_learning_program) VALUES ("pattay", "Taya", "Patel", "pattay@amazon.co.uk", 5, 5, False);
INSERT INTO lookuptool (alias, first_name, last_name, email_address, employee_level, years_of_employment, in_the_learning_program) VALUES ("mullola", "Lola", "Mullen", "mullola@amazon.co.uk", 5, 3, True);
INSERT INTO lookuptool (alias, first_name, last_name, email_address, employee_level, years_of_employment, in_the_learning_program) VALUES ("roapopp", "Poppie", "Roach", "roapopp@amazon.co.uk", 5, 5, False);
INSERT INTO lookuptool (alias, first_name, last_name, email_address, employee_level, years_of_employment, in_the_learning_program) VALUES ("reelil", "Lila", "Reeves", "reelil@amazon.co.uk", 4, 7, False);
INSERT INTO lookuptool (alias, first_name, last_name, email_address, employee_level, years_of_employment, in_the_learning_program) VALUES ("boltjea", "Jean", "Bolten", "boltjea@amazon.co.uk", 4, 6, True);
INSERT INTO lookuptool (alias, first_name, last_name, email_address, employee_level, years_of_employment, in_the_learning_program) VALUES ("edwsolo", "Solomon", "Edwards", "edwsolo@amazon.co.uk", 6, 4, False);
INSERT INTO lookuptool (alias, first_name, last_name, email_address, employee_level, years_of_employment, in_the_learning_program) VALUES ("mccelli", "Elliot", "McCain", "mccelli@amazon.co.uk", 7, 8, False);
INSERT INTO lookuptool (alias, first_name, last_name, email_address, employee_level, years_of_employment, in_the_learning_program) VALUES ("frlee", "Lee", "Fry", "frlee@amazon.co.uk", 5, 3, True);
INSERT INTO lookuptool (alias, first_name, last_name, email_address, employee_level, years_of_employment, in_the_learning_program) VALUES ("fletang", "Angus", "Fletcher", "fletang@amazon.co.uk", 5, 2, True);
INSERT INTO lookuptool (alias, first_name, last_name, email_address, employee_level, years_of_employment, in_the_learning_program) VALUES ("sykdeli", "Delilah", "Sykes", "sykdeli@amazon.co.uk", 5, 2, False);
INSERT INTO lookuptool (alias, first_name, last_name, email_address, employee_level, years_of_employment, in_the_learning_program) VALUES ("joylex", "Lexie", "Joyce", "joylex@amazon.co.uk", 4, 3, False);
INSERT INTO lookuptool (alias, first_name, last_name, email_address, employee_level, years_of_employment, in_the_learning_program) VALUES ("irwric", "Rico", "Irwin", "irwric@amazon.co.uk", 6, 1, True);
INSERT INTO lookuptool (alias, first_name, last_name, email_address, employee_level, years_of_employment, in_the_learning_program) VALUES ("romhass", "Hassan", "Roman", "romhass@amazon.co.uk", 4, 4, True);