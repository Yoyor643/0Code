import tkinter as tk
from tkinter import messagebox
import random
import ctypes


# =========================
# 可自定义区域
# =========================

CONFESSION_NAME = "她"
FINAL_TEXT = "我喜欢你，可以给我一个机会吗？"

DIALOG_COUNT = 80          # 对话框数量
APPEAR_INTERVAL = 70       # 每个对话框出现间隔，单位：毫秒
DIALOG_MIN_WIDTH = 300
DIALOG_MAX_WIDTH = 380
DIALOG_MIN_HEIGHT = 150
DIALOG_MAX_HEIGHT = 210

TEXTS = [
    "有句话想对你说",
    "这句话我想了很久",
    "每次见到你都会很开心",
    "你笑起来真的很好看",
    "我好像越来越喜欢你了",
    "不是开玩笑，是认真的",
    "今天想正式告诉你",
    "我喜欢你",
    "想和你一起看很多风景",
    "想把很多温柔都给你",
    "希望以后的日子里有你",
    "你愿意给我一个机会吗？",
]

BG_COLORS = [
    "#FFF2F2",
    "#FFE4E1",
    "#FFF0F5",
    "#FDE2E4",
    "#FAD2E1",
    "#E2F0CB",
    "#B5EAD7",
    "#C7CEEA",
    "#D7E3FC",
    "#FFF1BA",
    "#F6EAC2",
]


# =========================
# 高清显示修复，主要针对 Windows
# =========================

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except Exception:
    try:
        ctypes.windll.user32.SetProcessDPIAware()
    except Exception:
        pass


# =========================
# 主逻辑
# =========================

popup_windows = []


def close_all():
    """关闭所有弹出的对话框"""
    for win in popup_windows:
        try:
            win.destroy()
        except Exception:
            pass

    try:
        root.destroy()
    except Exception:
        pass


def create_one_dialog(index):
    """创建一个真实的 Tkinter 对话框窗口"""

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    width = random.randint(DIALOG_MIN_WIDTH, DIALOG_MAX_WIDTH)
    height = random.randint(DIALOG_MIN_HEIGHT, DIALOG_MAX_HEIGHT)

    x = random.randint(0, max(0, screen_width - width))
    y = random.randint(0, max(0, screen_height - height))

    bg_color = random.choice(BG_COLORS)
    text = random.choice(TEXTS)

    if random.random() < 0.2:
        text = f"{CONFESSION_NAME}，{text}"

    win = tk.Toplevel(root)
    win.title("提示")
    win.geometry(f"{width}x{height}+{x}+{y}")
    win.configure(bg=bg_color)
    win.resizable(False, False)

    popup_windows.append(win)

    label = tk.Label(
        win,
        text=text,
        bg=bg_color,
        fg="#333333",
        font=("Microsoft YaHei UI", 15, "bold"),
        wraplength=width - 50,
        justify="center"
    )
    label.pack(expand=True, padx=24, pady=(24, 8))

    button_frame = tk.Frame(win, bg=bg_color)
    button_frame.pack(pady=(0, 18))

    ok_button = tk.Button(
        button_frame,
        text="确定",
        font=("Microsoft YaHei UI", 11),
        width=10,
        command=win.destroy
    )
    ok_button.pack(side="left", padx=6)

    if index == DIALOG_COUNT:
        final_label = tk.Label(
            win,
            text=FINAL_TEXT,
            bg=bg_color,
            fg="#D6336C",
            font=("Microsoft YaHei UI", 13, "bold"),
            wraplength=width - 40,
            justify="center"
        )
        final_label.pack(padx=20, pady=(0, 12))

    win.lift()
    win.focus_force()


def show_dialogs_one_by_one(index=1):
    """让对话框一个个出现"""

    if index > DIALOG_COUNT:
        return

    create_one_dialog(index)

    root.after(
        APPEAR_INTERVAL,
        lambda: show_dialogs_one_by_one(index + 1)
    )


# =========================
# 程序入口
# =========================

root = tk.Tk()
root.withdraw()

root.bind("<Escape>", lambda event: close_all())
root.bind("<q>", lambda event: close_all())
root.bind("<Q>", lambda event: close_all())

messagebox.showinfo("提示", "点一下确定哦！")

show_dialogs_one_by_one()

root.mainloop()
