# AI Webpage Summarizer

A simple **Python command-line tool** that summarizes the content of a webpage using AI.  
This project is beginner-friendly and designed to help you understand how AI, user input, and error handling work together in a real application.


## What This Tool Does

- Takes a **webpage URL** from the user
- Lets the user choose an **AI model**
- Generates a **short summary** of the webpage
- Handles errors without crashing
- Allows retrying if something goes wrong

## How the Program Works

The program runs in a loop and follows these steps:

1. Ask the user to enter a webpage URL
2. Ask the user to select an AI model
3. Generate and display the summary
4. Exit if successful  
5. If an error occurs, ask the user if they want to retry

You can stop the program anytime by pressing **Ctrl + C**.

## Requirements

- Python **3.9 or higher**
- Ollama (Local & Free)
- UV package manager ([Setup](https://docs.astral.sh/uv/getting-started/installation/))

Common libraries you need:
- `requests`
- `beautifulsoup4`

## Installation

```bash
git clone https://github.com/your-username/ai-webpage-summarizer.git
cd ai-webpage-summarizer
uv sync
```

## How to Run

### Using UV
```bash
uv run main.py
```

### Using Python
```bash
# Run venv activation script (activate.ps1 on powershell, activate.bat on command prompt.)
.\.venv\Scripts\activate.ps1 
python main.py
```

### Example

```text
Enter webpage URL: https://example.com
Select model: gpt-oss

Summary generated successfully!
```

![Run AI Webpage Summarizer](./images/ai-webpage-summarizer.jpg)


## 📄 License

MIT License – free to use and modify.

## 👨‍💻 Author

**Gopalakrishnan Panchavarnam (@BuilderGK)**  
Helping QA engineers go beyond testing.

Website: https://buildergk.vercel.app  
GitHub: https://github.com/buildergk