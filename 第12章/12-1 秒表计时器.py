from tkinter import *
import time


class StopWatch(Frame):
    '''实现一个秒表部件'''
    msec = 50

    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self._start = 0.0
        self._elapsedtime = 0.0
        self._running = False
        self.timestr = StringVar()
        self.makeWidgets()
        self.flag = True

    def makeWidgets(self):
        '''制作时间标签'''
        l = Label(self, textvariable=self.timestr)
        self._setTime(self._elapsedtime)
        l.pack(fill=X, expand=NO, pady=2, padx=2)

    def _update(self):
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.after(self.msec, self._update)

    def _setTime(self, elap):
        '''将时间格式改为 分：秒：百分秒'''
        minutes = int(elap / 60)
        seconds = int(elap - minutes * 60.0)
        hseconds = int((elap - minutes * 60.0 - seconds) * 100)
        self.timestr.set('%2d:%2d:%2d' % (minutes, seconds, hseconds))

    def Start(self):
        if not self._running:
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = True

    def Stop(self):
        '''停止秒表'''
        if self._running:
            self.after_cancel(self._timer)
            self._elapsedtime = time.time() - self._start
            self._setTime(self._elapsedtime)
            self._running = False

    def Reset(self):
        '''重设秒表'''
        self._start = time.time()
        self._elapsedtime = 0.0
        self._setTime(self._elapsedtime)

    def stopwatch(self):
        if self.flag == True:
            self.pack(side=TOP)
            Button(self, text='开始', command=self.Start).pack(side=LEFT)
            Button(self, text='停止', command=self.Stop).pack(side=LEFT)
            Button(self, text='重置', command=self.Reset).pack(side=LEFT)
            Button(self, text='退出', command=self.quit).pack(side=LEFT)
        self.flag = False

if __name__ == '__main__':
    def main():
        root = Tk()
        root.title('秒表计时器')
        root.geometry('250x150')
        frame1 = Frame(root)
        frame1.pack(side=BOTTOM)
        sw = StopWatch(root)
        sw.stopwatch()
        root.mainloop()
    main()
