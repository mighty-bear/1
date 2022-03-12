from django.db import models

class node(models.Model):
    NodeId=models.IntegerField(primary_key=True)
    NodeName=models.CharField(max_length=100, default='')
    PreEdgeId=models.IntegerField(default='')
    NextEdgeId=models.IntegerField(default='')

class edge(models.Model):
    EdgeId=models.IntegerField(primary_key=True)
    EdgeName=models.CharField(max_length=100, default='')

class chain(models.Model):
    ChainId=models.IntegerField(primary_key=True)
    Node1Id=models.IntegerField(default='')
    Node2Id=models.IntegerField(default='')
    EdgeId=models.IntegerField(default='')
    Node1IdName=models.CharField(max_length=100, default='')
    Node2IdName=models.CharField(max_length=100, default='')
    EdgeName=models.CharField(max_length=100, default='')

class t_node(models.Model):
    StNodeId=models.IntegerField(default='')
    EdNodeId=models.IntegerField(default='')
    StNodeName=models.CharField(default='',max_length=100)
    EdNodeName=models.CharField(default='',max_length=100)
    PoemName=models.CharField(primary_key=True,max_length=100, default='')

class relationship(models.Model):
    PoemId=models.IntegerField(default='')
    PoemSenId=models.IntegerField(primary_key=True)
    PoemName=models.CharField(default='', max_length=100)
    PoemSenName=models.CharField(default='', max_length=100)

class paper(models.Model):
    Id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=20, default='')

class selection(models.Model):
    Id = models.IntegerField(primary_key=True) # 主键
    Title2 = models.ForeignKey('paper', on_delete=models.CASCADE) # 诗歌部分
    Question = models.CharField(max_length=150, default='') # 问题
    A = models.CharField(max_length=100, default='')
    B = models.CharField(max_length=100, default='')
    C = models.CharField(max_length=100, default='')
    D = models.CharField(max_length=100, default='')
    Answer = models.CharField(max_length=2, default='')