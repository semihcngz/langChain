from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()

model = ChatOpenAI(model='gpt-5-nano', temperature=0.1)

#message = [
#    SystemMessage(content='Translate the following from english to turkish'),
#    HumanMessage(content='Hi!')
#]

system_prompt = 'Translate the following into {language}'
prompt_template = ChatPromptTemplate.from_messages(
    [
        ('system', system_prompt),('user', '{text}')
    ]
)


parser = StrOutputParser()
#response = model.invoke(message)

chain = prompt_template | model | parser #modelin ciktisini parsera ver


if __name__ == '__main__':
    print(chain.invoke({'language': 'spanish', 'text': 'Hello, world!'}))


