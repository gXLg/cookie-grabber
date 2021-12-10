import sqlite3 as sql
from sys import argv
sitename = argv[1]
cookie = argv[2]

con = sql.connect("/data/data/com.android.chrome/app_chrome/Default/Cookies")
cur = con.cursor()
for entry in cur.execute("SELECT value FROM Cookies WHERE name = '" + cookie + "' AND host_key LIKE '%" + sitename + "%'"):
  print(entry[0])

con.close()
