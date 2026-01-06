# -*- coding: utf_8 -*-
import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QTimer

class MathGame(QWidget):
    def __init__(self):
        super().__init__()
        self.n1 = 0
        self.n2 = 0
        self.correct_answer = 0  # We store the exact answer here immediately
        self.score = 0
        self.mode = "add" 
        
        self.setWindowTitle("🌈 Magic Math Adventure")
        self.setMinimumSize(800, 750)
        self.setStyleSheet("background-color: #F0F4F8;")
        
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(30, 20, 30, 20)
        self.setLayout(self.main_layout)
        
        # UI Header (Score & Progress)
        self.score_card = QLabel("STARS: 0 ⭐")
        self.score_card.setFixedSize(220, 60)
        self.score_card.setAlignment(Qt.AlignCenter)
        self.score_card.setStyleSheet("""
            background-color: #FFD700; color: #5D4037; font-size: 24px; 
            font-weight: bold; border-radius: 30px; border: 3px solid #FBC02D;
        """)
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setMaximum(10)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setStyleSheet("""
            QProgressBar { border: 2px solid #D1D9E6; border-radius: 10px; background: white; height: 20px; }
            QProgressBar::chunk { background-color: #6BCB77; border-radius: 8px; }
        """)

        header = QHBoxLayout()
        header.addWidget(self.score_card)
        header.addStretch()
        header.addWidget(QLabel("Goal: 10 Stars 🏆"))
        self.main_layout.addLayout(header)
        self.main_layout.addWidget(self.progress_bar)

        self.card = QStackedWidget() 
        self.main_layout.addWidget(self.card)
        
        # Game UI Setup
        self.game_widget = QWidget()
        self.game_layout = QGridLayout(self.game_widget)
        self.game_widget.setStyleSheet("background-color: white; border-radius: 40px; border: 2px solid #D1D9E6;")
        self.card.addWidget(self.game_widget)
        
        # Win Screen Setup
        self.win_widget = QWidget()
        self.win_layout = QVBoxLayout(self.win_widget)
        self.win_widget.setStyleSheet("background-color: #FFF9C4; border-radius: 40px;")
        
        win_title = QLabel("YOU ARE A CHAMPION!")
        win_title.setFont(QFont("Comic Sans MS", 36, QFont.Bold))
        win_title.setAlignment(Qt.AlignCenter)
        win_title.setStyleSheet("color: #F57C00; border: none;")
        
        self.trophy_label = QLabel("🏆")
        self.trophy_label.setFont(QFont("Arial", 100))
        self.trophy_label.setAlignment(Qt.AlignCenter)
        self.trophy_label.setStyleSheet("border: none;")

        restart_btn = QPushButton("PLAY AGAIN! ✨")
        restart_btn.setFixedSize(300, 80)
        restart_btn.setStyleSheet("background-color: #4A90E2; color: white; font-size: 24px; border-radius: 40px; font-weight: bold;")
        restart_btn.clicked.connect(self.reset_game)

        self.win_layout.addStretch()
        self.win_layout.addWidget(win_title)
        self.win_layout.addWidget(self.trophy_label)
        self.win_layout.addWidget(restart_btn, 0, Qt.AlignCenter)
        self.win_layout.addStretch()
        self.card.addWidget(self.win_widget)

        self.setup_menu()
        self.new_question()

    def setup_menu(self):
        menubar = QMenuBar()
        self.main_layout.setMenuBar(menubar)
        game_menu = menubar.addMenu("🎯 Modes")
        game_menu.addAction("Adding").triggered.connect(lambda: self.set_mode("add"))
        game_menu.addAction("Taking Away").triggered.connect(lambda: self.set_mode("subt"))

    def set_mode(self, mode):
        self.mode = mode
        self.reset_game()

    def reset_game(self):
        self.score = 0
        self.update_ui()
        self.card.setCurrentIndex(0)
        self.new_question()

    def update_ui(self):
        self.score_card.setText(f"STARS: {self.score} ⭐")
        self.progress_bar.setValue(self.score)

    def new_question(self):
        # Clear previous question
        while self.game_layout.count():
            item = self.game_layout.takeAt(0)
            if item.widget(): item.widget().deleteLater()
        
        if self.mode == "add":
            self.n1 = random.randint(1, 9)
            self.n2 = random.randint(1, 9)
            self.correct_answer = self.n1 + self.n2 # Fix: Store answer here
            symbol, icon = "+", "img/apple.jpg"
        else:
            self.n1 = random.randint(2, 9)
            self.n2 = random.randint(1, self.n1 - 1) 
            self.correct_answer = self.n1 - self.n2 # Fix: Store answer here
            symbol, icon = "-", "img/fish.png"

        # Big Equation Display
        eq = QLabel(f"{self.n1} {symbol} {self.n2} = ?")
        eq.setFont(QFont("Comic Sans MS", 50, QFont.Bold))
        eq.setStyleSheet("border: none; color: #2C3E50;")
        self.game_layout.addWidget(eq, 0, 0, 1, 10, Qt.AlignCenter)

        # Visual Row 1
        self.draw_icons(self.n1, icon, 1)
        
        # Operator Row
        sep = QLabel(symbol)
        sep.setFont(QFont("Arial", 40))
        sep.setStyleSheet("border: none; color: #BDC3C7;")
        self.game_layout.addWidget(sep, 2, 0, 1, 10, Qt.AlignCenter)
        
        # Visual Row 2
        self.draw_icons(self.n2, icon, 3)

        # User Answer Input
        self.ans_input = QLineEdit()
        self.ans_input.setFixedSize(120, 100)
        self.ans_input.setFont(QFont("Arial", 40, QFont.Bold))
        self.ans_input.setAlignment(Qt.AlignCenter)
        self.ans_input.setStyleSheet("border: 4px solid #4A90E2; border-radius: 20px; background: #F9FBFF;")
        
        btn = QPushButton("GO!")
        btn.setFixedSize(150, 100)
        btn.setStyleSheet("background-color: #6BCB77; color: white; font-size: 28px; border-radius: 25px; font-weight: bold;")
        btn.clicked.connect(self.check_answer)
        
        self.game_layout.addWidget(self.ans_input, 5, 4, 1, 1, Qt.AlignRight)
        self.game_layout.addWidget(btn, 5, 5, 1, 1, Qt.AlignLeft)
        
        self.feedback = QLabel("")
        self.feedback.setStyleSheet("border: none;")
        self.game_layout.addWidget(self.feedback, 6, 0, 1, 10, Qt.AlignCenter)

    def draw_icons(self, count, path, row):
        container = QWidget()
        container.setStyleSheet("border: none; background: transparent;")
        lay = QHBoxLayout(container)
        pix = QPixmap(path).scaled(55, 55, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        for _ in range(count):
            lbl = QLabel(); lbl.setPixmap(pix); lbl.setStyleSheet("border: none;")
            lay.addWidget(lbl)
        self.game_layout.addWidget(container, row, 0, 1, 10, Qt.AlignCenter)

    def check_answer(self):
        try:
            # We compare directly to self.correct_answer calculated in new_question
            user_val = int(self.ans_input.text())
            
            if user_val == self.correct_answer:
                self.score += 1
                self.update_ui()
                self.feedback.setPixmap(QPixmap("img/checked.png").scaledToWidth(120, Qt.SmoothTransformation))
                
                if self.score >= 10:
                    QTimer.singleShot(1000, lambda: self.card.setCurrentIndex(1))
                else:
                    QTimer.singleShot(1500, self.new_question)
            else:
                self.feedback.setPixmap(QPixmap("img/error.png").scaledToWidth(100))
                self.ans_input.clear()
        except ValueError:
            pass # Handle empty or non-numeric input

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MathGame()
    ex.show()
    sys.exit(app.exec_())
