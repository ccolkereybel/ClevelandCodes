INSERT INTO invoices												-- 2 is foreign key that references term table
VALUES (DEFAULT, 32, "AX-014-027", "2014-08-01", "434.58", "0.00", "0.00", 2, "2014-08-31", NULL);

INSERT INTO invoice_line_items
VALUES (115, 1, 160, 180.23, "Hard drive"), 
(115, 2, 527, 254.35, "Exchange Server update"); 

UPDATE invoices 
SET credit_total = invoice_total * 0.1,
payment_total = invoice_total * 0.9,
payment_date = current_date()
WHERE invoice_id = 115;

UPDATE vendors
SET default_account_number = 403
WHERE vendor_id = 44;

DELETE FROM invoice_line_items
WHERE invoice_id = 115;

DELETE FROM invoices
WHERE invoice_id = 115