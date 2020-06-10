from django.shortcuts import render

# Create your views here.
def p1(request):
    return render(request, 'p1.html')

def p2(request):
    if request.method == 'GET':
        return render(request, 'p2.html')

    elif request.method == 'POST':
        city = request.POST.get('city')
        print('执行数据保存操作...')
        return render(request, 'popup.html',{'city':city})