import datetime
yest=datetime.datetime.now()-datetime.timedelta(days=1)
tod=datetime.datetime.now()
tom=datetime.datetime.now()+datetime.timedelta(days=1)
l=[yest,tod,tom]
for x in l :
    print(x.strftime("%c"))