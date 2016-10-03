#!/usr/bin/python

import wx
import app
import numpy

class CalcParabula(app.MyFrame):
	def __init__(self, parent):
		app.MyFrame.__init__(self, parent)
		self.num = self.yLimet(1)

	def InsertA(self, event):
		num = float(self.text_ctrl_2.GetValue())
		return num


	def InsertB(self, event):
		num = float(self.text_ctrl_3.GetValue())
		return num

	def InsertC(self, event):
		num = float(self.text_ctrl_4.GetValue())
		return num
	
	def xLimet(self, event):
		xlimet = int(self.text_ctrl_5.GetValue())
		return xlimet

	def yLimet(self, event):
		ylimet = int(self.text_ctrl_6.GetValue())
		return ylimet

        def pointsDiference(self, event):
		points_diference = float(self.text_ctrl_7.GetValue())
		return points_diference	

	def OpenParabula(self, event):
		import matplotlib.pyplot as plt

		def parabula(a, b, c):
			ponits = []
			for i in numpy.arange(-self.num, self.num+1, self.pointsDiference(1)):
				point = a*i**2+b*i+c
				ponits.append(point)
			return ponits

		plt.plot(numpy.arange(-self.num, self.num+1, self.pointsDiference(1)), parabula(self.InsertA(1), self.InsertB(1), self.InsertC(1)))
		plt.xlim(-self.xLimet(1), self.xLimet(1))
		plt.ylim(-self.yLimet(1), self.yLimet(1))
		plt.grid(True)
		plt.show()

myapp = wx.App(False)
frame = CalcParabula(None)
frame.Show(True)

myapp.MainLoop()
