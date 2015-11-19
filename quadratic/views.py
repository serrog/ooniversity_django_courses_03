# -*- coding: utf-8 -*-
from django.shortcuts import render

def quadratic_results(request):
	def check_for_error(val):
		result = None
		if len(val) == 0:
			result = "коэффициент не определен"
		elif val[0] == '-' and not val[1:].isdigit():
			result = "коэффициент не целое число"
		elif val[0] != '-' and not val.isdigit():
			result = "коэффициент не целое число"
		return result

	a = request.GET['a']
	b = request.GET['b']
	c = request.GET['c']
	cont = {}
	cont['a'] = "a = %s" % a
	cont['b'] = "b = %s" % b
	cont['c'] = "c = %s" % c

	
	if check_for_error(a) is not None:
		cont['err_a'] = check_for_error(a)
	elif int(a) == 0:
		cont['err_a'] = "коэффициент при первом слагаемом уравнения не может быть равным нулю"
	if check_for_error(b) is not None:
		cont['err_b'] = check_for_error(b)
	if check_for_error(c) is not None:
		cont['err_c'] = check_for_error(c)
	if not (cont.get('err_a') or cont.get('err_b') or cont.get('err_c')):
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
	return render(request, 'results.html', cont)
