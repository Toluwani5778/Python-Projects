```markdown
# 🧠 AI Coding Agent

An experimental AI-powered coding assistant that reads, analyzes, and modifies your Python code based on natural language instructions. It’s a local, agentic tool that simulates a "developer assistant" capable of debugging, refactoring, and extending codebases through structured tool use.

---

## 🚀 Features

- ✅ **Understand natural language instructions**
- 📂 **Read from and write to your Python files**
- 🧠 **Identify bugs and suggest or implement fixes**
- 🧹 **Refactor code for clarity or performance**
- 🆕 **Add or suggest new features**
- 🔁 **Iterate on tasks with reasoning**
- 🔒 **All operations remain local** (no file uploads or external requests unless you explicitly add them)

---

## 📁 Project Structure
```

Simple_AI_agent/
├── agentic_README.md
├── calculator
│ ├── README.md
│ ├── calculate.py
│ ├── lorem.txt
│ ├── main.py
│ ├── tests.py
│ ├── pkg
│ │ ├── calculator.py # Example module the agent can read/fix
│ │ ├── morelorem.txt
│ │ └── render.py # Renders output
├── functions # File and execution tools the agent can use
│ ├── call_function.py
│ ├── get_file_content.py
│ ├── get_files_info.py
│ ├── run_python.py
│ └── write_file.py
├── main.py # The entry point that runs the agent
├── requirements.txt
├── single_main.py
└── tests.py

````

---

## 🛠️ How It Works

The agent uses a system prompt that enables structured interaction with your file system through a set of well-defined functions. When you run a command, it:

1. **Reads the user's intent** (natural language prompt)
2. **Generates a plan** to diagnose the issue
3. **Lists and reads files** as needed
4. **Modifies code** by rewriting files (only when necessary)
5. **Optionally runs the code** to verify fixes or display output

Each step is thought through with a simulated reasoning trace ("Model Thought process"), which helps debug or trust the agent's actions.

---

## 🧪 Example

You can run the agent with a prompt like:

```bash
python main.py "fix the bug: 3 + 7 * 2 shouldn't be 20\nThe code can be found in main.py" --verbose
````

Sample output:

```
Iteration 1
Model Thought process: The expression '3 + 7 * 2' should be 17, not 20. I'll check how operator precedence is implemented.

...

Iteration 3
Model Thought process: '+' was mistakenly set to have higher precedence than '*'. Fixing the precedence map.

...

Model Response: I have corrected the operator precedence in `pkg/calculator.py`.
```

---

## 📦 Requirements

- Python 3.8+
- [openai](https://pypi.org/project/openai/) or other LLM SDKs (if you switch models). PS: This project uses Gemini by Google
- Dependencies from `requirements.txt` (if present)

Install using pip:

```bash
pip install -r requirements.txt
```

---

## 🧠 Prompts That Work Well

- `fix the bug where division by zero is not caught`
- `refactor the Calculator class to be more modular`
- `add support for exponentiation (^)`
- `show a better error if the user passes a non-numeric input`
- `make the CLI more user-friendly with argparse`

---

## 🛡️ Safety & Security

This tool gives an LLM access to:

- Read and write files
- Run arbitrary Python code

**USE EXTREME CAUTION** and **only on safe, local environments.** Always commit your changes before running the agent so you can roll back mistakes.

---

## 🧩 Customization

Want to add more power to your agent?

- Add new tools in `agent/tools.py`
- Modify the system prompt for different constraints or capabilities
- Change the LLM model you're using (e.g., switch to Claude or Gemini)
- Add more reasoning steps or safety checks
- Wrap it in a GUI or VSCode extension

---

## 💡 Extending the Project

You've done all the required steps, but have some fun (but carefully... be very cautious about giving an LLM access to your filesystem and python interpreter) with it! See if you can get it to:

- Fix harder and more complex bugs
- Refactor sections of code
- Add entirely new features

You can also try:

- Other LLM providers
- Other Gemini models
- Giving it more functions to call
- Other codebases (Commit your changes before running the agent so you can always revert!)

Remember, what we've built is a toy version of something like Cursor/Zed's Agentic Mode, or Claude Code. Even their tools aren't perfectly secure, so be careful what you give it access to, and don't give this code away to anyone else to use.

This project was created by learning from

<p align="center">
  <img src="https://github.com/bootdotdev/bootdev/assets/4583705/7a1184f1-bb43-45fa-a363-f18f8309056f" style="width:200px;" />
</p>
