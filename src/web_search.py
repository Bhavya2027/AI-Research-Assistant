from langchain_community.tools import DuckDuckGoSearchRun
search = DuckDuckGoSearchRun()

def search_web(query):
    return search.invoke(query) 