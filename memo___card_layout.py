from PyQt5.QtWidgets import (QApplication, QVBoxLayout, QHBoxLayout, 
                             QPushButton, QSpinBox, QLabel, QGroupBox, QButtonGroup, QRadioButton)
from PyQt5.QtCore import Qt
app = QApplication([])

m_card_layout = QVBoxLayout()
card_layout1 = QHBoxLayout()
card1_layout = QHBoxLayout()
card1_layout1 = QHBoxLayout()
menu_btn = QPushButton("Menu")
rest_btn = QPushButton("Have a rest")

spinb = QSpinBox()
spinb.setValue(30)
# spinb.
# працюємо з першою горизонтальною лінією
card_layout1.addWidget(menu_btn)
card_layout1.addStretch(1)
card_layout1.addWidget(rest_btn)
card_layout1.addWidget(spinb)
card_layout1.addWidget(QLabel('хвилин'))
# 2 line
question_lb = QLabel('apple')
group_box = QGroupBox('Варіанти відповідей')
button_group = QButtonGroup()
rb_list = []
for i in range(4):
    r = QRadioButton(' ')
    rb_list.append(r)
    button_group.addButton(r)

gb_layout1 = QHBoxLayout()
gb_layout2 = QVBoxLayout()
gb_layout3 = QVBoxLayout()

gb_layout2.addWidget(rb_list[0])
gb_layout2.addWidget(rb_list[1])

gb_layout3.addWidget(rb_list[2])
gb_layout3.addWidget(rb_list[3])

gb_layout1.addLayout(gb_layout2)
gb_layout1.addLayout(gb_layout3)

group_box.setLayout(gb_layout1)
ok_btn = QPushButton('Відповісти')
card_layout2 = QHBoxLayout()
# ховаємо групбокс
group_box2 = QGroupBox('Результати теста:')
result_lb = QLabel('вірно\невірно')
answ_lb = QLabel('щось тут має бути')

box_line3 = QVBoxLayout()
box_line3.addWidget(result_lb, alignment=(Qt.AlignTop | Qt.AlignLeft))
box_line3.addStretch(1)
box_line3.addWidget(answ_lb, alignment=Qt.AlignCenter)
box_line3.addStretch(1)
group_box2.setLayout(box_line3)
#group_box.hide()
# росподіляю елементи на на вертікальному лайауті
# card1_layout1.addLayout(m_card_layout)
m_card_layout.addLayout(card_layout1, stretch=1)
m_card_layout.addWidget(question_lb, alignment=Qt.AlignCenter, stretch=1)
m_card_layout.addWidget(group_box, stretch=4)
m_card_layout.addWidget(group_box2, stretch=4)
m_card_layout.addWidget(ok_btn, stretch=1)
group_box2.hide()
#m_card_layout.addWidget()

def show_question():
    group_box.show()
    group_box2.hide()
    ok_btn.setText('Відповісти')
def show_results():
    group_box2.show()
    group_box.hide()
    ok_btn.setText('Наступне питання')
