from django.http import HttpResponse
from django.shortcuts import render
from . models import tool
from . forms import toolform
def index(request):
    tools=tool.objects.all
    context={
        'tool_list':tools
    }
    return render(request,'index.html',context)
def detail(request, tools_id):
    tools=tool.objects.get(id=tools_id)
    return render(request,"details.html",{'tools':tools})
def add_tool(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc = request.POST.get('desc', )
        year = request.POST.get('year', )
        img = request.FILES['img']
        tools=tool(name=name,desc=desc,year=year,img=img)
        tools.save()
    return render(request,'add.html')
def update(request,id):
    tools=tool.objects.get(id=id)
    form=toolform(request.POST or request.FILES,instance=tools)
    if form.is_valid():
        form.save()
        return  redirect('/')
    return  render(request,'edit.html',{'form':form,'tool':tool})
def delete(request,id):
    if request.method=="POST":
        tools=tool.objects.get(id=id)
        tool.save()
        return redirect ('/')
    return render(request,'delete.html')
