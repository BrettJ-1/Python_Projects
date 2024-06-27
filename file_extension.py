import sqlite3

conn = sqlite3.connect('file_extension.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_extension( \ 
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \                 #Created datbase with integer and string
        col_filename TEXT,)")
    conn.commit()
conn.close()

conn = sqlite3.connect('file_extension.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO col_filename(information.docx, Hello.txt, myImage.png, myMovie.mpg, World.txt, data.pdf, myPhoto.jpg) VALUES (?, ?, ?, ?, ?, ?, ?)"  #Inserted values into col_filename
conn.close()

conn = sqlite3.connect('file_extension.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT information.docx, Hello.txt, myImage.png, myMovie.mpg, World.txt, data.pdf, myPhoto.jpg FROM col_filename WHERE TEXT = '.txt'") #Selecting data with the filename extension of .txts
    varPerson = cur.fetchall()
    for item in varPerson:
        msg = "First: ()\nSecond: ()".format(item[0],item[1])
    print(msg)
