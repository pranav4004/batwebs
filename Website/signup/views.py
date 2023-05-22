from django.shortcuts import render
import mysql.connector as sql
# Create your views here.
first_name=''
last_name=''
sex=''
email=''
password=''
def signup_action(request):
    global first_name,last_name,sex,email,password
    if request.method=="POST":
        sql_base = sql.connect(host="localhost", user="root", passwd="PS@41004", database="batwebs")
        cur=sql_base.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                first_name=value
            if key=="last_name":
                last_name=value
            if key=="sex":
                sex=value
            if key=="email":
                email=value
            if key=="password":
                password=value
                
        query_insert = "INSERT INTO users (first_name,second_name, sex, email, password) VALUES ('{}', '{}', '{}', '{}', '{}')".format(first_name, last_name, sex, email, password)

        cur.execute(query_insert)
        sql_base.commit()
        
    return render(request,'signup.html')

def home_page(request):
    return render(request,'homepage.html')