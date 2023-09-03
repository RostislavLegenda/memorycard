from random import shuffle, randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QGroupBox, QButtonGroup

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


def click_ok():
    if downbutton.text() == "Ответить":
        check_answer()
    else:
        next_question()

def next_question():
    ''' задает следующий вопрос из списка '''
    cur_question = randint(0, len(vopros_list)-1)
    ask(vopros_list[cur_question])
    main_win.total += 1
    


#функция одного правильного ответа
def ask(vopros: Question):
    
    box1.hide()
    
    rbtn_1.setText(vopros.right_answer)
    rbtn_2.setText(vopros.wrong1)
    rbtn_3.setText(vopros.wrong2)
    rbtn_4.setText(vopros.wrong3)

    shuffle(answers)
    line_Votvet1.addWidget(answers[0])
    line_Votvet2.addWidget(answers[1])
    line_Votvet1.addWidget(answers[2])
    line_Votvet2.addWidget(answers[3])

    RadioGroup.setExclusive(False)    #сброс флагов
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
    
    title.setText(vopros.question)
    true.setText(vopros.right_answer)
    RadioGroupBox.show()
    downbutton.setText('Ответить')


    

def check_answer():
    ans_correct = 'Верно'
    ans_wrong = 'Не верно'
    ans_miss = 'Не выбран вариант ответа'

    if rbtn_1.isChecked():
        show_correct(ans_correct)
        main_win.score += 1

    elif rbtn_2.isChecked() or rbtn_3.isChecked() or rbtn_4.isChecked():
        show_correct(ans_wrong)
    else:
        show_correct(ans_miss)
    print('Статистика')
    print('-Всего вопросов', main_win.total)
    print('-Правильных ответов', main_win.score)
    print('Рейтинг:', int(main_win.score/main_win.total*100),'%')
    


def show_correct(ans_correct):
    RadioGroupBox.hide()
    box1.hide()
    yes_no.setText(ans_correct)
    downbutton.setText('Следующий вопрос')
    box1.show()
    




app = QApplication([])
main_win = QWidget()
main_win.resize(400, 200)
main_win.setWindowTitle('Memory Card')
RadioGroupBox = QGroupBox('Варианты ответов')
RadioGroup = QButtonGroup()

title = QLabel('Какой национальности не существует?')


rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Чулымцы')
rbtn_3 = QRadioButton('Смурфы')
rbtn_4 = QRadioButton('Алеуты')
downbutton = QPushButton('Ответить')
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


#список ответов
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]




line_Votvet1 = QVBoxLayout()
line_Votvet2 = QVBoxLayout()
line_central = QHBoxLayout()

line_Votvet1.addWidget(rbtn_1)
line_Votvet2.addWidget(rbtn_2)
line_Votvet1.addWidget(rbtn_3)
line_Votvet2.addWidget(rbtn_4)

line_central.addLayout(line_Votvet1)
line_central.addLayout(line_Votvet2)
RadioGroupBox.setLayout(line_central)

#создание направляющих по х и y
line_text = QHBoxLayout()
line_button = QHBoxLayout()
line_Vcentral = QVBoxLayout()

box1 = QGroupBox('Результат теста')
yes_no = QLabel('Правильно/Неправильно')
true = QLabel('Правильный ответ')

line_ansV = QVBoxLayout()
line_ansV.addWidget(yes_no, alignment= Qt.AlignCenter)
line_ansV.addWidget(true, alignment= Qt.AlignCenter)


box1.setLayout(line_ansV)
line_text.addWidget(title, alignment = Qt.AlignCenter)
line_button.addWidget(downbutton, stretch= 6)
line_Vcentral.addLayout(line_text)
line_Vcentral.addWidget(RadioGroupBox)
line_Vcentral.addWidget(box1)
line_Vcentral.addLayout(line_button)



main_win.setLayout(line_Vcentral)
main_win.cur_question = -1

vopros_list = []
vopros_list.append(Question('Выберите перевод слова "переменная"', 'variable', 'variation', 'changing', 'variant'))
vopros_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Японский', 'Питон', 'Итальянский'))
vopros_list.append(Question('Сколько сфер у инвокера?', 'Три', 'Две', 'Одна', 'Четыре'))
vopros_list.append(Question('Sunstrike?', 'EEE', 'QWE', 'WWW', 'EEQ'))
main_win.cur_question = -1
downbutton.clicked.connect(click_ok)
main_win.total = 0
main_win.score = 0
next_question()

#показ и запуск программы

main_win.show()

app.exec_()