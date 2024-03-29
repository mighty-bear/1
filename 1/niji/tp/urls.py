from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers

from tp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),
    path('index/', views.index),
    path('古诗词列表/', views.gushiciliebiao),
    path('古建筑历史列表/', views.lishiliebiao),
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
    path('岳阳楼主要建筑/', views.YueYangLouZhuYaoJianZhu),
    path('岳阳楼历史沿革图谱/', views.YueYangLouLiShiYanGeTuPu),
    path('岳阳楼相关诗文/', views.YueYangLouXiangGuanShiWen),
    path('历史列表/', views.LiShiLieBiao),
    path('十一月四日风雨大作/', views.ShiYiYueSiRiFengYuDaZuo),
    path('玉门关/', views.YuMenGuan),
    path('tpshow/', views.tpshow)
]
