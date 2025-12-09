from django.shortcuts import render
def vehicle(request):
    distance=int(request.POST.get('distance',0))
    fuelconsumed=int(request.POST.get('fuelconsumed',0))
    mileage=distance/fuelconsumed if request.method=='POST' else 0
    print("Distance travelled=",distance)
    print("Fuel consumed=",fuelconsumed)
    print("Vehicle mileage=",mileage)
    return render(request,'mathapp/math.html',{'distance':distance,'fuelconsumed':fuelconsumed,'mileage':mileage})
