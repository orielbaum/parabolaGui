#!/usr/bin/env python
# -*- coding: ANSI_X3.4-1968 -*-
#
# generated by wxGlade 0.6.8 on Wed Sep 28 20:30:32 2016
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.label_1 = wx.StaticText(self, wx.ID_ANY, ("   a = "))
        self.text_ctrl_2 = wx.TextCtrl(self, wx.ID_ANY, "1")
        self.label_2 = wx.StaticText(self, wx.ID_ANY, ("   b = "))
        self.text_ctrl_3 = wx.TextCtrl(self, wx.ID_ANY, "0")
        self.label_3 = wx.StaticText(self, wx.ID_ANY, ("   c = "))
        self.text_ctrl_4 = wx.TextCtrl(self, wx.ID_ANY, "0")
        self.label_4 = wx.StaticText(self, wx.ID_ANY, ("   x limet ="))
        self.text_ctrl_5 = wx.TextCtrl(self, wx.ID_ANY, "50")
        self.label_5 = wx.StaticText(self, wx.ID_ANY, ("   y limet ="))
        self.text_ctrl_6 = wx.TextCtrl(self, wx.ID_ANY, "50")
        self.label_6 = wx.StaticText(self, wx.ID_ANY, " points distence")
        self.text_ctrl_7 = wx.TextCtrl(self, wx.ID_ANY, "0.5")	
        self.button_1 = wx.Button(self, wx.ID_ANY, ("ok"))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_TEXT_ENTER, self.InsertA, self.text_ctrl_2)
        self.Bind(wx.EVT_TEXT_ENTER, self.InsertB, self.text_ctrl_3)
        self.Bind(wx.EVT_TEXT_ENTER, self.InsertC, self.text_ctrl_4)
        self.Bind(wx.EVT_TEXT_ENTER, self.xLimet, self.text_ctrl_5)
	self.Bind(wx.EVT_TEXT_ENTER, self.yLimet, self.text_ctrl_6)
        self.Bind(wx.EVT_TEXT_ENTER, self.pointsDiference, self.text_ctrl_7)
        self.Bind(wx.EVT_BUTTON, self.OpenParabula, self.button_1)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle(("Parabula Gui"))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.GridSizer(7, 2, 0, 0)
        grid_sizer_1.Add(self.label_1, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_2, 0, 0, 0)
        grid_sizer_1.Add(self.label_2, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_3, 0, 0, 0)
        grid_sizer_1.Add(self.label_3, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_4, 0, 0, 0)
        grid_sizer_1.Add(self.label_4, 0, 0, 0)
	grid_sizer_1.Add(self.text_ctrl_5, 0, 0, 0)
        grid_sizer_1.Add(self.label_5, 0, 0, 0)
	grid_sizer_1.Add(self.text_ctrl_6, 0, 0, 0)
        grid_sizer_1.Add(self.label_6, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_7, 0, 0, 0)
        grid_sizer_1.Add(self.button_1, 0, 0, 1)
        sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

    def InsertA(self, event):  # wxGlade: MyFrame.<event_handler>
        print "Event handler 'InsertA' not implemented!"
        event.Skip()

    def InsertB(self, event):  # wxGlade: MyFrame.<event_handler>
        print "Event handler 'InsertB' not implemented!"
        event.Skip()

    def InsertC(self, event):  # wxGlade: MyFrame.<event_handler>
        print "Event handler 'InsertC' not implemented!"
        event.Skip()

    def xLimet(self, event):
	print "Event handler 'xLimet' not implemented!"
        event.Skip()

    def yLimet(self, event):
	print "Event handler 'yLimet' not implemented!"
        event.Skip()
    
    def pointsDiference(self, event):
	print "Event handler 'yLimet' not implemented!"
        event.Skip()

    def OpenParabula(self, event):  # wxGlade: MyFrame.<event_handler>
        print "Event handler 'OpenParabula' not implemented!"
        event.Skip()

# end of class MyFrame
#if __name__ == "__main__":
#    gettext.install("app") # replace with the appropriate catalog name

#    app = wx.PySimpleApp(0)
#    wx.InitAllImageHandlers()
#    frame_1 = MyFrame(None, wx.ID_ANY, "")
#    app.SetTopWindow(frame_1)
    #frame_1.Show()
    #app.MainLoop()
