users=[]
for x in range(3):
    user=input("enter the person to invite:\t")
    users.append(user)


user2=input("if want to add other choose y")

while (user2 =="y"):
 user=input("enter the person to invite")
 users.append(user)
 user2=input("if want to add other choose y")
 


print(f"you invite {users} thery are {len(users)} invited persons to party")