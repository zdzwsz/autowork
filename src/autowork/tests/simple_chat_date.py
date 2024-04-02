from autogen import UserProxyAgent,AssistantAgent


def chat_date():
    config_list = [
        {
            'model': 'glm-4',
            'api_key': '7bba79bbae38a98bba903c94a55a3cc6.OR1K0e3feciAHgaN',
            'base_url': "http://127.0.0.1:8000/v1",
            'api_type': 'openai'
        }
    ]
    '''
    config_list = [
        {
            'model': 'moonshot-v1-8k',
            'api_key': 'sk-O6gQ681pXwvnRQUclPKJ14EppFNMAhLex3vPi2WJ7OwkKTHG',
            'base_url': "https://api.moonshot.cn/v1",
            'api_type': 'openai'
        }
    ]
    '''
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

    assistant = AssistantAgent(name="小飞",system_message=system_message, llm_config={"config_list": config_list})

    user_proxy = UserProxyAgent("张大志", 
                                code_execution_config={"work_dir": "coding","use_docker":False},
                                human_input_mode="NEVER",
                                max_consecutive_auto_reply=5)

    user_proxy.initiate_chat(assistant, message="下礼拜一日期是多少？")
    #user_proxy.initiate_chat(assistant, message="有个coding文件夹，给我看看coding文件夹有什么文件？")



