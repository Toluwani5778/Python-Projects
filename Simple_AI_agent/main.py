import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types

def main():
    """
    Main function to generate content using Google Gemini AI.
    """
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    messages = [
    types.Content(role="user", parts=[types.Part(text=sys.argv[1])]),
    ]

    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=messages
    )
    print("Model Response:", response.text)

    try :
        if sys.argv[2] == "--verbose":
            print("User prompt:", sys.argv[1])
            print("Prompt tokens:", response.usage_metadata.prompt_token_count)
            print("Response tokens:", response.usage_metadata.candidates_token_count)
    except IndexError:
        pass


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        main()
    else:
        print("Please provide the necessary prompt to run the script.")
        sys.exit(1)