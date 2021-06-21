import tkinter as tk


class Calc(tk.Frame):  # 创建Calc类继承Frame
    def __init__(self, parent=None):
        """简易图形用户界面计算器构造函数"""
        tk.Frame.__init__(self, parent)
        self.pack()
        self.startOfNextOperand = True  # 开始输入下一个操作数
        # 创建计算过程和结果的标签
        self.expr = tk.StringVar()  # 显示运算表达式
        self.expr.set('')
        self.exprLabel = tk.Label(self, font=('Helvetica', 10),
                                  fg='#666666', width=64, anchor='e', textvariable=self.expr)
        self.exprLabel.grid(row=0, column=0, columnspan=4)
        self.result = tk.StringVar()  # 显示结果
        self.result.set(0)
        self.resultLabel = tk.Label(self, font=('Helvetica', 20), width=34, anchor='e',
                                    textvariable=self.result)
        self.resultLabel.grid(row=1, column=0, columnspan=4)
        # 简易计算器按钮的按钮，使用一个2D列表表示
        buttons = [['CE', 'C', '<-', '/','sin'],
                   ['7', '8', '9', '*','cos'],
                   ['4', '5', '6', '-','arctan'],
                   ['1', '2', '3', '+','arcsin'],
                   ['±', '0', '.', '=','']]

        # 然后使用嵌套的循环的方法创建和布局各个按钮
        for r in range(5):
            for c in range(5):
                # 定义事件处理函数cmd（），默认参数为按钮标签buttons[r][c]
                def cmd(key=buttons[r][c]):
                    self.click(key)
                b = tk.Button(self, text=buttons[r][c], width=16, command=cmd)
                b.grid(row=r+2, column=c)  # 前两行用于结果显示，按钮从第3行开始

    def click(self, key):
        """事件处理"""
        if key == '=':   #按等号键时， 求值， 并显示结果
            resultExpr = self.expr.get() + self.result.get()
            resultNum = eval(resultExpr)
            self.result.set(resultNum)
            self.expr.set('')
            self.startOfNextOperand = True
        elif key in '+-/*':
            resultExpr = self.expr.get() + self.result.get() + key
            self.expr.set(resultExpr)
            self.startOfNextOperand = True
        elif key == 'C':  # 全部清空， 回到初始状态
            self.expr.set('')
            self.result.set(0)
        elif key == 'CE':  # 清空当前输入
            self.result.set(0)
        elif key == '<-':
            oldnum = self.result.get()
            if len(oldnum) == 1: # 只有一个字符
                newnum = 0
            else:
                newnum = oldnum[:-1]
            self.result.set(newnum)
        elif key == '±':  # 正负号，切换正负号
            oldnum = self.result.get()  # 获取原来的值
            if oldnum[0] == '-':
                newnum = oldnum[1:]
            else:
                newnum = '-' + oldnum
            self.result.set(newnum)
        else: # 按数字或者小数点键
            if self.startOfNextOperand:
                self.result.set(0)
                self.startOfNextOperand = False
            oldnum = self.result.get()  # 获取原来的值
            if oldnum == '0':
                self.result.set(key)
            else:
                newnum = oldnum + key
                self.result.set(newnum)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('简易计算器')
    calc = Calc(root)
    root.mainloop()