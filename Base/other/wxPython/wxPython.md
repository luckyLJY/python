# wxPython
用于图形化开发
包含：窗口、控件、事件处理、布局管理
## 类结构
根类：wx.Object
窗口类：wx.Control、wx.NonOwned、wx.Panel、wx.MenuBar
wx.Control是控件类的根类；wx.NonOwnedWindow的顶级子类wx.TopLevelWindow是顶级窗口。
wx.Window
    wx.Control
        wx.StaticText
        wx.AnyButton
            wx.Button
                wx.BitmapBtton
            wx.ToggleButton
        wx.RadioButton
        wx.CheckButton
        wx.TextCtrl
        wx.ListBox
        wx.ComboBox
        wx.Choice
        wx.Slider
        wx.Gauge
        wx.ScrollBar
        wx.ToolBar
        wx.TreeCtrl
        wx.StaticBox
        wx.StaticBitmap
    wx.NonOwnedWindow
        wx.TopLevelWindow
            wx.Dialog
            wx.Frame
    wx.Panel
    wx.MenuBar
### 第一个图形案例ch19.3.2
1. 继承wx.Frame
2. 实现init
    构建父类init:parent、title、size、pos
3. 继承wx.App
4. 实现OnInit:
    创建Frame对象
    显示窗口
    返回true
5. 退出程序：返回0
### 添加面板及设置位置
在frame中的init中的设置为Center()
在frame中创建面板wx.Panel(parent=Frame)
创建静态文本添加到面板wx.StaticText(parent=panel,label='',pos)
### wxPython界面构建层次结构
Frame
    Panel
        StaticText
        其他子控件
    菜单栏
### 事件处理
1. 事件类wx.Event;按钮事件wx.CommandEvent；鼠标事件类：wx.MoveEvent
2. 事件类型：鼠标事件：wx.MoveEvent:右键按下wx.EVT_LEFT_DOWN和wx.EVT_LEFT_UP
3. 事件源 source
4. 事件处理者 handler
事件发生时系统会调用事件处理者。绑定通过Bind()方法：
Bind(self,event,handler,source=None,id=wx.ID_ANY,id2=wx.ID_ANY)
解除绑定Unbind
#### 一对一事件
ch19.4.1
#### 一对多事件
ch19.4.2
#### 鼠标事件处理
ch19.4.3
### 布局管理
1. 绝对布局
2. Sizer管理布局
wx.Sizer
    wx.BoxSizer
        wx.StaticBoxSizer
        wx.WrapSizer
        wx.StdDialogButtonSizer
    wx.GridSizer
        wx.FileGridSizer
            wx.GridBagSizer
#### Box布局器
hbox = wx.BoxSizer(wx.HORIZONTAL) # 设置为水平方向布局
hbox = wx.BoxSizer() # 设置为水平方向布局，wx.HORIZONTAL是默认值可以省略
vhox = wx.BoxSizer(wx.VERTICAL) # 设置为垂直方向布局
添加子窗口到父窗口时，需要调用wx.BoxSizer对象Add()方法，Add()
方法是从父类wx.Sizer继承而来的，Add()方法的语法如下：
Add(window,proportion=0,flag=0,border=0,userData=None) # 添加到父窗口
Add(sizer,proportion=0,flag=0,border=0,userData=None)# 添加到另一个Sizer中，用于嵌套
Add(width,height,proportion=0,flag=0,border=0,userData=None)# 添加一个空白空间
其中proportion参数仅被wx.BoxSizer使用，用来设置当前子窗口(或控件)在父窗口所占空间比例；
flag是参数标志，用来控制对齐、边框和调整尺寸；border参数用来设置边框的宽度；
userData参数可被用来传递额外数据
对齐flag标志:
            标志                                  说明
wx.ALIGN_TOP                            顶对齐
wx.ALIGN_BOTTOM                         底对齐
wx.ALIGN_LEFT                           左对齐
wx.ALIGN_RIGHT                          右对齐
wx.ALIGN_CENTER                         居中对齐
wx.ALIGN_CENTER_VERTICAL                垂直居中对齐
wx.ALIGN_CENTER_HORIZONTAL              水平居中对齐
wx.ALIGN_CENTRE                         同wx.ALIGN_CENTER
wx.ALIGN_CENTRE_VERTICAL                同wx.ALIGN_CENTER_VERTICAL
wx.ALIGN_CENTRE_HORIZONTAL              同wx.ALIGN_CENTER_HORIZONTAL

边框flag标志：
            标志                                  说明
wx.TOP                           设置有顶部边框，边框的宽度需要通过Add()方法的border参数设置
wx.BOTTOM                        设置有底部边框
wx.LEFT                          设置有左边框
wx.RIGHT                         设置有右边框
wx.ALL                           设置4面全有边框
调整尺寸的flag标志：
wx.EXPAND                        调整子窗口(或控件)完全填满有效空间
wx.SHAPED                        调整子窗口(或控件)填充有效空间，但保存高宽比
wx.FIXED_MINSIZE                 调整子窗口(或控件)为最小尺寸
wx.RESERVE_SPACE_EVEN_IF_HIDDEN  设置此标志后，子窗口(或控件)如果被隐藏，所占空间保留
vbox 与 hbox布局管理ch19.5.1
#### StaticBox布局ch19.5.2
wx.StaticBoxSizer(box,orient=HORIZONTAL):box参数是wx.StaticBox(静态框)对象，orient参数是布局方向；
wx.StaticBoxSizer(orient,parent,label=""):orient参数布局方向，parent参数是设置所在的父窗口，
label参数设置边框的静态文本。
#### Grid布局ch19.5.3
布局类时wx.GridSizer,Grid布局以网格形式对子窗口(或控件)进行摆放，容器被分成大小相等的矩形，
一个矩形中放置一个子窗口(或控件)。
1. wx.GridSizer(rows,cols,vgap,hgap):创建指定行数和列数的wx.GridSizer对象，并指定水平和垂直间隙，
参数hgap是水平间隙，参数vgap是垂直间隙。添加子窗口(或控件)个数超过rows与cols知己，则引发异常
2. wx.GridSizer(rows,cols,gap):gap参数指定垂直间隙和水平间隙，gap参数是wx.Size类型，例如wx.Size(2,3)
设置水平间隙为2像素，垂直间隙为3像素
3. wx.GridSizer(cols,vgap,hgap):创建指定列数的wx.GridSizer对象，并指定水平和垂直间隙。由于没有限定行数，
所有添加的子窗口(或控件)个数没有限制。
4. wx.GridSizer(cols,gap=wx.Size(0,0)):
#### FlexGrid布局 ch19.5.4
Grid布局时网格大小是固定的，如果想网格大小不同可以使用FlexGrid布局。布局类wx.FlexGridSizer
AddGrowableRow(idx,proportion=0):指定行是可以扩展的，参数idx是行索引，从零开始；参数proportion设置该行所占空间比例。
AddGrowableCol(idx,proportion=0):指定列是可扩展的，参数idx是列索引，从零开始；参数proportion设置该列所占空间比例。
### wxPython控件
#### 静态文本和按钮ch19.6.1
静态文本：wx.StaticText
按钮：wx.Button(普通按钮)、wx.BitmapButton(带有图标的按钮)、
wx.ToggleButton(两种状态切换的按钮)
#### 文本输入控件ch19.6.2
#### 复选框和单选框ch19.6.3
#### 下拉列表ch19.6.4
wx.Choice是只读的不可以修改的
wx.ComboBox默认是文本框是可以修改的
wx.CB_SIMPLE:列表部分一直显示不收起来
wx.CB_DROPDOWN:默认风格，单击向下按钮列表部分展开，选择完成是收起来。
wx.CB_READONLY:文本框不可修改
wx.CB_SORT：对列表选择项进行排序，
#### 列表ch19.6.5
wx.ListBox
#### 静态图片控件ch19.6.6
wx.StaticBitmap：静态图片控件
### 窗口
分隔窗口、树、网格
#### 分隔窗口ch19.7.1
wx.SplitterWindow中一些常用的方法有以下几种
- SplitVertically(window1,window2,sashPosition=0):设置左右布局的分隔窗口,window1为左窗口，
window2为上下窗口，sashPosition是窗框的位置。
- SplitHorizontally(window1,window2,sashPositon=0):设置上下布局的分隔窗口，window1为上窗口，
window2为上下窗口，sashPostion是窗框的位置。
- SetMinimumPaneSize(paneSize):设置最小窗口尺寸，如果是左右布局是指左窗口的最小尺寸，
如果是上下布局时指上窗口的最小尺寸，如果没有设置则默认为0。
#### 树控件wx.TreeCtrlch.19.7.2
- AddRoot(text,image=-1,selImage=-1,data=None):添加根节点，text参数是根节点显示的文本；
image参数是该节点被选中时的图片索引，wx.TreeCtrl中使用的图片被放到wx.ImageList图像列表中；
selImage参数是该节点被选中时的图片索引；data参数是给节点传递的数据；方法返回节点，节点类型是
wx.TreeItemId
- AppendItem(parent,text,image=-1,selImage=-1,data=None):添加子节点，parent参数是父节点，
其他参数同AddRoot()方法，方法返回值wx.TreeItemId
- SelectItem(item,select=True):选中item节点，
- Expand(item):展开item节点
- Expand():展开节点下的所有子节点
- ExpandAllChildren(item):展开item节点下的所有子节点
- AssignImageList(imageList):保存wx.ImageList图像列表到树中，这样就可以在AddRoot()和AppendItem()方法
中使用图像列表索引
#### 使用网格ch19.7.3-1
wx.grid.Grid
ch19.7.3-2
### 菜单栏
菜单栏wx.MenuBar、菜单wx.Menu、菜单项wx.MenuItem
菜单栏不添加到父窗口中，需要在顶级窗口中通过SetMenuBar(menuBar)方法添加到菜单栏。
通过Append(menu,title)方法将菜单添加到菜单栏中，其中menu是菜单对象，title是菜单上的文本。
菜单对象通过Append(menuItem)方法将菜单项添加到菜单中ch19.8
wx.ITEM_NORMAL:普通菜单项
wx.ITEM_CHECK:复选框形式的菜单项
wx.ITEM_RADIO:单选按钮形式的菜单项
wx.ITEM_DROPDOWN:下拉列表形式的菜单项
#### 使用工具栏ch19.9






























