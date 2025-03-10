from langchain.llms import OpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import WikipediaQueryRun
from langchain.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from langchain.utilities import SerpAPIWrapper
import os


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERPAPI_API_KEY =os.getenv("SERPAPI_API_KEY")
serpapi_tool = SerpAPIWrapper(serpapi_api_key=SERPAPI_API_KEY)
llm = OpenAI(api_key=OPENAI_API_KEY, temperature=0.7)
wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
serp_search = SerpAPIWrapper()
search_tool = Tool(
    name="Search",
    func=serp_search.run,
    description="Search the web for up-to-date information on a given topic."
)
wiki_tool = Tool(
    name="Wikipedia",
    func=wikipedia.run,
    description="Fetch information from Wikipedia about a given topic."
)


agent = initialize_agent(
    tools=[search_tool, wiki_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True
)

def generate_blog(topic):
    """Generates a blog post based on a given topic."""
    prompt = f"""
    Generate a well-structured blog post on the topic: {topic}.
    And the output is in the formate that is given below.
    Content should be 400 words long.
    The blog should have the following sections:
    - Heading
    - Introduction
    - Content (detailed information) of all the content also 
    - Summary
    Ensure the content is well-researched and engaging.
    
    """
    result = agent.run(prompt)
    return result





if __name__ == "__main__":
    blog_topic = "The impact of artificial intelligence on society"
    blog_post = generate_blog(blog_topic)  
    
    if blog_post:  
        print("\nGenerated Blog Post:\n")
        print(blog_post)  
        with open("blog_post.md", "w", encoding="utf-8") as f:
            f.write(blog_post)
        print("\nBlog post saved as 'blog_post.md'")
    else:
        print("Error: No blog post was generated.")
