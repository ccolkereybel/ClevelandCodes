# first install the mysql connector module
# at the Windows command line:
# python3 -m pip install mysql-connector-python

from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user="root",
        password="cara835182",
        database="ap"
    ) as connection:
        print()
        # dynamic SQL
        add_where = False #don't need where clause
        where = ""
        print("Dates must be YYYY/MM/DD")
        startdate = input("Enter a starting date: [] ")
        enddate = input("Enter an ending date: [] ")
        invtype = input("Open or Closed invoices: []/O/C")
        vendorid = input ("Enter a vendor ID: [] ")
        print()
        query = "SELECT vendor_name, invoice_number, invoice_date, invoice_total\
                FROM vendors JOIN invoices USING (vendor_id) "
        orderby = "ORDER BY vendor_name, invoice_date "
        if len(startdate)>0:
            if add_where:
                where += f" AND invoice_date >= '{startdate}' "
            else:
                where += f" WHERE invoice_date >= '{startdate}' "
                add_where = True
                
        if len(enddate)>0:
            if add_where:
                where += f" AND invoice_date <= '{enddate}' "
            else:
                where += f" WHERE invoice_date <= '{enddate}' "
                add_where = True
                
        if len(invtype)>0:
            if add_where:
                where += " AND "
            else:
                where += " WHERE "
                add_where = True

            if  invtype.upper() == "O":
                where += " invoice_total-payment_total-credit_total > 0"
            elif invtype.upper() == "C":
                where += " invoice_total-payment_total-credit_total = 0"
        if len(vendorid)>0:
            if add_where:
                where += f" AND {vendorid} = invoices.vendor_id "
            else:
                where += f" WHERE {vendorid} = invoices.vendor_id "
                add_where = True

        query = query + where + orderby    
        print(query)
        print()
        
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute(query)
            result = cursor.fetchall() #grabs data and puts in list
            print(f"{len(result)} rows")
            # connection.commit() #need this to get commits
            for row in result:
                vendor_name = row["vendor_name"]
                invoice_number = row["invoice_number"]
                invoice_date = row["invoice_date"]
                print(f"{vendor_name}\t{invoice_number}\t{invoice_date}\t{row['invoice_total']}")
except Error as e:
    print("ERROR: " + str(e))
print("Done")
