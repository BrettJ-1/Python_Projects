import sqlite3
conn = sqlite3.connect('test.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_extension(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                col_filename TEXT)")
    conn.commit()

fileList = ('information.docx', 'Hello.txt', 'myImage.ong',\
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_extension(col_filename) VALUES (?)", (x,))
            print(x)

conn.close()
