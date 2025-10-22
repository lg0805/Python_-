from socket import *
import threading
lock = threading.Lock()
openNum = 0
threads = []
def portScanner(host,port):
    global openNum
    try:
        s = socket(AF_INET,SOCK_STREAM)         
        s.connect((host,port))
        lock.acquire()
        openNum+=1
        print('[+] %d open' % port)
        lock.release()
        s.close()
    except:
        pass
def main():
    setdefaulttimeout(1)
    for p in range(1,65534):
        t = threading.Thread(target=portScanner,args=('127.0.0.1',p))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('[*] 扫描完成！')
    print('[*] 一共有 %d 个开放端口 ' % (openNum))
if __name__ == '__main__':
    main()
