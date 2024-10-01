SELECT count(*) FROM vendors
WHERE vendor_state = "CA";

SELECT vendor_state, count(*) AS ct
FROM vendors 
GROUP BY vendor_state
ORDER BY ct desc;

SELECT terms_description, count(*) AS ct
FROM invoices JOIN terms USING (terms_id)
GROUP BY terms_id
HAVING ct>10;

SELECT vendor_id, vendor_name, sum(invoice_total) AS INVTOT
FROM invoices JOIN vendors USING (vendor_id)
GROUP BY vendor_id
ORDER BY INVTOT desc
LIMIT 10;

SELECT vendor_name, sum(payment_total) AS TOTPAY
FROM vendors JOIN invoices USING (vendor_id)
GROUP BY vendor_id
ORDER BY TOTPAY DESC;

SELECT vendor_name, sum(invoice_total), count(*) AS ct
FROM vendors JOIN invoices USING (vendor_id)
GROUP BY vendor_id
ORDER BY ct DESC; 

SELECT DISTINCT vendor_id FROM invoices; 

SELECT account_description, count(*) AS ct, sum(line_item_amount) AS total
FROM general_ledger_accounts AS gla JOIN invoice_line_items AS ili 
	USING (account_number)
GROUP BY gla.account_number
HAVING ct>1
ORDER BY total DESC;

SELECT account_number, sum(line_item_amount)
FROM invoice_line_items
GROUP BY account_number
WITH ROLLUP; -- gives total of all rows above

SELECT vendor_name, count(distinct ili.account_number) AS acctCt
FROM vendors v JOIN invoices i USING (vendor_id) JOIN invoice_line_items ili
	ON ili.invoice_id = i.invoice_id
GROUP BY v.vendor_id 
HAVING acctCt > 1


