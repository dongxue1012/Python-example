#Python中的多线程

from  random import randint
from threading import  Thread
from time import time,sleep

class DownloadTask(Thread):

    def __init__(self,filename):
        super().__init__()
        self._filename=filename

    def run(self):
        print('开始下载%s'%self._filename)
        time_to_doenload = randint(5,10)
        sleep(time_to_doenload)
        print('%s下载完成！耗费了%d秒'%(self._filename,time_to_doenload))
def main():
    start = time()
    t1 = DownloadTask('123')
    t1.start()
    t2 = DownloadTask('Peking Hot.avi')
    t2.start()
    t1.join()
    t2.join()
    end = time()

if __name__ == '__main__':
    main()




if __name__ == '__main__':
    main()