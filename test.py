import requests
import os
# def wikipedia_query(topic):
#     try:
#         url = f"https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&exintro&titles={topic}"

#         response = requests.get(url)
#         data = response.json()
#         pages = data["query"]["pages"]
#         page_id, page_data = next(iter(pages.items()))
#         if "extract" in page_data:
#             return page_data["extract"]
#         return "No information found on Wikipedia for this topic."
#     except Exception as e:
#         return f"Error querying Wikipedia: {str(e)}"
    



# print(wikipedia_query("Python (programming language)"))


import requests

def duckduckgo_search(query):
    try:
        url = f"https://api.duckduckgo.com/?q={query}&format=json"
        response = requests.get(url)
        response.raise_for_status()  # Ensure we catch HTTP errors

        data = response.json()
        results = data.get("Results", [])

        # If no direct results, check "RelatedTopics"
        if not results:
            results = data.get("RelatedTopics", [])

        if not results:
            return "No results found."

        # Debugging: Print the first result to understand its structure
        print("Sample Result:", results[0])  

        # Extract text safely using .get() to prevent KeyErrors
        output = "\n".join([
            f"{item.get('Text', 'No title')} - {item.get('FirstURL', 'No URL')}"
            for item in results[:3]
        ])
        return output
    except Exception as e:
        return f"Error during web search: {str(e)}"

# Test
print(duckduckgo_search("python programming"))
