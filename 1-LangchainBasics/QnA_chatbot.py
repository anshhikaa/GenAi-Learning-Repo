import streamlit as st 
from langchain.chat_models import init_chat_model
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage , AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os

# Streamlit page config
st.set_page_config(page_title = "QnA Chatbot" ,  initial_sidebar_state = "collapsed")

# title
st.title("Simple Langchain chatbot with groq")
st.markdown("Learn langchain basics with groqs ultra fast inference!")

#sidebar
with st.sidebar :
    st.header("Setting")
    # Api key 
    api_key = st.text_input("GROQ_API_KEY", type ="password", help="get free api key at console.groq.com")
    #model selection 
    model_name = st.selectbox(
        "Model",
        ["llama3-8b-8192", "openai/gemma2-9b-it","openai/gpt-oss-120b"],
        index = 0 
    )
    #clear button
    if st.button("clear chat"):
        st.session_state.messages = []
        st.rerun()

#initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

#initialize LLM
@st.cache_resource 
def get_chain(api_key,model_name):
    if not api_key:
        return None
    # initialize llm model - if api key exists then initializ model
    llm =  ChatGroq(groq_api_key = api_key, model = model_name, temperature = 0.7 , streaming = True)

    #create prompt template
    prompt = ChatPromptTemplate(
        [
            ("system","You are a helpful assistant powered by Groq, answer the questions clearly and consisely"),
            ("user","{question}")
        ]
    )
    chain = prompt|llm|StrOutputParser()

    return chain

#get chain 
chain = get_chain(api_key,model_name)

if not chain :
    st.warning("Pleas enter your groq api key in the sidebar to star chatting")
    st.markdown("Get you free api key from (https://console.groq.com)")
else :
    #display chat message
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    # chat input from user
    if question:= st.chat_input("Ask my anything"):
        # add user message to session state
        st.session_state.messages.append({"role" : "user", "content" : question})
        with st.chat_message("user"):
            st.write(question)
    #generate response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            try :
                #stream response from groq
                for chunk in chain.stream({"question" : question}):
                    full_response += chunk
                    message_placeholder.markdown(full_response + " ")
                message_placeholder.markdown(full_response)
                #add to history
                st.session_state.messages.append({"role" : "assistant" , "content" : full_response})
            except Exception as e :
                st.error(f"Error : {str(e)}")


 


