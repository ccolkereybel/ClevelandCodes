SELECT vendor_name, invoice_number, invoice_date, invoice_total-payment_total-credit_total AS "balance_due"
FROM invoices AS i JOIN vendors AS v USING (vendor_id)
WHERE invoice_total-payment_total-credit_total <> 0
ORDER BY vendor_name;

SELECT vendor_name, default_account_number, account_description
FROM vendors AS v JOIN general_ledger_accounts AS gla ON v.default_account_number = gla.account_number
ORDER BY account_description, vendor_name;

SELECT vendor_name, invoice_date, invoice_number, invoice_sequence, line_item_amount
FROM invoices AS i JOIN invoice_line_items AS ili USING (invoice_id)
	JOIN vendors AS v USING (vendor_id)
ORDER BY vendor_name, invoice_date, invoice_number, invoice_sequence;

SELECT vendor_name, vendor_state 
FROM vendors
WHERE vendor_state in ("CA")

UNION

SELECT vendor_name, "OUTSIDE CA"
FROM vendors
WHERE vendor_state NOT in ("CA")
ORDER BY vendor_name
