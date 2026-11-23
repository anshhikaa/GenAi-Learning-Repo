# Learning repository for Generative Ai
## Topics :
#### 1. Langchain :


  Day 1 : made the project structure using uv package installer , got the api key from groq , gemini , openai for further use


  Day 2 : initialized llm model using init_chat_model function in the model chat_model , learnt about langchain_core module


  Day 3 : Part1) Tried to use dynamic prompt template , understood the difference between a static SystemMessage and dynamic prompt(flexible blueprint) 
  
  i) Inject the values of placeholders at runtime. The system message is created behind the scenes at runtime 
  
  ii) The systemMessage is reattached automaically by langchain to the LLM at every .invoke() or .stream(), instead of manually added it everytime in case of static SystemMessage.

  Part2) Built chain using LCEL 

  i) Simple sequential chaining to generate story (prompt|llm|parser)

  ii) State preserving chain where story is generated then stored in a dict using RunnablePassThrough before passing it onto analysis prompt , then storing the analysis as well , printing both story and analysis in a single .invoke().

  iii) why state preserving ? The story if not stored would be lost once the analysis prompt gets executed 

  Day4) Built a simple QnA chatbot using Langchain and strealit 
