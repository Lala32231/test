class Question:
    def __init__(self, question, right, wrong1, wrong2, wrong3):
        self.right = right
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
        self.question = question
    def show_quest(self, q_lb, rb_list):
        q_lb.setText(self.question)
        rb_list[0].setText(self.right)
        rb_list[1].setText(self.wrong1)
        rb_list[2].setText(self.wrong2)
        rb_list[3].setText(self.wrong3)
    def show_res(self, r_lb, answ_lb, rb_list):
        if rb_list[0].isChecked():
            r_lb.setText('Вірно')
        else:
            r_lb.setText('Не вірно')
        answ_lb.setText(self.right)

q1 = Question("яке ім'я у бориса", "максим", "апле", "барбарис", "ніяке")
q2 = Question('переклад = привіт', '4', 'こんにちわ', 'きださい', 'ください')
q3 = Question('переклад = ひと', 'люди', 'а?', 'людина', 'вона')
q4 = Question('переклад = すし', 'суши', 'шо', 'роли', 'борис')
q5 = Question('переклад = これ　わ　りんご　です', 'це яблуко', 'це груша', 'апле', 'то яблуко')
q6 = Question('переклад = わたし は アメリカ人です', 'я американець', 'я є амариканець', 'ми британці', 'шо')
q7 = Question('переклад = я Кен, приемно познайомитися', 'けんですどぞよろしく', 'ですけんどそよろしく', 'わちしけん', 'じゃねえ！')
q8 = Question('こにちわ', 'こにちわ！', 'じゃねえ。', 'はい', 'なに?')
q9 = Question('これわおいしカレーです', 'いいえ！', 'それわラーメンです', 'にほん', 'みず')
q10 = Question('виберіть првильно записане речення　（доброго вечора, я наомі)', 'こんばんわなおみです', 'こんばんうなおま', 'こんばんわなおみ', 'ですこんばんわなおみ')
q_list = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]