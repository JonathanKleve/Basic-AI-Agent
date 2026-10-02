# Basic AI Agent
A basic AI coding agent built in Python. It uses an LLM to inspect a codebase, call tools, and help diagnose or modify code.

## Features
- Sends prompts to an LLM
- Provides tools for interacting with a project
- Helps identify and fix bugs
- Can be extended with additional models and tools
## Requirements
- Python 3.10+
- An OpenRouter API key
## Setup
Clone the repository and install dependencies:
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
pip install -r requirements.txt
```

Create a .env file:

```bash
OPENROUTER_API_KEY=your_api_key_here
```

Do not commit your API key. Add .env to .gitignore.

## Usage
Run the agent with:

```bash
python main.py
```

Follow the prompts to provide a task or codebase for the agent to inspect.

## Safety
This project is intended for learning and experimentation. Be careful when giving the agent access to your filesystem or Python interpreter. Only run it in codebases you trust, and commit your work before using it so changes can be reverted.

## Future Improvements
- Support additional LLM providers
- Add more tools
- Improve error handling
- Support more complex refactoring tasks
- Add automated tests

## License
This project is for educational purposes.
