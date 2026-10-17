from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities  import WikipediaAPIWrapper
from langchain_core.tools import tool
from datetime import datetime


search = DuckDuckGoSearchRun()

@tool("search")
def search_tool(query : str) -> str:
  """Search the web for information"""
  return search.run(query)

api_wrapper = WikipediaAPIWrapper(top_k_results = 1, doc_content_chars_max = 100)

wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)

@tool("save_to_txt")
def save_to_txt(data: str, filename: str = "research_output.txt") -> str:
    """Save research data to a text file"""

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    formatted_text = f"--- Reasearch Output---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)

    return f"Data saved to {filename}"