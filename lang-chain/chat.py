from unittest import result
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder
)

chat = ChatOpenAI(temperature=0)

# result = chat([HumanMessage(content="Translate this sentence from English to French. I love programming.")])
# print(result)

# messages = [
#     SystemMessage(content="You are a helpful assistant that translates English to French."),
#     HumanMessage(content="Translate this sentence from English to French. I love programming.")
# ]
# result = chat(messages)
# print(result)

# batch_messages = [
#     [
#         SystemMessage(content="You are a helpful assistant that translates English to French."),
#         HumanMessage(content="Translate this sentence from English to French. I love programming.")
#     ],
#     [
#         SystemMessage(content="You are a helpful assistant that translates English to French."),
#         HumanMessage(content="Translate this sentence from English to French. I love artificial intelligence.")
#     ],
# ]
# result = chat.generate(batch_messages)
# print(result)
# result.llm_output['token_usage']
# print(result)


# template = "You are a helpful assistant that translates {input_language} to {output_language}."
# system_message_prompt = SystemMessagePromptTemplate.from_template(template)
# human_template = "{text}"
# human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
# chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
# result = chat(chat_prompt.format_prompt(input_language="English", output_language="French", text="I love programming.").to_messages())
# print(result)

# template = "You are a helpful assistant that translates {input_language} to {output_language}."
# system_message_prompt = SystemMessagePromptTemplate.from_template(template)
# human_template = "{text}"
# human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
# chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
# chain = LLMChain(llm=chat, prompt=chat_prompt)
# result = chain.run(input_language="English", output_language="French", text="I love programming.")
# print(result)

# llm = OpenAI(temperature=0)
# tools = load_tools(["serpapi", "llm-math"], llm=chat)
# agent = initialize_agent(tools, chat, agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
# agent.run("Who is Olivia Wilde's boyfriend? What is his current age raised to the 0.23 power?")

prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template("The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know."),
    MessagesPlaceholder(variable_name="history"),
    HumanMessagePromptTemplate.from_template("{input}")
])
memory = ConversationBufferMemory(return_messages=True)
conversation = ConversationChain(memory=memory, prompt=prompt, llm=chat)
result = conversation.predict(input="Hi there!")
print(result)
result = conversation.predict(input="I'm doing well! Just having a conversation with an AI.")
print(result)
result = conversation.predict(input="Tell me about yourself.")
print(result)