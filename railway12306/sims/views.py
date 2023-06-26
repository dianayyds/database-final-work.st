

from django.shortcuts import render
from django.http import  JsonResponse
# Create your views here.
import pymysql as MySQLdb
import random
import string
from django.shortcuts import render, redirect
import datetime

def success(request):
    return render(request, 'railway/success.html')

# Create your views here.
# 首页列表显示函数
def index(request):
    return render(request, 'index.html')

# 乘客列表预览
def passenger_index(request):
    return render(request, 'railway2/passenger_index.html')

#管理员列表预览
def administrator_index(request):
    return render(request, 'railway/administrator_index.html')


def ticket_information2(request):
    return render(request, 'railway2/ticket_information2.html')
#余票信息表
def ticket_information(request):
    NUM = request.GET.get('NUM', '')
    TRAINID = request.GET.get('TRAINID', '')
    DAPARTUREPLACE = request.GET.get('DAPARTUREPLACE', '')
    ARRIVALPLACE = request.GET.get('ARRIVALPLACE', '')
    DAPARTUREDATE = request.GET.get('DAPARTUREDATE', '')
    DAPARTURETIME = request.GET.get('DAPARTURETIME', '')
    ARRIVALTIME = request.GET.get('ARRIVALTIME', '')
    PRICE = request.GET.get('PRICE', '')
    SEATTYPE = request.GET.get('SEATTYPE', '')
    AMOUNT = request.GET.get('AMOUNT', '')
    sql = 'select NUM,TRAINID,DAPARTUREPLACE,ARRIVALPLACE,DAPARTUREDATE, DAPARTURETIME, ARRIVALTIME, PRICE, SEATTYPE, AMOUNT  from ticket '
    conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="12306railway", charset='utf8',
                           cursorclass=MySQLdb.cursors.DictCursor)
    cur = conn.cursor()
    cur.execute(sql)
    tickets = cur.fetchall()
    return render(request, 'railway/ticket_information.html', {'tickets': tickets,
                                                               'NUM':NUM,
                                                               'TRAINID ': TRAINID,
                                                               'DAPARTUREPLACE': DAPARTURETIME,
                                                               'ARRIVALPLACE': ARRIVALTIME,
                                                               'DAPARTUREDATE':DAPARTUREDATE,
                                                               'DAPARTURETIME': DAPARTURETIME,
                                                               'ARRIVALTIME': ARRIVALTIME,
                                                               'PRICE': PRICE,
                                                               'SEATTYPE': SEATTYPE,
                                                           'AMOUNT': AMOUNT})

#查询余票信息
def ticket_search(request):
    DAPARTUREPLACE = request.GET.get('DAPARTUREPLACE', '')
    ARRIVALPLACE = request.GET.get('ARRIVALPLACE', '')
    DAPARTUREDATE = request.GET.get('DAPARTUREDATE', '')
    conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="12306railway", charset='utf8', cursorclass=MySQLdb.cursors.DictCursor)
    with conn.cursor() as cursor:
        cursor.execute("select NUM, TRAINID,DAPARTUREPLACE, ARRIVALPLACE,DAPARTUREDATE,DAPARTURETIME, ARRIVALTIME, PRICE, SEATTYPE, AMOUNT "
                       "from ticket where DAPARTUREPLACE = %s AND ARRIVALPLACE = %s AND DAPARTUREDATE = %s", [DAPARTUREPLACE,ARRIVALPLACE,DAPARTUREDATE])
        conn.commit()
    tickets = cursor.fetchall()
    return render(request, 'railway/ticket_search.html', {'tickets': tickets})

#查询余票信息
def ticket_search2(request):
    DAPARTUREPLACE = request.GET.get('DAPARTUREPLACE', '')
    ARRIVALPLACE = request.GET.get('ARRIVALPLACE', '')
    DAPARTUREDATE = request.GET.get('DAPARTUREDATE', '')
    conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="12306railway", charset='utf8', cursorclass=MySQLdb.cursors.DictCursor)
    with conn.cursor() as cursor:
        cursor.execute("select NUM, TRAINID,DAPARTUREPLACE, ARRIVALPLACE,DAPARTUREDATE,DAPARTURETIME, ARRIVALTIME, PRICE, SEATTYPE, AMOUNT "
                       "from ticket where DAPARTUREPLACE = %s AND ARRIVALPLACE = %s AND DAPARTUREDATE = %s", [DAPARTUREPLACE,ARRIVALPLACE,DAPARTUREDATE])
        conn.commit()
    tickets = cursor.fetchall()
    return render(request, 'railway2/ticket_search2.html', {'tickets': tickets})

#添加余票信息
def ticket_add(request):
    if request.method == 'GET':
        print(request)
        return render(request, 'railway/ticket_add.html')
    else:
        NUM = request.POST.get('NUM', '')
        TRAINID = request.POST.get('TRAINID', '')
        DAPARTUREPLACE = request.POST.get('DAPARTUREPLACE', '')
        ARRIVALPLACE = request.POST.get('ARRIVALPLACE', '')
        DAPARTUREDATE = request.POST.get('DAPARTUREDATE','')
        DAPARTURETIME = request.POST.get('DAPARTURETIME', '')
        ARRIVALTIME = request.POST.get('ARRIVALTIME', '')
        PRICE = request.POST.get('PRICE', '')
        SEATTYPE = request.POST.get('SEATTYPE', '')
        AMOUNT = request.POST.get('AMOUNT', '')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="12306railway",
                               charset='utf8', cursorclass=MySQLdb.cursors.DictCursor)
        cursor = conn.cursor()
        cursor.execute("insert into TICKET(NUM, TRAINID,DAPARTUREPLACE, ARRIVALPLACE,DAPARTUREDATE,DAPARTURETIME, ARRIVALTIME, "
                       "PRICE, SEATTYPE, AMOUNT) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                       [NUM, TRAINID,DAPARTUREPLACE, ARRIVALPLACE,DAPARTUREDATE,DAPARTURETIME,ARRIVALTIME, PRICE, SEATTYPE, AMOUNT])
        conn.commit()
    return redirect('../ticket_information')

#编辑余票信息
def ticket_edit(request):
    if request.method == 'GET':
        print(request)
        NUM = request.GET.get('NUM', '')
        TRAINID = request.GET.get('TRAINID', '')
        DAPARTUREPLACE = request.GET.get('DAPARTUREPLACE', '')
        ARRIVALPLACE = request.GET.get('ARRIVALPLACE', '')
        DAPARTUREDATE = request.GET.get('DAPARTUREDATE','')
        DAPARTURETIME = request.GET.get('DAPARTURETIME', '')
        ARRIVALTIME = request.GET.get('ARRIVALTIME', '')
        PRICE = request.GET.get('PRICE', '')
        SEATTYPE = request.GET.get('SEATTYPE', '')
        AMOUNT = request.GET.get('AMOUNT', '')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="12306railway", charset='utf8', cursorclass=MySQLdb.cursors.DictCursor)
        cursor = conn.cursor()
        cursor.execute("select NUM, TRAINID,DAPARTUREPLACE, ARRIVALPLACE,DAPARTUREDATE,DAPARTURETIME, ARRIVALTIME, PRICE, SEATTYPE, AMOUNT "
                       "from ticket WHERE NUM = %s",
                       [NUM])
        tickets = cursor.fetchall()
        return render(request, 'railway/ticket_edit.html', {'tickets': tickets,
                                                                   'NUM': NUM,
                                                                   'TRAINID ': TRAINID,
                                                                   'DAPARTUREPLACE': DAPARTURETIME,
                                                                   'ARRIVALPLACE': ARRIVALTIME,
                                                                    'DAPARTUREDATE':DAPARTUREDATE,
                                                                   'DAPARTURETIME': DAPARTURETIME,
                                                                   'ARRIVALTIME': ARRIVALTIME,
                                                                   'PRICE': PRICE,
                                                                   'SEATTYPE': SEATTYPE,
                                                                   'AMOUNT': AMOUNT})
    else:
        NUM = request.POST.get('NUM', '')
        TRAINID = request.POST.get('TRAINID', '')
        DAPARTUREPLACE = request.POST.get('DAPARTUREPLACE', '')
        ARRIVALPLACE = request.POST.get('ARRIVALPLACE', '')
        DAPARTUREDATE = request.POST.get('DAPARTUREDATE','')
        DAPARTURETIME = request.POST.get('DAPARTURETIME', '')
        ARRIVALTIME = request.POST.get('ARRIVALTIME', '')
        PRICE = request.POST.get('PRICE', '')
        SEATTYPE = request.POST.get('SEATTYPE', '')
        AMOUNT = request.POST.get('AMOUNT', '')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="12306railway",
                               charset='utf8', cursorclass=MySQLdb.cursors.DictCursor)
        cursor = conn.cursor()

        cursor.execute("UPDATE ticket set NUM = %s,TRAINID=%s,DAPARTUREDATE=%s, DAPARTUREPLACE=%s, ARRIVALPLACE=%s, DAPARTURETIME=%s, ARRIVALTIME=%s, "
                       "PRICE=%s,SEATTYPE=%s,AMOUNT=%s"
                       "where NUM = %s ",
                        [NUM ,TRAINID,DAPARTUREPLACE, ARRIVALPLACE,DAPARTUREDATE,DAPARTURETIME, ARRIVALTIME, PRICE, SEATTYPE, AMOUNT,NUM])
        conn.commit()
        return redirect('../ticket_information')
#删除车票信息
def ticket_delete(request):
    NUM = request.GET.get('NUM', '')
    conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="12306railway", charset='utf8', cursorclass=MySQLdb.cursors.DictCursor)
    cursor=conn.cursor()
    cursor.execute("DELETE FROM ticket WHERE  NUM =%s", [NUM])
    conn.commit()
    return redirect('../ticket_information')

#订单信息表
def ticket_list(request):
    DINGDANHAO = request.GET.get('DINGDANHAO', '')
    PASSENGERID = request.GET.get('PASSENGERID', '')
    PASSENGERNAME = request.GET.get('PASSENGERNAME', '')
    PASSENGERIDNUM = request.GET.get('PASSENGERIDNUM', '')
    TRAINID = request.GET.get('TRAINID', '')
    DAPARTUREPLACE = request.GET.get('DAPARTUREPLACE', '')
    ARRIVALPLACE = request.GET.get('ARRIVALPLACE', '')
    DAPARTURETIME = request.GET.get('DAPARTURETIME', '')
    ARRIVALTIME = request.GET.get('ARRIVALTIME', '')
    PRICE = request.GET.get('PRICE', '')
    SEATTYPE = request.GET.get('SEATTYPE', '')
    CREATETIME = request.GET.get('CREATETIME', '')
    sql = 'select DINGDANHAO,PASSENGERID ,PASSENGERNAME ,PASSENGERIDNUM ,ticket.TRAINID ,ticket.DAPARTUREPLACE ,' \
          'ticket.ARRIVALPLACE ,ticket.DAPARTURETIME ,ticket.ARRIVALTIME ,ticket.PRICE ,ticket.SEATTYPE,' \
          'CREATETIME from ticketlist,ticket where ticket.TRAINID = ticketlist.TRAINID'
    conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="12306railway", charset='utf8',
                           cursorclass=MySQLdb.cursors.DictCursor)
    cur = conn.cursor()
    cur.execute(sql)
    ticketlists = cur.fetchall()
    return render(request, 'railway/ticket_list.html', {'ticketlists': ticketlists,
                                                               'DINGDANHAO':DINGDANHAO,
                                                                'PASSENGERID':PASSENGERID,
                                                                'PASSENGERNAME': PASSENGERNAME,
                                                                'PASSENGERIDNUM': PASSENGERIDNUM,
                                                               'TRAINID ': TRAINID,
                                                               'DAPARTUREPLACE': DAPARTURETIME,
                                                               'ARRIVALPLACE': ARRIVALTIME,
                                                               'DAPARTURETIME': DAPARTURETIME,
                                                               'ARRIVALTIME': ARRIVALTIME,
                                                               'PRICE': PRICE,
                                                               'SEATTYPE': SEATTYPE,
                                                               'CREATETIME': CREATETIME})

def ticket_list_search(request):
    PASSENGERID = request.GET.get('PASSENGERID', '')
    conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="12306railway", charset='utf8',
                           cursorclass=MySQLdb.cursors.DictCursor)
    with conn.cursor() as cursor:
        cursor.execute(
          'select DINGDANHAO,PASSENGERID ,PASSENGERNAME ,PASSENGERIDNUM ,ticket.TRAINID ,ticket.DAPARTUREPLACE ,' \
          'ticket.ARRIVALPLACE ,ticket.DAPARTURETIME ,ticket.ARRIVALTIME ,ticket.PRICE ,ticket.SEATTYPE,' \
          'CREATETIME from ticketlist,ticket where ticket.TRAINID = ticketlist.TRAINID and PASSENGERID = %s ',
           [PASSENGERID])
        conn.commit()
    ticketlists = cursor.fetchall()
    return render(request, 'railway2/ticket_list_search.html', {'ticketlists': ticketlists})

#退票信息表
def ticket_deleted(request):
    DINGDANHAO = request.GET.get('DINGDANHAO', '')
    PASSENGERID = request.GET.get('PASSENGERID', '')
    PASSENGERNAME = request.GET.get('PASSENGERNAME', '')
    PASSENGERIDNUM = request.GET.get('PASSENGERIDNUM', '')
    TRAINID = request.GET.get('TRAINID', '')
    DAPARTUREPLACE = request.GET.get('DAPARTUREPLACE', '')
    ARRIVALPLACE = request.GET.get('ARRIVALPLACE', '')
    DAPARTURETIME = request.GET.get('DAPARTURETIME', '')
    ARRIVALTIME = request.GET.get('ARRIVALTIME', '')
    PRICE = request.GET.get('PRICE', '')
    SEATTYPE = request.GET.get('SEATTYPE', '')
    DELETETIME = request.GET.get('DELETETIME', '')
    sql = 'select DINGDANHAO,PASSENGERID ,PASSENGERNAME ,PASSENGERIDNUM ,ticket.TRAINID ,ticket.DAPARTUREPLACE ,' \
          'ticket.ARRIVALPLACE ,ticket.DAPARTURETIME ,ticket.ARRIVALTIME ,ticket.PRICE ,ticket.SEATTYPE,' \
          'DELETETIME from deleted,ticket where deleted.TRAINID = ticket.TRAINID'
    conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="12306railway", charset='utf8',
                           cursorclass=MySQLdb.cursors.DictCursor)
    cur = conn.cursor()
    cur.execute(sql)
    deletes = cur.fetchall()
    return render(request, 'railway2/ticket_deleted.html', {'deletes': deletes,
                                                               'DINGDANHAO':DINGDANHAO,
                                                                'PASSENGERID':PASSENGERID,
                                                                'PASSENGERNAME': PASSENGERNAME,
                                                                'PASSENGERIDNUM': PASSENGERIDNUM,
                                                               'TRAINID ': TRAINID,
                                                               'DAPARTUREPLACE': DAPARTURETIME,
                                                               'ARRIVALPLACE': ARRIVALTIME,
                                                               'DAPARTURETIME': DAPARTURETIME,
                                                               'ARRIVALTIME': ARRIVALTIME,
                                                               'PRICE': PRICE,
                                                               'SEATTYPE': SEATTYPE,
                                                               'DELETETIME': DELETETIME})

#购票
def ticket_buy(request):
    if request.method == 'GET':
        print(request)
        return render(request, 'railway2/ticket_buy.html')
    else:
        DINGDANHAO = random1(6)+random2(10)
        PASSENGERID = request.POST.get('PASSENGERID', '')
        PASSENGERNAME = request.POST.get('PASSENGERNAME', '')
        PASSENGERIDNUM = request.POST.get('PASSENGERIDNUM', '')
        TRAINID = request.POST.get('TRAINID', '')

        conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="12306railway",
                               charset='utf8', cursorclass=MySQLdb.cursors.DictCursor)
        cursor = conn.cursor()
        sql1="select *from ticket where trainID=%s"
        cursor.execute(sql1,(TRAINID))
        row = cursor.fetchone()
        print(row["NUM"])
        dapartureplace=row["DAPARTUREPLACE"]
        arrivalplace=row["ARRIVALPLACE"]
        daparturetime=row["DAPARTURETIME"]
        arrivaltime=row["ARRIVALTIME"]
        price=row["PRICE"]
        seattype=row["SEATTYPE"]
        curr_time = datetime.datetime.now()
        createtime=str(curr_time)
        daparturedate=row["DAPARTUREDATE"]
        sql2="update ticket set AMOUNT=AMOUNT-1 where trainID=%s"
        cursor.execute(sql2,(TRAINID))
        cursor.execute("insert into ticketlist(dingdanhao, passengerid, passengername, passengeridnum, trainid, dapartureplace, arrivalplace, daparturetime, arrivaltime, price, seattype, createtime, daparturedate) " \
              "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[DINGDANHAO,PASSENGERID ,PASSENGERNAME ,PASSENGERIDNUM ,TRAINID,dapartureplace,arrivalplace,daparturetime,arrivaltime,price,seattype,createtime,daparturedate])
        conn.commit()
    return redirect('../success')


#用户信息表
def passenger_information(request):
    ID = request.GET.get('ID', '')
    PASSWORD = request.GET.get('PASSWORD', '')
    NAME = request.GET.get('NAME', '')
    AGE = request.GET.get('AGE ')
    SEX = request.GET.get('SEX', '')
    IDNUMBER = request.GET.get('IDNUMBER', '')
    TEL = request.GET.get('TEL', '')
    sql ='select ID, PASSWORD, NAME, AGE, SEX, IDNUMBER, TEL from passenger '
    conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="12306railway", charset='utf8',
                           cursorclass=MySQLdb.cursors.DictCursor)
    cur = conn.cursor()
    cur.execute(sql)
    passengers = cur.fetchall()
    return render(request, 'railway/passenger_information.html', {'passengers':passengers,
                                                                 'ID': ID,
                                                                 'PASSWORD': PASSWORD,
                                                                  'NAME': NAME,
                                                                  'AGE': AGE,
                                                                  'SEX': SEX,
                                                                  'IDNUMBER': IDNUMBER,
                                                                  'TEL': TEL
                                                                  })
#添加用户信息
def passenger_add(request):
    if request.method == 'GET':
        print(request)
        return render(request, 'railway/passenger_add.html')
    else:
        ID = request.POST.get('ID','')
        PASSWORD = request.POST.get('PASSWORD')
        NAME = request.POST.get('NAME')
        AGE = request.POST.get('AGE')
        SEX = request.POST.get('SEX')
        IDNUMBER = request.POST.get('IDNUMBER')
        TEL = request.POST.get('TEL')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="12306railway",
                               charset='utf8', cursorclass=MySQLdb.cursors.DictCursor)
        cursor = conn.cursor()
        cursor.execute("insert into passenger(ID, PASSWORD, NAME, AGE, SEX, IDNUMBER, TEL) values(%s,%s,%s,%s,%s,%s,%s)",
                       [ID, PASSWORD, NAME, AGE, SEX, IDNUMBER, TEL])
        conn.commit()
    return redirect('../success')

#编辑用户信息
def passenger_edit(request):
    if request.method == 'GET':
        print(request)
        ID = request.GET.get('ID', '')
        PASSWORD = request.GET.get('PASSWORD', '')
        NAME = request.GET.get('NAME', '')
        AGE = request.GET.get('AGE')
        SEX = request.GET.get('SEX', '')
        IDNUMBER = request.GET.get('IDNUMBER', '')
        TEL = request.GET.get('TEL', '')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="12306railway", charset='utf8', cursorclass=MySQLdb.cursors.DictCursor)
        cursor = conn.cursor()
        cursor.execute("SELECT ID, PASSWORD, NAME, AGE, SEX, IDNUMBER, TEL  FROM passenger where ID = %s",
                       [ID])
        passenger = cursor.fetchone()
        return render(request, 'railway/passenger_edit.html', {'passenger;': passenger,
                                                                 'ID': ID,
                                                                 'PASSWORD': PASSWORD,
                                                                  'NAME': NAME,
                                                                  'AGE': AGE,
                                                                  'SEX': SEX,
                                                                  'IDNUMBER': IDNUMBER,
                                                                  'TEL': TEL})
    else:
        ID = request.POST.get('ID', '')
        PASSWORD = request.POST.get('PASSWORD', '')
        NAME = request.POST.get('NAME', '')
        AGE = request.POST.get('AGE')
        SEX = request.POST.get('SEX', '')
        IDNUMBER = request.POST.get('IDNUMBER', '')
        TEL = request.POST.get('TEL', '')

        conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="12306railway",
                               charset='utf8', cursorclass=MySQLdb.cursors.DictCursor)
        cursor = conn.cursor()

        cursor.execute("UPDATE passenger set ID=%s,PASSWORD=%s, NAME=%s, AGE=%s, SEX=%s, IDNUMBER=%s, TEL=%s"
                       "where ID = %s ",
                        [ID, PASSWORD, NAME, AGE, SEX, IDNUMBER, TEL,ID])
        conn.commit()
        return redirect('../success')
#删除用户信息
def passenger_delete(request):
    ID = request.GET.get('ID', '')
    conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="12306railway", charset='utf8', cursorclass=MySQLdb.cursors.DictCursor)
    cursor=conn.cursor()
    cursor.execute("DELETE FROM passenger WHERE  ID =%s", [ID])
    conn.commit()
    return redirect('../passenger_information')

#查询用户信息
def passenger_search(request):
    ID = request.GET.get('ID', '')
    conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="12306railway", charset='utf8', cursorclass=MySQLdb.cursors.DictCursor)
    with conn.cursor() as cursor:
        cursor.execute("select ID, PASSWORD,NAME, AGE, SEX, IDNUMBER, TEL from passenger where ID = %s", [ID])
        conn.commit()
    passengers = cursor.fetchall()
    return render(request, 'railway/passenger_search.html', {'passengers': passengers})

#管理员信息表
def administrator_information(request):
    ID = request.GET.get('ID', '')
    PASSWORD = request.GET.get('PASSWORD', '')
    JOBNUMBER = request.GET.get('JOBNUMBER', '')
    NAME = request.GET.get('NAME','')
    TEL = request.GET.get('TEL','')
    POSTISION = request.GET.get('POSTISION', '')
    sql ='select ID, PASSWORD, JOBNUMBER,NAME,TEL,POSTISION from administrator '
    conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="12306railway", charset='utf8',
                           cursorclass=MySQLdb.cursors.DictCursor)
    cur = conn.cursor()
    cur.execute(sql)
    administrators = cur.fetchall()
    return render(request, 'railway/administrator_information.html', {'administrators':administrators,
                                                                      'ID': ID,
                                                                      'PASSWORD': PASSWORD,
                                                                      'JOBNUMBER': JOBNUMBER,
                                                                      'NAME':NAME,
                                                                      'TEL':TEL,
                                                                      'POSTISION': POSTISION
                                                                      })

#添加管理员信息
def administrator_add(request):
    if request.method == 'GET':
        print(request)
        return render(request, 'railway/administrator_add.html')
    else:
        ID = request.POST.get('ID','')
        PASSWORD = request.POST.get('PASSWORD')
        JOBNUMBER = request.POST.get('JOBNUMBER')
        NAME = request.POST.get('NAME', '')
        TEL = request.POST.get('TEL', '')
        POSTISION = request.POST.get('POSTISION')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="12306railway",
                               charset='utf8', cursorclass=MySQLdb.cursors.DictCursor)
        cursor = conn.cursor()
        cursor.execute("insert into administrator(ID, PASSWORD,JOBNUMBER, NAME,TEL,POSTISION) values(%s,%s,%s,%s,%s,%s)",
                       [ID, PASSWORD,JOBNUMBER, NAME,TEL,POSTISION])
        conn.commit()
    return redirect('../administrator_information')

#编辑管理员信息
def administrator_edit(request):
    if request.method == 'GET':
        print(request)
        ID = request.GET.get('ID', '')
        PASSWORD = request.GET.get('PASSWORD', '')
        JOBNUMBER = request.GET.get('JOBNUMBER', '')
        NAME = request.GET.get('NAME', '')
        TEL = request.GET.get('TEL', '')
        POSTISION = request.GET.get('POSITISION', '')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="12306railway", charset='utf8', cursorclass=MySQLdb.cursors.DictCursor)
        cursor = conn.cursor()
        cursor.execute("SELECT ID, PASSWORD,JOBNUMBER,NAME,TEL, POSTISION FROM administrator where ID = %s",
                       [ID])
        administrator = cursor.fetchone()
        return render(request, 'railway/administrator_edit.html', {'administrator': administrator,
                                                                 'ID': ID,
                                                                 'PASSWORD': PASSWORD,
                                                                  'JOBNUMBER': JOBNUMBER,
                                                                   'NAME': NAME,
                                                                   'TEL': TEL,
                                                                  'POSTISION': POSTISION})
    else:
        ID = request.POST.get('ID', '')
        PASSWORD = request.POST.get('PASSWORD', '')
        JOBNUMBER = request.POST.get('JOBNUMBER')
        NAME = request.POST.get('NAME', '')
        TEL = request.POST.get('TEL', '')
        POSTISION = request.POST.get('POSTISION')

        conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="12306railway",
                               charset='utf8', cursorclass=MySQLdb.cursors.DictCursor)
        cursor = conn.cursor()

        cursor.execute("UPDATE administrator set ID=%s,PASSWORD=%s, JOBNUMBER=%s,NAME=%s, TEL=%s,  POSTISION=%s"
                       "where ID = %s ",
                        [ID, PASSWORD,JOBNUMBER,NAME,TEL,POSTISION,ID])
        conn.commit()
        return redirect('../administrator_information')
#删除管理员信息
def administrator_delete(request):
    ID = request.GET.get('ID', '')
    conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="12306railway", charset='utf8', cursorclass=MySQLdb.cursors.DictCursor)
    cursor=conn.cursor()
    cursor.execute("DELETE FROM administrator WHERE  ID =%s", [ID])
    conn.commit()
    return redirect('../administrator_information')

#退票
def ticket_back(request):
    dingdanhao=request.GET.get('DINGDANHAO','')
    TRAINID = request.GET.get('TRAINID', '')
    conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="12306railway", charset='utf8', cursorclass=MySQLdb.cursors.DictCursor)
    cursor=conn.cursor()
    sql1="delete from ticketlist where TRAINID=%s and DINGDANHAO=%s"
    cursor.execute(sql1,(TRAINID,dingdanhao))
    sql2 = "update ticket set AMOUNT=AMOUNT+1 where trainID=%s"
    cursor.execute(sql2, (TRAINID))
    conn.commit()
    return redirect('../success')


#查询管理员信息
def administrator_search(request):
    ID = request.GET.get('ID', '')
    conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="12306railway", charset='utf8', cursorclass=MySQLdb.cursors.DictCursor)
    with conn.cursor() as cursor:
        cursor.execute("select ID, PASSWORD,JOBNUMBER,POSTISION "
                       "from administrator where ID = %s", [ID])
        conn.commit()
    administrators = cursor.fetchall()
    return render(request, 'railway/administrator_search.html', {'administrators': administrators})

def random1(y):
    cname=[]
    for x in range(0, y):
        c=random.choice(string.ascii_uppercase)
        cname .append(c)

    cname1="".join(cname)
    return cname1
def random2(y):
    cname=[]
    for x in range(0, y):
        c=random.choice(string.digits)
        cname .append(c)

    cname2="".join(cname)
    return cname2