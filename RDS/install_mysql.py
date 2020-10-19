#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author : huazai
# @Time : 2017/5/4 22:04
# @File : installmysql.py
# @Description : mysql数据目录路径：/data/mysql/  ,mysql安装目录路径：/usr/local/mysql


import os
import sys
from optparse import OptionParser
from subprocess import Popen, PIPE
import shlex
import time
# import MySQLdb
import re
import shutil
import tarfile
import stat
import logging
import  pwd


logger = None
MYSQL_DATA_DIR = '/data/mysql/'
MYSQL_INSTALL_DIR = '/usr/local/mysql/'
MYSQL_CONF_DIR = '/etc/'
MYSQL_BACK_DIR = '/data/backup/mysql/'
MYSQL_STARTUP_SCRIPT = '/etc/init.d/mysql'


def init_log():
    global logger
    fmt_date = '%Y-%m-%d %H:%M:%S.%s'
    fmt_file = '%(lineno)s %(asctime)s  [%(process)d]: %(levelname)s  %(filename)s  %(message)s'

    log_file = 'installmysql.log'
    logger = logging.getLogger('mysqlinstallloging')
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(log_file, mode='a')
    file_handler.setFormatter(logging.Formatter(fmt_file, fmt_date))
    logger.addHandler(file_handler)


def opt():
    parser = OptionParser("Usage: %prog -P -f -b -p")
    parser.add_option("-P", "--port",
                      dest="port",
                      action="store",
                      default="3306",
                      help='port 3306')
    parser.add_option("-f", "--tarfile",
                      dest="tarfile",
                      action="store",
                      default="/tmp/mysql-5.6.28-linux-glibc2.5-x86_64.tar.gz",
                      help='file  /tmp/mysql-5.6.28-linux-glibc2.5-x86_64.tar.gz')
    parser.add_option("-b", "--bashfile",
                      dest="myfile",
                      action="store",
                      default="/tmp/createmycnf.sh",
                      help='file  /tmp/createmycnf.sh')
    parser.add_option("-p", "--mysqlpwd",
                      dest="mysqlpwd",
                      action="store",
                      default="123456",
                      help='password 123456')
    options, args = parser.parse_args()
    return options, args


# 设置安装目录和数据目录的权限
def setOwner(mysqlport):
    list=[]
    with open('/etc/passwd', 'r') as fd:
        for line in fd:
            matchmysql = re.search(r'mysql', line, re.I)

    if matchmysql:
        os.system('chown -R mysql:mysql %s' % MYSQL_DATA_DIR)
        os.system('chown -R mysql:mysql %s' % MYSQL_INSTALL_DIR)
    else:
        os.system('useradd  -M  -s /sbin/nologin  mysql')
        os.system('chown -R mysql:mysql %s' % MYSQL_DATA_DIR)
        os.system('chown -R mysql:mysql %s' % MYSQL_INSTALL_DIR)
    #检查安装目录和数据目录权限
    for i in  pwd.getpwnam('mysql'):
        list.append(i)
    mysqluid = list[2]
    mysqlgid = list[3]
    stdatadirmode = os.stat(MYSQL_DATA_DIR).st_mode
    stinstalldirmode = os.stat(MYSQL_INSTALL_DIR).st_mode
    if not (os.stat(MYSQL_DATA_DIR).st_uid == mysqluid and os.stat(MYSQL_DATA_DIR).st_gid == mysqlgid):
        logger.error('chown mysql datadir or installdir not ok ')
        sys.exit(1)
    if not (os.stat(MYSQL_DATA_DIR+'mysql%s/data' %(mysqlport)).st_uid == mysqluid and os.stat(MYSQL_DATA_DIR+'mysql%s/data' %(mysqlport)).st_gid == mysqlgid):
        logger.error('chown mysql datadir or installdir not ok ')
        sys.exit(1)
    if not (os.stat(MYSQL_DATA_DIR+'mysql%s/logs' %(mysqlport)).st_uid == mysqluid and os.stat(MYSQL_DATA_DIR+'mysql%s/data' %(mysqlport)).st_gid == mysqlgid):
        logger.error('chown mysql datadir or installdir not ok ')
        sys.exit(1)
    if not (os.stat(MYSQL_DATA_DIR + 'mysql%s/tmp' % (mysqlport)).st_uid == mysqluid and os.stat(MYSQL_DATA_DIR + 'mysql%s/tmp' % (mysqlport)).st_gid == mysqlgid):
        logger.error('chown mysql datadir or installdir not ok ')
        sys.exit(1)





# 创建必要的目录
def makeDIR(port):
    if os.path.exists('/data/mysql/mysql%s/data' % port):
        logger.error('mysql %s already install' % port)
        sys.exit(1)

    try:
        # os.makedirs('/usr/local/mysql')
        os.makedirs('/data/mysql/mysql%s/data' % port)
        os.makedirs('/data/mysql/mysql%s/tmp' % port)
        os.makedirs('/data/mysql/mysql%s/logs' % port)
    except Exception as e:
        logger.error(e)


# 解压二进制安装包
def extract(mysqlfile):
    if not os.path.exists(mysqlfile):
        logger.error('%s is not exists' % mysqlfile)
        sys.exit(1)
    os.chdir(os.path.dirname(mysqlfile))
    t = tarfile.open(mysqlfile, 'r:gz')
    t.extractall()  # 解压到当前目录
    t.close()


# 拷贝安装包文件到程序目录
def copyFile(mysqlfile):
    shutil.copytree(mysqlfile.split('.tar.gz')[0], MYSQL_INSTALL_DIR)
    shutil.copy2(MYSQL_INSTALL_DIR + 'support-files/mysql.server', MYSQL_STARTUP_SCRIPT)
    shutil.rmtree(mysqlfile.split('.tar.gz')[0])


# 设置环境变量
def setEnv():
    with open('/etc/profile', 'a') as fd:
        fd.write('export PATH=$PATH:/usr/local/mysql/bin' + '\n')
    os.system('source /etc/profile')


# 初始化mysql
def mysqlInstall():
    cnf = '/etc/my.cnf'
    if os.path.exists(cnf):
        cmd = MYSQL_INSTALL_DIR + "bin/mysqld --defaults-file=%s  --initialize-insecure" % cnf
        p = Popen(shlex.split(cmd), stdout=PIPE, stderr=PIPE)
        stdout, stderr = p.communicate()
        if stdout:
            logger.info('install output: %s' % (stdout))
        if stderr:
            logger.error('install error output: %s' % (stderr))

        if p.returncode == 0:
            logger.info('initialize completed')
            logger.info('install returncode: %s' % (p.returncode))
        else:
            logger.info('initialize failed , please check the mysql errror log')
            logger.info('install returncode: %s' % (p.returncode))
            sys.exit(1)
    else:
        logger.error(cnf + ' do not esixts')
        sys.exit(1)


# 设置my.cnf
def mycnfCreate(mybashfile, mysqlport):
    cnf = '/etc/my.cnf'
    cmd = "/bin/bash  %s" % mybashfile
    p = Popen(shlex.split(cmd), stdout=PIPE, stderr=PIPE)
    p.communicate()
    p.returncode
    f1 = open(cnf, "r", )
    f2 = open("%s.bak" % cnf, "w", )
    for line in f1:
        f2.write(re.sub(r'3306', mysqlport, line, count=1))
    f1.close()
    f2.close()
    os.remove(cnf)
    os.rename("%s.bak" % cnf, cnf)


# 设置启动脚本
def modifyStartupscript(port):
    isdatadirfind = 0
    isbasedirfind = 0
    f1 = open(MYSQL_STARTUP_SCRIPT, "r", )
    f2 = open("%s.bak" % MYSQL_STARTUP_SCRIPT, "w", )
    for line in f1:
        if line.startswith('datadir=') and not isdatadirfind:
            f2.write(line.replace('datadir=', 'datadir=/data/mysql/mysql%s/data' % port, 1))
            isdatadirfind = 1
        elif line.startswith('basedir=') and not isbasedirfind:
            f2.write(line.replace('basedir=', 'basedir=/usr/local/mysql', 1))
            isbasedirfind = 1
        else:
            f2.write(line)
    f1.close()
    f2.close()
    os.remove(MYSQL_STARTUP_SCRIPT)
    os.rename("%s.bak" % MYSQL_STARTUP_SCRIPT, MYSQL_STARTUP_SCRIPT)
    # 设置启动脚本执行权限
    stmode = os.stat(MYSQL_STARTUP_SCRIPT).st_mode
    os.chmod(MYSQL_STARTUP_SCRIPT, stmode | stat.S_IXOTH | stat.S_IXGRP | stat.S_IXUSR)


# 检查安装
def checkInstall(port):
    if not os.path.exists('/data/mysql/mysql%s/data/ibdata1' % port):
        logger.error('mysql not install ')
        sys.exit(1)
    with open('/data/mysql/mysql%s/logs/error.log' % port, 'r') as fd:
        fdlist = [i for i in fd if i]
        fdstr = ''.join(fdlist)
        re_error = re.compile(r'\s\[error\]\s', re.I | re.M)  # 匹配errorlog日志格式
        errorlist = re_error.findall(fdstr)

    if errorlist:
        logger.error('error.log error count:' + str(len(errorlist)))
        logger.error('mysql not install ')
        sys.exit(1)
    else:
        logger.info('install mysql  ok')


def mysqlserviceStart():
    cnf = '/etc/my.cnf'
    cmd = MYSQL_INSTALL_DIR+"bin/mysqld --defaults-file=%s &" %(cnf)
    p = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
    stdout, stderr = p.communicate()
    if stdout:
        logger.info('mysql startup output: %s' % (stdout))
    if stderr:
        logger.error('mysql startup error output: %s' % (stderr))

    if p.returncode == 0:
        logger.info('mysql startup completed')
        logger.info('mysql startup returncode: %s' % (p.returncode))
    else:
        logger.info('mysql startup failed , please check the mysql errror log')
        logger.info('mysql startup returncode: %s' % (p.returncode))
        sys.exit(1)
    time.sleep(4) # 休眠4秒 让mysql完全启动完毕


#连接mysql
# def connMysql(mysqlport):
#     cnf = '/etc/my.cnf'
#     if os.path.exists(cnf):
#         host = 'localhost'
#         user = 'root'
#         dbname = 'mysql'
#         usocket = MYSQL_DATA_DIR+'mysql%s/tmp/mysql.sock' % (mysqlport)
#         try:
#             conn = MySQLdb.connect(host=host, user=user, db=dbname, unix_socket=usocket)
#         except Exception, e:
#             logger.error(e)
#             sys.exit(1)
#         cur = conn.cursor()
#         return cur

#设置mysql的root的密码
# def runSQL(mysqlport, mysqlpwd):
#     sql = "alter user root@localhost identified  by '%s' " % (mysqlpwd)
#     cur = connMysql(mysqlport)
#     cur.execute(sql)


if __name__ == '__main__':
    init_log()

    options, args = opt()
    try:
        cmd = args[0]
    except IndexError:
        print "%s follow a command" % __file__
        print "%s -h" % __file__
        sys.exit(1)

    if (options.port and str.isdigit(options.port)) and (options.tarfile and os.path.isfile(options.tarfile)) and (
                options.myfile and os.path.isfile(options.myfile)) and (
            options.mysqlpwd):
        mysqlport = options.port
        mysqlfile = options.tarfile
        mybashfile = options.myfile
        mysqlpwd = options.mysqlpwd

    else:
        print "%s -h" % __file__
        sys.exit(1)

    if cmd == 'create':
        mycnfCreate(mybashfile, mysqlport)
        logger.info('step1:mycnfCreate completed')

        makeDIR(mysqlport)
        logger.info('step2:makeDIR completed')

        extract(mysqlfile)
        logger.info('step3:extract completed')

        copyFile(mysqlfile)
        logger.info('step4:copyFile completed')

        setOwner(mysqlport)
        logger.info('step5:setOwner completed')

        mysqlInstall()
        logger.info('step6:mysql_install completed')

        setEnv()
        logger.info('step7:setEnv completed')

        modifyStartupscript(mysqlport)
        logger.info('step8:modify_startupscript completed')

        checkInstall(mysqlport)
        logger.info('step9:checkInstall completed')

        mysqlserviceStart()
        logger.info('step10:mysqlserviceStart completed')

        # runSQL(mysqlport, mysqlpwd)
        # logger.info('step11:runSQL completed')

        print  'mysql install finish'

        # 调用示例
        # python /tmp/installmysql.py  -f /data/download/mysql-5.7.19-linux-glibc2.12-x86_64.tar.gz -P3306 -p123456 -b /tmp/createmycnf.sh  create