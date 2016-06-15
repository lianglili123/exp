from Dao import *

d=Dao()
res=d.selectSmemory()
print dir(res)
for rec in res:
    print rec
