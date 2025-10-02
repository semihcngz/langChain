from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from fastapi import FastAPI
from langserve import add_routes

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

app = FastAPI(
    title='LangChain API',
    version='1.0',
    description='A simple language chain API',
)

add_routes(app, chain, path='/chain')



if __name__ == '__main__':
    #print(chain.invoke({'language': 'spanish', 'text': 'Hello, world!'}))
    import uvicorn
    uvicorn.run(app, host='localhost', port=8000)

