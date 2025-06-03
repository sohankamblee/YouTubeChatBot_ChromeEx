from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import load_prompt

load_dotenv()

llm = ChatOpenAI(model = 'gpt-4o-mini')

splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 50)

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

vector_store = FAISS.from_documents(chunks, embeddings)

prompt = load_prompt('template.json')