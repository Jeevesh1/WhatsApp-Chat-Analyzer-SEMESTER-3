# WhatsApp Chat Analyzer

This project is a simple Python application that analyzes an exported WhatsApp
chat. It uses Streamlit to display charts and statistics in a web browser.

## What this project can show

After uploading a WhatsApp chat file, the application can show:

- Total messages, words, links, and shared media
- Monthly and daily message activity
- Busiest days and months
- Weekly activity using a heatmap
- The most active users in a group chat
- A word cloud and commonly used words
- Frequently used emojis

You can analyze the whole chat or select one user from the sidebar.

## Requirements

You need:

- Python 3
- A WhatsApp chat exported as a `.txt` file
- The following Python packages:

```text
streamlit
pandas
matplotlib
seaborn
wordcloud
emoji
```

## Installation

1. Open a terminal in the project folder.
2. Open the application folder:

   ```bash
   cd whatsapp_chat_analyzer_remake
   ```

3. Install the required packages:

   ```bash
   pip install streamlit pandas matplotlib seaborn wordcloud emoji
   ```

## Running the application

From inside the `whatsapp_chat_analyzer_remake` folder, run:

```bash
streamlit run whatsappanalyzer_main.py
```

Streamlit will open the analyzer in your web browser. If it does not open
automatically, copy the local URL shown in the terminal and open it manually.

## How to use it

1. Open a WhatsApp chat on your phone.
2. Choose **Export chat** and export the chat **without media**.
3. Save the exported `.txt` file on your computer.
4. Start the application using the command above.
5. Upload the `.txt` file using the sidebar.
6. Select **All Users** or a particular user.
7. Click **Show Analysis** to view the results.

## Project structure

```text
Project_Final/
├── README.md
└── whatsapp_chat_analyzer_remake/
    ├── whatsappanalyzer_main.py  # Streamlit application
    ├── filePreprocessor.py       # Converts chat text into a data table
    ├── helpingFunctions.py       # Statistics and analysis functions
    └── stop_hinglish.txt         # Words ignored in word analysis
```

## Note

The application currently expects WhatsApp exports in a date and time format
that matches the format used in the preprocessing code. The stop-word file is
also referenced using a computer-specific file path in the current code, so it
may need to be updated if the project is run on another computer.