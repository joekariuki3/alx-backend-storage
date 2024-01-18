-- Create a trigger to reset valid_email only when email has been changed
DELIMITER $$
CREATE TRIGGER reset_valid_email_after_update
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    -- Check if the email column has been updated
    IF NEW.email != OLD.email THEN
        -- Reset the valid_email attribute
        SET NEW.valid_email = 0;
    END IF;
END;$$
DELIMITER ;
