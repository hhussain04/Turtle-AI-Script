# Turtle-AI Script

This Python script uses the Groq API to generate turtle graphics commands based on user input. It allows users to describe a shape in natural language and see it drawn using Python's turtle graphics.

## Prerequisites

- Python 3.6 or higher
- A Groq API key

## Installation

1. Clone this repository:
```bash
git clone https://github.com/hhussain/Turtle-Ai-Script.git
cd Turtle-Ai-Scrip
```

2. Install required packages:
```bash
pip install python-dotenv groq
```

3. Create a `.env` file in the project directory and add your Groq API key (NOTE YOU MUST SIGN UP TO GROQ TO GET A KEY, IT IS FREE):
```
GROQ_API_KEY=your_api_key_here
```

## Usage

Run the script (you can rename the file if you wish):
```bash
python main.py
```

When prompted, enter a description of the shape you want to draw (e.g., "blue square", "red circle", "green star").

## How It Works

1. The script prompts the user for a shape description
2. It sends this description to the Groq API
3. The API returns turtle graphics commands
4. The script filters and validates these commands
5. Valid commands are executed to draw the shape

## Contributing

Feel free to open issues or submit pull requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
