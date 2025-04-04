
####################################################################################################
################################## FUNCTION CALLING WITH ARGUMENTS ######################################



import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()

#GEMINI_KEY=AA 
KEY= os.getenv("GEMINI_KEY")
genai.configure(api_key=KEY)
configuration={
    "temperature":1,
    "top_p":0.95,
    "top_k":40,
    "max_output_tokens":8192,
    "response_mime_type":"text/plain"
    }

def transfer_to_customer_team(name:str):
        
        """Simulates transferring the chat to the customer service team."""\
       "Arguments: Extract user name"
        message = f"Sure {name} I'm transferring your call to the customer service team. Please wait a moment. Call transferred to the customer service team successfully!!!!"
            
        
        
       
        return message

def wishing(name:str,wish:str=None):
        """
        Simulates reply back to wishing
        Arguments:name:Extract user name 
                    wish:Extract user gretting
        """
        return f"UserName:{name} and wishing:{wish}"

prompt="You're call agent.if user ask for transfer of call then execute transfer_to_customer_team function,If does wishing by providing name then execute wishing function"


model=genai.GenerativeModel(model_name="gemini-1.5-flash",generation_config=configuration, 
                            
                            
                            system_instruction=prompt,
                             tools=[transfer_to_customer_team,wishing])

chat=model.start_chat()
input="Good morning!!Im Captain america"
response=chat.send_message(input)
for part in response.candidates[0].content.parts:

        if hasattr(part, "function_call") and part.function_call is not None and part.function_call.name == "transfer_to_customer_team":
                ans=transfer_to_customer_team(input)
                print(ans)
        if hasattr(part, "function_call") and part.function_call is not None and part.function_call.name == "wishing":
                ans=wishing(input)
                print(ans)
                
print(response)
##############
#Responses:
# Sure please transfer my call to chat team.Im Tony Stark I'm transferring your call to the customer service team. Please wait a moment. Call transferred to the customer service team successfully!!!!
# response :
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
#                     "name": "Tony Stark"
#                   }
#                 }
#               }
#             ],
#             "role": "model"
#           },
#           "finish_reason": "STOP",
#           "avg_logprobs": -1.1920794804609613e-07
#         }
#       ],
#       "usage_metadata": {
#         "prompt_token_count": 104,
#         "candidates_token_count": 10,
#         "total_token_count": 114
#       },
#       "model_version": "gemini-1.5-flash"
#     }),
# )
##############
# UserName:Good morning!!Im Captain america and wishing:None
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
#                   "name": "wishing",
#                   "args": {
#                     "wish": "Good morning!!",
#                     "name": "Captain america"
#                   }
#                 }
#               }
#             ],
#             "role": "model"
#           },
#           "finish_reason": "STOP",
#           "avg_logprobs": -0.00034079188480973244
#         }
#       ],
#       "usage_metadata": {
#         "prompt_token_count": 99,
#         "candidates_token_count": 9,
#         "total_token_count": 108
#       },
#       "model_version": "gemini-1.5-flash"
#     }),
# )
