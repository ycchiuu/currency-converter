"""
currency converter
(USD to TWD, fix rate)
__author__: chiu
"""
import tkinter as tk

win= tk.Tk()                        # 設定視窗
win.wm_title('currency converter')
win.geometry('350x150')
win.configure(bg='#fbbc93')

usdMsg=tk.DoubleVar()               # 設定 小數 變數
twdTrans=tk.IntVar()

def converter():
    try:                            # 防呆措施
        u1=usdMsg.get()*29.92
    except:
        twdTrans.set('請輸入數字')
    twdTrans.set(round(u1))          # 將美金轉換為台幣

# 轉換button
btn1= tk.Button(win, text= '轉換',activeforeground= 'blue', font= ('標楷體',13 ), command=converter)
btn1.place(x=85, y=50)
# 美元label
usdLabel=tk.Label(win, text= '美元 USD' , fg= 'black',bg='#fbbc93', font= ('標楷體'))
usdLabel.place(x=20,y=20)
# 美元entry
usdEntry= tk.Entry(win,textvariable= usdMsg,bg= 'white',fg='black', font= ('Ariel'),justify='center' )
usdEntry.place(x=130, y=20)
# 台幣label
twdLabel=tk.Label(win, text='台幣 TWD ',fg= 'black',bg='#fbbc93', font= ('標楷體'))
twdLabel.place(x=20,y=85)
# 台幣return label
twdTransLabel=tk.Label(win,textvariable=twdTrans,bg= 'white',fg='red', font= ('Ariel'),width=16,height=int(0.8))
twdTransLabel.place(x=130,y=85)


win.mainloop()

