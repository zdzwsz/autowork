import autogen
from autogen.agentchat.contrib.retrieve_assistant_agent import RetrieveAssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent

def chat_rag():
    config_list = [
        {
            'model': 'glm-3-turbo',
            'api_key': '7bba79bbae38a98bba903c94a55a3cc6.OR1K0e3feciAHgaN',
            'base_url': "http://127.0.0.1:8000/v1",
            'api_type': 'openai'
        }
    ]

    assistant = RetrieveAssistantAgent(
        name="assistant",
        system_message="You are a helpfull assistant",
        llm_config={"config_list": config_list}
    )

    user_proxy = RetrieveUserProxyAgent(
        name="rag_user_proxy",
        code_execution_config={"work_dir": "coding","use_docker":False},
        retrieve_config={
            "task": "qa",
            "docs_path": "data.txt"
        }
    )

    assistant.reset()
    user_proxy.initiate_chat(assistant, problem="In what timeframe can I return an item?")