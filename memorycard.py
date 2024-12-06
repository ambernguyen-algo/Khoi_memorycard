#create a memory card application
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

app = QApplication([]) 

window = QWidget()
window.setWindowTitle('Memory Card')

lb_Question = QLabel('The most difficult questions in the world')

#create radio group box for 4 radio buttons
radio_groupbox = QGroupBox('Answer options')

#create 4 radio buttons
rbtn_1 = QRadioButton('Option 1')
rbtn_2 = QRadioButton('Option 2')
rbtn_3 = QRadioButton('Option 3')
rbtn_4 = QRadioButton('Option 4')

#Create button for answering
btn_answer = QPushButton('Answer')

#Create group for 4 radio buttons 
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)



window.show()
app.exec_()
