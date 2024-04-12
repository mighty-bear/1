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
        poem = puzzle.objects.filter(keyword=c_keyword).first().content
        return JsonResponse({'c_keyword': c_keyword, 'poem': poem})
    else:
        return JsonResponse({'error': 'Invalid request method'})

def check_answer(request):
    if request.method == 'POST':
        data = request.POST
        c_keyword = data.get('c_keyword')
        input_poem = data.get('poem')
        answered_poems = data.getlist('answeredPoems[]')

        if not c_keyword or not input_poem:
            return JsonResponse({'error': 'Missing data'})

        answer = puzzle.objects.filter(keyword=c_keyword, content=input_poem).first()
        correct = False
        if answer:
            correct = True

        if correct:
            answered_poems.append(answer.content)
            reply_poem = puzzle.objects.filter(keyword=c_keyword).exclude(content__in=answered_poems).first().content
            message = '�ǳ���! "' + input_poem + '" ����' + answer.author + '�ġ�' + answer.title + '����' + '�ֵ����ˣ�' + reply_poem
            response = {'correct': True, 'message': message, 'replyPoem': reply_poem}
        else:
            response = {'correct': False, 'message': '�Ҳ�������ʫ���ǲ��Ǵ�����أ���סʫ��֮����ȫ�Ƕ��ŷָ�Ŷ'}

        return JsonResponse(response)
    else:
        return JsonResponse({'error': 'Invalid request method'})