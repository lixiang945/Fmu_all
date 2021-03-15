# logging模块有四个组件：
# 1、logger：日志器 提供了应用程序的接口
# 2、handle： 处理器 通过logger在不同位置输出日志
# 3、formator：格式器 决定了日志以什么样式显示
# 4、Filter：过滤器 过滤哪些需要记录输出，哪些需要丢弃
# 导包
import logging.handlers
# 新建 类
import os
import time
from Fmu_all.config import file_path


class GetLog:
    # 新建一个日志器变量
    __logger = None

    # 新建获取日志器的方法
    @classmethod
    def get_logger(cls):
        # 判断日志器为空：
        if cls.__logger is None:
            # 创建日志器
            cls.__logger = logging.getLogger()
            # 设置日志输出的默认最低级别
            cls.__logger.setLevel(logging.INFO)
            now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
            file_paths = file_path + os.sep + "log" + os.sep + f"{now}_info.log"
            # 创建处理器
            th = logging.handlers.TimedRotatingFileHandler(filename=file_paths,
                                                           when="midnight",
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding="utf-8")
            # 创建格式器
            # asctime:什么时间、filename：哪个文件、levelname：什么等级的错误信息、message：错误信息的内容
            fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
            fm = logging.Formatter(fmt)
            # fm = logging.Formatter(fmt, datefmt='%Y/%m/%d/%X')
            cls.__logger.debug("debug信息")
            cls.__logger.info("info信息")
            cls.__logger.warning('warning info')
            cls.__logger.error("error信息")
            cls.__logger.critical('critical info')
            # 将格式器添加到处理器中
            th.setFormatter(fm)
            # 将处理器添加到日志器中
            cls.__logger.addHandler(th)
        # 返回日志器
        return cls.__logger

    # def print_log(self):
    #     self.logger = logging.getLogger('logger')
    #     self.logger.setLevel(logging.INFO)
    #     if not self.logger.handlers:
    #         now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
    #         sh = logging.StreamHandler()    # 控制台输出日志
    #         #创建文件处理器
    #         fh = logging.FileHandler(filename=fr'D:\project\test002\log/{now}_log', encoding='utf-8')
    #
    #         self.logger.setLevel(logging.INFO)
    #         formator = logging.Formatter("%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s",
    #                                      datefmt='%Y/%m/%d %X')
    #         sh.setFormatter(formator)
    #         fh.setFormatter(formator)
    #
    #         self.logger.addHandler(sh)
    #         self.logger.addHandler(fh)
    #     # 日志等级从小到到
    #     # logger.debug("debug信息")
    #     # logger.info("info信息")
    #     # logger.warning('warning info')
    #     # logger.error("error信息")
    #     # logger.critical('critical info')
    #     return self.logger


if __name__ == '__main__':
    gl = GetLog()