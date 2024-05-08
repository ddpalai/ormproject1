from django.shortcuts import render
from testapp.models import Employee
from django.db.models import Q
from django.db.models import Avg,Max,Min,Sum,Count
# Create your views here.
def aggregate_view(request):
    avg = Employee.objects.all().aggregate(Avg('esal'))
    max = Employee.objects.all().aggregate(Max('esal'))
    min = Employee.objects.all().aggregate(Min('esal'))
    sum = Employee.objects.all().aggregate(Sum('esal'))
    count = Employee.objects.all().aggregate(Count('esal'))
    return render(request,'testapp/aggregate.html', {'avg':avg['esal__avg'],'max':max['esal__max'], 'min':min['esal__min'], 'sum':sum['esal__sum'], 'count':count['esal__count']})
from django.db.models.functions import Lower
def retrieve_view(request):
    print(request.user)
    q1 = Employee.objects.filter(esal__lt=12000)
    q2 = Employee.objects.filter(ename__startswith='s')
    emp_list = q1.union(q2)
    return render(request,'testapp/index.html',{'emp_list':emp_list})
    #return render(request,'testapp/specificcolumns.html',{'emp_list':emp_list})
    #emp_list = Employee.objects.all()
    #emp_list = Employee.objects.filter(esal__lte=15000)
    #emp_list = Employee.objects.filter(ename__contains='john')
    #emp_list = Employee.objects.filter(id__in=[1,3,5,51])
    #emp_list = Employee.objects.filter(~Q(ename__startswith='S'))
    #emp_list = Employee.objects.filter(ename__endswith='s')
    #emp_list = Employee.objects.filter(esal__range=[13000,15000])
    #emp_list = Employee.objects.filter(Q(ename__startswith='D') | Q(esal__lt=11000))
    #emp_list = Employee.objects.filter(ename__startswith='S') & Employee.objects.filter(esal__lt=15001)
    #emp_list = Employee.objects.filter(ename__startswith='A',esal__lt=13000)
    #return render(request,'testapp/index.html',{'emp_list':emp_list})
