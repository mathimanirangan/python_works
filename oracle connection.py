import cx_Oracle
 
# Create a table in Oracle database
try:
 
    con = cx_Oracle.connect('af41536/Oradb#10@spsodsvc-p-01.internal.das:1525/SPSODSVCP')
    print(con.version)
 
    # Now execute the sqlquery
    cursor = con.cursor()
 
    # Creating a table employee
    cursor.execute(
        "select * from SPSOWNER.PROV where MSTR_RPOV_ID = '101'")
 
    print("query executed successfully")
 
except cx_Oracle.DatabaseError as e:
    print("There is a problem with Oracle", e)
 
# by writing finally if any error occurs
# then also we can close the all database operation
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
