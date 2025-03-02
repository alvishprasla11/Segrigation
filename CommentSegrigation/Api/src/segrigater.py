import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key = os.getenv("API_KEY"))

def gemini(comment,headings):
    try:
        model = genai.GenerativeModel("gemini-2.0-flash-thinking-exp-01-21")
        if headings == "":
            response = model.generate_content(f"""Take this comment: {comment}      and segrigate it using a broader topic it falls under.it should be one word or two word max only.
                                              and after that inside a bracket write if it is positive/neutral/negative 
                                              so you will be returning just two words the heading it falls under and is it postive/negative/neutral according to you""")
        else:
            response = model.generate_content(f"""Take this comment: {comment}      and segrigate it putting it in one of the {headings} which ever you think it falls under.
                                              and after that inside a bracket write if it is positive/neutral/negative 
                                              so you will be returning just two words the heading it falls under and is it postive/negative/neutral according to you
                                              if it falls under two or three max given headings give them and their positive/neutral/negative  seprated with a comma so max 6 letters that way only and only if it falls or else try to just return 1""")
        # Remove any "Assistant:" prefix from the response

        return response.text

    except Exception as e:
        print(f"Error using Gemini API: {e}")
        return None
    
print(gemini("the food was very bad quality",""))


