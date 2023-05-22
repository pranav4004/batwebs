from django.shortcuts import render
import mysql.connector as sql
# Create your views here.
email=''
password=''
def login_action(request):
    global email,password
    if request.method=="POST":
        sql_base = sql.connect(host="localhost", user="root", passwd="PS@41004", database="batwebs")
        cur=sql_base.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                email=value
            if key=="password":
                password=value
                
        query_login = "SELECT * FROM users WHERE EMAIL='{}' AND  PASSWORD='{}'".format(email, password)

        cur.execute(query_login)
        t=tuple(cur.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request,'welcome.html')
        
    return render(request,'login.html')