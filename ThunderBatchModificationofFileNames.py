import os

#读取文本文档中的文件地址，转换为文件名
def read_fname(pathname):
    f=open(pathname,'r')
    lines=[]
    line=f.readline()
    while line:
        line=f.readline()
        if line!='\n':
            lines.append(line[line.rfind('/')+1:])
    f.close()

    return lines




#改名字过程
def change_fname(path,f):
    #获取该目录下所有文件，存入列表中
    # f = os.listdir(path)
    n = 0
    for i in f:
        #设置旧文件名（就是路径+文件名）
        oldname = path + f[n]
        #设置新文件名
        newname = path +'mjgsy'+ str(n + 1).zfill(3) + '.m4a'
        #用os模块中的rename方法对文件改名
        os.rename(oldname,newname)
        print(oldname,'======>',newname)
    
        n+=1

if __name__=='__main__':
    #定义文本文档所在路径
    pathname='D:\\张栋栋工作专用文档\\张栋栋个人资料\\苗疆蛊事艾宝良版120集全\\苗疆蛊事艾宝良版120集全.txt'
    fns=read_fname(pathname)
    fnsn=[]
    for fn in fns:
        fn=fn[:fn.rfind('\n')]
        fnsn.append(fn)
    #定义音频文件所在目录
    path = 'D:/迅雷下载/苗疆蛊事艾宝良版120集全/'
    change_fname(path,fnsn)