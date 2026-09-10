# AI Question Answering App

## Project Overview

AI Question Answering App is a simple and interactive web application built using **Python, Streamlit, and the Hugging Face Inference API**. It allows users to ask questions in natural language and receive AI-generated answers using the **OpenAI GPT-OSS 120B** large language model.

## Project Objective

The objective of this project is to demonstrate how **Large Language Models (LLMs)** can be integrated into a Streamlit application to build an intelligent question-answering system.

## Features

* Ask questions in natural language
* AI-generated answers using an LLM
* Interactive Streamlit interface
* Fast responses through the Hugging Face Inference API
* Beginner-friendly implementation

## Technologies Used

* Python
* Streamlit
* Hugging Face Hub (`InferenceClient`)
* Hugging Face Inference API
* OpenAI GPT-OSS 120B

## Project Structure

```text
AI-Question-Answering/
│
├── app.py
├── requirements.txt
├── .streamlit/
│   └── secrets.toml
└── README.md
```

## Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/your-username/AI-Question-Answering.git
```

### Step 2: Open the project folder

```bash
cd AI-Question-Answering
```

### Step 3: Install the required libraries

```bash
pip install -r requirements.txt
```

## Requirements

```text
streamlit
huggingface_hub
```

## Configure the API Token

Create a `.streamlit/secrets.toml` file and add your Hugging Face API token:

```toml
HF_TOKEN = "your_hugging_face_token"
```

## Run the Application

Execute the following command:

```bash
streamlit run app.py
```

The application will automatically open in your web browser.

## How It Works

1. Open the Streamlit application.
2. Enter a question in the text area.
3. Click **Ask AI**.
4. The question is sent to the Hugging Face Inference API.
5. The GPT-OSS 120B model generates an answer.
6. The AI response is displayed on the screen.

## Example

### Input

```text
What is Artificial Intelligence?
```

### Output

```text
Artificial Intelligence is the simulation of human intelligence in machines that can learn, reason, solve problems, and make decisions.
```

## Future Enhancements

* Chat history
* Multiple LLM model selection
* Real-time streaming responses
* Improved user interface
* Better error handling

## Learning Outcomes

* Large Language Models (LLMs)
* Hugging Face Inference API
* Streamlit web application development
* Natural Language Processing
* Python for AI applications

## Author

**Keerthiga K U**

B.Sc. Computer Science with Artificial Intelligence

SDNB Vaishnav College for Women
