import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # 创建QApplication示例
    app = QApplication(sys.argv)
    # 创建窗口
    w = QWidget()
    # 设置窗口大小
    w.resize(300, 200)
    # 移动窗口
    w.move(300, 300)
    # 设置窗口标题
    w.setWindowTitle('demo')
    # 显示窗口
    w.show()
    sys.exit(app.exec_())
