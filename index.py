from PySide6.QtWidgets import QApplication, QMainWindow
from ui.untitled_ui import Ui_MainWindow
from pyFile import ReturnToWorkshop,OutsourcedRtWh,OriRepl,Review,common


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()  # UI类的实例化（)
        self.ui.setupUi(self)
        self.band()
        common.MyClass.__init__(self)

    def band(self):
        self.ui.btn_ReturnToWorkshop.clicked.connect(ReturnToWorkshop.WriteExcels)
        self.ui.btn_OutsourcedRtWh.clicked.connect(OutsourcedRtWh.WriteExcels)
        self.ui.btn_OriRepl.clicked.connect(OriRepl.WriteExcels)
        self.ui.btn_Review.clicked.connect(Review.WriteExcels)


if __name__ == '__main__':
    app = QApplication([])  # 启动一个应用
    window = MainWindow()  # 实例化主窗口
    window.show()  # 展示主窗口
    app.exec()  # 避免程序执行到这一行后直接退出
