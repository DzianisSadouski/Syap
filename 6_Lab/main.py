import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QRadioButton, QWidget, QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

class QuizApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.current_question = 0
        self.score = 0
        self.max_score = 0

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.question_label = QLabel(self.central_widget)
        self.option1_button = QRadioButton(self.central_widget)
        self.option2_button = QRadioButton(self.central_widget)
        self.option3_button = QRadioButton(self.central_widget)
        self.option4_button = QRadioButton(self.central_widget)
        self.submit_button = QPushButton('Ответить', self.central_widget)

        self.init_ui()
        self.load_question()

    def init_ui(self):
        layout = QVBoxLayout(self.central_widget)
        layout.addWidget(self.question_label)
        layout.addWidget(self.option1_button)
        layout.addWidget(self.option2_button)
        layout.addWidget(self.option3_button)
        layout.addWidget(self.option4_button)
        layout.addWidget(self.submit_button)

        self.submit_button.clicked.connect(self.check_answer)

    def load_question(self):
        # Load question from the database
        query = QSqlQuery()
        query.exec_("SELECT * FROM questions WHERE id = {}".format(self.current_question + 1))

        if query.next():
            question_text = query.value(1)
            options = [query.value(i) for i in range(2, 6)]
            correct_option = query.value(6)

            self.question_label.setText(question_text)
            self.option1_button.setText(options[0])
            self.option2_button.setText(options[1])
            self.option3_button.setText(options[2])
            self.option4_button.setText(options[3])

            self.correct_option = correct_option
            self.max_score += 1
        else:
            self.show_result()

    def check_answer(self):
        if self.option1_button.isChecked() and self.correct_option == 'option1':
            self.score += 1
        elif self.option2_button.isChecked() and self.correct_option == 'option2':
            self.score += 1
        elif self.option3_button.isChecked() and self.correct_option == 'option3':
            self.score += 1
        elif self.option4_button.isChecked() and self.correct_option == 'option4':
            self.score += 1

        self.current_question += 1
        self.load_question()

    def show_result(self):
        result_text = f"Опрос завершен!\nВаш счет: {self.score} из {self.max_score}"
        QMessageBox.information(self, "Результат опроса", result_text)
        sys.exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Connect to SQLite3 database
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('questions.db')
    if not db.open():
        QMessageBox.critical(None, "Ошибка", "Невозможно подключиться к базе данных")
        sys.exit()

    quiz_app = QuizApp()
    quiz_app.show()

    sys.exit(app.exec_())
