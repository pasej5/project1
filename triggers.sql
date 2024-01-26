DELIMITER $$

CREATE TABLE users (
    username VARCHAR(200),
    age INT
);

CREATE TRIGGER must_be_adult BEFORE INSERT ON users FOR EACH ROW 
BEGIN
    IF NEW.age < 18 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Must be an Adult';
    END IF;
END;
$$
DELIMITER ;