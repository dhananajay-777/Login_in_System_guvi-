email = input('Enter email: ')
password = input('Enter password: ')
import json
def email_veri(email):
    #print("email veri")
    s='[@_!#$%^&*()<>?/\|}{~:]' # special character set
    e1=False
    if(e1==False):
        c1=email.__contains__("@")
        c2=email.__contains__(".")
        c3=email.__contains__("@.")
        c4=email[0].isnumeric()
        c5=email[0] in s
        if(c1==True)and(c2==True)and(c3==False)and(c4==False)and(c5==False):
            e1=True
    return e1
def password_veri(password):
    l1=len(password)
    c1=0
    c2=0
    c3=0
    p1=False
    for i in password:
        if(p1==False):
            if i.isupper:
                c1+=1
            if i.islower:
                c2+=1
            if i.isnumeric():
                c3+=1
            c4=0
            l1=len(password)
            s='[@_!#$%^&*()<>?/\|}{~:]' # special character set
                # checking if any special character is present in given string or not
            for i in s:
                c4+=1
    if(c1>0)and(c2>0)and(c3>0)and(c4>0)and(l1>5)and(l1<16):
        p1=True
        #print(p1)  
    return p1    
f = open('demo1.json', 'r+')
content = json.load(f)
out_file = open('demo1out.json', 'w')

def write_json(new_data, filename='demo1.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        content['Entries'].append(new_data)
        file_data.update(content)
        file.seek(0)
        json.dump(file_data, file, indent = 4)
def password_reset_json(new_data, filename='demo1.json'):
    new_password = input('Please enter your new password: ')
    id=int(e["ID"])-1
    content["Entries"][id]["password"]=new_password
    print("Password has been updated",new_password)
    f.seek(0)
    f.write(json.dumps(content))
    f.truncate()
for c in content:
    for e in content['Entries']:

            if email_veri(email)!=True:
                print("Invalid  format of email address")
            else:
                if email == e['email']:
                    if (password_veri(password)):
                        if password == e['password']:
                            print('you are now logged in!')
                            break
                        else:
                            #forgot password process.
                            print('Wrong password Going to reset password')
                            password_reset_json(content)
                            break
                    else:
                        print("Invalid password")
                        break
                else:
                    continue
      
print('do you want to add a new user? Enter 1 for yes and 0 for no ')
Q=int(input('Enter the option: '))
if(Q==1):
    print('Your name is not in the file.')
    print('You need to register.')
    new_email= input('Please enter your email in a valid formate: ')
    if(email_veri(new_email)==True):
        new_password = input('Please enter your password formate: ')
        if(password_veri(new_password)== False):
            id = len(content['Entries'])
            new_full = {"email":f"{new_email}",
                        "password": f"{new_password}",
                        "ID": f"{id + 1}"
                        }
            write_json(new_full)
            print(new_full)
            print('Your name is added in the file.')
        else:
            print("Invalid password")
    else:
        print("Invalid email")

"""
{
    "Entries": [
        {
            "email": "dsw777@gmail.com",
            "password": "Aa1!234",
            "ID": "1"
        }
    ]
}
"""
