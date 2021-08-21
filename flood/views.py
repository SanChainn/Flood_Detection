from django.shortcuts import render
from django.http import HttpResponse
from .models import Sensor
import random
my_context = {
        "Zone1": "100%",
        "Zone2": "100%",
        "Zone3": "100%",
        "Zone4": "50%",
    }
value = ["10%","20%","30%","40%","50%","60%","70%","80%","90%","100%"]
# Create your views here.
def index_view(request , *args , **kwargs):
    print(request)
    
    
    v1 = Sensor.objects.get(id=1)  # get sensor value1 from sensor model
    my_context["Zone1"]=v1.value+"%"
    
    v2 = Sensor.objects.get(id=2)   # get sensor value2 from sensor model
    my_context["Zone2"]=v2.value+"%"
    
    v3 = Sensor.objects.get(id=3)   # get sensor value3 from sensor model
    my_context["Zone3"]=v3.value+"%"
    
    v4 = Sensor.objects.get(id=4)   # get sensor value4 from sensor model
    my_context["Zone4"]=v4.value+"%"
    # a = random.randint(0,9)
    # my_context["Zone1"]=value[a]
    # a = random.randint(0,9)
    # my_context["Zone2"]=value[a]
    # a = random.randint(0,9)
    # my_context["Zone3"]=value[a]
    # a = random.randint(0,9)
    # my_context["Zone4"]=value[a]
    return render(request , "version2.html" , my_context)


def new(request, *args , **kwargs):
    return render(request)

def hello(request):
    print(request.GET)
    print('code :',request.GET.get('code'))
    return render(request,'index.html',{"name":"sanchaintun"})

def sen(request):
    ss = Sensor.objects.values()
    print(request.GET)
    print('code :',request.GET.get('code'))
    return HttpResponse(ss)

## sensor values for raspberry pi request and front end
def value1(request):
    ss = Sensor.objects.get(id=1)
    return HttpResponse(ss.value)

def value2(request):
    ss = Sensor.objects.get(id=2)
    return HttpResponse(ss.value)

def value3(request):
    ss = Sensor.objects.get(id=3)
    return HttpResponse(ss.value)

def value4(request):
    ss = Sensor.objects.get(id=4)
    return HttpResponse(ss.value)
## sensor values for raspberry pi request and front end



def sensor_store(request):
    if request.GET.get('code') == '1234':
        print('code :: 1234')

        sensor = Sensor()
        sensor.name = request.GET.get('name')
        sensor.value = request.GET.get('value')
        sensor.save()
        print("sensor ",sensor.name,"\nValue ",sensor.value)
    else:
        #return print("hi")
        return HttpResponse("HI")
    #return render(request,"home.html")
    return HttpResponse(Sensor.objects.values('name','value'))

def sensor_update(request):
    if request.GET.get('code') == '1234':
        print('code :: 1234')

        # sensor = Sensor()
        # sensor.name = request.GET.get('name')
        # sensor.value = request.GET.get('value')
        if request.GET.get('id') and request.GET.get('value'):
            iid = request.GET.get('id')
            ssensor = request.GET.get('sensor')
            vvalue = request.GET.get('value')
            sensor = Sensor(id=iid,name=ssensor,value=vvalue)
            sensor.save()
            print("sensor:",sensor.id,"\nValue:",sensor.value)
    else:
        #return print("hi")
        return HttpResponse("Wrong Parameter! Try again!! Haha \U0001F602 \U0001F602")
    #return render(request,"home.html")

    s = Sensor.objects.values('id','name','value')
    print(s)
    # iid =[]
    # nname =[]
    # vvalue = []
    # print(s)
    # for no in range(len(s)):
    #     iid.append(s[no]['id'])
    #     nname.append(s[no]['name'])
    #     vvalue.append(s[no]['value'])
        
    # print(iid , nname , vvalue)

    # for no in range(5):
    #     print('id :' , iid[no] , ' , name :',nname[no] , ', value :' ,vvalue[no])
    #
    return HttpResponse(Sensor.objects.values('id','name','value'))

    