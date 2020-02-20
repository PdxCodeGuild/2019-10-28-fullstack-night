from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Macros

def home(request):
    return render(request, 'calc/home.html')

def calc_form(request):
    return render(request, 'calc/calc-form.html')

def calc_macros(request):
    data = request.POST
    meas_sys = data['meas']
    weight_in = int(data['weight'])
    bfp = int(data['bfp'])#body fat percentage
    act_lvl = float(data['act_lvl'])
    goal = data['goal']

    if meas_sys == 'lbs':
        weight = round(weight_in * .45)
        meas_sys_bool = True
    else:
        weight = weight_in
        meas_sys_bool = False

    lbm = round(weight - (weight * (bfp / 100)))#lean body mass
    bmr = round(370 + 21.6 * lbm)#basal metabolic rate
    tdee = round(bmr * act_lvl)#total daily energy expenditure

    if goal == 'gain':
        adj = 1.2#adjustment
        fat_mult = .25#fat intake as a percentage of total calories
        goal_bool = False
    else:
        bfr = bfp // 10 #body fat range
        if bfr >= 3:
            adj = .7
        else:
            adj_list = [.85, .8, .75]
            adj = adj_list[bfr]
        fat_mult = 1.1#fat intake g / kg lbm
        goal_bool = True
    
    tadci = round(tdee * adj)#target average daily calorie intake
    tdci = round(tadci * 1.2)#training day calorie intake
    rdci = round(tadci * .8)#rest day calorie intake
    protein = round(lbm * 2.5)#protein g / day

    if goal == 'gain':
        train_fat = round(((fat_mult * tadci) / 9) * .7)
        rest_fat = round(((fat_mult * tadci) / 9) * 1.3)
    else:
        train_fat = round(fat_mult * lbm * .7)
        rest_fat = round(fat_mult * lbm * 1.3)
    
    train_carb = round((tdci - (protein * 4) - (train_fat * 9)) / 4)
    rest_carb = round((rdci - (protein * 4) - (rest_fat * 9)) / 4)

    macros = Macros(meas_sys=meas_sys_bool, weight=weight_in, bfp=bfp, act_lvl=act_lvl, goal=goal_bool, lbm=lbm, bmr=bmr, protein=protein, train_kcal=tdci, rest_kcal=rdci, train_fat=train_fat, rest_fat=rest_fat, train_carb=train_carb, rest_carb=rest_carb)
    macros.save()
    
    if request.user.is_authenticated:
        old_macros = request.user.macros
        old_macros.update(active=False)
        macros.user = request.user
        macros.active = True
        macros.save()
        
    return render(request, 'calc/macros.html', {'macros': Macros.objects.get(pk=macros.pk)})

@login_required
def view_macros(request):
    return render(request, 'calc/macros.html', {'macros': Macros.objects.get(user=request.user, active=True)})

@login_required
def re_calc(request):
    return render(request, 'calc/re-calc.html')