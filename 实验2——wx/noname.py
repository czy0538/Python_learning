
# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################


class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(472, 466), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"IP：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        bSizer8.Add(self.m_staticText1, 0, wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.BOTTOM | wx.LEFT, 5)

        self.ip_text = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.ip_text, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"  Port：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        bSizer8.Add(self.m_staticText3, 0, wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.BOTTOM | wx.LEFT, 5)

        self.port_text = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.port_text, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.enter_btn = wx.Button(self, wx.ID_ANY, u"进入", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.enter_btn, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer2.Add(bSizer8, 1, wx.EXPAND, 5)

        bSizer1.Add(bSizer2, 1, wx.EXPAND, 5)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.showmessage = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TE_MULTILINE)
        bSizer3.Add(self.showmessage, 1, wx.ALL | wx.EXPAND, 5)

        bSizer1.Add(bSizer3, 5, wx.EXPAND, 5)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.sendmessage = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.sendmessage, 1, wx.ALL | wx.EXPAND, 5)

        bSizer4.Add(bSizer5, 6, wx.EXPAND, 5)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.send_btn = wx.Button(self, wx.ID_ANY, u"发送", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.send_btn, 5, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.exit_btn = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.exit_btn, 5, wx.ALL, 5)

        bSizer4.Add(bSizer7, 1, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer1.Add(bSizer4, 2, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.enter_btn.Bind(wx.EVT_BUTTON, self.btn_login)
        self.send_btn.Bind(wx.EVT_BUTTON, self.btn_send)
        self.exit_btn.Bind(wx.EVT_BUTTON, self.btn_out)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def btn_login(self, event):
        event.Skip()

    def btn_send(self, event):
        event.Skip()

    def btn_out(self, event):
        event.Skip()
