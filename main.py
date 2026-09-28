import sqlite3
import json
from datetime import date
from datetime import datetime
import random
connect=sqlite3.connect("db.db")
cursor=connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS doctors(
name TEXT,
id TEXT,
work TEXT)""")
connect.commit()
def wrong():
    print("there is something wrong")

def enter_number():
    print("enter number")

with open("patient.json","r") as file:
    data=json.load(file)
num=random.randint(1,99999999)

while True:
    try:
        quest=int(input("""1. i am patient
        2. see result
        3. i am doctor
        4. exit
        type: """))
    except ValueError:
        enter_number()
    else:
        if quest==1:
            f_name=input("gave your first name: ").lower()
            if f_name.isspace() is False and f_name!="":
                l_name=input("gave your lastname: ")
                if l_name.isspace() is False and l_name!="":
                    try:
                        age=int(input("gave your age: "))
                    except ValueError:
                        enter_number()
                    else:
                        if l_name.isspace() is False and l_name!="" and age>=0 and age<=140:
                            print("you will see the result soon")
                            now=datetime.now()
                            today=date.today()
                            data[f"{f_name,l_name}"]={"firstname":f_name,
                            "lastname":l_name,
                            "id":f"{random.randint(1,99999999)}",
                            "day":f"{today}",
                            "time":f"{now}",
                            "report":""}
                            with open("patient.json","w") as file:
                                json.dump(data,file,indent=4)
                            print(f"your id is {data[f"{f_name,l_name}"]["id"]}")
                        else:
                            enter_number()
                else:
                    wrong()
            else:
                wrong()
        elif quest==2:
            f_name2=input("gave your first name: ").lower()
            if f_name2.isspace() is False and f_name2!="":
                l_name2=input("gave your lastname: ")
                if l_name2.isspace() is False and l_name2!="":
                    try:
                        age=int(input("gave your age: "))
                    except ValueError:
                        enter_number()
                    else:
                        if age>=0 and age<=130:
                            try:
                                questid=int(input("gave your id: "))
                            except ValueError:
                                enter_number()
                            else:
                                if data[f_name2,l_name2]["id"]==questid:
                                    print(f"your result is: {data[f"{f_name2,l_name2}"]["report"]}")
                                else:
                                    wrong()
                        else:
                            wrong()
                else:
                    wrong()
            else:
                wrong()
        elif quest==3:
            try:
                idd=int(input("gave your id: "))
            except ValueError:
                enter_number()
            else:
                cursor.execute("SELECT * FROM doctors WHERE id=?",(idd,))
                result1=cursor.fetchone()
                if result1:
                    cursor.execute("SELECT name FROM doctors WHERE id=? ",(idd,))
                    result2=cursor.fetchone()
                    print(f"welcome here {result2}")
                    while True:
                        try:
                            menu=int(input("gave id enter 0 for exit: "))
                        except ValueError:
                            enter_number()
                        else:
                            menu2=str(menu)
                            if menu2!="0":
                                for things in data:
                                    if menu2==data[things]["id"] and menu2!=0:
                                        print(f"your patient name is: {data[things]["firstname"],data[things]["lastname"]} ")
                                        print("okay then import your report")
                                        fname=data[things]["firstname"]
                                        lname=data[things]["lastname"]
                                        report=input("type here: ")
                                        data[f"{fname,lname}"]["report"]=report
                            else:
                                break
                else:
                    print("there is something wrong")
        elif quest==4:
            print("good luck")
            break
