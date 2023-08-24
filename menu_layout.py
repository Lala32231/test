from PyQt5.QtWidgets import (QPushButton, QVBoxLayout, QWidget)
from PyQt5.QtCore import Qt

menu_layout = QVBoxLayout()
test_btn = QPushButton('Розпочати тестування')
learn_btn = QPushButton('Розпочати навчання')
menu_layout.addWidget(test_btn)
win_card = QWidget()
menu_layout.addWidget(learn_btn)
card_width, card_height = 600, 500


