# pass_gen.py
import sys
import string
import secrets

def pass_gen(size=12):
   chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
   # 記号を含める場合
   chars += '/'
   #chars += '%&$#()/'

   return ''.join(secrets.choice(chars) for x in range(size))

if __name__ == '__main__':
    if(len(sys.argv) == 2):
        print(pass_gen(int(sys.argv[1])))
    else:
        print(pass_gen())

