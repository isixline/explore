from langchain.llms import OpenAI
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain import OpenAI, ConversationChain
from dotenv import load_dotenv
load_dotenv()


llm = OpenAI(temperature=0)
conversation = ConversationChain(llm=llm, verbose=True)

conversation.run("Hi there!")
