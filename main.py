import turtle
import re
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def get_turtle_instructions(prompt):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("No Groq API key found. Please set the GROQ_API_KEY environment variable.")
    
    print("Attempting to connect to Groq API...")
    client = Groq(api_key=api_key)
    
    try:
        print("Sending request to Groq API...")
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": """You are a Python turtle graphics expert. Provide only valid turtle commands, one per line.
IMPORTANT:
1. Always complete the entire shape - never leave a drawing unfinished
3. For regular shapes like squares, make sure to return to the starting point
4. Always use color if specified in the request
5. Begin_fill and end_fill should be used for solid shapes
6. Double check that your commands will create a complete, closed shape

Example of a complete square:
turtle.color("blue")
turtle.begin_fill()
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.end_fill()"""
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="mixtral-8x7b-32768",
            temperature=0.7,
            max_tokens=10000,
        )
        
        print("Received response from API")
        raw_response = chat_completion.choices[0].message.content
        print("\nRaw API Response:")
        print(raw_response)
        
        instructions = raw_response.split('\n')
        print(f"\nSplit into {len(instructions)} lines")
        
        return instructions
    except Exception as e:
        print(f"Error getting instructions from Groq: {e}")
        return None

def clean_and_filter_instructions(instructions):
    if not instructions:
        print("No instructions returned from the model.")
        return []

    valid_commands = [
        "turtle.forward", "turtle.backward", "turtle.left", "turtle.right", 
        "turtle.penup", "turtle.pendown", "turtle.circle", "turtle.color", 
        "turtle.begin_fill", "turtle.end_fill"
    ]
    cleaned_instructions = []

    print("\nFiltering instructions:")
    for i, command in enumerate(instructions):
        print(f"Processing line {i+1}: '{command}'")
        command = command.strip()
        if not command:
            print("  - Empty line, skipping")
            continue
        
        is_valid_start = any(command.startswith(valid_cmd) for valid_cmd in valid_commands)
        print(f"  - Starts with valid command: {is_valid_start}")
        
        if is_valid_start:
            cleaned_instructions.append(command)
            print(f"  - Added to valid commands")
        else:
            print(f"  - Rejected")

    print(f"\nFound {len(cleaned_instructions)} valid commands:")
    for cmd in cleaned_instructions:
        print(f"  {cmd}")
    
    return cleaned_instructions

def execute_turtle_instructions(instructions):
    if not instructions:
        print("No instructions to execute.")
        return

    turtle.speed(5)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()

    for command in instructions:
        try:
            if re.match(r"^turtle\.(forward|backward|left|right|penup|pendown|circle|color|begin_fill|end_fill)\(.*\)$", command):
                print(f"Executing: {command}")
                exec(command)
            else:
                print(f"Ignoring invalid command: {command}")
        except Exception as e:
            print(f"Error executing command: {command}. Error: {e}")

    turtle.hideturtle()

def main():
    try:
        print("Starting turtle graphics program...")
        turtle_screen = turtle.Screen()
        turtle_screen.setup(600, 600)
        
        user_input = turtle_screen.textinput("Turtle Drawing", "Enter a shape to draw (e.g., blue square, red circle):")
        print(f"User requested to draw: {user_input}")

        if user_input:
            prompt = f"""Draw a {user_input} using only these Python turtle commands:
turtle.forward(number)
turtle.backward(number)
turtle.left(number)
turtle.right(number)
turtle.penup()
turtle.pendown()
turtle.circle(number)
turtle.color("color")
turtle.begin_fill()
turtle.end_fill()

Make sure to complete the entire shape and use the correct angles.
For a star, use 144 degree turns for 5 points.
For regular shapes, return to the starting point.
Use actual numbers, not variables.
Provide only the commands, one per line."""

            instructions = get_turtle_instructions(prompt)

            if instructions:
                cleaned_instructions = clean_and_filter_instructions(instructions)
                if cleaned_instructions:
                    print("Executing turtle commands...")
                    execute_turtle_instructions(cleaned_instructions)
                else:
                    print("No valid turtle commands found in the API response.")
            else:
                print("No instructions received from the API.")

        turtle.done()
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
