import os

#提取文本文件内资源链接，截取文件名，返回文件名列表
def getthefilesname(textpath):
     #文本文档地址
    textpath=textpath.replace('\\','/')
    #读取文档内资源链接字符串并转化为文件名
    tf=open(textpath,'r')
    tfnlist=[]
    line=tf.readline(1000000)
    while line:
        tfnlist.append(line)
        line=tf.readline(1000000)
    tf.close()
    tfl=[]
    for name in tfnlist:
        dirtoname=name[name.rfind('/')+1:]
        tfl.append(dirtoname)
    ftnlist=tfl.copy()
    return ftnlist

def changdownloadthunderfilenames(textpath,audiopath):

    #取得文件名列表
    textfilenames=getthefilesname(textpath)

    #获取目标目录下所有音频文件，存入列表中
    audiofilenames = os.listdir(audiopath)

    n = 0
    for textfilename,audiofilename in zip(textfilenames,audiofilenames):
    
        #设置旧文件名
        oldname = textfilename
    
        #设置新文件名
        newname = audiopath + 'mjgsy' + str(n + 1).zfill(3) + 'j.JPG'
    
        #用os模块中的rename方法对文件改名
        os.rename(oldname,newname)
        print(oldname,'======>',newname)
    
        n+=1
