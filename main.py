from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

model = ChatOpenAI(model='gpt-5-nano', temperature=0.1)
message = [
    SystemMessage(content='Translate the following from english to turkish'),
    HumanMessage(content='Hi!')
]




if __name__ == '__main__':
    response = model.invoke(message)
    print(response.content)


