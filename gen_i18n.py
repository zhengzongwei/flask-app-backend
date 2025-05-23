#  Copyright (c)2024. zhengzongwei
#  flask-app-backend is licensed under Mulan PSL v2.
#  You can use this software according to the terms and conditions of the Mulan PSL v2.
#  You may obtain a copy of Mulan PSL v2 at:
#          http://license.coscl.org.cn/MulanPSL2
#  THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
#  EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
#  MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
#  See the Mulan PSL v2 for more details.


import argparse
import subprocess

path = "app/translations"


def extract_translations():
    """
    提取待翻译的字符串
    """
    command = f"pybabel extract -F babel.cfg -o translations/messages.pot ."
    print(command)
    subprocess.run(command, shell=True)


def init_translations(language):
    """
    初始化翻译文件
    """
    command = f"pybabel init -i translations/messages.pot -d {path} -l {language}"
    subprocess.run(command, shell=True)


def update_translations():
    """
    更新翻译文件
    """
    command = f"pybabel update -i translations/messages.pot -d {path}"
    subprocess.run(command, shell=True)


def compile_translations():
    """
    编译翻译文件
    """
    command = f"pybabel compile -d {path}"
    subprocess.run(command, shell=True)


if __name__ == "__main__":
    # 创建命令行解析器
    parser = argparse.ArgumentParser(description="Flask-Babel 命令行工具")
    parser.add_argument("command", choices=["extract", "init", "compile", "update"], help="命令选项：extract, init, update,"
                                                                                          "compile")
    parser.add_argument("-l", "--language", help="目标语言代码（用于 init 命令）")

    # 解析命令行参数
    args = parser.parse_args()

    # 根据命令执行相应操作
    if args.command == "extract":
        extract_translations()
    elif args.command == "init":
        if args.language:
            init_translations(args.language)
        else:
            print("必须指定目标语言代码")
    elif args.command == "update":
        update_translations()

    elif args.command == "compile":
        compile_translations()
