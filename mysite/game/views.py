from django.shortcuts import render

# Create your views here.


def game(request,**kwargs):
    if request.method == 'POST':
        print ("---POST---",request.POST)
    elif request.method == 'GET':
        print ("***GET***",request.GET)
        # vals = request.GET.copy()
        # s = vals.get('option1',False)
        # vals['desc'] = s
        # print (vals)
        # https://api.printful.com/countries



    else:
        print ("Something Else")

    return render(request, 'game/tic_tac.html')
