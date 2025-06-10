from instr import *
from final_win import *
from PyQt5.QtCore import Qt, QTimer, QTime

# добавить импорты
from PyQt5.QtGui import QFont 
from PyQt5.QtWidgets import ( QWidget, QHBoxLayout, QVBoxLayout, 
                            QPushButton, QLabel, QLineEdit)

class Experiment():
    def __init__(self, age, test1, test2, test3):
        self.age = age
        self.t1 = test1
        self.t2 = test2
        self.t3 = test3

class TestWin(QWidget):
    def __init__(self):
        super().__init__() 
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width,win_height) 
        self.move(win_x,win_y)
        
    def initUI(self):
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()

        self.text1 = QLabel(txt_name) # замени переменную # text_name
        self.text2 = QLabel(txt_age) # text_age
        self.text3 = QLabel(txt_test1) # text_test1
        self.text4 = QLabel(txt_test2) # text_test2
        self.text5 = QLabel(txt_test3) # text_test3
        self.text6 = QLabel(txt_timer) # text_timer

        self.button1 = QPushButton(txt_starttest1) # btn_test1
        self.button2 = QPushButton(txt_starttest2) # btn_test2
        self.button3 = QPushButton(txt_starttest3) # btn_test3

        self.button4 = QPushButton(txt_sendresults) # btn_next

        self.line1 = QLineEdit() # line_name
        self.line2 = QLineEdit() # line_age
        self.line3 = QLineEdit() # line_test1
        self.line4 = QLineEdit() # line_test2
        self.line5 = QLineEdit() # line_test3

        # дполнительно для красоты
        self.line1.setPlaceholderText(txt_hintname)
        self.line2.setPlaceholderText(txt_hintage)
        self.line3.setPlaceholderText(txt_hinttest1)
        self.line4.setPlaceholderText(txt_hinttest2)
        self.line5.setPlaceholderText(txt_hinttest3)

        # добавить выравнивание
        self.l_line.addWidget(self.text1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.button1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line3, alignment = Qt.AlignLeft)
        # добавить
        self.l_line.addWidget(self.text4, alignment = Qt.AlignLeft)

        self.l_line.addWidget(self.button2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text5, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.button3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line4, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line5, alignment = Qt.AlignLeft)
        # добавить 
        self.l_line.addWidget(self.button4, alignment = Qt.AlignCenter)


        self.r_line.addWidget(self.text6, alignment = Qt.AlignCenter)

        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        
        self.setLayout(self.h_line)
    
    def next_click(self):
        self.hide()
        self.exp = Experiment(self.line2.text(), self.line3.text(), self.line4.text(), self.line5.text())
        self.tw = Finalwin(self.exp)

    def connects(self):
        self.button4.clicked.connect(self.next_click)
        self.button1.clicked.connect(self.timer_test)
        self.button2.clicked.connect(self.timer_sits)
        self.button3.clicked.connect(self.timer_final)
    def timer_test(self):
        global time
        time = QTime(0, 0, 16)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text6.setText(time.toString('hh:mm:ss'))
        self.text6.setFont(QFont('Times', 36, QFont.Bold))
        self.text6.setStyleSheet('color: rgb(0,0,0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()
    def timer_sits(self):
        global time
        time = QTime(0, 0, 31)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text6.setText(time.toString('hh:mm:ss')[6:8])
        self.text6.setFont(QFont('Times', 36, QFont.Bold))
        self.text6.setStyleSheet('color: rgb(0,0,0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()
    def timer_final(self):
        global time
        time = QTime(0, 1, 1)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)
    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text6.setText(time.toString('hh:mm:ss'))
        if int(time.toString('hh:mm:ss')[6:8]) >= 45:
            self.text6.setStyleSheet('color: rgb(0,255,0)')
        elif int(time.toString('hh:mm:ss')[6:8]) <= 15:
            self.text6.setStyleSheet('color: rgb(0,255,0)')
        else:
            self.text6.setStyleSheet('color: rgb(0,0,0)')
        self.text6.setFont(QFont('Times', 36, QFont.Bold))
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()