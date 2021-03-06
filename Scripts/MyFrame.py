#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.3 on Tue Apr 09 13:12:03 2019
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
import Tools
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((400, 300))
        
        # Tool Bar
        self.frame_toolbar = wx.ToolBar(self, -1)
        self.SetToolBar(self.frame_toolbar)
        self.frame_toolbar.AddTool(100, "Open", self.toolsOpen, wx.NullBitmap, wx.ITEM_NORMAL, "Open existing file", "")
        self.frame_toolbar.AddTool(101, "Save", self.toolsSave, wx.NullBitmap, wx.ITEM_NORMAL, "Save", "")
        # Tool Bar end
        self.window_1 = wx.SplitterWindow(self, wx.ID_ANY, style=wx.SP_THIN_SASH)
        self.window_1_pane_1 = wx.ScrolledWindow(self.window_1, wx.ID_ANY, style=wx.TAB_TRAVERSAL)
        self.txtTop = wx.TextCtrl(self.window_1_pane_1, wx.ID_ANY, "", style=wx.TE_MULTILINE)
        self.window_1_pane_2 = wx.ScrolledWindow(self.window_1, wx.ID_ANY, style=wx.TAB_TRAVERSAL)
        self.txtBottom = wx.TextCtrl(self.window_1_pane_2, wx.ID_ANY, "", style=wx.TE_MULTILINE)
        self.btnClose = wx.Button(self, wx.ID_ANY, "Close")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_TOOL, self.onToolOpen, id=100)
        self.Bind(wx.EVT_TOOL, self.onToolSave, id=101)
        self.Bind(wx.EVT_BUTTON, self.OnClose, self.btnClose)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("frame")
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(self.mainIcon)
        self.SetIcon(_icon)
        self.frame_toolbar.Realize()
        self.window_1_pane_1.SetScrollRate(10, 10)
        self.window_1_pane_2.SetScrollRate(10, 10)
        self.window_1.SetMinimumPaneSize(100)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4.Add(self.txtTop, 1, wx.ALL | wx.EXPAND, 1)
        self.window_1_pane_1.SetSizer(sizer_4)
        sizer_5.Add(self.txtBottom, 1, wx.ALL | wx.EXPAND, 1)
        self.window_1_pane_2.SetSizer(sizer_5)
        self.window_1.SplitHorizontally(self.window_1_pane_1, self.window_1_pane_2)
        sizer_1.Add(self.window_1, 12, wx.EXPAND, 0)
        sizer_3.Add(self.btnClose, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_1.Add(sizer_3, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL | wx.BOTTOM | wx.TOP, 5)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def onFileOpen(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'onFileOpen' not implemented!")
        event.Skip()

    def OnOpen(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'OnOpen' not implemented!")
        event.Skip()

    def OnClose(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'OnClose' not implemented!")
        event.Skip()

    def OnSave(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'OnSave' not implemented!")
        event.Skip()
    def onToolOpen(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'onToolOpen' not implemented!")
        event.Skip()
    def onToolSave(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'onToolSave' not implemented!")
        event.Skip()
# end of class MyFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
