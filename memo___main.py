from memo___card_layout import *
from PyQt5.QtWidgets import QWidget
from random import shuffle # будем перемешивать ответы в карточке вопроса
from data import *
from random import shuffle
from menu_layout import *
shuffle(q_list)
quest_num = 0
q_list[quest_num].show_quest(question_lb, rb_list)
quest_num += 1
# app = QApplication([])
def ok_click():
    global quest_num
    if ok_btn.text() == 'Відповісти':
        q_list[quest_num].show_res(result_lb, answ_lb, rb_list)
        show_results()
        quest_num +=1
    else:
        q_list[quest_num].show_res(result_lb, answ_lb, rb_list)
        show_question()
def start_study():
    list_widget.clear()
    for item in q_list:
        list_widget.addItemm(q_list[0].question)
    window_study.show()
    window_menu.hide()

def test_click():
    #print('ви натиснули кнопку!!!')
    win_card.show()
    win_menu.hide()
def menu_click():
    win_test


card_width, card_height = 300, 400
# начальные размеры окна "карточка"
win_menu = QWidget()
win_menu.resize(300, 400)
win_menu.setWindowTitle('menu')
win_menu.show()
win_menu.setLayout(menu_layout)

card_width, card_height = 300, 400 
win_card = QWidget()
win_card.resize(600, 500)
win_card.setWindowTitle('Питання')
#win_card.show()
win_card.setLayout(m_card_layout)
# card_layout2 = QHBoxLayout()
ok_btn.clicked.connect(ok_click)
test_btn.clicked.connect(test_click)
menu_btn.clicked.connect(menu_click)
#learn_btn.clicked.connect()
app.exec_()