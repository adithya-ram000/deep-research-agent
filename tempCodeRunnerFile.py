
while True:
    input("You: ")
    user_input =input()
    if user_input.lower()=="exit":
        break
    response =model.invoke(user_input)
    print("AI:",response.content)
