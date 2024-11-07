import os
import time
from datetime import datetime

import psutil
import pywinauto
import win32con
import win32gui
import win32clipboard as wc

from pywinauto.application import Application
from pywinauto.keyboard import send_keys

import uiautomation as uia

chat_name = "苏州新时代全民健身预订平台"  # 需要发送消息的聊天名称
message = "测试"  # 需要发送的消息


# 输入进程名，获取PID
def get_pid(p_name):
    pids = psutil.pids()
    for pid in pids:
        p = psutil.Process(pid)
        if p_name in p.name():
            return pid


def pids():
    PID = 0
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
        except psutil.NoSuchProcess:
            pass
        else:
            dt_object = datetime.utcfromtimestamp(pinfo['create_time'])
            pinfo['create_time_format'] = dt_object

            print(f"pinfo->{pinfo}")
            # print(pinfo['name'],pinfo['pid'])
            if 'WeChat.exe' == pinfo['name']:
                PID = pinfo['pid']


def click(coords):
    pywinauto.mouse.move((coords[0], coords[1]))
    pywinauto.mouse.click(coords=(coords[0], coords[1]))


def click_center(control, main_win, click_main=True):
    coords = control.rectangle()
    if click_main:
        win_rect = main_win.rectangle()
        x = (coords.left + coords.right) // 2 - win_rect.left
        y = (coords.top + coords.bottom) // 2 - win_rect.top
        main_win.click_input(coords=(x, y))
    else:
        win_rect = control.rectangle()
        control.click_input(coords=((coords.left + coords.right) // 2 - win_rect.left,
                                    (coords.top + coords.bottom) // 2 - win_rect.top))


def connect():
    # 常用方式一：连接已有微信进程（进程号在 任务管理器-详细信息 可以查看,项目中一般根据进程名称自动获取）
    wechat_pid = get_pid("WeChat.exe")
    print(wechat_pid)
    app = Application(backend='uia').connect(process=wechat_pid)
    we_chat_main_dialog = app.window(class_name='WeChatMainWndForPC')

    # print(we_chat_main_dialog.is_dialog)

    # 给控件画个红色框便于看出是哪个
    # we_chat_main_dialog.draw_outline(colour='red')

    # list_data = we_chat_main_dialog.child_window(title="会话", control_type="List")
    # for item in list_data:
    #     print(type(item))
    #     element_info = item.element_info
    #     print(type(element_info))
    #     print("window_text:", )
    #     print("rich_text:", element_info.rich_text)
    #     print("name:", element_info.name)
    #     print("visible:", element_info.visible)
    #     print("rectangle:", element_info.rectangle)
    #     print("class_name:", element_info.class_name)
    #     print("enabled:", element_info.enabled)
    #     print("parent:", element_info.parent)
    #     print("children:", element_info.children())
    #     print("iter_children:", element_info.iter_children())

    # 打印当前窗口的所有controller（控件和属性）
    # we_chat_main_dialog.print_control_identifiers(depth=None, filename=None)
    # 通过搜索，定位聊天
    search_elem = we_chat_main_dialog.child_window(control_type='Edit', title='搜索')

    # search_elem = we_chat_main_dialog.child_window(control_type="UIA_EditControlTypeId (0xC354)", title="搜索")
    search_elem.click_input()
    search_elem.type_keys('^a').type_keys(chat_name)
    time.sleep(1)

    # send_keys('{ENTER}')
    time.sleep(1)

    # _t = we_chat_main_dialog.child_window(control_type='Window', title="文章、公众号、视频号等")
    _t = we_chat_main_dialog.child_window(control_type='Text', title="搜索 " + chat_name)
    # _t.click()
    click_center(control=_t, main_win=we_chat_main_dialog)

    # pids()

    # 创建一个Application对象，指定使用UIA后端
    _new_app = Application(backend='uia')
    # 连接到一个已经运行的应用程序
    # 你可以通过窗口的标题来连接，这里的'your_app_title'需要替换成实际的窗口标题
    new_win = _new_app.connect(title="微信", class_name="Chrome_WidgetWin_0", control_type='Pane')
    # 打印当前窗口的所有controller（控件和属性）
    new_win.print_control_identifiers(depth=None, filename=None)
    # _bt = new_win.child_window(title='苏州新时代全民健身预订平台 - 小程序').parent().parent().parent().children()[1]
    # click_center(control=_bt, main_win=new_win)
    #

    # list_data = new_win.child_window(control_type="Pane")
    # for item in list_data:
    #     print(type(item))
    #     element_info = item.element_info
    #     print(type(element_info))
    #     print("window_text:", )
    #     print("rich_text:", element_info.rich_text)
    #     print("name:", element_info.name)
    #     print("visible:", element_info.visible)
    #     print("rectangle:", element_info.rectangle)
    #     print("class_name:", element_info.class_name)
    #     print("enabled:", element_info.enabled)
    #     print("parent:", element_info.parent)
    #     print("children:", element_info.children())
    #     print("iter_children:", element_info.iter_children())

    # new_win_1 = new_win[1].child_window(control_type='Pane', found_index=0)
    # new_win_1 = new_win[1]

    # _new_tab = new_win.child_window(class_name='Chrome_RenderWidgetHostHWND')

    # _new_tab = new_win.child_window(title='苏州新时代全民健身预订平台 - 搜一搜')
    # _new_tab = new_win.window(class_name='Chrome_WidgetWin_0')
    # _new_tab = app.window(title=chat_name)
    # _new_tab = app.top_window()
    # 打印当前窗口的所有controller（控件和属性）
    # _new_tab.print_control_identifiers(depth=None, filename=None)
    #  账号描述: 打造全国一流文体旅游综合运营商，助力苏州人民拥抱美好
    # _o = _new_tab.children()[0].children()[0].children()[0].children()[0].children()[5].children()[0].children()[
    #     0].children()[1]
    # _o.click()
    # _target = _new_tab.child_window(control_type='Button',
    #                                title="苏州新时代全民健身预订平台 账号描述: 打造全国一流文体旅游综合运营商，助力苏州人民拥抱美好生活。 苏州新时代文体会展集团有限公司")
    # click_center(control=_target, main_win=_new_tab)
    # 苏州新时代全民健身预订平台 账号描述: 打造全国一流文体旅游综合运营商，助力苏州人民拥抱美好生活。 苏州新时代文体会展集团有限公司"
    print("---------")

    # mini_program_panel = we_chat_main_dialog.child_window(control_type='Button', title='小程序面板')
    # element_info = mini_program_panel.element_info
    # print(type(element_info))
    # print("window_text:", )
    # print("rich_text:", element_info.rich_text)
    # mini_program_panel.click()

    # chat_ = we_chat_main_dialog.child_window(control_type='Button', title='朋友圈')
    # element_info = chat_.element_info
    # print(type(element_info))
    # print("window_text:", )
    # print("rich_text:", element_info.rich_text)
    # chat_.click()
    # chat_.click()

    # 点击要发送消息的聊天
    # chat_list = we_chat_main_dialog.child_window(control_type='List', title='会话')
    # for chat_item in chat_list.items():
    #     if chat_name in chat_item.element_info.name:
    #         chat_item.click_input()
    #         time.sleep(1)

    print("-------------------------")


COPYDICT = {}


class WxParam:
    SYS_TEXT_HEIGHT = 33
    TIME_TEXT_HEIGHT = 34
    RECALL_TEXT_HEIGHT = 45
    CHAT_TEXT_HEIGHT = 52
    CHAT_IMG_HEIGHT = 117
    SpecialTypes = ['[文件]', '[图片]', '[视频]', '[音乐]', '[链接]']


class WxUtils:

    @staticmethod
    def start_we_chat():
        # 输入进程名，获取PID
        def get_pid(p_name):
            pids = psutil.pids()
            for pid in pids:
                p = psutil.Process(pid)
                if p_name in p.name():
                    return pid

        we_chat_path = r"D:\Program Files (x86)\Tencent\WeChat\WeChat.exe"  # 微信路径  C:\Program Files (x86)\Tencent\WeChat

        # 获取微信PID并获取微信窗口
        we_chat_id = get_pid("WeChat.exe")
        app = Application(backend='uia').connect(process=we_chat_id)
        we_chat_main_dialog = app.window(class_name='WeChatMainWndForPC')

        # 微信挂在后台时，通过再次运行唤醒
        if not we_chat_main_dialog.exists():
            tmp = Application().start(we_chat_path)

        # 通过先最小化，再恢复使得窗口置顶
        we_chat_main_dialog.minimize()
        we_chat_main_dialog.restore()

    def SplitMessage(MsgItem):
        uia.SetGlobalSearchTimeout(0)
        MsgItemName = MsgItem.Name
        if MsgItem.BoundingRectangle.height() == WxParam.SYS_TEXT_HEIGHT:
            Msg = ('SYS', MsgItemName, ''.join([str(i) for i in MsgItem.GetRuntimeId()]))
        elif MsgItem.BoundingRectangle.height() == WxParam.TIME_TEXT_HEIGHT:
            Msg = ('Time', MsgItemName, ''.join([str(i) for i in MsgItem.GetRuntimeId()]))
        elif MsgItem.BoundingRectangle.height() == WxParam.RECALL_TEXT_HEIGHT:
            if '撤回' in MsgItemName:
                Msg = ('Recall', MsgItemName, ''.join([str(i) for i in MsgItem.GetRuntimeId()]))
            else:
                Msg = ('SYS', MsgItemName, ''.join([str(i) for i in MsgItem.GetRuntimeId()]))
        else:
            Index = 1
            User = MsgItem.ButtonControl(foundIndex=Index)
            try:
                while True:
                    if User.Name == '':
                        Index += 1
                        User = MsgItem.ButtonControl(foundIndex=Index)
                    else:
                        break
                Msg = (User.Name, MsgItemName, ''.join([str(i) for i in MsgItem.GetRuntimeId()]))
            except:
                Msg = ('SYS', MsgItemName, ''.join([str(i) for i in MsgItem.GetRuntimeId()]))
        uia.SetGlobalSearchTimeout(10.0)
        return Msg

    def SetClipboard(data, dtype='text'):
        '''复制文本信息或图片到剪贴板
        data : 要复制的内容，str 或 Image 图像'''
        if dtype.upper() == 'TEXT':
            type_data = win32con.CF_UNICODETEXT
        elif dtype.upper() == 'IMAGE':
            from io import BytesIO
            type_data = win32con.CF_DIB
            output = BytesIO()
            data.save(output, 'BMP')
            data = output.getvalue()[14:]
        else:
            raise ValueError('param (dtype) only "text" or "image" supported')
        wc.OpenClipboard()
        wc.EmptyClipboard()
        wc.SetClipboardData(type_data, data)
        wc.CloseClipboard()

    def Screenshot(hwnd, to_clipboard=True):
        '''为句柄为hwnd的窗口程序截图
        hwnd : 句柄
        to_clipboard : 是否复制到剪贴板
        '''
        import pyscreenshot as shot
        bbox = win32gui.GetWindowRect(hwnd)
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, \
                              win32con.SWP_SHOWWINDOW | win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, \
                              win32con.SWP_SHOWWINDOW | win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        win32gui.BringWindowToTop(hwnd)
        im = shot.grab(bbox)
        if to_clipboard:
            WxUtils.SetClipboard(im, 'image')
        return im

    def SavePic(savepath=None, filename=None):
        Pic = uia.WindowControl(ClassName='ImagePreviewWnd', Name='图片查看')
        Pic.SendKeys('{Ctrl}s')
        SaveAs = Pic.WindowControl(ClassName='#32770', Name='另存为...')
        SaveAsEdit = SaveAs.EditControl(ClassName='Edit', Name='文件名:')
        SaveButton = Pic.ButtonControl(ClassName='Button', Name='保存(S)')
        PicName, Ex = os.path.splitext(SaveAsEdit.GetValuePattern().Value)
        if not savepath:
            savepath = os.getcwd()
        if not filename:
            filename = PicName
        FilePath = os.path.realpath(os.path.join(savepath, filename + Ex))
        SaveAsEdit.SendKeys(FilePath)
        SaveButton.Click()
        Pic.SendKeys('{Esc}')

    def ControlSize(control):
        locate = control.BoundingRectangle
        size = (locate.width(), locate.height())
        return size

    def ClipboardFormats(unit=0, *units):
        units = list(units)
        wc.OpenClipboard()
        u = wc.EnumClipboardFormats(unit)
        wc.CloseClipboard()
        units.append(u)
        if u:
            units = WxUtils.ClipboardFormats(u, *units)
        return units

    def CopyDict(self):
        Dict = {}
        for i in WxUtils.ClipboardFormats():
            if i == 0:
                continue
            wc.OpenClipboard()
            try:
                content = wc.GetClipboardData(i)
                wc.CloseClipboard()
            except:
                wc.CloseClipboard()
                raise ValueError
            if len(str(i)) >= 4:
                Dict[str(i)] = content
        return Dict


def test1():
    print()


if __name__ == '__main__':
    connect()
