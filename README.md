# LLM-Powered Prompt Router for Intent Classification

## Project Overview

This project implements an **LLM-powered prompt routing system** that classifies a user's message into a specific intent and routes it to a specialized expert persona.

Instead of using one generic prompt, the system first **detects the user's intent** and then **delegates the request to a specialized expert prompt** designed for that task.

This architecture improves response quality and reflects how many **real-world AI applications** are built.

---

# System Architecture

The application follows a **two-stage pipeline**:

```
User Message
      ↓
Intent Classification (LLM)
      ↓
Intent Label + Confidence Score
      ↓
Prompt Router
      ↓
Expert Persona Prompt
      ↓
Final Response
      ↓
Request Logging
```

### Steps in the Pipeline

1. **User Message**
   The user inputs a query into the system.

2. **Intent Classification**
   A Large Language Model (LLM) analyzes the message and classifies it into one of several predefined intents.

3. **Intent Label and Confidence Score**
   The classifier returns a JSON object containing the predicted intent and confidence score.

4. **Prompt Router**
   Based on the detected intent, the system selects a specialized prompt.

5. **Expert Persona Response**
   The selected expert persona generates the response.

6. **Logging**
   Each request is recorded in a log file for observability and debugging.

---

# Supported Intents

| Intent    | Description                                    |
| --------- | ---------------------------------------------- |
| `code`    | Programming questions and debugging            |
| `data`    | Data analysis, statistics, and datasets        |
| `writing` | Writing improvement and feedback               |
| `career`  | Career advice and professional guidance        |
| `unclear` | Requests that cannot be confidently classified |

---

# Expert Personas

The system includes four expert personas.

### Code Expert

Provides technical programming advice and debugging help.

### Data Analyst

Helps interpret datasets, statistics, and data patterns.

### Writing Coach

Suggests improvements in clarity, tone, and sentence structure.

### Career Advisor

Provides career guidance and professional advice.

---

# Project Structure

```
prompt-router/
│
├── main.py
├── classifier.py
├── router.py
├── prompts.py
├── logger.py
├── test_cases.py
├── route_log.jsonl
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env.example
└── README.md
```

### File Description

**main.py**
Runs the interactive command-line application.

**classifier.py**
Uses a Large Language Model to classify user intent.

**router.py**
Routes requests to the appropriate expert persona.

**prompts.py**
Stores the expert system prompts.

**logger.py**
Logs each request and response in JSON format.

**test_cases.py**
Runs automated tests using sample user messages.

**route_log.jsonl**
Stores request logs for monitoring and debugging.

**Dockerfile**
Defines the containerized environment for the application.

**docker-compose.yml**
Runs the containerized application using Docker Compose.

**.env.example**
Documents required environment variables.

---

# Environment Variables

Create a `.env` file using `.env.example`.

Example:

```
HF_API_KEY=your_huggingface_api_key
OPENAI_API_KEY=your_openai_api_key
```

These keys are used for accessing LLM services.

---

# Installation (Local Run)

Clone the repository:

```
git clone <repository_url>
cd prompt-router
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the application:

```
python main.py
```

---

# Running the Application with Docker

Build and run the container:

```
docker compose up --build
```

Alternatively run interactively:

```
docker compose run --rm prompt-router
```

This starts the CLI application inside a Docker container.

Example interaction:

```
You: how do i sort a list in python?

Detected Intent: {'intent': 'code', 'confidence': 0.47}

Assistant:
Code Expert Advice:
Break the problem into steps and use built-in Python functions.
```

---

# Running Test Cases

The project includes a test suite with multiple sample prompts.

Run:

```
python test_cases.py
```

This executes several example messages and prints the detected intent and response.

---

# Logging System

Every request is logged in:

```
route_log.jsonl
```

Each log entry contains:

```
{
 "message": "...",
 "intent": "...",
 "confidence": 0.85,
 "response": "..."
}
```

This provides transparency and debugging capability.

---

# Manual Override Feature

Users can bypass the classifier and manually specify an intent using the `@intent` syntax.

Example:

```
@code write a python loop
```

This forces the router to send the request directly to the **Code Expert**.

---

# Technologies Used

* Python
* HuggingFace LLM (Zero-Shot Classification)
* Requests Library
* JSON Logging
* Docker
* Docker Compose

---

# Key Features

* LLM-based intent classification
* Prompt routing architecture
* Multiple expert personas
* Confidence threshold handling
* Manual override capability
* Request logging
* Automated testing
* Docker containerization

---

# Conclusion

This project demonstrates a **production-style prompt routing architecture** where an LLM is used to classify user intent and route requests to specialized prompts.

Such systems are widely used in modern AI applications to improve response quality and maintain modular system design.

