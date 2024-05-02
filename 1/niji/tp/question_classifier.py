# -*- coding: utf-8 -*-
import os

import ahocorasick
import jieba
import mysql.connector


class QuestionClassifier:
    def __init__(self):
        # 　特征词路径
        self.author_path = os.path.join('tp/static/authors.txt')
        self.poem_path = os.path.join('tp/static/poems.txt')
        self.dynasty_path = os.path.join('tp/static/dynasties.txt')
        # 加载特征词
        self.author_wds = [i.strip() for i in open(self.author_path, encoding='utf-8') if i.strip()]
        self.poem_wds = [i.strip() for i in open(self.poem_path, encoding='utf-8') if i.strip()]
        self.dynasty_wds = [i.strip() for i in open(self.dynasty_path, encoding='utf-8') if i.strip()]
        '''
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="poems"
        )
        cursor = connection.cursor()
        # 加载特征词
        cursor.execute("SELECT DISTINCT name FROM lv_writing_authors")
        self.author_wds = [row[0] for row in cursor.fetchall()]
        print(1)

        cursor.execute("SELECT DISTINCT name FROM lv_writing_dynastys")
        self.dynasty_wds = [row[0] for row in cursor.fetchall()]
        print(1)

        cursor.execute("SELECT DISTINCT title FROM lv_writing_works")
        self.poem_wds = [row[0] for row in cursor.fetchall()]
        print(1)
        print(1)
        '''

        self.region_words = set(self.author_wds + self.poem_wds + self.dynasty_wds)

        # 构造领域actree
        self.region_tree = self.build_actree(list(self.region_words))

        # 构建词典
        self.wdtype_dict = self.build_wdtype_dict()

        # 疑问词
        self.create_qwds = ['创作', '写', '代表作', '创造', '创作了', '写了', '作品', '诗', '词', '曲', '歌']
        self.belongA_qwds = ['作者', '创作者', '谁写的', '哪位诗人的', '哪位作家的', '属于谁的']
        self.belongD_qwds = ['属于', '来自', '哪个朝代', '哪个年代的', '是哪个时代的', '在哪个时期的']
        self.Dhas_qwds = ['有哪些诗人', '包括哪些诗人', '出现过哪些诗人', '哪些诗人']
        self.poemContent_qwds = ['内容', '全文', '全诗', '原文', '内容是什么']
        self.poemIntro_qwds = ['讲解', '解释', '分析', '解析', '说明', '阐释', '讨论', '赏析', '意思', '含义', '诠释', '介绍', '表达', '蕴含']
        self.authorDesc_qwds = ['介绍', '是谁', '生平', '简介', '背景', '来历']

    def classify(self, question):
        data = {}
        medical_dict = self.check_question(question)
        if not medical_dict:
            return {}
        data['args'] = medical_dict
        # 收集问句当中所涉及到的实体类型
        types = []
        for t in medical_dict.values():
            types += t

        question_types = []

        if self.check_words(self.create_qwds, question) and ('author' in types):
            question_type = 'author_create'
            question_types.append(question_type)

        if self.check_words(self.belongA_qwds, question) and ('poem' in types):
            question_type = 'poem_belong'
            question_types.append(question_type)

        if self.check_words(self.belongD_qwds, question) and ('author' in types):
            question_type = 'author_belong'
            question_types.append(question_type)

        if self.check_words(self.Dhas_qwds, question) and ('dynasty' in types):
            question_type = 'dynasty_has'
            question_types.append(question_type)

        if self.check_words(self.poemContent_qwds, question) and ('poem' in types):
            question_type = 'poem_content'
            question_types.append(question_type)

        if self.check_words(self.poemIntro_qwds, question) and ('poem' in types):
            question_type = 'poem_intro'
            question_types.append(question_type)

        if self.check_words(self.authorDesc_qwds, question) and ('author' in types):
            question_type = 'author_desc'
            question_types.append(question_type)

        data['question_types'] = question_types
        return data

    def build_actree(self, wordlist):
        actree = ahocorasick.Automaton()
        for index, word in enumerate(wordlist):
            actree.add_word(word, (index, word))
        actree.make_automaton()
        return actree

    def build_wdtype_dict(self):
        wd_dict = dict()
        for wd in self.poem_wds:
            wd_dict[wd] = []
            wd_dict[wd].append('poem')
        for wd in self.author_wds:
            wd_dict[wd] = []
            wd_dict[wd].append('author')
        for wd in self.dynasty_wds:
            wd_dict[wd] = []
            wd_dict[wd].append('dynasty')
        return wd_dict

    def check_words(self, wds, sent):
        for wd in wds:
            if wd in sent:
                return True
        return False

    def check_question(self, question):
        region_wds = []
        '''
        question_words = jieba.cut(question)
        for qw in question_words:
            if qw in self.region_words:
                region_wds.append(qw)
        '''
        for i in self.region_tree.iter(question):
            wd = i[1][1]
            region_wds.append(wd)

        stop_wds = []
        for wd1 in region_wds:
            for wd2 in region_wds:
                if wd1 in wd2 and wd1 != wd2:
                    stop_wds.append(wd1)
        final_wds = [i for i in region_wds if i not in stop_wds]
        final_dict = {i: self.wdtype_dict.get(i) for i in final_wds}
        return final_dict


if __name__ == '__main__':
    handler = QuestionClassifier()
    while 1:
        question = input('input an question:')
        data = handler.classify(question)
        print(data)
