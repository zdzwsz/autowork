import logging
import datetime
from autogen import AssistantAgent, UserProxyAgent


config_list = [
        {
            'model': 'glm-3-turbo',
            'api_key': '7bba79bbae38a98bba903c94a55a3cc6.OR1K0e3feciAHgaN',
            'base_url': "http://127.0.0.1:8000/v1",
            'api_type': 'openai'
        }
    ]

llm_config = {
                "tools": [
                     {
                        "type":"function",
                        "function":{
                            "name": "query_weather",
                            "description": "查询城市天气预报,如果不输入时间，默认是今天。",
                            "parameters": {
                                "type": "object",
                                "properties": {
                                    "city": {
                                        "type": "string",
                                        "description":"城市名称，比如珠海",
                                    },
                                    "date": {
                                        "type": "string",
                                        "description":"日期，格式如下：2020-08-09。如果为空，默认是今天。输入1表示明天，2表示后天，也可以输入具体时间"
                                    }
                                } ,
                                "required": ["city"]
                            }
                        }
                     }
                ],
                "config_list": config_list,
                "timeout": 60,
                "seed": 42}


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def query_weather(city,date=datetime.datetime.now().strftime("%Y-%m-%d")):
    logging.info("开始查询日期")
    
    try:
        logging.info("查询成功")
        return {
            "temperature" : 25,
            "wind" : 3
        }
    except Exception as e:
        logging.exception("查询异常")
        raise e
    

def chat_weather():
    system_message='''
        使用您的编码和语言技能解决任务。
        在以下情况下，选择一种脚本语言（python、shell）。
        1.当你需要收集信息时，使用代码输出你需要的信息，例如，浏览或搜索网页，下载/读取文件，打印网页或文件的内容，获取当前日期/时间，检查操作系统。在打印出足够的信息并准备好根据你的语言技能解决任务后，你自己解决任务。
        2.当你需要用代码执行一些任务时，使用代码来执行任务并输出结果。巧妙地完成任务。
        如果需要，逐步解决任务。如果没有提供计划，请先解释你的计划。明确哪一步使用代码，哪一步则使用您的语言技能。
        使用代码时，必须在代码块中指明脚本类型。不要在一个响应中包含多个代码块。在相关的情况下，对输出使用“打印”功能。检查用户返回的执行结果。
        如果结果表明存在错误，请修复错误并再次输出代码。建议使用完整代码，而不是部分代码或代码更改。
        当你找到答案时，仔细核实答案。如果可能的话，在你的回复中包括可验证的证据。
        当任务完成后，回复“TERMINATE”。
    '''

    assistant = AssistantAgent(name="小飞",system_message=system_message, llm_config=llm_config)
    user_proxy = UserProxyAgent("张大志", 
                                code_execution_config={"work_dir": "coding","use_docker":False},
                                human_input_mode="NEVER",
                                is_termination_msg=lambda x: x.get("content", "") and x.get("content", "").rstrip().endswith("TERMINATE"),
                                max_consecutive_auto_reply=5,
                                function_map={"query_weather": query_weather}
                                )
    #user_proxy.initiate_chat(assistant, message="珠海的天气如何？")
    user_proxy.initiate_chat(assistant, message="查询下深圳明天的天气如何？")