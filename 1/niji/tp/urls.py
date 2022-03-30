from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers

from tp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),
    path('index/', views.index),
    path('靖康之变/', views.jingkangzhibian),
    path('夏日绝句/', views.xiarijueju),
    path('汴州/', views.bianzhou),
    path('宋徽宗/', views.songhuizong),
    path('古诗词列表/', views.gushiciliebiao),
    path('历史列表/', views.lishiliebiao),
    path('满江红·写怀/', views.manjianghongxiehuai),
    path('示儿/', views.shier),
    path('菩萨蛮·书江西造口壁/', views.pusamanshujiangxizaokoubi),
    path('诉衷情·当年万里觅封侯/', views.suzhongqingdangnianwanlimifenghou),
    path('书愤/', views.shufen),
    path('秋夜将晓出篱门迎凉有感二首其二/', views.qiuyejiangxiaochulimenyingliangyouganqier),
    path('病起书怀/', views.bingqishuhuai),
    path('相见欢·金陵城上西楼/', views.xiangjianhuanjinlingchengshangxilou),
    path('贺新郎·送胡邦衡待制/', views.hexinlangsonghubanghengdaizhi),
    path('蝶恋花·上巳召亲族/', views.dielianhuashangsizhaoqinzu),
    path('夜游宫·记梦寄师伯浑/', views.yeyougongjimengjishibohun),
    path('十一月四日风雨大作·其二/', views.shiyiyuesirifengyudazuoqier),
    path('添字丑奴儿·窗前谁种芭蕉树/', views.tianzichounuerchuangqianshuizhongbajiaoshu),
    path('题临安邸/', views.tilinandi),
    path('念奴娇·登多景楼/', views.nianujiaodengduojinglou),
    path('念奴娇·炎精中否/', views.nianujiaoyanjingzhongfou),
    path('声声慢·寻寻觅觅/', views.shenshenmanxunxunmimi),
    path('长相思·惜梅/', views.changxiangsiximei),
    path('永遇乐·京口北固亭怀古/', views.yongyulejingkoubeigutinghuaigu),
    path('宋徽宗不理朝政/', views.songhuizongbulichaozheng),
    path('北宋联金攻辽/', views.beisonglianjingongliao),
    path('海上之盟/', views.haishangzhimeng),
    path('辽国灭亡/', views.liaoguomiewang),
    path('金国撕毁海上之盟/', views.jinguosihuihaishangzhimeng),
    path('金国攻打北宋/', views.jinguogongdabeisong),
    path('徽钦二宗被掳/', views.huiqinerzongbeilu),
    path('金军占领汴州/', views.jinjunzhanlingbianzhou),
    path('北宋灭亡/', views.beisongmiewang),
    path('康王赵构南下继位宋高宗/', views.kangwangzhaogounanxiajiweisonggaozong),
    path('南宋建立/', views.nansongjianli),
    path('金军南扑/', views.jinjunnanpu),
    path('宋军英勇反抗/', views.songjunyingyongfankang),
    path('宋高宗入海逃避/', views.songgaozongruhaitaobi),
    path('金军北撤/', views.jinjunbeiche),
    path('韩世忠围困金军/', views.hanshizhongweikunjinjun),
    path('岳飞大败金军/', views.yuefeidabaijinjun),
    path('宋金议和/', views.songjinyihe),
    path('金毁和约攻南宋/', views.jinhuiheyuegongnansong),
    path('岳飞抗金/', views.yuefeikangjin),
    path('南宋采用投降政策/', views.nansongcaiyongtouxiangzhence),
    path('秦桧任宰相/', views.qinhuirenzaixiang),
    path('岳飞被害/', views.yuefeibeihai),
    path('宋金和议《绍兴和约》/', views.songjinyiheshaoxinheyue),
    path('南宋偏安杭州/', views.nansongpiananhangzhou),
    path('南宋不思北上中原/', views.nansongbusibeishangzhongyuan),
    path('宋钦宗/', views.songqinzong),
    path('宋高宗/', views.songgaozong),
    path('岳飞/', views.yuefei),
    path('韩世忠/', views.hanshizhong),
    path('秦桧/', views.qinhui),
    path('杭州/', views.hangzhou),
    path('燕云十六州/', views.yanyunshiliuzhou),
    path('黄天荡/', views.huangtiandang),
    path('声声慢·寻寻觅觅/test/', views.test),
    path('search', views.search),
    # new
    path('1/', views.One),
    path('2/', views.Two),
    path('3/', views.Three),
    path('4/', views.Four),
    path('5/', views.Five),
    path('6/', views.Six),
    path('7/', views.Seven),
    path('8/', views.Eight),
    path('9/', views.Nine),
    path('10/', views.Ten),
    path('11/', views.Eleven),
    path('12/', views.Twelve),
    path('13/', views.Thirteen),
    path('14/', views.Fourteen),
    path('15/', views.Fifteen),
    path('16/', views.Sixteen),
    path('17/', views.Seventeen),
    path('18/', views.Eighteen),
    path('19/', views.Nineteen),
    path('20/', views.Twenty),
    path('题岳阳楼/', views.TiYueYangLou),
    path('雨中登岳阳楼望君山/', views.YuZhongDengYueYangLouWangJunShan),
    path('岳阳楼/', views.YueYangLou),
    path('与夏十二登岳阳楼/', views.YuXiaShiErDengYueYangLou),
    path('游岳阳楼记/', views.YouYueYangLouJi),
    path('岳阳楼记/', views.YueYangLouJi),
    path('泊岳阳城下/', views.BoYueYangChengXia),
    path('登岳阳楼/', views.DengYueYangLou),
    path('岳阳楼历史沿革/', views.YueYangLouLiShiYanGe),
    path('岳阳楼建筑格局/', views.YueYangLouJianZhuGeJu),
    path('岳阳楼主要建筑/', views.YueYangLouZhuYaoJianZhu)
]
