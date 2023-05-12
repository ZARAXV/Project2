from PyQt5.QtWidgets import *
from view import *
import random

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    happy_song = ['UGLY by Celeste Alison', 'Weirdo by More Fatter', 'Chemicals by SG Lewis']
    sad_song = ['Modus by Joji', 'Turning Tables by Adele', 'Call Out My Name by The Weeknd']
    anger_song = ['Plague Dr Mask II by Ghostemane', 'HDMI by BONES', 'Mount Sinai by $uicideboy$']
    calm_song = ['Wine pon you by Doja Cat', 'My love by Maye', 'Velvet Light by Jakob']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.button_intro.clicked.connect(lambda: self.begin_bttn())
        self.list_moods.itemDoubleClicked.connect(self.get_item)
        self.button_next.clicked.connect(lambda: self.next_bttn())

        self.list_moods.hide()
        self.label_question.hide()
        self.label_rec.hide()
        self.button_next.hide()

    def begin_bttn(self):
        happy, sad, anger, calm = 'Happiness', 'Sadness', 'Anger', 'Calm'
        self.list_moods.show()
        self.label_question.show()
        self.button_intro.hide()

        self.list_moods.addItems([happy, sad, anger, calm])

    def get_item(self, item):

        self.list_moods.hide()
        self.button_next.show()

        self.label_question.clear()
        self.label_question.setText(f'Based on what you chose: {item.text()}\n'
                                    f'YOU should listen to this')

        if item.text() == 'Happiness':
            random_happy = random.choice(Controller.happy_song)
            self.label_rec.show()
            self.label_rec.setText(f'{random_happy}')
        elif item.text() == 'Sadness':
            random_sad = random.choice(Controller.sad_song)
            self.label_rec.show()
            self.label_rec.setText(f'{random_sad}')
        elif item.text() == 'Anger':
            random_anger = random.choice(Controller.anger_song)
            self.label_rec.show()
            self.label_rec.setText(f'{random_anger}')
        else:
            random_calm = random.choice(Controller.calm_song)
            self.label_rec.show()
            self.label_rec.setText(f'{random_calm}')

    def next_bttn(self):
        self.label_question.clear()
        self.label_question.setText('How can songs change our emotions!')
        self.label_rec.clear()
        self.label_rec.setText('Songs have a great impact on us! Based on'
                               ' how we feel, songs can amplify those emotions')
        self.button_next.hide()

