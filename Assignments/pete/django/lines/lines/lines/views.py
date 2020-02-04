from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json

from .models import Line, LineCollection

@csrf_exempt
def lines(request):
    if request.body:
        data = json.loads(request.body)
        for line in data['lines']:
            new_line = Line(x0=line['start'][0], y0=line['start'][1], x1=line['end'][0], y1=line['end'][1])
            new_line.save()
    all_lines = Line.objects.all()
    line_dicts = [{'start': [one_line.x0, one_line.y0], 'end': [one_line.x1, one_line.y1]} for one_line in all_lines]
    return JsonResponse({'lines': line_dicts})