# from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI

# load_dotenv()

# model = ChatGoogleGenerativeAI(
#     model ="gemini-2.5-flash",
#     temperature =0.2,
# )

# from langchain_core.prompts import ChatPromptTemplate

# prompt =ChatPromptTemplate.from_template(
#     """
# You are an experienced programming instructor.
# Explain{topic}.
# The audience is {audience}.
# Keep the explanation under 200 words.
# Include one simple example.
# End with one interview question.
# """
# )

# formatted_prompt =prompt.invoke(
#     {
#         "topic" :"Depth first search",
#         "audience" :"DSA learners"
#     }
# )
# # print(formatted_prompt)

# response =model.invoke(formatted_prompt)
# print(response.content)


# from langchain_core.messages import (
#     SystemMessage,
#     HumanMessage,
# )

# messages =[
#     SystemMessage(
#         content= "You are an experienced programming instructor."
#     ),
# ]

# while True:
#     user_input =input("You: ")
#     if user_input =="exit":
#         break
#     messages.append(
#         HumanMessage{
#             content =user_input
#         }
#     )
#     response =model.invoke(messages)
#     print("AI:",response.content)
#     messages.append(response)

# ???????????????
from graph.workflow import app

initial_state ={
    "user_query":"Research Artificial Intelligence",
    "research_plan":[],
    "search_results":{},
    "analysis":"",
    "final_report":"",
}
result =app.invoke(initial_state)
print(result)





