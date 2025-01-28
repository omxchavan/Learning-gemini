import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key='AIzaSyD_xFrv1YGDJgEJlxkQ3dtxmLgKZJpskGI')

# Initialize Gemini model
model = genai.GenerativeModel('gemini-pro')

def chat_with_gemini():
    print("Welcome to the Gemini Chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # Send user input to Gemini
        response = model.generate_content(user_input)
        print(f"Gemini: {response.text}")

if __name__ == "__main__":
    chat_with_gemini()