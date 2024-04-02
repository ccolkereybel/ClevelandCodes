-- SELECT invoice_number, invoice_total-payment_total-credit_total AS "Balance Due", payment_date
-- FROM invoices
-- WHERE payment_date is NULL
-- ORDER BY invoice_total-payment_total-credit_total DESC

-- SELECT 60000 AS Principle, 60000* .065 AS Interest, 60000*1.065 AS Total 

-- SELECT NOW() AS "CURRENT TIME"

-- SELECT CURRENT_TIME

-- SELECT vendor_name, vendor_state
-- FROM   vendors
-- ORDER BY vendor_state

-- SELECT vendor_name, vendor_state
-- FROM   vendors
-- WHERE NOT vendor_state in ("OH", "PA", "IN")
-- ORDER BY vendor_state

SELECT invoice_number, invoice_date
FROM invoices
WHERE MONTH (invoice_date) = 4 and YEAR(invoice_date) = 2014
-- WHERE invoice_date >= "2014-04-01" and invoice_date <= "2014-04-30"
ORDER BY invoice_date  