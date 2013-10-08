# -*- coding: utf-8 -*-

import wx

from generate_qrcode import make_qrcode
from encrypt_elgamal import encrypt_code
from read_qrcode import read
from motor_control import motor_switch
from pay_nfc import TestProgram
from pay_stud import process_card
 
########################################################################
class MainPanel(wx.Panel):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.frame = parent
 
        sizer = wx.BoxSizer(wx.VERTICAL)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        bmp = wx.Image("black.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self, -1, bmp, pos=(10, 10), size=(413, 400))
        
        self.dialog = wx.TextCtrl(self, style = wx.TE_READONLY|wx.TE_MULTILINE, size = (200, 90))
        self.dialog.SetValue("Please select an option from the above list")
        
        coke_button = wx.Button(self, label = "Coca Cola (340ml)")
        lays_button = wx.Button(self, label = "Lay's Lightly Salted (35g)")
        continue_button = wx.Button(self, label = "Continue with purchase")
        nfc_button = wx.Button(self, label = "Pay using NFC")
        stud_button = wx.Button(self, label = "Pay using SU Card")
        
        coke_button.Bind(wx.EVT_BUTTON, self.OnCoke)
        lays_button.Bind(wx.EVT_BUTTON, self.OnLays)
        continue_button.Bind(wx.EVT_BUTTON, self.OnContinue)
        nfc_button.Bind(wx.EVT_BUTTON, self.OnNfc)
        stud_button.Bind(wx.EVT_BUTTON, self.OnStud)
        
        sizer.Add(coke_button, 0, wx.ALL, 5)    
        sizer.Add(lays_button, 0, wx.ALL, 5) 
        sizer.Add(continue_button, 0, wx.ALL, 5)
        sizer.Add(nfc_button, 0, wx.ALL, 5)
        sizer.Add(stud_button, 0, wx.ALL, 5)
        sizer.Add(self.dialog, 0, wx.ALL, 5)
        
        hSizer.Add((1,1), 1, wx.EXPAND)
        hSizer.Add(sizer, 0, wx.TOP, 10)
        hSizer.Add((1,1), 0, wx.ALL, 10)
        self.SetSizer(hSizer)
        #self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
 
    #----------------------------------------------------------------------
    def OnEraseBackground(self, evt):
        """
        Add a picture to the background
        """
        # yanked from ColourDB.py
        dc = evt.GetDC()
 
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("qrcode.png")
        dc.DrawBitmap(bmp, 0, 0)
 
    def OnCoke(self, e):
        global challenge, motor
        
        url, challenge = encrypt_code('A061')
        make_qrcode(url)
        
        self.dialog.SetValue("Please scan the code on the left and click /'Continue with purchase/' afterwards")
        
        motor = 1
        
        bmp = wx.Image("qrcode.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self, -1, bmp, pos=(10, 10), size=(420, 500))
        
    def OnLays(self, e):
        global challenge, motor
        
        url, challenge = encrypt_code('233C')
        make_qrcode(url)
        
        self.dialog.SetValue("Please scan the code on the left and click /'Continue with purchase/' afterwards")

        motor = 2
        
        bmp = wx.Image("qrcode.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self, -1, bmp, pos=(10, 10), size=(420, 500))
        
    def OnContinue(self, e):
        
        global motor
        read(challenge, motor)
        
        self.dialog.SetValue("")

        bmp = wx.Image("black.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self, -1, bmp, pos=(10, 10), size=(413, 415))
        
    def OnNfc(self, e):
        
        self.dialog.SetValue("Swipe your phone across the receiver when prompted by your phone")
        
        TestProgram().run()
        
    def OnStud(self, e):
        
        global motor
        
        uid_list = ['e243e3c3', '2b8000c6', 'db9b01c6']
        
        self.dialog.SetValue("Please swipe your SU card across the receiver")
        
        uid = process_card()
        
        if uid in uid_list:
            motor_switch(motor)
            print uid
            
########################################################################
class MainFrame(wx.Frame):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, size=(650,450))
        panel = MainPanel(self)        
        self.Center()
 
########################################################################
class Main(wx.App):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, redirect=False, filename=None):
        """Constructor"""
        wx.App.__init__(self, redirect, filename)
        dlg = MainFrame()
        dlg.Show()
 
#----------------------------------------------------------------------
if __name__ == "__main__":
    app = Main()
    app.MainLoop()
