# Blog Generation System

This project is an AI-powered blog generation system that utilizes LangChain, OpenAI, Groq, Wikipedia, and SerpAPI to generate well-structured blog posts on any given topic.

## Features

- Uses **LangChain** for orchestrating AI agents
- Fetches data from **Wikipedia** and **SerpAPI** for research
- Generates structured blog posts with headings, introduction, content, and summary
- Saves generated blog posts as Markdown files



## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Aniket9977/Upnyx.git
cd blog-generator
```

### 2. Install Dependencies
Ensure you have Python installed, then install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Set Up API Keys
Create a `.env` file and add the following keys:
```env
OPENAI_API_KEY=your_openai_api_key
GROQ=your_groq_api_key
SERPAPI_API_KEY=your_serpapi_key
```

Alternatively, you can set these keys as environment variables.

## Usage
Run the script to generate a blog post on a specific topic:
```bash
python main.py
```
The script will generate a blog post and save it as `blog_post.md`.

## Example Output
```
# Artificial Intelligence in Healthcare

## Introduction
Artificial Intelligence (AI) is revolutionizing the healthcare industry...

## Content
- AI-assisted diagnosis
- Predictive analytics for patient care
- Automation in medical procedures

## Summary
AI continues to improve patient outcomes and medical efficiency...
```

## Troubleshooting
- If you encounter `ValueError: An output parsing error occurred`, try adding `handle_parsing_errors=True` in the `AgentExecutor` initialization.
- If no results are found for Wikipedia or SerpAPI searches, ensure your API keys are valid.

## Contributing
Feel free to fork this repository and submit pull requests for improvements!

## License
This project is licensed under the MIT License.

