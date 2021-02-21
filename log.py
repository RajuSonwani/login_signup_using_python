import os,json

print('<<<<<<<<<<< "Sign_In/Sign_Up Page">>>>>>>>>>>>>>>\n1.sign_in\n2.sign_up')
z=input("choose one:_")
if z=="2":
	lst=["user_id","password",]
	dic={}
	for x in range(len(lst)):
		a=input(lst[x]+":_")
		dic[lst[x]]=a
	# dic0={dic["user_id"]:dic}
	# with open("data.json","w") as file:
	# 	json.dump(dic0,file,indent=4)
	
	with open("data.json") as file:
		z=json.load(file)

	z[dic["user_id"]]=dic
	with open("data.json","r+") as file:
		json.dump(z,file,indent=4)
	print("u r successfully registered")
else:
	with open("data.json") as file:
		z=json.load(file)
	count=0
	while count!=3:
		i=input("user_id:_")
		count+=1
		if i not in z:
			print("invalid")
			continue

		else:
			for s in range(4):
				if s==3:
					print("u have crossed the limit")
					break
				else:
					m=input("password:_")
					if m!=z[i]["password"]:
						print("wrong pass!")
						continue
					else:
						print("welcome")
						break
		break

