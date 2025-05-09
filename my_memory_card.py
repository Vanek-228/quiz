from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QGroupBox, QPushButton, QButtonGroup
from random import shuffle, randint


class Question():
    def __init__(self, question ,right_ans, wrong1, wrong2, wrong3):
        self.right_ans = right_ans
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
        self.question = question


def show_qustion():
    ''' Прячет группу с результатами и показывает группу с ответами'''
    group1.hide()
    group.show()
    button5.setText('Ответить')
    q_group.setExclusive(False)
    button1.setChecked(False)
    button2.setChecked(False)
    button3.setChecked(False)
    button4.setChecked(False)
    q_group.setExclusive(True)


def show_answer():
    ''' Прячет группу с ответами и показывает группу с результатами'''
    group.hide()
    group1.show()
    button5.setText('Следующий вопрос')


def ask(question_: Question):
    ''' Перемешивает кнопки в списке, распологает надписи в нужных виджетах'''
    shuffle(answers)
    answers[0].setText(question_.right_ans)
    answers[1].setText(question_.wrong1)
    answers[2].setText(question_.wrong2)
    answers[3].setText(question_.wrong3)
    which.setText(question_.question)
    label2.setText(question_.right_ans)
    show_qustion()


def check_answer():
    ''' проверяет ответ пользователя на правильность'''
    if answers[0].isChecked():
        main_win.score += 1
        show_correct('Правильно')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неправильно')
    print('\nСтатистика\n-Всего вопросов:', main_win.total, '\nПравильных ответов:', main_win.score)
    print('Рейтинг:', round((main_win.score / main_win.total) * 100, 2), '%')


def show_correct(result):
    ''' Показывает результаты ответов на вопрос'''
    label1.setText(result)
    show_answer()


def next_question():
    ''' Перемешает между вопросами'''
    main_win.total += 1
    counter = randint(0, len(questions) - 1)
    questions_ = questions[counter]
    print('\nСтатистика\n-Всего вопросов:', main_win.total, '\nПравильных ответов:', main_win.score)
    ask(questions_)


def click_ok():
    ''' Вызывает нужную функцию в зависимости от названия кнопки'''
    if button5.text() == 'Ответить':
        check_answer()
    else:
        next_question()


app = QApplication([])
main_win = QWidget()    
main_win.setWindowTitle('Memory Card')
main_win.resize(400, 300)

main_win.total = 0
main_win.score = 0
which = QLabel('Какой национальности не существует?')
button1 = QRadioButton('Энцы')
button2 = QRadioButton('Смурфы')
button3 = QRadioButton('чулмынцы')
button4 = QRadioButton('Алеуты')
answers = [button1, button2, button3, button4]
group = QGroupBox('Варианты ответов')
button5 = QPushButton('Ответить')
label1 = QLabel('Правильно/Неправильно')
label2 = QLabel('Правильный ответ')
group1 = QGroupBox('Результат теста')
q_group = QButtonGroup()
q_group.addButton(button1)
q_group.addButton(button2)
q_group.addButton(button3)
q_group.addButton(button4)

v4_line = QVBoxLayout()
v4_line.addWidget(label1, alignment = (Qt.AlignLeft | Qt.AlignTop))
v4_line.addWidget(label2, alignment = Qt.AlignHCenter, stretch = 2)
group1.setLayout(v4_line)

h_line = QHBoxLayout()
v1_line = QVBoxLayout()
v2_line = QVBoxLayout()
h1_line = QHBoxLayout()
h2_line = QHBoxLayout()
v3_line = QVBoxLayout()
h3_line = QHBoxLayout()

v1_line.addWidget(button1)
v1_line.addWidget(button2)
v2_line.addWidget(button3)
v2_line.addWidget(button4)
h1_line.addWidget(which, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
h2_line.addStretch(1)
h2_line.addWidget(button5, stretch = 2)
h2_line.addStretch(1)
h_line.addLayout(v1_line)
h_line.addLayout(v2_line)
group.setLayout(h_line)
h3_line.addWidget(group)
h3_line.addWidget(group1)
group1.hide()    

v3_line.addLayout(h1_line, stretch = 2)
v3_line.addLayout(h3_line, stretch = 8)
v3_line.addStretch(1)
v3_line.addLayout(h2_line, stretch = 1)
v3_line.addStretch(1)
v3_line.setSpacing(5)
main_win.setLayout(v3_line)


language = Question('Государственный язык Бразилии', 'Португальский', 'Итальянский', 'Испанский', 'Бразильский')
how_many = Question('Сколько хромосом у человека', '46 хромосом', '48 хромосом', '23 пары', '52 хромосомы')
game = Question('выберите программу не являющейся игрой', 'Steam', 'Stardew Valley', 'Roblox', 'Don"t Starve Together')
version = Question('Какая самая последняя версия майнкрафта', '1.21.4', '1.12.2', '1.21.6', '1.20.1')
letter = Question('Сколько букв в алфавите', '33', '32', '31', '26')

questions = [language, how_many, game, version, letter]

next_question()
button5.clicked.connect(click_ok)

main_win.show()
app.exec_()