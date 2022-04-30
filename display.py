from tabulate import tabulate
import sqlite3
conn=sqlite3.connect('Hospital.db')
c=conn.cursor()

with conn:
    c.execute("""SELECT * FROM csf_fluid_data""")
data=c.fetchall()
print(tabulate(data,headers=["Date", "RBC","Glucose","Protein","Total Count","Color","App.","ADA"]))
