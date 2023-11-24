from dotenv import load_dotenv
from modules import *
load_dotenv() # Load .env file
from openai import OpenAI

client = OpenAI() # Initialize OpenAI Client

get_premade_assistant = True
get_previous_thread = True

assistant_id_to_use = "asst_LvM5fVQc4nwVisQwCo3NUCVO"
thread_id_to_use = "thread_QGuCTrfjUL2ZloLudpCohitv"

if get_premade_assistant:
    assistant = get_assistant(client, assistant_id_to_use) # Retrieve Assistant
    print(assistant.name + " is ready to go!")
# else:
#     name = "Science Tutor"
#     description = "A tutor for science students"
#     instructions = "You are going to help 5th grade students with their science homework. Make sure you give examples and explain the concepts in a way that they can understand."
#     tools = [
#         {type: "code_interpreter"},
#         {type: "retrieval"}
#     ]
    
    # Retrieve the previous conversation thread

if get_previous_thread:
    thread = get_chat(client, thread_id_to_use)
    print("Chat retrieved with ID: " + thread.id)
    print(thread)
else:
    thread = start_new_chat(client)
    print("New chat created with ID: " + thread.id)
    
# Message to send to the assistant

content = "What are your best sports bet picks for today?"

# Add the message into the thread

new_message = add_message(client, thread, content)
print(new_message)

# Run the thread with the assistant with the new message

run_chat(client, thread, assistant)

# Retrieve the chat history

history = get_messages_in_chat(client, thread)
messages = history.data[::-1]
for i in messages:
    print(i.role.upper() + ": "+ i.content[0].text.value)