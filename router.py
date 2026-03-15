from prompts import PROMPTS


def route_and_respond(message: str, intent_data: dict):

    intent = intent_data.get("intent", "unclear")

    if intent == "unclear":
        return "I'm not sure what you need help with. Could you please clarify your request?"

    if intent == "code":
        return f"""
Code Expert Advice:
For programming problems like: "{message}"

Break the problem into steps.
Use correct syntax and built-in Python functions where possible.
Test your code and handle errors carefully.
"""

    if intent == "data":
        return f"""
Data Analyst Insight:
For the question: "{message}"

Think about statistical measures like mean, median, or correlations.
Use charts such as bar graphs or scatter plots to visualize patterns.
"""

    if intent == "writing":
        return f"""
Writing Coach Feedback:
Regarding: "{message}"

Focus on clarity, tone, and sentence structure.
Avoid passive voice and unnecessary filler words.
"""

    if intent == "career":
        return f"""
Career Advisor Suggestion:
For your statement: "{message}"

Consider your skills, interests, and long-term goals.
Build relevant projects and learn industry tools.
Networking and continuous learning are important.
"""

    return "Sorry, I cannot process this request."