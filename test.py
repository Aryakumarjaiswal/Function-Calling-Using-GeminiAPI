########################### FUNCTION CALLING WITH NO ARGUMENTS ########################################

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
#create .env file define api key i.e ->GEMINI_API_KEY="geniniapikeyicq2jr09q2r9gj"
KEY=os.getenv("GEMINI_API_KEY")
genai.configure(api_key=KEY)
configuration={
    "temperature":1,
    "top_p":0.95,
    "top_k":40,
    "max_output_tokens":8192,
    "response_mime_type":"text/plain"
    }

def transfer_to_customer_team():
        
        """Simulates transferring the chat to the customer service team."""
       
        message = "Sure I'm transferring your call to the customer service team. Please wait a moment. Call transferred to the customer service team successfully!!!!"
            
        
        
       
        return message
model=genai.GenerativeModel(model_name="gemini-1.5-flash",generation_config=configuration,  tools=[transfer_to_customer_team])

chat=model.start_chat()
response=chat.send_message("please transfer my call to chat team")
# print(response)
# response:
# GenerateContentResponse(
#     done=True,
#     iterator=None,
#     result=protos.GenerateContentResponse({
#       "candidates": [
#         {
#           "content": {
#             "parts": [
#               {
#                 "function_call": {
#                   "name": "transfer_to_customer_team",
#                   "args": {}
#                 }
#               }
#             ],
#             "role": "model"
#           },
#           "finish_reason": "STOP"
#         }
#       ],
#       "usage_metadata": {
#         "prompt_token_count": 25,
#         "candidates_token_count": 7,
#         "total_token_count": 32
#       }
#     }),
# )

############################################ END ########################################################
################################## FUNCTION CALLING WITH ARGUMENTS ######################################
import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()

KEY=os.getenv("GEMINI_KEY")
genai.configure(api_key=KEY)
configuration={
    "temperature":1,
    "top_p":0.95,
    "top_k":40,
    "max_output_tokens":8192,
    "response_mime_type":"text/plain"
    }

def transfer_to_customer_team(input:str,name:str=None,email:str=None,phone:str=None):
        
        """Simulates Extraction of name,email & phone number of user if it exists in input.
        Arguments:
        input: str: User's input string.
        name: str: Extract User's name here.
        email:str: Extract User's email here.
        phone:int: Extract User's phone number here.
 
        """

       
        message = f"Sure {name},email:{email},phone:{phone} I'm transferring your call to the customer service team. Please wait a moment. Call transferred to the customer service team successfully!!!!"
            

        return message
model=genai.GenerativeModel(model_name="gemini-1.5-flash",generation_config=configuration,  tools=[transfer_to_customer_team])

chat=model.start_chat()
ip="Im Dhoni,mobile no:887983454 & conctact me via msd11@gmail.com also please transfer my call to chat team"
#ip="Hi good morning.how ca you assist me today?"

response=chat.send_message(ip)

for part in response.candidates[0].content.parts:

        if hasattr(part, "function_call") and part.function_call is not None and part.function_call.name == "transfer_to_customer_team":
                ans=transfer_to_customer_team(ip,part.function_call.args['name'],part.function_call.args['email'],part.function_call.args['phone'])
                print(ans)

#OUTPUT:
#Sure Dhoni,email:msd11@gmail.com,phone:887983454 I'm transferring your call to the customer service team. Please wait a moment. Call transferred to the customer service team successfully!!!!

##########################################################################################################
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
#create .env file define api key i.e ->GEMINI_API_KEY="geniniapikeyicq2jr09q2r9gj"
KEY=os.getenv("GEMINI_API_KEY")
genai.configure(api_key=KEY))
configuration={
    "temperature":1,
    "top_p":0.95,
    "top_k":40,
    "max_output_tokens":8192,
    "response_mime_type":"text/plain"
    }

def transfer_to_customer_team(name:str):
        
        """Simulates transferring the chat to the customer service team."""
       
        message = f"Sure {name} I'm transferring your call to the customer service team. Please wait a moment. Call transferred to the customer service team successfully!!!!"
            
        
        
       
        return message
model=genai.GenerativeModel(model_name="gemini-1.5-flash",generation_config=configuration,  tools=[transfer_to_customer_team])

chat=model.start_chat()
response=chat.send_message("please transfer my call to chat team")
for part in response.candidates[0].content.parts:

        if hasattr(part, "function_call") and part.function_call is not None and part.function_call.name == "transfer_to_customer_team":
                ans=transfer_to_customer_team("Krishna")
                print(ans)
                
print(response)
# Sure Krishna I'm transferring your call to the customer service team. Please wait a moment. Call transferred to the customer service team successfully!!!!
# response:
# GenerateContentResponse(
#     done=True,
#     iterator=None,
#     result=protos.GenerateContentResponse({
#       "candidates": [
#         {
#           "content": {
#             "parts": [
#               {
#                 "function_call": {
#                   "name": "transfer_to_customer_team",
#                   "args": {
#                     "name": ""
#                   }
#                 }
#               }
#             ],
#             "role": "model"
#           },
#           "finish_reason": "STOP"
#         }
#       ],
#       "usage_metadata": {
#         "prompt_token_count": 27,
#         "candidates_token_count": 8,
#         "total_token_count": 35
#       }
#     }),
# )

############################################ END ########################################################
