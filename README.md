# Learning repository for Generative Ai
## Topics :
#### 1. Langchain :


  Day 1 : made the project structure using uv package installer , got the api key from groq , gemini , openai for further use
  Day 2 : initialized llm model using init_chat_model function in the model chat_model , learnt about langchain_core module
  Day 3 : tried to use dynamic prompt template , understood the difference between a static SystemMessage and dynamic prompt(flexible blueprint) , 
  
  i) Inject the values of placeholders at runtime. The system message is created behind the scenes at runtime 
  
  ii) The systemMessage is reattached automaically by langchain to the LLM at every .invoke() or .stream(), instead of manually added it everytime in case of static SystemMessage.