# -*- coding: utf-8 -*-
from django.shortcuts import render
from quadratic import forms

def quadratic_results(request):
    if request.method == 'GET':
        a = request.GET.get('a')
        b = request.GET.get('b')
        c = request.GET.get('c')
        cont = {}
        print a
        if a == None and b == None and c == None:
            form = forms.QuadraticForm()
        else:
            form = forms.QuadraticForm(request.GET)
        if form.is_valid():
            d = int(b) * int(b) - 4 * int(a) * int(c)
            cont['d'] = "Дискриминант: %(d)d" % { 'd':d }
            if d == 0:
                x = -int(b) / (2.0 * int(a))
                cont['result'] = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %(x).1f" % {'x' : x}
            elif d > 0:
                x1 = (-int(b) + d ** (1 / 2.0)) / (2.0 * int(a))
                x2 = (-int(b) - d ** (1 / 2.0)) / (2.0 * int(a))
                cont['result'] = "Квадратное уравнение имеет два действительных корня: x1 = %(x1).1f, x2 = %(x2).1f" % {'x1':x1, 'x2':x2 }
            else:
                cont['result'] = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений." 
        cont['form'] = form
    return render(request, 'results.html', cont)
