#coding:utf-8
import requests as rq
import datetime
import time
import csv

def main(Date):
    rea = []
    rea.append(str(Date))
    Page = rq.get("http://www.cnyes.com/futures/History.aspx?mydate="+str(Date)+"&code=GL")#目標網佔
    Start = Page.content.index('"cr"') #搜索"cr"

    con = str(Page.content[Start-15:Start+150])
    con_f = int(con.index('<td'))+len('<td  class="cr">')
    con_e = int(con.index('</td>'))
    rea.append(str(con[con_f:con_e]))

    con = str(con[con_e+len('</td>'):])
    con_f = int(con.index('<td'))+len('<td  class="cr">')
    con_e = int(con.index('</td>'))
    rea.append(str(con[con_f:con_e]))

    con = str(con[con_e+len('</td>'):])
    con_f = int(con.index('<td'))+len('<td  class="cr">')
    con_e = int(con.index('</td>'))
    rea.append(str(con[con_f:con_e]))

    con = str(con[con_e+len('</td>'):])
    con_f = int(con.index('<td'))+len('<td  class="cr ">')
    con_e = int(con.index('</td>'))
    rea.append(str(con[con_f:con_e]))

    con = str(con[con_e+len('</td>'):])
    con_f = int(con.index('<td'))+len('<td  class="cr">')
    con_e = int(con.index('</td>'))
    rea.append(str(con[con_f:con_e]))

    return rea


sd = datetime.datetime(2012, 1, 2)
Endday = (datetime.datetime.now()-datetime.timedelta(days=2)).strftime('%Y%m%d')
Datesf = sd.strftime('%Y%m%d')
Date = sd
MainArray=[]
MainArray.append(["日期",'開盤','最高','最低','收盤','成交量'])
MainArray.append(main(Datesf))

while (Datesf != Endday):
    Date = Date+datetime.timedelta(days=1)
    Datesf = Date.strftime('%Y%m%d')
    try:
        MainArray.append(main(Datesf))
    except:
       pass
    print Datesf
    time.sleep(0)

print MainArray
f = open("stock.csv","a+w")
w = csv.writer(f)
w.writerows(MainArray)
f.close()
