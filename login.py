import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

dic_signup = {}
#시작화면 구성
class Start(QDialog):
    def __init__(self):
        super(Start,self).__init__()
        loadUi("Start.ui",self)
        self.start_button.clicked.connect(self.startfunction)

    def startfunction(self):
        start = Locate_choose()
        widget.addWidget(start)
        widget.setCurrentIndex(widget.currentIndex()+1)

#장소 선택화면 구성
class Locate_choose(QDialog):
    def __init__(self):
        super(Locate_choose,self).__init__()
        loadUi("Locate_choose.ui",self)
        self.Submit_button.clicked.connect(self.Submitfunction)

    def Submitfunction(self):
        start2 = Login()
        widget.addWidget(start2)
        widget.setCurrentIndex(widget.currentIndex()+1)

#로그인 화면 구현
class Login(QDialog):
    
    def __init__(self):
        super(Login,self).__init__()
        loadUi("login.ui",self)
        self.Login_button.clicked.connect(self.loginfunction)
        self.PW.setEchoMode(QtWidgets.QLineEdit.Password)

    def loginfunction(self):
        cnt_people = 0
        ID=self.ID.text() #id에서 텍스트 가져오겠다, 그리고 변수에 넣겠다
        PW=self.PW.text()
        print("로그인 되었습니다. 사용자: ",ID)
        self.Login_button.clicked.connect(self.nextloginfunction)
        if(cnt_people==0):#최초 로그인
            dic_signup[ID] = PW
            cnt_people+=1
        #else:#이후 로그인. 키 값 뒤져서 id있으면 비번 확인 없으면 추가
            
        


#테스트 여서 로그인 버튼 2번 눌러서 다음으로 연결하게 함 이후 위의 코드랑 통합 예정
    def nextloginfunction(self):
        start3 = Login_test()
        widget.addWidget(start3)
        widget.setCurrentIndex(widget.currentIndex()+1)
#재 로그인 시 아이디 비밀번호 확인 및 아이디 없으면 재생성
class Login_test(QDialog):
    def __init__(self):
        super(Login_test,self).__init__()
        loadUi("login_test.ui",self)
        self.return_button.clicked.connect(self.returnfunction)

    def returnfunction(self):
        start4 = Login()
        widget.addWidget(start4)
        widget.setCurrentIndex(widget.currentIndex()+1)

app = QApplication(sys.argv)
mainwindow = Start()

widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(960)
widget.setFixedHeight(1240)
widget.show()
app.exec_()