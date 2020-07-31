import wx
import noname
from socket import *

s = socket(AF_INET, SOCK_STREAM)


class ClientFrame(noname.MyFrame1):
    def __init__(self, parent):
        noname.MyFrame1.__init__(self, parent)

    def btn_login(self, event):
        address = self.ip_text.GetValue()
        port = int(self.port_text.GetValue())
        s.connect((address, port))

    def btn_send(self, event):
        buffsize = 1024
        senddata = self.sendmessage.GetValue()
        s.send(senddata.encode())
        recvdata = s.recv(buffsize).decode('utf-8')
        self.showmessage.AppendText('\n' + recvdata)
        self.sendmessage.SetValue("")

    def btn_out(self, event):
        self.Close(True)


def main():
    app = wx.App(False)
    frame = ClientFrame(None)
    frame.Show(True)
    # 启动窗口
    app.MainLoop()


if __name__ == "__main__":
    try:
        main()
    finally:
        s.close()

