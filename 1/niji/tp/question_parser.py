class QuestionParser:
    def parser_main(self, res_classify):
        args = res_classify['args']
        entity_dict = self.build_entitydict(args)
        question_types = res_classify['question_types']
        sqls = []
        for question_type in question_types:
            sql_ = {}
            sql_['question_type'] = question_type
            sql = []
            if question_type == 'author_create':
                sql = self.sql_transfer(question_type, entity_dict.get('author'))

            elif question_type == 'poem_belong':
                sql = self.sql_transfer(question_type, entity_dict.get('poem'))

            elif question_type == 'author_belong':
                sql = self.sql_transfer(question_type, entity_dict.get('author'))

            elif question_type == 'dynasty_has':
                sql = self.sql_transfer(question_type, entity_dict.get('dynasty'))

            if sql:
                sql_['sql'] = sql

                sqls.append(sql_)

        return sqls

    def sql_transfer(self, question_type, entities):
        if not entities:
            return []

        # ²éÑ¯Óï¾ä
        sql = []

        if question_type == 'author_create':
            sql = [
                "MATCH (m:Disease)-[r:has_symptom]->(n:Symptom) where n.name = '{0}' return m.name, r.name, n.name".format(
                    i) for i in entities]

        elif question_type == 'poem_belong':
            pass

        elif question_type == 'author_belong':
            pass

        elif question_type == 'dynasty_has':
            pass