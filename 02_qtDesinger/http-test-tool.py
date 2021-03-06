import traceback
from threading import Thread
from PySide2.QtWidgets import QApplication, QHeaderView
from PySide2.QtUiTools import QUiLoader
import requests
from PySide2.QtCore import QFile, Signal, QObject
from PySide2.QtGui import QIcon


# https://www.bilibili.com/video/BV1cJ411R7bP?p=9&spm_id_from=pageDriver

class MySignals(QObject):
    # 用于在子线程里更新图形界面
    text_print = Signal(str)


class HttpClient:
    def __init__(self):
        # 从文件中加载UI定义
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        qfile = QFile("http-test-tool.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()
        self.ui = QUiLoader().load(qfile)
        self.my_signal = MySignals()
        # self.ui = QUiLoader().load('untitled.ui')
        # self.ui.boxMethod.addItems(['GET', 'POST', 'PUT', 'DELETE'])
        self.ui.headersTable.horizontalHeader().setStretchLastSection(True)
        self.ui.headersTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.ui.buttonSend.clicked.connect(self.sendRequest)
        self.my_signal.text_print.connect(self.print_to_gui)
        self.ui.buttonAddHeader.clicked.connect(self.addOneHeader)
        self.ui.buttonDelHeader.clicked.connect(self.delOneHeader)
        self.ui.clearButton.clicked.connect(self.clearWindow)

    def print_to_gui(self, text):
        # print(text)
        self.ui.outputWindow.append(str(text))

    def addOneHeader(self):
        addRowNumber = self.ui.headersTable.currentRow() + 1
        self.ui.headersTable.insertRow(addRowNumber)

    def delOneHeader(self):
        self.ui.headersTable.removeRow(
            self.ui.headersTable.currentRow()
        )

    def sendRequest(self):
        print('clicked')
        method = self.ui.boxMethod.currentText()
        url = self.ui.editUrl.text()
        payload = self.ui.editBody.toPlainText()
        headers = dict()
        ht = self.ui.headersTable
        for row in range(ht.rowCount()):
            k = ht.item(row, 0).text()
            v = ht.item(row, 1).text()
            if k.strip() == '':
                continue
            headers[k] = v

        req = requests.Request(method, url, headers=headers, data=payload)
        prepared = req.prepare()

        self.pretty_print_request(prepared)
        s = requests.Session()
        t = Thread(target=self.req_thread, args=(s, prepared))
        t.start()

    def req_thread(self, s, prepared):
        try:
            r = s.send(prepared)
            self.pretty_print_response(r)
        except:
            self.my_signal.text_print.emit(traceback.format_exc())

    def pretty_print_request(self, req):
        if req.body == None:
            msgBody = ''
        else:
            msgBody = req.body

        # self.ui.outputWindow.append(
        #     '{}\n{}\n{}\n\n{}'.format(
        #         '\n\n------发送请求------',
        #         req.method + ' ' + req.url,
        #         '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        #         msgBody,
        #     ))
        text = '{}\n{}\n{}\n\n{}'.format(
            '\n\n------发送请求------',
            req.method + ' ' + req.url,
            '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
            msgBody,
        )
        self.my_signal.text_print.emit(text)

    def pretty_print_response(self, res):
        # self.ui.outputWindow.append(
        #     '{}\nHTTP/1.1 {}\n{}\n\n{}'.format(
        #         '\n\n----得到响应------',
        #         res.status_code,
        #         '\n'.join('{}: {}'.format(k, v) for k, v in res.headers.items()),
        #         res.text,
        #     ))
        text = '{}\nHTTP/1.1 {}\n{}\n\n{}'.format(
            '\n\n----得到响应------',
            res.status_code,
            '\n'.join('{}: {}'.format(k, v) for k, v in res.headers.items()),
            res.text,
        )
        self.my_signal.text_print.emit(text)

    def clearWindow(self):
        self.ui.outputWindow.clear()


app = QApplication([])
app.setWindowIcon(QIcon('http-logo.png'))
httpClinet = HttpClient()
httpClinet.ui.show()
app.exec_()
