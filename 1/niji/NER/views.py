from django.shortcuts import render
from neo4j import GraphDatabase
from django.conf import settings
import mysql.connector

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
           '高楼', '凭栏', '危栏', '浮云', '寒山', '宿鸟', '日暮', '明月', '明月光'],
    "爱国": ['松柏', '梅花', '石灰', '丹青', '竹子', '九州', '龙城'],
    "离别": ['柳', '酒', '日暮', '斜阳', '夕阳', '暮雪', '暮钟', '衰草', '长亭', '短亭', '离歌', '孤帆', '杨花',
           '江花',
           '胡马', '越鸟', '洛城花', '罗裙', '芳草', '歧路', '阳关三叠', '谢亭', '行舟', '阳关曲', '渭城曲'],
    "闺怨": ['寒蝉', '更漏', '花红', '鹦鹉', '黄莺', '燕子', '银河', '流萤', '飞蛾', '烛光', '织布', '捣衣', '缝衣',
           '凭栏', '梳洗', '画眉', '梳妆', '珠帘', '团扇', '床枕', '帷幕', '帏帐', '画屏', '熏笼', '玉阶',
           ]}
"""
yx_dict = {
    "柳": ["写景", "送别", "思乡", "爱情", "友情"],
    "秋风": ["相思", "感怀", "怀古", "离别", "羁旅"],
    "落叶": ["写景", "送别", "思乡", "闺怨", "羁旅", "悼亡"],
    "落花": ["写景", "闺怨", "怀古", "悼亡", "感怀"],
    "岱宗": ["壮志", "怀古", "爱国", "励志", "哲理"],
    "夕阳": ["羁旅", "思乡", "离别", "感怀"],
    "梧桐": ["羁旅", "爱情"],

}
"""


# Create your views here.
def test(request):
    return render(request, '诗人行迹.html')


def yxProcess(request):
    # yxScript()
    if request.method == 'POST':
        input_sentence = request.POST['input_sentence']
        res = []
        yx_list = main.yx_recognition(input_sentence)
        count_dict = {"战争": 0, "思乡": 0, "爱国": 0, "离别": 0, "闺怨": 0}
        yx_list = list(set(yx_list))
        print(yx_list)
        for yx in yx_list:
            flag = 1
            for k, v in yx_dict.items():
                if yx in v:
                    res.append(yx + "——" + k)
                    count_dict[k] += 1
                    flag = 0
            if flag == 1:
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


# MySQL连接和读取数据
def read_from_mysql():
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='poems'
    )
    cursor = conn.cursor()
    cursor.execute("SELECT title, content FROM lv_writing_works")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data


# 创建Neo4j会话
def get_neo4j_session(uri, user, password):
    driver = GraphDatabase.driver(uri, auth=(user, password))
    return driver.session()


# 创建并链接节点
def create_and_link_nodes(session, myTitle, nyContent):
    query = (
        "MERGE (p:Poem {title: $myTitle}) "
        "MERGE (y:YX {name: $nyContent}) "
        "MERGE (p)-[:classified]->(y)"
    )
    print(myTitle+"->"+nyContent)
    session.run(query, myTitle=myTitle, nyContent=nyContent)


# 主函数，串联上述过程
def yxScript():
    # 读取MySQL数据
    mysql_data = read_from_mysql()

    # 连接到Neo4j
    session = get_neo4j_session("bolt://localhost:7687", "neo4j", "xhr020628")

    # 处理数据并在Neo4j中创建节点和关系
    try:
        for title, content in mysql_data:
            print(title, content)
            nyContent = yxProcess(content)
            create_and_link_nodes(session, title, nyContent)
    finally:
        # 关闭Neo4j会话
        session.close()
