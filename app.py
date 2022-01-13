# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import gevent
import webbrowser
import os
import sys
from PySide2.QtWidgets import QWidget, QApplication
from locust.env import Environment
from locust.stats import stats_printer, stats_history
from locust import HttpUser, between, task


class Ui_Gui(object):
    def setupUi(self, Gui):
        if not Gui.objectName():
            Gui.setObjectName(u"Gui")
        Gui.resize(500, 200)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Gui.sizePolicy().hasHeightForWidth())
        Gui.setSizePolicy(sizePolicy)
        Gui.setMinimumSize(QSize(500, 200))
        Gui.setMaximumSize(QSize(500, 200))
        Gui.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0454545 rgba(102, 139, 255, 255), stop:0.159091 rgba(11, 131, 255, 255), stop:0.982955 rgba(59, 226, 205, 255));")
        self.verticalLayout = QVBoxLayout(Gui)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Gui)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.insertUrl = QLineEdit(self.frame)
        self.insertUrl.setObjectName(u"insertUrl")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.insertUrl.sizePolicy().hasHeightForWidth())
        self.insertUrl.setSizePolicy(sizePolicy1)
        self.insertUrl.setMinimumSize(QSize(0, 40))
        self.insertUrl.setMaximumSize(QSize(16777215, 40))
        self.insertUrl.setSizeIncrement(QSize(0, 40))
        self.insertUrl.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 10pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 4px;\n"
"padding: 8px;")
        self.insertUrl.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.insertUrl)

        self.startButton = QPushButton(self.frame)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setMinimumSize(QSize(100, 40))
        self.startButton.setMaximumSize(QSize(100, 40))
        self.startButton.setSizeIncrement(QSize(0, 40))
        self.startButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"Arial\";\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.074, x2:0, y2:0.966227, stop:0 rgba(0, 0, 0, 255), stop:0.9375 rgba(10, 29, 2, 255));\n"
"border-radius: 4px;")

        self.horizontalLayout_2.addWidget(self.startButton)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Gui)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(70, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.insertUsers = QLineEdit(self.frame_2)
        self.insertUsers.setObjectName(u"insertUsers")
        sizePolicy.setHeightForWidth(self.insertUsers.sizePolicy().hasHeightForWidth())
        self.insertUsers.setSizePolicy(sizePolicy)
        self.insertUsers.setMinimumSize(QSize(140, 40))
        self.insertUsers.setMaximumSize(QSize(140, 40))
        self.insertUsers.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 10pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 4px;\n"
"padding: 8px;")
        self.insertUsers.setClearButtonEnabled(True)

        self.horizontalLayout_3.addWidget(self.insertUsers)

        self.horizontalSpacer_2 = QSpacerItem(70, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.insertCount = QLineEdit(self.frame_2)
        self.insertCount.setObjectName(u"insertCount")
        sizePolicy.setHeightForWidth(self.insertCount.sizePolicy().hasHeightForWidth())
        self.insertCount.setSizePolicy(sizePolicy)
        self.insertCount.setMinimumSize(QSize(140, 40))
        self.insertCount.setMaximumSize(QSize(140, 40))
        self.insertCount.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 10pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 4px;\n"
"padding: 8px;")
        self.insertCount.setClearButtonEnabled(True)

        self.horizontalLayout_3.addWidget(self.insertCount)

        self.horizontalSpacer_4 = QSpacerItem(70, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.insertTime = QLineEdit(self.frame_2)
        self.insertTime.setObjectName(u"insertTime")
        sizePolicy.setHeightForWidth(self.insertTime.sizePolicy().hasHeightForWidth())
        self.insertTime.setSizePolicy(sizePolicy)
        self.insertTime.setMinimumSize(QSize(140, 40))
        self.insertTime.setMaximumSize(QSize(140, 40))
        self.insertTime.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 10pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 4px;\n"
"padding: 8px;")
        self.insertTime.setClearButtonEnabled(True)

        self.horizontalLayout_3.addWidget(self.insertTime)

        self.horizontalSpacer_3 = QSpacerItem(70, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(Gui)

        QMetaObject.connectSlotsByName(Gui)
    # setupUi

    def retranslateUi(self, Gui):
        Gui.setWindowTitle(QCoreApplication.translate("Gui", u"Gui", None))
        self.insertUrl.setPlaceholderText(QCoreApplication.translate("Gui", u"Insira uma URL", None))
        self.startButton.setText(QCoreApplication.translate("Gui", u"INICIAR", None))
        self.insertUsers.setPlaceholderText(QCoreApplication.translate("Gui", u"Spawn", None))
        self.insertCount.setPlaceholderText(QCoreApplication.translate("Gui", u"Usu\u00e1rios iniciais", None))
        self.insertTime.setPlaceholderText(QCoreApplication.translate("Gui", u"Tempo ", None))
    # retranslateUi


########################


class ReqUrl(HttpUser):
    wait_time = between(1, 6)

    url = ''
    host = url

    @task
    def get_page(self):
        self.client.get(self.url)


class RunLocust:

    ip = '127.0.0.1'
    port = 8089

    def __init__(self, spawn_rate='', tot_users='', time=''):
        self.spawn_rate = spawn_rate
        self.tot_users = tot_users
        self.time = time

    def create_web_ui(self):
        env = Environment(user_classes=[ReqUrl])
        env.create_local_runner()
        env.create_web_ui(self.ip, self.port)
        webbrowser.open('http://localhost:8089/')
        gevent.spawn(stats_printer(env.stats))
        gevent.spawn(stats_history, env.runner)
        env.runner.start(int(self.tot_users), int(self.spawn_rate))
        gevent.spawn_later(int(self.time), lambda: env.runner.quit())
        env.runner.greenlet.join()
        env.web_ui.stop()


class MainGui(QWidget, Ui_Gui):

    def __init__(self):
        super(MainGui, self).__init__()
        self.setupUi(self)

        self.startButton.setStyleSheet('QPushButton{background-color: qlineargradient(spread:pad, x1:1, y1:0.074, '
                                       'x2:0, '
                                       'y2:0.966227, stop:0 rgba(0, 0, 0, 255), stop:0.9375 rgba(10, 29, 2, 255)); '
                                       'border-radius: 10px;padding: 5px;color: rgb(255, 255, 255);font: 12pt '
                                       '\"Courier\"; '
                                       'border-bottom: 2px outset black;}'
                                       'QPushButton:pressed{padding: 1px -1px -1px 1px;border-bottom: 0 inset black;}'
                                       'QPushButton:hover{background-color: #4000FF;}')

        self.setWindowTitle('Testes')
        self.insertCount.setPlaceholderText('Pico')
        # self.setWindowIcon(QIcon(os.path.join(os.getcwd(), 'teste.png')))

    def run_teste(self):
        req = ReqUrl
        req.url = self.insertUrl.text()
        run = RunLocust(spawn_rate=self.insertUsers.text(), tot_users=self.insertCount.text(),
                        time=self.insertTime.text())
        run.create_web_ui()

    def start_operations(self):
        self.startButton.clicked.connect(self.run_teste)


if __name__ == '__main__':
    app = QApplication([])
    ui = MainGui()
    ui.start_operations()
    ui.show()
    sys.exit(app.exec_())

"""
# Setup the environment and runner
env = Environment(user_classes=[ReqUrl])
env.create_local_runner()
# Start web UI
env.create_web_ui('127.0.0.1', 8089)
webbrowser.open('http://localhost:8089/')
# start a greenlet that periodically outputs the current stats
# Greenlets são tipo micro processos que executam uma tarefa
gevent.spawn(stats_printer(env.stats)) # Gevent - são tipo corotinas que são funções que podem
# suspender sua execução antes de atingir um retorno
# Save the stats
gevent.spawn(stats_history, env.runner)
# Start the test
env.runner.start(1, spawn_rate=10)
# stop the runner in 60 seconds
gevent.spawn_later(60, lambda: env.runner.quit())
# Wait for the greelets
env.runner.greenlet.join()
# Stop the web server
env.web_ui.stop()
"""