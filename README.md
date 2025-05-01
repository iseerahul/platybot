# Platy AI Assistant 🤖

A modern AI chatbot powered by Google's Gemini AI that provides intelligent conversations and responses.

## Features ✨

- Real-time chat interface
- Powered by Gemini 2.0 Flash
- Session management
- Error handling
- Clean, modern UI
- Mobile responsive design

## Prerequisites 📋

Before running the project, make sure you have:

- Python 3.8 or higher
- A Google API key for Gemini AI
- Flask web framework

## Installation 🚀

1. Clone the repository:
```bash
git clone https://github.com/yourusername/platybot.git
cd platybot
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root:
```env
GOOGLE_API_KEY=your_google_api_key_here
```

## Running the Application 🏃‍♂️

1. Start the Flask server:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

## Project Structure 📁

```
platybot/
│
├── app.py           # Flask application
├── platy.py         # Core AI logic
├── templates/       # HTML templates
│   └── index.html   # Main chat interface
├── .env            # Environment variables
└── README.md       # Documentation
```

## Configuration ⚙️

You can modify the AI behavior by adjusting parameters in `platy.py`:

- `temperature`: Controls response creativity (0-1)
- `top_p`: Controls response diversity
- `max_output_tokens`: Maximum response length

## Contributing 🤝

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

