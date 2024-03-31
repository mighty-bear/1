# -*- coding: gbk -*-
from django.http import JsonResponse
from django.shortcuts import render
import random
from .models import keywords
from .models import puzzle

# Create your views here.

def index(request):
    return render(request, 'fhl_index.html')

def start_game(request):
    if request.method == 'POST':
        keyword = random.choice(keywords.objects.all())
        c_keyword = keyword.name
        return JsonResponse({'c_keyword': c_keyword})
    else:
        return JsonResponse({'error': 'Invalid request method'})

def check_answer(request):
    if request.method == 'POST':
        data = request.POST
        c_keyword = data.get('c_keyword')
        input_poem = data.get('poem')

        if not c_keyword or not input_poem:
            return JsonResponse({'error': 'Missing data'})

        previous, latter = input_poem.split('，')
        previous = previous.strip()
        latter = latter.strip()

        puzzles = puzzle.objects.filter(keyword=c_keyword)
        correct = False
        answer = puzzle.objects
        for puzzle_instance in puzzles:
            # print(puzzle_instance.previous_content,puzzle_instance.extracted_content,puzzle_instance.latter_content)
            if (puzzle_instance.previous_content == previous and puzzle_instance.extracted_content == latter) or \
                    (puzzle_instance.extracted_content == previous and puzzle_instance.latter_content == latter):
                correct = True
                answer = puzzle_instance
                break

        if correct:
            response = {'correct': True, 'message': '回答正确! "' + input_poem + '" 出自'
                                                    + answer.author + '的《' + answer.title + '》'}
        else:
            response = {'correct': False, 'message': '回答错误，游戏结束'}

        return JsonResponse(response)
    else:
        return JsonResponse({'error': 'Invalid request method'})