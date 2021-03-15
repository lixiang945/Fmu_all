import os
import string,random

for files in os.listdir(r'D:\fmu\APP_FMU_0129\win32_FMU'):
    # print(os.path.splitext(files)[0])
    l1 = string.digits+string.ascii_uppercase+string.ascii_lowercase
    s1 = ''.join(random.sample(l1, 4))
    s2 = ''.join(random.sample(l1, 4))
    print(f'{s1}-{s2}')