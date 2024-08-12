import os
import gradio as gr
from dotenv import load_dotenv
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.runnables import RunnablePassthrough

load_dotenv()
Splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)
Embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
Prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a super talented assistant who provided with a document will answer questions about it. This is the context - {context}"),
    ("human", "{question}"),
])
Model = ChatGroq(model = "mixtral-8x7b-32768")
QA_chain = create_stuff_documents_chain(Model, Prompt)


def start(message, history, URL):
    Loader = WebBaseLoader(URL)
    data = Loader.load()
    Docs = Splitter.split_documents(data)
    Vector_DB = Chroma.from_documents(Docs, Embeddings)
    Retriever = Vector_DB.as_retriever()
    Rag_chain = {"context": Retriever, "question": RunnablePassthrough()} | Prompt | Model
    Response = Rag_chain.invoke(message)
    return Response.content


with gr.Blocks() as Demo:
    URL = gr.Textbox(placeholder = "Enter the URL of the Webpage")
    gr.ChatInterface(
        start,
        chatbot=gr.Chatbot(height=500),
        title = "WebRAG",
        description = "Lets chat with the Website you want !!!",
        textbox=gr.Textbox(placeholder="Ask anything about this webpage", container=False),
        theme = "soft",
        additional_inputs=[URL]
    )

Demo.launch()
