#coding:utf-8
from sys import argv
from os.path import exists #exists命令将文件名作为参数，返回布尔值

script,from_file,to_file=argv

print "Copying form %s to %s"%(from_file,to_file)

input=open(from_file)
indata=input.read()

print"The input file is %d bytes long"% len(indata)

print "Does the output file exist?%r"%exist(to_file)
print "Ready,hit RETURN to continue,CTRL-C to abort."
raw_input()

output=open(to_file,'w')
output.write(indata)

print "Alright,all done."

output.close()
input.close()