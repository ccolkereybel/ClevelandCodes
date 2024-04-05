-- inner join
SELECT vendor_name, first_name, last_name
FROM vendors JOIN vendor_contacts USING (vendor_id)
ORDER BY last_name;

-- natural join
SELECT vendor_name, first_name, last_name
FROM vendors NATURAL JOIN vendor_contacts 
ORDER BY last_name;

-- cross join, cartesian product
SELECT vendor_name, first_name, last_name
FROM vendors JOIN vendor_contacts 
ORDER BY last_name;

-- implicit inner join
SELECT vendor_name, first_name, last_name
FROM vendors AS v JOIN vendor_contacts as vc
WHERE v.vendor_id = vc.vendor_id; 

-- explicit left outer join
SELECT vendors.vendor_id, vendor_name, last_name
FROM vendors LEFT JOIN vendor_contacts USING (vendor_id)
WHERE last_name is NULL;

SELECT account_number, account_description, invoice_id
FROM general_ledger_accounts LEFT JOIN invoice_line_items USING (account_number)
WHERE invoice_id is NULL;

-- update
SET SQL_SAFE_UPDATES = 0;
UPDATE vendor_contacts
SET first_name = "Chuck" 
WHERE last_name = "Bucket";

UPDATE vendors
SET vendor_address1 = "Attn: Windows Service", 
	vendor_address2 = "PO BOX 5007"
WHERE vendor_id = 1;

-- delete 
DELETE from vendor_contacts 
WHERE last_name = "Bucket";

-- insert 
-- option 1 (column list)
INSERT INTO vendor_contacts
(vendor_id,first_name, last_name)
VALUES (50, "Wayne", "Largent");

-- option 2
INSERT INTO vendor_contacts
VALUES (60, "TheBuilder", "Bob");

-- option 3
INSERT INTO vendor_contacts
SET vendor_id=70,
first_name="Felix",
last_name = "TheCat";

-- auto increment --> use default for terms_id
INSERT INTO terms
VALUES (DEFAULT, "test description", 999);

-- will fill in terms_id automatically if leave it off
INSERT INTO terms
(terms_description, terms_due_days)
VALUES ("another test description", 888);

DELETE FROM terms
WHERE terms_id IN (6,7,10)