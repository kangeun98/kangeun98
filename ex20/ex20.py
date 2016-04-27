#-*-coding:utf8
#시스템으로 부터 매개변수 입력
from sys import argv
#매개변수 나열 input_file
script,input_file = argv
#print_all(f) 를 f읽는것으로 정의한다
def print_all(f):
    print f.read()
#처음으로 되돌린다 seek(0):되돌리다.
def rewind(f):
     f.seek(0)

def print_a_line(line_count,f):
    print line_count,f.readline()

current_file=open(input_file)

print"First let's print the whole file:\n"

print_all(current_file)

print"Now let's rewind,kind of like a tape."

rewind(current_file)

print"Let's print three lines"

current_line=1
print_a_line(current_file,current_file)

current_line=current_line+1
print_a_line(current_line,current_file)

current_line=current_line+1
print_a_line(current_line,current_file)