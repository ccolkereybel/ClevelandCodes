 USE AP;
SELECT CONCAT(vendor_contact_last_name, ", ", + vendor_contact_first_name) AS "Full Name"
FROM vendors
WHERE LEFT(vendor_contact_last_name, 1) in ("A", "B", "C", "E")
ORDER BY vendor_contact_last_name;
 
 SELECT current_date, date_format(current_date, "%m-%d-%Y") AS "curent_date";
 
SELECT round(AVG(invoice_total),2) AS Average
FROM invoices
WHERE invoice_date between "2014-04-01" and "2014-04-30";
 
 SELECT AVG(DATEDIFF(payment_date, invoice_date)) AS "Avg Ageing"
 FROM invoices
 WHERE payment_date is not NULL;
 
 SELECT invoice_number, invoice_due_date, payment_date, DATEDIFF(payment_date, invoice_due_date)
	AS "Days Late"
 FROM invoices
 WHERE payment_date > invoice_due_date;
 
 
 -- explicit INNER JOIN 
 SELECT vendor_name, invoice_number, invoice_total
 FROM invoices JOIN vendors ON invoices.vendor_id = vendors.vendor_id
 ORDER BY vendor_name; 
 
 SELECT invoice_number, terms_description 
 FROM invoices AS i JOIN terms AS t ON i.terms_id = t.terms_id;
 
 SELECT vendor_name, invoice_number, invoice_total
 FROM invoices JOIN vendors USING (vendor_id)
 ORDER BY vendor_name; 

-- Cartesian Join
 SELECT vendor_name, invoice_number
 FROM invoices cross join vendors;
 
 SELECT vendor_name, invoice_number, invoice_total, terms_description
FROM invoices AS i JOIN vendors AS v USING(vendor_id) JOIN terms AS t ON i.terms_id = t.terms_id
ORDER BY vendor_name;

-- above are explicit joins

-- implicit join
SELECT vendor_name, invoice_number, invoice_total
FROM invoices, vendors 
WHERE invoices.vendor_id = vendors.vendor_id
ORDER BY vendor_name; 