import os
import random
import string
import unittest
import warnings
from Fmu_all.get_name import GetLog
import requests
from ddt import ddt, file_data
import time
from Fmu_all.read_file import ReadFiles

log = GetLog()
rf = ReadFiles()
@ddt
class FmuUnit(unittest.TestCase):

    def setUp(self) -> None:
        warnings.simplefilter('ignore', ResourceWarning)

    def tearDown(self) -> None:
        pass

    @unittest.skip
    @file_data(r'./data/fmu_register.yml')
    def test1(self, **kwargs):
        l1 = string.digits + string.ascii_lowercase + string.ascii_uppercase
        count = 0
        fmu_list = list()

        for files in os.listdir(kwargs['fmupath']):  #根据fmu文件实际路径填写绝对路径
            s1 = ''.join(random.sample(l1, 5))
            s2 = ''.join(random.sample(l1, 4))
            s3 = ''.join(random.sample(l1, 4))
            s4 = ''.join(random.sample(l1, 5))
            self.ss = f'{s1}-{s2}-{s3}-{s4}'
            filepath = kwargs['fmupath'] + '/' + files  #根据fmu文件实际路径填写绝对路径，字符串拼接完整文件路径
            kwargs['data']['comId'] = f"{self.ss}"
            # print(f"comId is {kwargs['data']['comId']}")
            if kwargs['value'] == 32:
                kwargs['data']['comName'] = f"{os.path.splitext(files)[0]}_32"
            elif kwargs['value'] == 64:
                kwargs['data']['comName'] = f"{os.path.splitext(files)[0]}_64"
            updata_files = {
                "comFile": open(filepath, 'rb'),
                "comIconFile": open(kwargs['imagepath'], 'rb'),#根据缩略图文件实际路径填写绝对路径
                "comResFile": ''
            }
            requests.post(url=kwargs['url'], data=kwargs['data'], files=updata_files)
            log.get_logger().info(f"name is {kwargs['data']['comName']}")
            time.sleep(5)
            count += 1
            log.get_logger().info(f'上传文件 {count} 次，上传的文件名为: {files}')
            if count == 5:
                break
            log.get_logger().info(f"comId is {kwargs['data']['comId']}")

    @unittest.skip
    @file_data(r'./data/fmu_register.yml')
    def test2(self, **kwargs):
        l1 = string.digits + string.ascii_lowercase + string.ascii_uppercase
        count = 0
        fmu_list = list()

        for files in os.listdir(kwargs['fmupath']):  # 根据fmu文件实际路径填写绝对路径
            s1 = ''.join(random.sample(l1, 5))
            s2 = ''.join(random.sample(l1, 4))
            s3 = ''.join(random.sample(l1, 4))
            s4 = ''.join(random.sample(l1, 5))
            self.ss = f'{s1}-{s2}-{s3}-{s4}'
            filepath = kwargs['fmupath'] + '/' + files  # 根据fmu文件实际路径填写绝对路径，字符串拼接完整文件路径
            kwargs['data']['comId'] = f"{self.ss}"

            if kwargs['value'] == 32:
                kwargs['data']['comName'] = f"{os.path.splitext(files)[0]}_32"
            elif kwargs['value'] == 64:
                kwargs['data']['comName'] = f"{os.path.splitext(files)[0]}_64"
            fmu_list.append(kwargs['data']['comName'])
            # rf.write_json(fmu_list, 'test1')
            for i in fmu_list:
                if f"{os.path.splitext(files)[0]}_32" or f"{os.path.splitext(files)[0]}_64" in i:
                    continue
                else:
                    count += 1
            if count == 5:
                break
            print(kwargs['data']['comName'])

    @file_data(r'./data/excel_register.yml')
    def test3(self, **kwargs):
        l1 = string.digits + string.ascii_lowercase + string.ascii_uppercase
        count = 0
        for files in os.listdir(kwargs['excelpath']):  #根据excel文件实际路径填写绝对路径
            s1 = ''.join(random.sample(l1, 5))
            s2 = ''.join(random.sample(l1, 4))
            s3 = ''.join(random.sample(l1, 4))
            s4 = ''.join(random.sample(l1, 5))
            self.ss = f'{s1}-{s2}-{s3}-{s4}'
            filepath = kwargs['excelpath'] + os.sep + files  #根据excel文件实际路径填写绝对路径，字符串拼接完整文件路径
            # print(filepath)
            kwargs['data']['comId'] = f"{self.ss}"
            updata_files = {
                "comFile": open(filepath, 'rb'),
                "comIconFile": open(kwargs['imagepath'], 'rb'),  # 根据缩略图文件实际路径填写绝对路径
                "comResFile": ''
            }
            if files.endswith('.xlsx'):
            # print(f"comId is {kwargs['data']['comId']}")
            #   获取文件名
                kwargs['data']['comName'] = f"{os.path.splitext(files)[0]}".split(' ')[1]
                print(kwargs['data']['comName'])
                res = requests.post(url=kwargs['url'], data=kwargs['data'], files=updata_files)
                log.get_logger().info(f"name is {kwargs['data']['comName']}")
                count += 1
                log.get_logger().info(f'上传文件 {count} 次，上传的文件名为: {files}')
                log.get_logger().info(f"comId is {kwargs['data']['comId']}")
                log.get_logger().info(res.json())
                log.get_logger().info(kwargs['data']['comName'])


if __name__ == '__main__':
    unittest.main()
