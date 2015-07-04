#coding=gbk

from sys import argv#调用模块

script, filename=argv

print "we're going to erase %r."%filename
print "If you don't want that,hit CTRL-c(^c)"
print "if you do want that ,hit RETURN."

raw_input("?")

print "opening the file..."
target=open(filename,'w')#w是open函数的写参数，在这种模式下，文件原有的内容将会被删除

print "Truncating the file.Goodbye!"
target.truncate() #删除

print "Now I'm going to ask you for three lines."

line1=raw_input("line 1:")
line2=raw_input("line 2:")
line3=raw_input("line 3:")#用户输入3行

print "I'm going to write these to the file"

target.write(line1)#写入
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print "And finally, we close it."
target.close()