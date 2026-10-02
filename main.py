import os
import argparse
import json
import sys
from prompts import system_prompt
from openai import OpenAI
from dotenv import load_dotenv
from call_function import available_functions, call_function

def main():
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if api_key == None:
        raise RuntimeError("api key not found")

    client = OpenAI(
        base_url = "https://openrouter.ai/api/v1",
        api_key = api_key,
    )

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]

    for _ in range(20):
        response = client.chat.completions.create(
            model="openrouter/free",
            messages=messages,
            tools=available_functions,
            temperature=0,
        )

        if response.usage == None:
            raise RuntimeError("Response usage does not exist")
        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {response.usage.prompt_tokens}")
            print(f"Response tokens: {response.usage.completion_tokens}")

        message = response.choices[0].message
        messages.append(message)

        if message.tool_calls:
            for tool_call in message.tool_calls:
                result_message = call_function(tool_call, args.verbose)
                if not result_message['content']: #not sure if this fails if it is empty which it should
                    raise Exception("No response from function call")

                if args.verbose:
                    print(f"-> {result_message['content']}")
                
                messages.append(result_message)
        else:
            print("Final response:")
            print(message.content)
            return
    
    print("Max iterations reached but final response not generated")
    sys.exit(1)

if __name__ == "__main__":
    main()
