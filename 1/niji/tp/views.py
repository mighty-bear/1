# 各页面主函数

from django.shortcuts import render, redirect, get_object_or_404
from docx.api import Document
import pymysql
from .models import *
from niji import models as md
import re
from django.contrib.auth.models import User
from docx import Document
from fuzzywuzzy import fuzz
from neo4j import GraphDatabase
from django.conf import settings
from django.http import JsonResponse
from . import question_classifier
from . import gpttest
import json
from .models import Poem
from .models import Author
from django.urls import reverse
from NER.views import yxProcess, locationProcess


def index(request):
    names = ["靖康之变", "夏日绝句", "汴州", "宋徽宗", "满江红·写怀", "示儿", "菩萨蛮·书江西造口壁", "诉衷情·当年万里觅封侯", "书愤", "秋夜将晓出篱门迎凉有感二首其二", "病起书怀",
             "相见欢·金陵城上西楼", "贺新郎·送胡邦衡待制", "蝶恋花·上巳召亲族", "夜游宫·记梦寄师伯浑", "十一月四日风雨大作·其二", "添字丑奴儿·窗前谁种芭蕉树", "题临安邸", "念奴娇·登多景楼",
             "念奴娇·炎精中否", "声声慢·寻寻觅觅", "长相思·惜梅", "永遇乐·京口北固亭怀古", "宋徽宗不理朝政", "北宋联金攻辽", "海上之盟", "辽国灭亡", "金国撕毁海上之盟", "金国攻打北宋",
             "徽钦二宗被掳", "金军占领汴州", "北宋灭亡", "康王赵构南下继位宋高宗", "南宋建立", "金军南扑", "宋军英勇反抗", "宋高宗入海逃避", "金军北撤", "韩世忠围困金军",
             "岳飞大败金军", "宋金议和", "金毁和约攻南宋", "岳飞抗金", "南宋采用投降政策", "秦桧任宰相", "岳飞被害", "宋金和议《绍兴和约》", "南宋偏安杭州", "南宋不思北上中原",
             "宋钦宗", "宋高宗", "岳飞", "韩世忠", "秦桧", "杭州", "燕云十六州", "黄天荡"]
    if request.method == "GET":
        # i = 1
        # ans = ""
        # que = ""
        # select = []
        # obj = {}
        # document = Document('D:\\qqDownload\\niji-master\\niji\\tp\\static\\shengsheng.docx')
        # if not paper.objects.filter(Title='声声慢·寻寻觅觅'):
        #     paper.objects.create(Title='声声慢·寻寻觅觅', Id=1) # paper表中无记录时，需指定id为1
        #     for paragph in document.paragraphs:
        #         if re.match('\d、', paragph.text): # 题干部分
        #             ans = re.search('[A-Z]', paragph.text).group()
        #             que = re.sub('（[A-Z]）', '()', paragph.text)
        #             obj['Question'] = que
        #             obj['Answer'] = ans
        #         else: # 选项部分
        #             select = re.sub('[A-D].', ' ', paragph.text.strip()).split(' ')
        #             del select[0]
        #             if len(select) > 1:
        #                 obj['A'] = select[0]
        #                 obj['B'] = select[1]
        #                 obj['C'] = select[2]
        #                 obj['D'] = select[3]
        #                 obj['Title2_id'] = 1
        #                 obj['Id'] = i
        #                 i += 1
        #                 selection.objects.create(**obj)
        #             else:
        #                 p = re.search('[A-D]', paragph.text).group()
        #                 obj[p] = select[0]
        #                 if p == 'D':
        #                     obj['Title2_id'] = 1
        #                     obj['Id'] = i
        #                     i += 1
        #                     selection.objects.create(**obj)
        return render(request, 'test.html')
        # for name in names:
        #     i = name.find(t)
        #     j = t.find(name)
        #     # if i != -1:
        #     #     t = '/' + name + '/'
        #     #     break
        #     if j != -1:
        #         t = '/' + name + '/'
        #         break
        # if i == -1 and j == -1:
        #     print('?')
        #     return render(request, 'test.html')
        # else:
        #     print(t)
        #     return redirect(t)
        # if t == '靖康之变':
        #     return redirect('/靖康之变/')
        # if t == '夏日绝句':
        #     return redirect('/夏日绝句/')
        # if t == '汴州':
        #     return redirect('/汴州/')
        # if t == '宋徽宗':
        #     return redirect('/宋徽宗/')
        # else:
        #     return render(request, 'test.html')


def search(request):
    t = request.POST.get('title')
    # names = ["靖康之变", "夏日绝句", "汴州","宋徽宗","满江红·写怀","示儿","菩萨蛮·书江西造口壁","诉衷情·当年万里觅封侯","书愤","秋夜将晓出篱门迎凉有感二首其二","病起书怀","相见欢·金陵城上西楼","贺新郎·送胡邦衡待制","蝶恋花·上巳召亲族","夜游宫·记梦寄师伯浑","十一月四日风雨大作·其二","添字丑奴儿·窗前谁种芭蕉树","题临安邸","念奴娇·登多景楼","念奴娇·炎精中否","声声慢·寻寻觅觅","长相思·惜梅","永遇乐·京口北固亭怀古","宋徽宗不理朝政","北宋联金攻辽","海上之盟","辽国灭亡","金国撕毁海上之盟","金国攻打北宋","徽钦二宗被掳","金军占领汴州","北宋灭亡","康王赵构南下继位宋高宗","南宋建立","金军南扑","宋军英勇反抗","宋高宗入海逃避","金军北撤","韩世忠围困金军","岳飞大败金军","宋金议和","金毁和约攻南宋","岳飞抗金","南宋采用投降政策","秦桧任宰相","岳飞被害","宋金和议《绍兴和约》","南宋偏安杭州","南宋不思北上中原","宋钦宗","宋高宗","岳飞","韩世忠","秦桧","杭州","燕云十六州","黄天荡"]
    names = ["岳阳楼主要建筑", "岳阳楼历史沿革", "岳阳楼历史沿革图谱", "岳阳楼相关诗文", "岳阳楼建筑格局", "雨中登岳阳楼望君山", "游岳阳楼记",
             "泊岳阳城下", "岳阳楼记", "岳阳楼", "题岳阳楼", "登岳阳楼", "与夏十二登岳阳楼"
             ]
    dic = {}
    for name in names:
        dic[name] = fuzz.partial_ratio(name, t)
    print(dic)
    marks = sorted(dic.items(), key=lambda d: d[1], reverse=True)
    if marks[0][1] <= 20:
        pass
    else:
        for i in range(len(marks)):
            if marks[i][1] < 50:
                marks = marks[:i]
                break
        marks = dict(marks)
    return render(request, 'search.html', {'sea_list': marks})


def QA(request):
    return render(request, 'test.html')


def gushiciliebiao(request):
    return render(request, '古诗词列表.html')


def lishiliebiao(request):
    return render(request, '历史列表.html')


def One(request):
    return render(request, '1.html')


def Two(request):
    return render(request, '2.html')


def Three(request):
    return render(request, '3.html')


def Four(request):
    return render(request, '4.html')


def Five(request):
    return render(request, '5.html')


def Six(request):
    return render(request, '6.html')


def Seven(request):
    return render(request, '7.html')


def Eight(request):
    return render(request, '8.html')


def Nine(request):
    return render(request, '9.html')


def Ten(request):
    return render(request, '10.html')


def Eleven(request):
    return render(request, '11.html')


def Twelve(request):
    return render(request, '12.html')


def Thirteen(request):
    return render(request, '13.html')


def Fourteen(request):
    return render(request, '14.html')


def Fifteen(request):
    return render(request, '15.html')


def Sixteen(request):
    return render(request, '16.html')


def Seventeen(request):
    return render(request, '17.html')


def Eighteen(request):
    return render(request, '18.html')


def Nineteen(request):
    return render(request, '19.html')


def Twenty(request):
    return render(request, '20.html')


def TiYueYangLou(request):
    return render(request, '题岳阳楼.html')


def YuZhongDengYueYangLouWangJunShan(request):
    return render(request, "雨中登岳阳楼望君山.html")


def YueYangLou(request):
    return render(request, "岳阳楼.html")


def YuXiaShiErDengYueYangLou(request):
    return render(request, "与夏十二登岳阳楼.html")


def YouYueYangLouJi(request):
    return render(request, "游岳阳楼记.html")


def YueYangLouJi(request):
    return render(request, "岳阳楼记.html")


def BoYueYangChengXia(request):
    return render(request, "泊岳阳城下.html")


def DengYueYangLou(request):
    return render(request, "登岳阳楼.html")


def YueYangLouLiShiYanGe(request):
    return render(request, "岳阳楼历史沿革.html")


def YueYangLouJianZhuGeJu(request):
    return render(request, "岳阳楼建筑格局.html")


def YueYangLouZhuYaoJianZhu(request):
    return render(request, "岳阳楼主要建筑.html")


def YueYangLouLiShiYanGeTuPu(request):
    return render(request, "岳阳楼历史沿革图谱.html")


def YueYangLouXiangGuanShiWen(request):
    return render(request, "岳阳楼相关诗文.html")


def LiShiLieBiao(request):
    return render(request, "历史列表.html")


def ShiYiYueSiRiFengYuDaZuo(request):
    return render(request, "十一月四日风雨大作.html")


def YuMenGuan(request):
    return render(request, "玉门关.html")


def test(request):
    if request.method == 'GET':
        poem = paper.objects.filter(Title="声声慢·寻寻觅觅").first()
        que = poem.selection_set.filter(Title2_id=poem.Id)
        return render(request, 'test.html', {'que': que, 'title': poem.Title})


def tpshow(request):
    driver = GraphDatabase.driver(
        f"bolt://{settings.NEO4J_HOST}:{settings.NEO4J_PORT}",
        auth=(settings.NEO4J_USERNAME, settings.NEO4J_PASSWORD)
    )

    with driver.session() as session:
        selected_dynasty = request.POST.get('dynasty')
        input_author = request.POST.get('author')
        input_title = request.POST.get('title')
        # 执行Neo4j查询，获取知识图谱数据
        if request.method == 'GET' or (selected_dynasty == '' and input_author == '' and input_title == ''):
            query = """
            MATCH (poem:Poem)-[:BELONGS_TO]->(dynasty:Dynasty),
                  (poem:Poem)-[:WRITTEN_BY]->(author:Author)
            WHERE dynasty.name = '唐'
            RETURN poem.title AS title, poem.content AS content,
                   dynasty.name AS dynasty, author.name AS author
            LIMIT 50
            UNION
            MATCH (poem:Poem)-[:BELONGS_TO]->(dynasty:Dynasty),
                  (poem:Poem)-[:WRITTEN_BY]->(author:Author)
            WHERE dynasty.name = '宋'
            RETURN poem.title AS title, poem.content AS content,
                   dynasty.name AS dynasty, author.name AS author
            LIMIT 50
            UNION
            MATCH (poem:Poem)-[:BELONGS_TO]->(dynasty:Dynasty),
                  (poem:Poem)-[:WRITTEN_BY]->(author:Author)
            WHERE dynasty.name = '元'
            RETURN poem.title AS title, poem.content AS content,
                   dynasty.name AS dynasty, author.name AS author
            LIMIT 50
            UNION
            MATCH (poem:Poem)-[:BELONGS_TO]->(dynasty:Dynasty),
                  (poem:Poem)-[:WRITTEN_BY]->(author:Author)
            WHERE dynasty.name = '明'
            RETURN poem.title AS title, poem.content AS content,
                   dynasty.name AS dynasty, author.name AS author
            LIMIT 50
            UNION
            MATCH (poem:Poem)-[:BELONGS_TO]->(dynasty:Dynasty),
                  (poem:Poem)-[:WRITTEN_BY]->(author:Author)
            WHERE dynasty.name = '清'
            RETURN poem.title AS title, poem.content AS content,
                   dynasty.name AS dynasty, author.name AS author
            LIMIT 50
            """
        else:
            query = """
                    MATCH (poem:Poem)-[:BELONGS_TO]->(dynasty:Dynasty),
                          (poem:Poem)-[:WRITTEN_BY]->(author:Author) WHERE true
                    """

            if selected_dynasty:
                query += "\nAND dynasty.name = '" + selected_dynasty + "'"

            if input_author:
                query += "\nAND author.name = '" + input_author + "'"

            if input_title:
                query += "\nAND poem.title CONTAINS '" + input_title + "'"

            query += "\nRETURN poem.title AS title, poem.content AS content,dynasty.name AS dynasty, author.name AS author LIMIT 200"

        print(query)
        result = session.run(query)
        print(result)

        nodes = []
        links = []

        # 整理查询结果为echarts所需的节点和关系数据
        for record in result:
            poem_title = record["title"]
            poem_content = record["content"]
            dynasty_name = record["dynasty"]
            author_name = record["author"]

            # 添加Poem节点
            if {"name": poem_title, "category": 0, "content": poem_content} not in nodes:
                nodes.append({"name": poem_title, "category": 0, "content": poem_content})
            # 添加Dynasty节点
            if {"name": dynasty_name, "category": 1} not in nodes:
                nodes.append({"name": dynasty_name, "category": 1})
            # 添加Author节点
            if {"name": author_name, "category": 2} not in nodes:
                nodes.append({"name": author_name, "category": 2})
            # 添加BELONGS_TO关系
            links.append({"source": poem_title, "target": dynasty_name, "value": "BELONGS_TO"})
            # 添加WRITTEN_BY关系
            links.append({"source": poem_title, "target": author_name, "value": "WRITTEN_BY"})

        context = {
            "nodes": nodes,
            "links": links,
            "query_result": len(nodes) > 0
        }

    driver.close()
    # print(nodes)
    # print(links)

    return render(request, 'tpshow.html', context)

def nodeClicked(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        category = data.get('category')
        name = data.get('name')

        # 古诗
        if category == 0:
            p = Poem.objects.filter(title=name).first()
            if p:
                redirect_url = reverse('poem_info', kwargs={'poem_id': p.id})
                return JsonResponse({'redirect': redirect_url})

        # 诗人
        if category == 2:
            a = Author.objects.filter(name=name).first()
            if a:
                redirect_url = reverse('author_info', kwargs={'author_id': a.id})
                return JsonResponse({'redirect': redirect_url})
        return JsonResponse({'error': 'Not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def poemInfo(request, poem_id):
    p = get_object_or_404(Poem, id=poem_id)
    return render(request, 'poem_info.html', {'poem': p})

def authorInfo(request, author_id):
    a = get_object_or_404(Author, id=author_id)
    return render(request, 'author_info.html', {'author': a})

def poemToAuthor(request, author):
    a = Author.objects.filter(name=author).first()
    if a:
        return render(request, 'author_info.html', {'author': a})
    return JsonResponse({'error': 'Not found'}, status=404)

def poemToYx(request):
    poem_content = request.POST.get('poem_content', '')
    return yxProcess(request, poem_content)

def authorToLocation(request):
    author_desc = request.POST.get('author_desc', '')
    return locationProcess(request, author_desc)

def chat(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        # 在这里根据用户的输入进行逻辑处理，生成系统的回答
        system_message = get_system_response(user_message)
        return JsonResponse({'user_message': user_message, 'system_message': system_message})
    return render(request, 'QA.html')


def get_system_response(user_message):
    # 这里是一个简单的示例，你可以根据实际需求进行修改
    return "1"


def build_entitydict(args):
    entity_dict = {}
    for arg, types in args.items():
        for type in types:
            if type not in entity_dict:
                entity_dict[type] = [arg]
            else:
                entity_dict[type].append(arg)

    return entity_dict


handler = question_classifier.QuestionClassifier()
gptModel = gpttest.GPTModel()


def getAnswer(request):
    if request.method == 'POST':
        data = request.POST
        question = data.get('question')

        res_classify = handler.classify(question)
        print(res_classify)
        message = ""
        maxToken = gptModel.max_token
        if "question_types" not in res_classify or not res_classify['question_types']:
            message = "无"
        else:
            question_type = res_classify['question_types'][0]
            entity_dict = build_entitydict(res_classify['args'])

            driver = GraphDatabase.driver(
                f"bolt://{settings.NEO4J_HOST}:{settings.NEO4J_PORT}",
                auth=(settings.NEO4J_USERNAME, settings.NEO4J_PASSWORD)
            )
            with driver.session() as session:
                if question_type == 'author_create':
                    author = entity_dict.get('author')[0]
                    sql = 'MATCH (n:Poem) WHERE n.author = "' + author + '" RETURN n.title as title'
                    result = session.run(sql)
                    message = author + "的作品有："
                    i = 0
                    for record in result:
                        if i == 5:
                            break
                        i += 1
                        title = record["title"]
                        title_ = "《" + title + "》，"
                        message += title_
                    message = message[:-1]
                    message += "等等"


                elif question_type == 'poem_belong':
                    poem = entity_dict.get('poem')[0]
                    sql = 'MATCH (n:Poem) WHERE n.title = "'+ poem +'" RETURN n.author AS author'
                    result = session.run(sql)
                    author = ''
                    for record in result:
                        author = record["author"]
                    message = "《" + poem + "》的作者是" + author

                elif question_type == 'author_belong':
                    author = entity_dict.get('author')[0]
                    sql = 'MATCH p=(author)<-[r2:WRITTEN_BY]-(poem)-[r1:BELONGS_TO]->(dynasty) WHERE author.name = "' \
                          + author + '" RETURN dynasty.name AS name LIMIT 1'
                    result = session.run(sql)
                    dynasty = ''
                    for record in result:
                        dynasty = record["name"]
                    message = author + "是" + dynasty + "朝的诗人"

                elif question_type == 'dynasty_has':
                    dynasty = entity_dict.get('dynasty')[0]
                    if "朝" in dynasty:
                        dynasty = dynasty[:-1]
                    sql = 'MATCH p=(author)<-[r2:WRITTEN_BY]-(poem)-[r1:BELONGS_TO]->(dynasty) WHERE dynasty.name = "' + \
                          dynasty + '"return DISTINCT author.name AS name limit 25'
                    result = session.run(sql)
                    message = dynasty + "朝的诗人有："
                    i = 0
                    for record in result:
                        if i == 5:
                            break
                        i += 1
                        name = record["name"]
                        name_ = name + "，"
                        message += name_
                    message = message[:-1]
                    message += "等等"

                elif question_type == 'poem_content':
                    poem = entity_dict.get('poem')[0]
                    sql = 'MATCH (n:Poem) WHERE n.title = "' + poem + '" RETURN n.content AS content LIMIT 1'
                    result = session.run(sql)
                    message = "《" + poem + "》的内容是："
                    for record in result:
                        print(record)
                        message += record["content"]
                    response = {'message': message}
                    return JsonResponse(response)

                elif question_type == 'poem_intro':
                    poem = entity_dict.get('poem')[0]
                    sql = 'MATCH (n:Poem) WHERE n.title = "' + poem + '" RETURN n.introduction AS intro LIMIT 1'
                    result = session.run(sql)
                    message = ""
                    maxToken += 150
                    for record in result:
                        message += record["intro"]

                elif question_type == 'author_desc':
                    author = entity_dict.get('author')[0]
                    sql = 'MATCH (n:Author) WHERE n.name = "' + author + '" RETURN n.description AS desc LIMIT 1'
                    result = session.run(sql)
                    message = ""
                    maxToken += 150
                    for record in result:
                        print(record)
                        message += record["desc"]

                else:
                    message = "无"
            driver.close()
        print("???????")
        prompt = "问题：" + question + " 事实信息：" + message
        print(prompt)
        gptModel.max_token = maxToken
        message = gptModel.chat_gpt(prompt)
        response = {'message': message}

        return JsonResponse(response)
