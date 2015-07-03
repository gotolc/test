#coding=utf-8

popoo="I am 6'2\" tall."
print '%s' % popoo
print 'I am 6\'2" tall.'

tabby_cat="\tI'm tabbed in."
persian_cat="I'm split\non a line."
backslash_cat="i'm \\ a \\ cat."

fat_cat='''
I'll do a list:
\t* cat food
\t* fishies
\t* catnip\n\t* grass
'''
# t 是输出一个tab的意思
# %r 打印出来的是你写在脚本里的内容，而 %s 打印的是你应该看到的内容。
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat