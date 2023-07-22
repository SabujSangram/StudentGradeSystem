import statistics
users={"user1":"pass1","user2":"pass2"}

stds={"Om":[78,98,67],
      "Aysha":[98,87,56],
      "Sabuj":[98,86,96],
      "Jyoti":[96,57,95]}

def entergrade():
  name=input("Enter the Student name : ")
  grade=input("Enter the Grade: ")
  if name in stds:
    print("Adding Grade ...")
    stds[name].append(int(grade))
    print(stds)
  else :
    print("Student dose not exist")
  

def removestudent():
  name=input("Plese enter a name: ")
  if name in stds:
    print("Removing Student ...")
    del stds[name]
    print(stds)
  else:
    print("Student dose not exist")

def studentsavggrade():
  for eachstd in stds:
    gradelist=stds[eachstd]
    avg=statistics.mean(gradelist)
    print(f"{eachstd} has an average grade of {avg}")

    
def main():
  print (''' welcome to Grade Control
  [1] - Enter Grade
  [2] - Remove Student
  [3] - Students Avarage Grade
  [4] - Exit''')
  action=input("What would you like to do ? (plese enter a number): ")
  if action=='1':
    entergrade()
  elif action=='2':
    removestudent()
  elif action =='3':
    studentsavggrade()
  elif action=='4':
    exit()
  else:
    print("Invalid choice!! plese enter a valid number ")

login=input("Plese enter your login ID : ")
password=input("Plese enter the password: ")
if login in users:
  if users[login]==password:
    print("Hello", login)
    while True:
      main()
  else: 
    print("Invalid Password ")
else:
  print("Invalid login ID !!")