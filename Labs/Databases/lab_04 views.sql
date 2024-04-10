CREATE VIEW open_invoices AS 
SELECT vendor_name, invoice_number, invoice_date, invoice_total-payment_total-credit_total
FROM invoices JOIN vendors USING (vendor_id)