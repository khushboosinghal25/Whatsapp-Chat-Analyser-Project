# WhatsApp Chat Analysis

A Streamlit application to analyze your WhatsApp chat data. This tool helps you understand your chat patterns, such as the most active hours, the frequency of messages, and the usage of emojis.

## Features

- Upload WhatsApp chat text files and preprocess them.
- Analyze chat data by user, date, time, and more.
- Visualize data with interactive charts and graphs.
- Extract and display emoji usage statistics.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/khushboosinghal25/Whatsapp-Chat-Analyser-Project.git
    cd whatsapp-chat-analysis
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit application:
    ```bash
    streamlit run main.py
    ```

2. Open your browser and go to `http://localhost:8501`.

3. Upload your WhatsApp chat text file using the sidebar.

4. Explore the various analyses and visualizations.

## Preprocessing

The preprocessing function extracts and structures the WhatsApp chat data, splitting it into user messages, dates, and various other components. It also identifies and extracts emojis used in the chats.
