from langchain_aws import ChatBedrock
from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryBufferMemory
def demo_chatbot():
    # Initialize ChatBedrock model with AWS credentials and model parameters
    demo_llm = ChatBedrock(
        credentials_profile_name='default',  # ensure credentials profile is set up in AWS CLI
        model_id='anthropic.claude-3-haiku-20240307-v1:0',
        model_kwargs={
            "max_tokens": 300,
            "temperature": 0.5,
            "top_p": 0.9,
            "stop_sequences": ["\n\nHuman:"]
        },
    )
    return demo_llm

    def demo_memory():
        llm_data= demo_chatbot()
        memory= ConversationSummaryBufferMemory(llm=llm_data, max_token_limit=300)
        return memory
        
        def demo_conversation(input_text, memory):
            llm_chain_data= demo_chatbot()
            llm_conversation= ConversationChain(llm=llm_chain_data, memory=memory, verbose=True)

            chat_reply=llm_conversation.invoke(input_text)
            return chat_reply['response']
           

# Provide the input text and print the response
#response = demo_chatbot(input_text="How are you?")
#print(response)

