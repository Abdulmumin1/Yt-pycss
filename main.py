from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QFrame, QPushButton, QLabel
from PyQt5.QtCore import Qt
import random
from db import get_all_facts

class customFrame(QFrame):
    def __init__(self, fact):
        super().__init__()
        self.setStyleSheet('background:white; border-radius:10px; margin:15px;') 
        layout = QVBoxLayout()
        
        dyn_label = QLabel(text='Do you<br> know')
        dyn_label.setStyleSheet('font-size:40px; font-weight:bold;')
        dyn_label.setAlignment(Qt.AlignCenter)
        dyn_label.setWordWrap(True)
        self.content_label = QLabel(text=fact)
        self.content_label.setStyleSheet('font-size:20px;')
        self.content_label.setAlignment(Qt.AlignCenter)
        self.content_label.setWordWrap(True)
        layout.addWidget(dyn_label, alignment=Qt.AlignTop)
        layout.addStretch(0)
        layout.addWidget(self.content_label, alignment=Qt.AlignCenter)
        layout.addStretch(0)
        self.setLayout(layout)

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(350, 560)
        
        self.current_index = 0
        self.fact_list = get_all_facts()
        random.shuffle(self.fact_list)
        
        main_frame = QFrame() 
        button_layout = QHBoxLayout()
        main_layout = QVBoxLayout(main_frame)
        
        button_prev = self.create_button('←', self.prev_fact)
        button_next = self.create_button('→', self.next_fact)
        
        self.frame = customFrame(self.fact_list[self.current_index])
        button_layout.addWidget(button_prev, alignment=Qt.AlignLeft)
        button_layout.addWidget(button_next, alignment=Qt.AlignRight)

        main_layout.addWidget(self.frame)

        main_layout.addLayout(button_layout)
        self.change_color()
        self.setCentralWidget(main_frame)
    def create_button(self, name, func):
        button = QPushButton(text=name, clicked=func)
        button.setStyleSheet('font-size:25px; background:white; min-width:70px;'+ 
            'margin:0 15 0 15; font-weight:bold; border-radius:5px; padding-bottom:6px;')
        return button
    
    def next_fact(self): 
        if self.current_index < len(self.fact_list)-1:
            self.current_index += 1
            self.frame.content_label.setText(self.fact_list[self.current_index])
            self.change_color()
    
    def prev_fact(self):
        if self.current_index != -len(self.fact_list): 
            self.current_index -= 1
            self.frame.content_label.setText(self.fact_list[self.current_index])
            self.change_color()
    
    def change_color(self):
        red = random.randint(0,255)
        blue = random.randint(0,255)
        green = random.randint(0,255)

        color = f'rgb({red},{green},{blue})'
        self.setStyleSheet('background:{};'.format(color))

def main():
    app = QApplication([])
    win = Main()
    win.show()
    app.setStyle('fusion')
    app.exec_()

if __name__ == '__main__':
    main()

