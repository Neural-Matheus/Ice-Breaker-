"""
!pip install langchain==0.3.0
!pip install langchain-groq==0.2.0
!pip install langchain-community==0.3.0
!pip install youtube_transcript_api==0.6.2
!pip install pypdf==5.0.0
!pip install pydantic==1.10
!pip install cohere
!pip install langchain==0.3.0 pydantic==2.7.4 cohere openai langchain_cohere langchain_openai langchain_cohere
"""
import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

information = """
Elon Reeve Musk FRS (Pretória, 28 de junho de 1971) é um empreendedor,[5] empresário e filantropo sul-africano-canadense, naturalizado estadunidense. Ele é o fundador, diretor executivo e diretor técnico da SpaceX; CEO da Tesla, Inc.; um dos cofundadores da OpenAI, fundador e CEO da Neuralink; cofundador, presidente da SolarCity e proprietário do X (antigo Twitter). Em 2023, ele era a pessoa mais rica do mundo, com um patrimônio líquido estimado em US$ 225 bilhões de dólares, de acordo com o Bloomberg Billionaires Index. Já a revista Forbes estimou sua fortuna em US$ 221,3 bilhões, principalmente de suas participações acionárias nas empresas Tesla e na SpaceX.[1][2]

Musk demonstrou publicamente preocupações com a extinção humana[6] e também propôs soluções, das quais algumas são o objetivo principal de suas empresas e já estão sendo feitas na prática. Entre elas, a redução do aquecimento global, através do uso de energias renováveis, um projeto multiplanetário, mais especificamente a colonização de Marte,[7] e o desenvolvimento seguro da inteligência artificial.

Em janeiro de 2011, uma de suas empresas, a SpaceX, tornou-se a primeira empresa no mundo a vender um voo comercial à Lua. A missão, marcada para 2013, foi contratada pela empresa Astrobotic Technology, tendo como objetivo colocar um pequeno jipe na superfície lunar, o que não aconteceu. Em 2012, encerrou o projeto do Tesla Roadster, o primeiro modelo da sua autoria, um carro totalmente elétrico que custava cerca de 92 mil dólares. A Tesla já lançou quatro modelos: S, Y, X e o Modelo 3, este último com a responsabilidade de trazer os carros elétricos para as massas, partindo de um custo inicial de 35 mil dólares.[8] Em 25 de abril de 2022, ele também concordou em comprar o Twitter por 44 bilhões de dólares.[9]

Musk expressou opiniões que o tornaram uma figura polarizadora e controversa.[10] Ele foi criticado por fazer declarações não científicas, enganosas, ou endossar teorias da conspiração, incluindo sobre a pandemia de COVID-19 e a eleição presidencial nos Estados Unidos em 2020, além de endossar postagens antissemitas,[11] sendo que por este último ele se desculpou.[12]
"""
summary_template = """
  Irei fornecer {information} informações para você e crie um resumo direto sobre essas pessoas:
  1. Um resumo curto
  2. Dois fatos interessantes
"""

os.environ['GROQ_API_KEY']

summary_prompt_template = PromptTemplate(
    input_variables=['information'], template=summary_template)
  
llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')

chain = summary_prompt_template | llm
res = chain.invoke(input={"information": information})

print(res)