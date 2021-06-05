import json

def Train():
    dict={}
    val_dict=[]
    flag=0
    obj_Name=input("Enter The Object Name")
    while flag!=1:
        obj_attribute=input("Enter object Property Name:")
        obj_Property=input(f"The {obj_attribute} is?: ")
        val_dict.append({obj_attribute:obj_Property})
        chek=input("Wanna add another property(y/n")
        if(chek=='y'):
            continue
        else:
            dict.update({obj_Name:val_dict})
            flag=flag+1
    return dict

def Test(ret):
    print(ret)
    data_val=input("Enter querry:")
    li=list(data_val.split(" "))
    for i in li:
        for x,y in ret.items():
            for j in range(0,len(y)):
                if i==x:
                    print(y)
                elif i==y[j]:
                    print(y[j].keys())
                elif i==y[j].keys():
                    print(y[j].values())

ret=Train()
Test(ret)


