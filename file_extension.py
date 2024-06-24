import sqlite3

conn = sqlite3.connect('file_extension.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_extension( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_information.docx TEXT, \
        col_Hello.txt TEXT, \
        col_myImage.png TEXT \
        col_myMovie.mpg TEXT \
        col_World.txt TEXT, \
        col_data.pdf TEXT \
        col_myPhoto.jpg TEXT \
        )")
    conn.commit()
conn.close()


conn = sqlite3.connect('file_extension.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_extension(information.docx, Hello.txt, myImage.png, myMovie.mpg, World.txt, data.pdf, myPhoto.jpg) VALUES (?, ?, ?, ?, ?, ?, ?)", \
                ('Classified', 'Hello!', 'Cat Photo', 'Back to The Future', 'Earth', 'Company Files', 'Smiling'))
    
conn.close()

conn = sqlite3.connect('file_extension.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT information.docx, Hello.txt, myImage.png, myMovie.mpg, World.txt, data.pdf, myPhoto.jpg FROM tbl_extension WHERE TEXT = '.txt'")
    varPerson = cur.fetchall()
    for item in varPerson:
        msg = "First: ()\nSecond: ()".format(item[0],item[1])
    print(msg)
