# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from quadratic import forms

def quadratic_results(request):
    if request.method == 'GET':
        a = request.GET.get('a')
        b = request.GET.get('b')
        c = request.GET.get('c')
        cont = {}
        if a == None and b == None and c == None:
            form = forms.QuadraticForm()
        else:
            form = forms.QuadraticForm(request.GET)
        if form.is_valid():
            a_f = form.cleaned_data['a']
            b_f = form.cleaned_data['b']
            c_f = form.cleaned_data['c']
            d = b_f * b_f - 4 * a_f * c_f
            cont['d'] = "Дискриминант: %(d)d" % { 'd':d }
            if d == 0:
                x = -b_f / (2.0 * a_f)
                cont['result'] = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %(x).1f" % {'x' : x}
            elif d > 0:
                x1 = (-b_f + d ** (1 / 2.0)) / (2.0 * a_f)
                x2 = (-b_f - d ** (1 / 2.0)) / (2.0 * a_f)
                cont['result'] = "Квадратное уравнение имеет два действительных корня: x1 = %(x1).1f, x2 = %(x2).1f" % {'x1':x1, 'x2':x2 }
            else:
                cont['result'] = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений." 
        else: 
            cont['result'] = "коэффициент не целое число"
        cont['form'] = form
    return render(request, 'results.html', cont)
