from django.shortcuts import render

# Create your views here.

d = {
    'contents':[
        {
            'name':'azmain',
            'id':223089,
            'cgpa':4.00,    
        },
        {
            'name':'amirul',
            'id':2230419,
            'cgpa':3.50,
        },
        {
            'name':'dipto',
            'id':2230470,
            'cgpa':3.26,
        },
    ],
}

def printer(request):
    return render(request, 'dynamic_view.html', d)