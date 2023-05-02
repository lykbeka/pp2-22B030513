import psycopg2
conn=psycopg2.connect(
       host="localhost",
       database="phonebook",
       user="postgres",
       password="pass"
    )

ins="""INSERT INTO fb(first_name,last_name,phone_number) VALUES(%s,%s,%s)"""
cur=conn.cursor()
cur.execute("""SELECT first_name,last_name,phone_number FROM fb""")
print("('First name','Last name','Phone number')")
for row in cur.fetchall():
    
    print(row)
isrt=input("insert new data?(yes=1/no=0):")


if isrt=="1":
    cur.execute(
        ins,(input("First name:"),input("Last name:"),input("Phone number:"))
    )
    print("new data inserted")
elif isrt=="0":
    pass
else :
    print("Error")
    exit()
upd=input("update?(yes=1/no=0):")
if upd=="1":
    choi=input("update by first name or phone number?(f_n=1/ph_n=0): ")
    if choi=="1":
        fn=input("First name:")
        ln=input("New last name:")
        pn=input("New phone number:")

        cur.execute("""
        UPDATE fb set phone_number=%s where first_name=%s""",(pn,fn))
        cur.execute(
            """
            UPDATE fb set last_name=%s where first_name=%s""",
            (ln,fn)
        )
    elif choi=="0":
        pn=input("Phone number:")
        fn=input("New first name:")
        ln=input("New last name:")
        cur.execute("""
        UPDATE fb set first_name=%s where phone_number=%s""",(fn,pn))
        cur.execute("""
        UPDATE fron fb set last_name=%s where phone_name=%s""",(ln,pn))
    else:
        print("Error")
        exit()
elif upd=="0":
    pass
else :
    print("Error")
delete=input("Delete data?(yes=1/no=0):")
if delete=="1":
    choi=input("delete by first name or phone number?(f_n=1/ph_n=0): ")
    if choi=="1":
        fn=input("First name:")
        cur.execute("""
        DELETE from fb where first_name=%s;""",(fn,))
    elif choi=="0":
        pn=input("Phone number:")
        cur.execute("""
        DELETE from fb where phone_number=%s;""",(pn,))
    else:
        print("Error")
        exit()
elif delete=="0":
    pass
else :
    print("Error")
    exit()
cur.execute("""SELECT first_name,last_name,phone_number FROM fb""")
print("('First name','Last name','Phone number')")
for row in cur.fetchall():
    
    print(row)

conn.commit()
cur.close()
conn.close()
