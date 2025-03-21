# News Aggregator with MCP & Claude Desktop

## Overview

This project is a real-time news aggregator that retrieves and summarizes news from multiple sources using Claude Desktop as the client and MCP (VS Code) as the host. It fetches news from sources like BBC, Ars Technica, TechCrunch, and IPLT20 and allows users to bookmark articles and set news preferences.

## Features

- Fetch real-time news from BBC, TechCrunch, Ars Technica, and IPLT20.
- MCP-powered backend using `FastMCP` for efficient data retrieval.
- User preferences to customize news categories.
- Bookmark articles for later reading.
- Asynchronous fetching using `httpx` and `asyncio` for fast data retrieval.

## Tech Stack

- **Programming Language**: Python (>=3.9 recommended)
- **Framework**: MCP (`fastmcp`)
- **Libraries**:
  - `httpx` for making async HTTP requests
  - `beautifulsoup4` for web scraping
  - `dotenv` for environment variables
  - `mcp[cli]` for communication with Claude Desktop

## Installation

### Prerequisites

Ensure you have Python installed (recommended **Python >=3.9** instead of `3.13` as in `pyproject.toml`).

### Installing UV

UV is an alternative package manager that provides faster dependency resolution. Install UV using the following commands:

#### Windows

```powershell
scoop install uv
```

#### MacOS

```bash
brew install uv
```

### Installing Dependencies with UV

After installing UV, you can install project dependencies using:

```bash
uv pip install -r requirements.txt
```

### Installing UV via PowerShell Script

For automated installation of UV on Windows, create and run the following PowerShell script:

```powershell
$ProgressPreference = 'SilentlyContinue'
Invoke-WebRequest -Uri "https://github.com/astral-sh/uv/releases/latest/download/uv-installer.exe" -OutFile "uv-installer.exe"
Start-Process -FilePath "uv-installer.exe" -Wait
Remove-Item "uv-installer.exe"
```

### Steps to Run:

```bash
# Clone the repository
git clone https://github.com/your-username/news-aggregator-mcp.git
cd news-aggregator-mcp

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'

# Install dependencies using pip or UV
pip install -r requirements.txt  # OR
uv pip install -r requirements.txt
```

## Configuration

Create a `.env` file to store API keys or other environment variables if needed.

```env
USER_AGENT="news-app/1.0"
```

## Running the Application

```bash
python main.py
```

## Setting Up Claude Desktop & MCP Configuration

### 1. Download Claude Desktop  
Download Claude Desktop from the following link:  
[Claude Desktop Download](https://claude.ai/download) 

### 2. Open Settings  
Go to the **top left corner**, click on **File**, then select **Settings**.  
![Screenshot 2025-03-21 231858](https://github.com/user-attachments/assets/96c94bbc-5ac2-454b-a150-74a66b4a3a5e)


### 3. Enable Developer Mode  
Inside the settings menu, enable **Developer Mode** to allow editing the MCP configuration.  
![Screenshot 2025-03-21 232009](https://github.com/user-attachments/assets/fb948d6a-a5db-4c5f-b09f-ec53001e9aff)


### 4. Edit MCP Configuration JSON  
Locate the configuration file and edit it using Notepad. The file should be formatted as follows:  
![Screenshot 2025-03-21 232223](https://github.com/user-attachments/assets/67c9fef1-bce9-48cb-bf9c-1496971af29a)


```json
{
    "mcpServers": {
        "mcp-server-project": {
            "command": "C:\\Users\\Devanshu\\.local\\bin\\uv",
            "args": [
                "--directory",
                "C:\\Users\\Devanshu\\OneDrive\\Desktop\\new_mcp\\new_mcp",
                "run",
                "main.py"
            ]
        }
    }
}
```

### 5. Edit with Notepad  
Open the JSON file with **Notepad** or any text editor and make the necessary changes.  
![Screenshot 2025-03-21 232344](https://github.com/user-attachments/assets/b70b51f6-4728-4fbe-b9b6-a789e732c290)


## MCP Overview

The Model Context Protocol (MCP) allows applications to provide context for large language models (LLMs) in a standardized way, separating the concerns of providing context from the actual LLM interaction. This Python SDK implements the full MCP specification, making it easy to:

- Build MCP clients that can connect to any MCP server.
- Create MCP servers that expose resources, prompts, and tools.
- Use standard transports like `stdio` and `SSE`.
- Handle all MCP protocol messages and lifecycle events.

### Adding MCP to Your Python Project

We recommend using UV to manage your Python projects. In a UV-managed Python project, add MCP to dependencies by:

```bash
uv add "mcp[cli]"
```

Alternatively, for projects using pip for dependencies:

```bash
pip install mcp
```

### Running the Standalone MCP Development Tools

To run the MCP command with UV:

```bash
uv run mcp
```

### Quickstart

You can install this server in Claude Desktop and interact with it right away by running:

```bash
mcp install server.py
```

Alternatively, you can test it with the MCP Inspector:
Use this for the vscode 
```bash
mcp dev server.py
```

## MCP Tools Available

This project uses MCP tools to interact with the news aggregator through predefined commands.

### Tool Context

MCP (Message Control Protocol) is used to facilitate communication between different components of the application. In this project, MCP enables the backend to efficiently process and distribute news articles. The tools allow the system to fetch, store, and manage news articles dynamically, ensuring real-time interaction between the user and the news data. MCP runs within VS Code, acting as the middleware between the client (Claude Desktop) and the external news sources.

### Available MCP Commands

| Command                                           | Description                                                       |
| ------------------------------------------------- | ----------------------------------------------------------------- |
| `get_tech_news(source: str)`                      | Fetches latest news from the given source (BBC, TechCrunch, etc.) |
| `get_all_articles()`                              | Retrieves all stored news articles                                |
| `get_user_preferences(user_id: str)`              | Gets news preferences for a user                                  |
| `bookmark_article(user_id: str, article_id: str)` | Bookmarks an article for a user                                   |

## Future Improvements

- Store articles in a lightweight database (SQLite/TinyDB) instead of memory.
- Add better error handling for `httpx` requests.
- Improve summarization using NLP techniques.
- Enhance the UI for better user experience (if a frontend is added).

## Contributing

Feel free to open issues or submit pull requests to improve this project.

## License

This project is licensed under the MIT License.
```
