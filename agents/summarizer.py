from tools.research_tool import llm

def run_summarizer(raw_data: dict):
    def stringify(value):
        if isinstance(value, list):
            return "\n".join([str(v) for v in raw_data.values()])
        return str(value)
    
    combined_text = "\n".join([stringify(v) for v in raw_data.values()])
    prompt = f"""
You are an expert career roadmap planner.

When the user asks about career paths, courses, or preparation strategies, provide a structured roadmap from beginner to expert.

Recommend specific courses and learning resources from platforms like Coursera, edX, DeepLearning.AI, and others.

First,strictly maintain the maximum number of nodes as 20.

Break down the career roadmap into clear **phases** using the following format:

Phase -> Subtopics -> Recommended Tools or Concepts -> Estimated time to complete

🔁 Use arrows (->) **only**. Do **not** use colons, asterisks (*), dots (.), slashes (/) or lists. Wrap multi-word terms with underscores (e.g., Machine_Learning, Data_Structures).

Example:
AI_Engineer -> Programming_Fundamentals -> Python_SQL_Libraries -> 4_weeks  
AI_Engineer -> ML_Foundations -> Scikit_Learn_Pandas_Numpy -> 3_weeks

✳️ Ensure:
- 12 to 20 roadmap paths
- Realistic timelines and achievable steps
- Encourage user commitment and consistency
- Every path must start from a clear role (e.g., AI_Engineer, Data_Scientist)

Use the following context to build the roadmap:
{combined_text}
"""


    response = llm.invoke(prompt)
    try:
        return response["choices"][0]["message"]["content"]
    except Exception:
        return str(response)

