

num='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$*'
a=input("Enter Password:")
print("Applying brute force attack.....")
getpass=""
count=0

while getpass!=a:
    try:
        for i in num:
            if a[count]==i:
                getpass=getpass+i
                count=count+1
    except:
        print("Your password is=", getpass)











