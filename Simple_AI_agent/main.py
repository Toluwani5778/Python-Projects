import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
from functions.call_function import call_function


def main():
    """
    Main function to generate content using Google Gemini AI.
    Now this more resembles a full AI agent that can perform multiple function calls in sequence.
    """
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    user_input = sys.argv[1]
    verbose = "--verbose" in sys.argv
    MAX_ITERATIONS = 20
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_input)]),
    ]
    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories
    - Read file contents
    - Execute Python files with optional arguments
    - Write or overwrite files

    Always work in sequence, so first you will list files, then read a file, and finally run a Python file if needed. Only when the operation requires it that you will write to a file. If the user does not specify a directory, you will use the working directory as the base path for all operations.
    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """
    schema_get_files_info = types.FunctionDeclaration(
        name="get_files_info",
        description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "directory": types.Schema(
                    type=types.Type.STRING,
                    description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
                ),
            },
        ),
    )

    schema_get_file_content = types.FunctionDeclaration(
        name="get_file_content",
        description="Reads the content of a file from a specified directory, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The path to the file to be read relative to the working directory. If not provided, reads a file in the working directory itself. The file must be a regular file and not a directory.",
                ),
            },
        ),
    )

    schema_run_python_file = types.FunctionDeclaration(
        name="run_python_file",
        description="Runs a Python file in a specified directory, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The path to the Python file to be executed, relative to the working directory. If not provided, runs a file in the working directory itself.",
                ),
            },
        ),
    )

    schema_write_file = types.FunctionDeclaration(
        name="write_file",
        description="Write content to a file in a specified directory, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The path of the file to write, relative to the working directory. If not provided, writes to a file in the working directory itself.",
                ),
                "content": types.Schema(
                    type=types.Type.STRING,
                    description="The content to write to the file.",
                ),
            },
        ),
    )

    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file,
        ]
    )

    for i in range(MAX_ITERATIONS):
        if verbose:
            print(f"\nIteration {i+1}")

        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions], system_instruction=system_prompt
            ),
        )
        try:
            if response.candidates:
                for candidate in response.candidates:
                    if verbose:
                        print("Model Thought process:", candidate.content.parts[0].text)
                    messages.append(candidate.content)
        except AttributeError:
            pass

        if response.function_calls:
            for function_call_part in response.function_calls:
                function_call_result = call_function(
                    function_call_part, verbose=verbose
                )
                if not function_call_result.parts[0].function_response.response:
                    raise ValueError("Function call did not return a valid response.")
                else:
                    if verbose:
                        print(
                            f"-> {function_call_result.parts[0].function_response.response} \n"
                        )
                    messages.append(function_call_result)

        else:
            print("\nModel Response:", response.text)
            if verbose:
                print("User prompt:", user_input)
                print("Prompt tokens:", response.usage_metadata.prompt_token_count)
                print(
                    "Response tokens:", response.usage_metadata.candidates_token_count
                )
            break


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        main()
    else:
        print("Please provide the necessary prompt to run the script.")
        sys.exit(1)
