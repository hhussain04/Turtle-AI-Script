
# Turtle-AI-Script

This project integrates Python's `turtle` graphics module with Groq's API to draw shapes based on user input. The program allows users to describe shapes or drawings, and then dynamically generates the corresponding turtle graphics commands using AI-generated instructions. The generated commands are filtered and executed to produce complete and accurate visualizations.

## Features

- Uses the Groq API to generate turtle commands from user prompts.
- Filters the generated instructions to ensure only valid turtle commands are executed.
- Automatically completes shapes, ensuring closed paths and filled shapes when specified.
- Supports various commands, including moving the turtle, changing colors, and drawing shapes.
- Handles errors gracefully and provides feedback on invalid commands.

## Prerequisites

- Python 3.6 or above
- Required Python packages: `turtle`, `re`, `os`, `groq`, `python-dotenv`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/hhussain04/Turtle-AI-Script.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Turtle-AI-Script
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up the `.env` file:
   - Create a file named `.env` in the project directory.
   - Add the following line to the `.env` file:
     ```
     GROQ_API_KEY=(your api key here)
     ```

## Usage

1. Run the program:
   ```bash
   python main.py
   ```
2. When prompted, enter a description of the shape you want to draw (e.g., "blue square" or "red circle").
3. The program will connect to the Groq API to generate turtle commands based on the description.
4. Valid commands will be executed to render the shape on the screen.

## Supported Commands

The program supports the following turtle commands:
- `turtle.forward(number)`
- `turtle.backward(number)`
- `turtle.left(number)`
- `turtle.right(number)`
- `turtle.penup()`
- `turtle.pendown()`
- `turtle.circle(number)`
- `turtle.color("color")`
- `turtle.begin_fill()`
- `turtle.end_fill()`


## Example

To draw a filled red square, you can enter "red square" as the prompt. The program will generate the appropriate turtle commands to draw a filled red square on the screen.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have suggestions or find any bugs.
(Seriously would be nice to find a way to make the shapes more accurate...try drawing a heart lol)

## License

This project is licensed under the MIT License.
