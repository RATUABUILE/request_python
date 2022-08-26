import requests
import json
def request():
    ax= requests.get("http://saral.navgurukul.org/api/courses")
    x=ax.json()
    with open("courses.json","w") as f:
        json.dump(x,f,indent=4)
    with open("courses.json","r") as f:
        data = json.load(f)
    id= [] 
    i = 0
    while i < len(data['availableCourses']):
        print(i+1,"",data['availableCourses'][i]['name'],"=",data['availableCourses'][i]['id'])
        id.append(data['availableCourses'][i]['id'])
        i+=1 
    user= int(input("enter the id number:"))-1
    n1=requests.get("http://saral.navgurukul.org/api/courses/"+str(id[user])+"/exercises")
    a=n1.json()
    with open("humty.json","w") as f:
        json.dump(a,f,indent=4)
    with open("humty.json","r") as f:
        data = json.load(f)
    j=0
    l=0
    slug=[]
    while j<len(a["data"]):
        print(l+1,"=",a["data"][j]["name"])
        slug.append(a['data'][j]["slug"])
        l=l+1
        j=j+1
    slugname=int(input("Enter your slug number:"))-1
    list=requests.get("http://saral.navgurukul.org/api/courses/"+ str(user)+"/exercise/getBySlug?slug=" + slug[slugname])
    b=list.json()
    with open("sluglist.json","w") as f:
        json.dump(b,f,indent=4)
    with open("sluglist.json","r") as f:
        data = json.load(f)
    print(b["name"])
    print(b["slug"])
    print("CONTENT",b["content"])
    for i in range(len(slug)):
            s = input("enter the 'n' for next : ")
            if s == "n":
                i=0
                if i < len(slug):
                    print(slug[i])
                    print(b["content"]) 
                    break
            else:
                print(":your page is not  found")
                i=i+1
                print("*")
request()