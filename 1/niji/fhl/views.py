# -*- coding: gbk -*-
from django.http import JsonResponse
from django.shortcuts import render
import random
from .models import Keywords
from .models import Puzzle

# Create your views here.
nodes = []
links = []


def index(request):
    return render(request, 'fhl_index.html')


def updateNodesAndLinks(puzzle, c_keyword):
    global nodes, links
    print("Before update:", len(nodes), len(links))
    poem_content = puzzle.content
    poem_title = puzzle.title
    author_name = puzzle.author
    dynasty_name = puzzle.dynasty

    # ���Poem�ڵ�
    if {"name": poem_title, "category": 0, "symbolSize": 10} not in nodes:
        nodes.append({"name": poem_title, "category": 0, "symbolSize": 10})
    # ���Dynasty�ڵ�
    if {"name": dynasty_name, "category": 1, "symbolSize": 10} not in nodes:
        nodes.append({"name": dynasty_name, "category": 1, "symbolSize": 10})
    # ���Author�ڵ�
    if {"name": author_name, "category": 2, "symbolSize": 10} not in nodes:
        nodes.append({"name": author_name, "category": 2, "symbolSize": 10})
    # ���Content�ڵ�
    if {"name": poem_content, "category": 3, "symbolSize": 10} not in nodes:
        nodes.append({"name": poem_content, "category": 3, "symbolSize": 10})
    # ���Keyword�ڵ�
    if {"name": c_keyword, "category": 4, "symbolSize": 50} not in nodes:
        nodes.append({"name": c_keyword, "category": 4, "symbolSize": 50})

    # ��ӹ�ϵ
    links.append({"source": author_name, "target": dynasty_name})
    links.append({"source": poem_title, "target": author_name})
    links.append({'source': poem_content, 'target': poem_title})
    links.append({'source': c_keyword, 'target': poem_content})

    print("After update:", len(nodes), len(links))


def start_game(request):
    if request.method == 'POST':
        global nodes,links
        nodes.clear()
        links.clear()
        keyword = random.choice(Keywords.objects.all())
        c_keyword = keyword.name

        puzzle = Puzzle.objects.filter(keyword=c_keyword).first()
        updateNodesAndLinks(puzzle, c_keyword)
        print(nodes,links)

        return JsonResponse({'c_keyword': c_keyword, 'poem': puzzle.content, 'nodes': nodes, 'links': links})
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

        puzzle = Puzzle.objects.filter(keyword=c_keyword, content=input_poem).first()
        correct = False
        if puzzle:
            correct = True

        if correct:
            updateNodesAndLinks(puzzle, c_keyword)
            answered_poems.append(puzzle.content)
            reply_puzzle = Puzzle.objects.filter(keyword=c_keyword).exclude(content__in=answered_poems).first()
            reply_poem = reply_puzzle.content
            updateNodesAndLinks(reply_puzzle, c_keyword)
            print(nodes, links)
            message = '�ǳ���! "' + input_poem + '" ����' + puzzle.author + '�ġ�' + puzzle.title + '����' + '�ֵ����ˣ�' + reply_poem
            response = {'correct': True, 'message': message, 'replyPoem': reply_poem, 'nodes': nodes, 'links': links}
        else:
            response = {'correct': False, 'message': '�Ҳ�������ʫ���ǲ��Ǵ�����أ���סʫ��֮����ȫ�Ƕ��ŷָ�Ŷ'}

        return JsonResponse(response)
    else:
        return JsonResponse({'error': 'Invalid request method'})
