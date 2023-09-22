
from PyQt5.QtWidgets import(
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QMenu
)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.__Init()

    def __Init(self):
        self.setFixedSize(500, 500)

        self.label_name = QLabel(self)
        self.label_lname = QLabel(self)
        self.label_phone = QLabel(self)
        self.edit_name = QLineEdit(self)
        self.edit_lname = QLineEdit(self)
        self.edit_phone = QLineEdit(self)
        self.btn_add = QPushButton(self)
        self.menu = QMenu(self)

        self.label_name.setText('First name')
        self.label_lname.setText('Last name')
        self.label_phone.setText('Phone number')
        self.btn_add.setText('Add new contact')

        self.label_name.move(50, 100)
        self.label_lname.move(50, 130)
        self.label_phone.move(50, 160)
        self.edit_name.move(150, 100)
        self.edit_lname.move(150, 130)
        self.edit_phone.move(170, 160)
        self.edit_phone.resize(120, 30)
        self.btn_add.move(50, 200)
        self.btn_add.resize(240, 30)
        self.btn_add.setStyleSheet("background-color: pink")


app = QApplication([])
win = Window()
win.show()
app.exec_()

