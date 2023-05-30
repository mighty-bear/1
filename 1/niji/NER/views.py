from django.shortcuts import render
from neo4j import GraphDatabase
from django.conf import settings

import sys

sys.path.append('D:\\github\\1\\1\\niji\\NER')
sys.path.append('D:\\github\\1\\1\\niji\\NER\\zh_ner_tf')

print(sys.path)
from zh_ner_tf import main

"""
war_yx = ['角弓', '铁衣', '红旗', '烽火', '投笔', '长城', '羌笛', '楼兰', '柳营', '请缨', '胡乐', '关山', '孤城',
          '孤鸿', '铁马', '冰河', '沙场', '黄沙', '胡马', '玉门关', '匈奴', '胡尘', '征人', '征夫', '烽火', '三军',
          '吴钩', '干将', '莫邪', '戟', '宝刀', '宝马', '驽', '青骢', '铁骑', '羌管', '胡笳', '燕然', '将军', '壮士',
          '战士', '细柳营', '将军营', '班超', '金鼓', '玉鞍', '西戎', '蓟门', '蓟门关', '青海', '凌烟阁', '龙泉剑',
          '逐鹿', '问鼎']

sixiang_yx = ['月亮', '笛', '梧桐', '芦管', '杜鹃', '猿啼', '天涯', '高楼', '乌鸦', '浮萍', '泛舟', '扁舟', '鸿雁',
              '捣衣', '哀鸿', '莼羹鲈脍', '莼羹', '鲈鱼', '鲤鱼', '双鲤', '泊船', '尺素', '砧声', '秋风', '西楼',
              '高楼', '凭栏', '危栏', '浮云', '寒山', '宿鸟', '日暮']

aiguo_yx = ['松柏', '梅花', '石灰', '丹青', '竹子', '九州', '龙城']

libie_yx = ['柳', '酒', '日暮', '斜阳', '夕阳', '暮雪', '暮钟', '衰草', '长亭', '短亭', '离歌', '孤帆', '杨花', '江花',
            '胡马', '越鸟', '洛城花', '罗裙', '芳草', '歧路', '阳关三叠', '谢亭', '行舟', '阳关曲', '渭城曲']

guiyuan_yx = ['寒蝉', '更漏', '花红', '鹦鹉', '黄莺', '燕子', '银河', '流萤', '飞蛾', '烛光', '织布', '捣衣', '缝衣',
              '凭栏', '梳洗', '画眉', '梳妆', '珠帘', '团扇', '床枕', '帷幕', '帏帐', '画屏', '熏笼', '玉阶',
              ]
"""

yx_dict = {
    "战争": ['角弓', '铁衣', '红旗', '烽火', '投笔', '长城', '羌笛', '楼兰', '柳营', '请缨', '胡乐', '关山', '孤城',
             '孤鸿', '铁马', '冰河', '沙场', '黄沙', '胡马', '玉门关', '匈奴', '胡尘', '征人', '征夫', '烽火', '三军',
             '吴钩', '干将', '莫邪', '戟', '宝刀', '宝马', '驽', '青骢', '铁骑', '羌管', '胡笳', '燕然', '将军', '壮士',
             '战士', '细柳营', '将军营', '班超', '金鼓', '玉鞍', '西戎', '蓟门', '蓟门关', '青海', '凌烟阁', '龙泉剑',
             '逐鹿', '问鼎'],
    "思乡": ['月亮', '笛', '梧桐', '芦管', '杜鹃', '猿啼', '天涯', '高楼', '乌鸦', '浮萍', '泛舟', '扁舟', '鸿雁',
             '捣衣', '哀鸿', '莼羹鲈脍', '莼羹', '鲈鱼', '鲤鱼', '双鲤', '泊船', '尺素', '砧声', '秋风', '西楼',
             '高楼', '凭栏', '危栏', '浮云', '寒山', '宿鸟', '日暮'],
    "爱国": ['松柏', '梅花', '石灰', '丹青', '竹子', '九州', '龙城'],
    "离别": ['柳', '酒', '日暮', '斜阳', '夕阳', '暮雪', '暮钟', '衰草', '长亭', '短亭', '离歌', '孤帆', '杨花',
             '江花',
             '胡马', '越鸟', '洛城花', '罗裙', '芳草', '歧路', '阳关三叠', '谢亭', '行舟', '阳关曲', '渭城曲'],
    "闺怨": ['寒蝉', '更漏', '花红', '鹦鹉', '黄莺', '燕子', '银河', '流萤', '飞蛾', '烛光', '织布', '捣衣', '缝衣',
             '凭栏', '梳洗', '画眉', '梳妆', '珠帘', '团扇', '床枕', '帷幕', '帏帐', '画屏', '熏笼', '玉阶',
             ]}


# Create your views here.
def test(request):
    return render(request, '诗人行迹.html')


def yxProcess(request):
    if request.method == 'POST':
        input_sentence = request.POST['input_sentence']
        res = []
        yx_list = main.yx_recognition(input_sentence)
        count_dict = {"战争": 0, "思乡": 0, "爱国": 0, "离别": 0, "闺怨": 0}
        for yx in yx_list:
            for k, v in yx_dict.items():
                if yx in v:
                    res.append(yx + "——" + k)
                    count_dict[k] += 1
                else:
                    res.append(yx)
        res = list(set(res))
        key_max = max(count_dict.keys(), key=(lambda t: count_dict[t]))
        print(res)
        print(count_dict)
        print(key_max)
        driver = GraphDatabase.driver(
            f"bolt://{settings.NEO4J_HOST}:{settings.NEO4J_PORT}",
            auth=(settings.NEO4J_USERNAME, settings.NEO4J_PASSWORD)
        )
        with driver.session() as session:
            query = "MATCH p=(a)-[r:Classified]->(b) WHERE b.name='" + key_max + "' RETURN a.title as title,a.content " \
                                                                                 "as content,b.name as yx"

            result = session.run(query)

            print(result)

            nodes = []
            links = []

            for record in result:
                poem_title = record["title"]
                poem_content = record["content"]
                yx_name = record["yx"]

                # 添加Poem节点
                if {"name": poem_title, "category": 0, "content": poem_content} not in nodes:
                    nodes.append({"name": poem_title, "category": 0, "content": poem_content})
                # 添加yx节点
                if {"name": yx_name, "category": 1} not in nodes:
                    nodes.append({"name": yx_name, "category": 1})
                # 添加Classified关系
                links.append({"source": poem_title, "target": yx_name, "value": "Classified"})

            context = {
                "nodes": nodes,
                "links": links,
                "query_result": len(nodes) > 0
            }
            # print(context)
            print(nodes)
            print(links)
            driver.close()
        return render(request, '意象搜索.html', {"res": res, "nodes": nodes, "links": links})
    return render(request, '意象搜索.html')


def locationProcess(request):
    if request.method == 'POST':
        input_sentence = request.POST['input_sentence']
        loc_list = main.location_recognition(input_sentence)
        print(loc_list)
        return render(request, '诗人行迹.html', {"res": loc_list})
    return render(request, '诗人行迹.html')
