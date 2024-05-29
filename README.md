# AI-Blogging-assistant

## Overview
The AI Blogging Assistant is a tool designed to help bloggers generate high-quality content efficiently using the Gemini-Pro language model. This assistant can suggest topics, generate drafts, and improve existing content.

## Features
- Topic suggestion
- Draft generation
- Content improvement
- Grammar and spell check
- SEO optimization tips

## Installation

To install the AI Blogging Assistant, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/your-username/ai-blogging-assistant.git
    cd ai-blogging-assistant
    ```

2. **Create a virtual environment** (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up your API keys**:
    - Create a file named `api_key.py` in the root directory of the project.
    - Add your Gemini-Pro API key in `api_key.py`:
      ```python
      API_KEY = 'your-gemini-pro-api-key'
      ```

## Usage

To use the AI Blogging Assistant, run the `app.py` file:

```sh
streamlit app.py
