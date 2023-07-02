from langchain import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from langchain.chains.summarize import load_summarize_chain
from dotenv import load_dotenv
load_dotenv()

llm = OpenAI(temperature=0)

text_splitter = CharacterTextSplitter()

with open("./future-unit-mesh.md") as f:
    state_of_the_union = f.read()
texts = text_splitter.split_text(state_of_the_union)
docs = [Document(page_content=t) for t in texts[:3]]

chain = load_summarize_chain(llm, chain_type="stuff")
summarize = chain.run(docs)
print(summarize)





