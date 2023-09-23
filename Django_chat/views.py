from django.http import HttpResponse
from django.shortcuts import render,redirect
from models.models import Register
from models.models import chatData



def homePage(request):

    return render (request,'index.html') 

def registerPage(request):


        return render (request,'register.html') 


def registerProcess(request):


        msg="" 
        name=request.POST['name']
        email=request.POST['email'] 
        if request.method=='POST' and name!='' and email!='' :
            name=request.POST['name']
            email=request.POST['email']
            password=request.POST['password']
            data=Register(name=name,email=email,password=password)

            data.save()

            msg="Record Insert successfully"
            return render (request,'register.html',{'message':msg}) 

        else:
         msg='Please input all field !!'
         return render (request,'register.html',{'message':msg}) 
        
               

       



def loginProcess(request):


        msg=""  
        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            
            flag=Register.objects.filter(email=username,password=password).values().exists()
            data=Register.objects.filter(email=username,password=password).values()
            data2=Register.objects.all().values().exclude(email=username)
           

            if flag :
                    
                     context={
                        'mydata':data,
                        'data2':data2
 
                   }
                   
                     return render (request,'loginProfile.html',context)   
                   
            else:
                  msg="Login Failed !!"
                  return render (request,'index.html',{'message':msg})
                                 


def chatProcess(request):


        
        data=request.POST['chat']
        newdata=data.split("/")
        

        context={
              'friend_email':newdata[1],
              'profile_email':newdata[0],
        }


        return render(request,'chat.html',context)

        # context={
        #        'mydata':data,
        #        'profile':profile,
        #        'pemail':pemail,
        # }




        # return render (request,'chat.html',context) 


def displayChat(request):
        
         if request.method=='POST':

             data3=request.POST['sendbutton']
             newdata=data3.split("/")
             data2=chatData.objects.filter(my_email=newdata[0]).values()
             chatDB={
                'chats':data2,
                'profile_email':newdata[0],
                'friend_email':newdata[1],
                'fl':False,
                }

             message=request.POST['message']
             if message!='':

                        data3=request.POST['sendbutton']
                        newdata=data3.split("/")


                        data=chatData(my_email=newdata[0],friend_email=newdata[1],my_message=message,friend_message='None')
                        data.save()
                        data=chatData(my_email=newdata[1],friend_email=newdata[0],my_message='None',friend_message=message)
                        data.save()



                        data2=chatData.objects.filter(my_email=newdata[0]).values()

                        chatDB={
                                'chats':data2,
                                'profile_email':newdata[0],
                                'friend_email':newdata[1],

                                
                        }

                        




                        


                        return render(request,'chat.html',chatDB) 
                
                
             return render(request,'chat.html',chatDB) 






                  

          


      


