from langchain import PromptTemplate, LLMChain
from langchain.llms import Ollama

# Initialize the Llama 3 model
llm = Ollama(model="llama-3")

# Create a prompt template
prompt_template = PromptTemplate(input_variables=["conversation_history", "user_input"],
                                 template="You are a helpful assistant. Here is the conversation history: {conversation_history}. User says: {user_input}")

# Set up the LLM chain
llm_chain = LLMChain(llm=llm, prompt=prompt_template)

# Chat function
def chat_with_bot():
    conversation_history = ""
    print("🤖 Chatbot is ready! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        conversation_history += f"User: {user_input}\n"
        response = llm_chain.run(conversation_history=conversation_history, user_input=user_input)
        conversation_history += f"Bot: {response}\n"
        print(f"Bot: {response}")

# Start the chatbot
if __name__ == "__main__":
    chat_with_bot()
