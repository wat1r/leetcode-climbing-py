import os
import time

import psutil
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
    # search_elem = we_chat_main_dialog.child_window(control_type='Edit', title='搜索')
    # search_elem = we_chat_main_dialog.child_window(control_type="UIA_EditControlTypeId (0xC354)", title="搜索")
    # search_elem.click_input()
    # search_elem.type_keys('^a').type_keys(chat_name)
    # time.sleep(1)

    # send_keys('{ENTER}')

    # mini_program_panel = we_chat_main_dialog.child_window(control_type='Button', title='小程序面板')
    # element_info = mini_program_panel.element_info
    # print(type(element_info))
    # print("window_text:", )
    # print("rich_text:", element_info.rich_text)
    # mini_program_panel.click()

    chat_ = we_chat_main_dialog.child_window(control_type='Button', title='朋友圈')
    element_info = chat_.element_info
    print(type(element_info))
    print("window_text:", )
    print("rich_text:", element_info.rich_text)
    chat_.click()
    chat_.click()

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
