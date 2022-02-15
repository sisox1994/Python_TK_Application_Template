import threading
import tkinter as tk
import time

def Window_on_Close():
    global win
    print("Windows close")
    win.destroy()


def Create_Win():
    global win
    win = tk.Tk()
    win.title("Title")
    #==========  UI code here ====================

    #=========================================
    win.protocol("WM_DELETE_WINDOW", Window_on_Close)
    win.mainloop()
    

def Background_Task():
    sys_cnt = 0
    while True:
        #==========  Do Something Background  ==============

        #===================================================
        sys_cnt+=1
        if(sys_cnt % 10 == 0):
            print("sys:",sys_cnt/10)
        time.sleep(0.1)    


if __name__ == "__main__":
    # 建立 TK UI Window 視窗
    task_1 = threading.Thread(target = Create_Win)
   
    # setDaemon 可以讓背景程序 Background_Task 隨視窗關閉結束
    task_2 = threading.Thread(target = Background_Task)
    task_2.setDaemon(True)

    task_1.start()
    task_2.start()
