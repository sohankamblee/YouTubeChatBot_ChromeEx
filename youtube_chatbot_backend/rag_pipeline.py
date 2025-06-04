from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import load_prompt
from langchain_core.documents.base import Document
import os

load_dotenv()

llm = ChatOpenAI(model = 'gpt-4o-mini', temperature=0.4,api_key=os.getenv("OPENAI_API_KEY"))
splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 50)
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

def get_transcript_context(retrieved_context:list[Document]):
    return "  ".join([doc.page_content for doc in retrieved_context])# context converted to str format

def get_chat_response(context:str,user_input:str) -> str:
    chunks = splitter.create_documents([context])
    vector_store = FAISS.from_documents(chunks, embeddings)
    retrieved_context = vector_store.similarity_search(user_input,k=3)
    context_str = get_transcript_context(retrieved_context)
    prompt = load_prompt('template.json')
    final_prompt = prompt.invoke({"transcript_context":context_str, "user_input": user_input})
    answer = llm.invoke(final_prompt)
    return answer.content
