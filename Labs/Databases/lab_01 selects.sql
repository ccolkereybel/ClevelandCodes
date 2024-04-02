SELECT invoice_number, invoice_total-payment_total-credit_total AS "Balance Due", payment_date
FROM invoices
WHERE payment_date is NULL
-- ORDER BY invoice_total-payment_total-credit_total DESC