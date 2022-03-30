# 各页面主函数

from django.shortcuts import render, redirect
from docx.api import Document
import pymysql
from .models import *
from niji import models as md
import re
from django.contrib.auth.models import User
from docx import Document
from fuzzywuzzy import fuzz

def index(request):
    names = ["靖康之变", "夏日绝句", "汴州","宋徽宗","满江红·写怀","示儿","菩萨蛮·书江西造口壁","诉衷情·当年万里觅封侯","书愤","秋夜将晓出篱门迎凉有感二首其二","病起书怀","相见欢·金陵城上西楼","贺新郎·送胡邦衡待制","蝶恋花·上巳召亲族","夜游宫·记梦寄师伯浑","十一月四日风雨大作·其二","添字丑奴儿·窗前谁种芭蕉树","题临安邸","念奴娇·登多景楼","念奴娇·炎精中否","声声慢·寻寻觅觅","长相思·惜梅","永遇乐·京口北固亭怀古","宋徽宗不理朝政","北宋联金攻辽","海上之盟","辽国灭亡","金国撕毁海上之盟","金国攻打北宋","徽钦二宗被掳","金军占领汴州","北宋灭亡","康王赵构南下继位宋高宗","南宋建立","金军南扑","宋军英勇反抗","宋高宗入海逃避","金军北撤","韩世忠围困金军","岳飞大败金军","宋金议和","金毁和约攻南宋","岳飞抗金","南宋采用投降政策","秦桧任宰相","岳飞被害","宋金和议《绍兴和约》","南宋偏安杭州","南宋不思北上中原","宋钦宗","宋高宗","岳飞","韩世忠","秦桧","杭州","燕云十六州","黄天荡"]
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
        return render(request, 'index.html')
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
        #     return render(request, 'index.html')
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
        #     return render(request, 'index.html')

def search(request):
    t = request.POST.get('title')
    names = ["靖康之变", "夏日绝句", "汴州","宋徽宗","满江红·写怀","示儿","菩萨蛮·书江西造口壁","诉衷情·当年万里觅封侯","书愤","秋夜将晓出篱门迎凉有感二首其二","病起书怀","相见欢·金陵城上西楼","贺新郎·送胡邦衡待制","蝶恋花·上巳召亲族","夜游宫·记梦寄师伯浑","十一月四日风雨大作·其二","添字丑奴儿·窗前谁种芭蕉树","题临安邸","念奴娇·登多景楼","念奴娇·炎精中否","声声慢·寻寻觅觅","长相思·惜梅","永遇乐·京口北固亭怀古","宋徽宗不理朝政","北宋联金攻辽","海上之盟","辽国灭亡","金国撕毁海上之盟","金国攻打北宋","徽钦二宗被掳","金军占领汴州","北宋灭亡","康王赵构南下继位宋高宗","南宋建立","金军南扑","宋军英勇反抗","宋高宗入海逃避","金军北撤","韩世忠围困金军","岳飞大败金军","宋金议和","金毁和约攻南宋","岳飞抗金","南宋采用投降政策","秦桧任宰相","岳飞被害","宋金和议《绍兴和约》","南宋偏安杭州","南宋不思北上中原","宋钦宗","宋高宗","岳飞","韩世忠","秦桧","杭州","燕云十六州","黄天荡"]
    dic = {}
    for name in names:
        dic[name] = fuzz.partial_ratio(name, t)
    print(dic)
    marks = sorted(dic.items(), key=lambda d:d[1], reverse=True)
    if marks[0][1] <= 20:
        pass
    else:
        for i in range(len(marks)):
            if marks[i][1] < 50:
                marks = marks[:i]
                break
        marks = dict(marks)
    return render(request, 'search.html', {'sea_list': marks})

def gushiciliebiao(request):
    return render(request, '古诗词列表.html')

def lishiliebiao(request):
    return render(request, '历史列表.html')

def jingkangzhibian(request):
    return render(request, '靖康之变.html')

def xiarijueju(request):
    return render(request, '夏日绝句.html')

def bianzhou(request):
    return render(request, '汴州.html')

def songhuizong(request):
    return render(request, '宋徽宗.html')

def manjianghongxiehuai(request):
    return render(request, '满江红·写怀.html')

def shier(request):
    return render(request, '示儿.html')

def pusamanshujiangxizaokoubi(request):
    return render(request, '菩萨蛮·书江西造口壁.html')

def suzhongqingdangnianwanlimifenghou(request):
    return render(request, '诉衷情·当年万里觅封侯.html')

def shufen(request):
    return render(request, '书愤.html')

def qiuyejiangxiaochulimenyingliangyouganqier(request):
    return render(request, '秋夜将晓出篱门迎凉有感二首其二.html')

def bingqishuhuai(request):
    return render(request, '病起书怀.html')

def xiangjianhuanjinlingchengshangxilou(request):
    return render(request, '相见欢·金陵城上西楼.html')

def hexinlangsonghubanghengdaizhi(request):
    return render(request, '贺新郎·送胡邦衡待制.html')

def dielianhuashangsizhaoqinzu(request):
    return render(request, '蝶恋花·上巳召亲族.html')

def yeyougongjimengjishibohun(request):
    return render(request, '夜游宫·记梦寄师伯浑.html')

def shiyiyuesirifengyudazuoqier(request):
    return render(request, '十一月四日风雨大作·其二.html')

def tianzichounuerchuangqianshuizhongbajiaoshu(request):
    return render(request, '添字丑奴儿·窗前谁种芭蕉树.html')

def tilinandi(request):
    return render(request, '题临安邸.html')

def nianujiaodengduojinglou(request):
    return render(request, '念奴娇·登多景楼.html')

def nianujiaoyanjingzhongfou(request):
    return render(request, '念奴娇·炎精中否.html')

def shenshenmanxunxunmimi(request):
    return render(request, '声声慢·寻寻觅觅.html')

def changxiangsiximei(request):
    return render(request, '长相思·惜梅.html')

def yongyulejingkoubeigutinghuaigu(request):
    return render(request, '永遇乐·京口北固亭怀古.html')

def songhuizongbulichaozheng(request):
    return render(request, '宋徽宗不理朝政.html')

def beisonglianjingongliao(request):
    return render(request, '北宋联金攻辽.html')

def haishangzhimeng(request):
    return render(request, '海上之盟.html')

def liaoguomiewang(request):
    return render(request, '辽国灭亡.html')

def jinguosihuihaishangzhimeng(request):
    return render(request, '金国撕毁海上之盟.html')

def jinguogongdabeisong(request):
    return render(request, '金国攻打北宋.html')

def huiqinerzongbeilu(request):
    return render(request, '徽钦二宗被掳.html')

def jinjunzhanlingbianzhou(request):
    return render(request, '金军占领汴州.html')

def beisongmiewang(request):
    return render(request, '北宋灭亡.html')

def kangwangzhaogounanxiajiweisonggaozong(request):
    return render(request, '康王赵构南下继位宋高宗.html')

def nansongjianli(request):
    return render(request, '南宋建立.html')

def jinjunnanpu(request):
    return render(request, '金军南扑.html')

def songjunyingyongfankang(request):
    return render(request, '宋军英勇反抗.html')

def songgaozongruhaitaobi(request):
    return render(request, '宋高宗入海逃避.html')

def jinjunbeiche(request):
    return render(request, '金军北撤.html')

def hanshizhongweikunjinjun(request):
    return render(request, '韩世忠围困金军.html')

def yuefeidabaijinjun(request):
    return render(request, '岳飞大败金军.html')

def songjinyihe(request):
    return render(request, '宋金议和.html')

def jinhuiheyuegongnansong(request):
    return render(request, '金毁和约攻南宋.html')

def yuefeikangjin(request):
    return render(request, '岳飞抗金.html')

def nansongcaiyongtouxiangzhence(request):
    return render(request, '南宋采用投降政策.html')

def qinhuirenzaixiang(request):
    return render(request, '秦桧任宰相.html')

def yuefeibeihai(request):
    return render(request, '岳飞被害.html')

def songjinyiheshaoxinheyue(request):
    return render(request, '宋金和议《绍兴和约》.html')

def nansongpiananhangzhou(request):
    return render(request, '南宋偏安杭州.html')

def nansongbusibeishangzhongyuan(request):
    return render(request, '南宋不思北上中原.html')

def songqinzong(request):
    return render(request, '宋钦宗.html')

def songgaozong(request):
    return render(request, '宋高宗.html')

def yuefei(request):
    return render(request, '岳飞.html')

def hanshizhong(request):
    return render(request, '韩世忠.html')

def qinhui(request):
    return render(request, '秦桧.html')

def hangzhou(request):
    return render(request, '杭州.html')

def yanyunshiliuzhou(request):
    return render(request, '燕云十六州.html')

def huangtiandang(request):
    return render(request, '黄天荡.html')

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


def test(request):
    if request.method == 'GET':
        poem = paper.objects.filter(Title="声声慢·寻寻觅觅").first()
        que = poem.selection_set.filter(Title2_id=poem.Id)
        return render(request, 'test.html', {'que': que, 'title': poem.Title})