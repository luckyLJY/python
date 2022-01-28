#coding:utf-8
#author:Twobox

import wx

class Mywin(wx.Frame):
    def __init__(self, parent, title):
        super(Mywin, self).__init__(parent, title = title)
        self.InitUI()

    def InitUI(self):
        #创建一个菜单栏
        menuBar = wx.MenuBar()

        #创建一个菜单 1
        fileMenu = wx.Menu()

        #创建一个菜单项 1-1
        newItem = wx.MenuItem(fileMenu, id = wx.ID_NEW, text = 'New', kind = wx.ITEM_NORMAL)
        fileMenu.AppendItem(newItem)

        #添加一行线
        fileMenu.AppendSeparator()

        #创建一个子菜单 1-2
        editMenu = wx.Menu()

        #创建三个子菜单的菜单项目 1-2-1 and 1-2-2 and 1-2-3
        cutItem = wx.MenuItem(editMenu, id = 122, text = "Cut", kind = wx.ITEM_NORMAL)
        copyItem = wx.MenuItem(editMenu, id = 121, text = "Copy", kind = wx.ITEM_NORMAL)
        pasteItem = wx.MenuItem(editMenu, id = 123, text = "Paste", kind = wx.ITEM_NORMAL)
        editMenu.AppendItem(copyItem)
        editMenu.AppendItem(cutItem)
        editMenu.AppendItem(pasteItem)

        #把子菜单 1-2 添加到菜单 1 中
        fileMenu.AppendMenu(wx.ID_ANY, "Edit", editMenu)

        # 添加一行线
        fileMenu.AppendSeparator()

        #添加两个单选框 1-3 and 1-4
        radio1 = wx.MenuItem(fileMenu, id = 13, text = "Radio_One", kind = wx.ITEM_RADIO)
        radio2 = wx.MenuItem(fileMenu, id = 14, text = "Radio_Two", kind = wx.ITEM_RADIO)
        fileMenu.AppendItem(radio1)
        fileMenu.AppendItem(radio2)
        #PS.单选框 只在自己区域之间（两行线之间） 相互作用

        # 添加一行线
        fileMenu.AppendSeparator()

        #添加一个 可选中 的菜单项 1-5
        fileMenu.AppendCheckItem(id = 15, item = "Check")

        #添加一个 菜单项 1-6 并注册快捷键
        quit = wx.MenuItem(fileMenu, id = wx.ID_EXIT, text = "Quit\tCtrl+Q", kind = wx.ITEM_NORMAL)
        fileMenu.AppendItem(quit)

        #将 fileMenu 菜单添加到菜单栏中
        menuBar.Append(fileMenu, title = 'File')

        #设置窗口框架的菜单栏为 menuBar
        self.SetMenuBar(menuBar)

        #绑定事件处理
        self.Bind(wx.EVT_MENU, self.menuHandler)

        #让其在屏幕中间打开调整大小展示
        self.SetSize((300,400))
        self.Centre()
        self.Show()

    def menuHandler(self, event):
        id = event.GetId()
        if id == wx.ID_NEW:
            print("NEW")
        if id == wx.ID_EXIT:
            exit(0)



if __name__ == "__main__":
    ex = wx.App()
    Mywin(None, 'Menu - Test')
    #Mywin(None, 'Menu - Test')      #可以同时打开两个窗口  果然体现面向对象的程序开发思想
    ex.MainLoop()