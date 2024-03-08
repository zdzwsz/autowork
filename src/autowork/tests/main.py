from simple_chat_date import chat_date
from simple_chat_file import chat_file
import importlib
import sys
'''
加载llm目录下的模块
'''     
def load_module(module_name):
    module_all_name = "simple_"+module_name
    module = importlib.import_module("." + module_all_name,"autowork.tests")
    return getattr(module, module_name)


if __name__ == "__main__":
    if sys.argv[1]:
        instance = load_module(sys.argv[1])
        instance()
    
