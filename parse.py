from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

# Load env vars
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("❌ GOOGLE_API_KEY not found. Please set it in your .env or environment variables.")

# Prompt template
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. *Extract Information:* Only extract the information that directly matches the provided description: {parse_description}. "
    "2. *No Extra Content:* Do not include any additional text, comments, or explanations in your response. "
    "3. *Empty Response:* If no information matches the description, return an empty string (''). "
    "4. *Direct Data Only:* Your output should contain only the data that is explicitly requested, with no other text."
)

# ✅ Use faster Gemini Flash model
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",   # ⚡ much faster than gemini-pro
    temperature=0,
    google_api_key=api_key
)

def parse_with_gemini(dom_chunks, parse_description, max_length=4000):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parsed_result = []
    
    for i, chunk in enumerate(dom_chunks, start=1):
        # ✅ Trim to avoid huge slow requests
        chunk = chunk[:max_length]

        response = chain.invoke(
            {"dom_content": chunk, "parse_description": parse_description}
        )
        result_text = response.content if hasattr(response, "content") else str(response)
        print(f"parse batch {i} of {len(dom_chunks)}")
        if result_text.strip():
            parsed_result.append(result_text.strip())
    
    return "\n".join(parsed_result)
