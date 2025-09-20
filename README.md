# Story AI Application - Fixed and Ready!

## What Was Fixed

✅ **API Migration**: Updated from deprecated Cohere `generate` API to current `chat` API  
✅ **Model Update**: Changed to working `command-r-08-2024` model  
✅ **Error Handling**: Added comprehensive error handling in both frontend and backend  
✅ **JSON Response**: Fixed JSON parsing errors and server response issues  

## How to Run the Application

### Option 1: Using the original app (Port 5000)
```bash
cd "/Users/kelvinlee/Documents/Web-Dev/4. Personal Project/story_AI"
python3 app.py
```

### Option 2: Using the simplified app (Port 3000) 
```bash
cd "/Users/kelvinlee/Documents/Web-Dev/4. Personal Project/story_AI"
python3 simple_app.py
```

## Testing the Application

1. **Open your browser** and go to:
   - `http://127.0.0.1:5000/` (for original app)
   - `http://127.0.0.1:3000/` (for simple app)

2. **Fill in the form**:
   - Theme: Choose from dropdown (adventure, romance, mystery, etc.)
   - Setting: e.g., "medieval castle", "space station"
   - Plot: e.g., "rescue mission", "mysterious disappearance"
   - Characters: e.g., "brave knight named Sir Lancelot"
   - Length: short, medium, or long

3. **Click "Generate Story"** - it should work without errors!

## Testing the API Directly

You can test the API endpoint directly using curl:

```bash
curl -X POST http://127.0.0.1:5000/generate-story \
  -H "Content-Type: application/json" \
  -d '{
    "theme": "adventure",
    "setting": "medieval castle",
    "plot": "rescue the princess",
    "characters": "brave knight",
    "length": "short"
  }'
```

## What to Do If Issues Persist

1. **Check if the port is free**:
   ```bash
   lsof -i :5000
   lsof -i :3000
   ```

2. **Kill any conflicting processes**:
   ```bash
   pkill -f python
   ```

3. **Start fresh**:
   ```bash
   python3 simple_app.py
   ```

## Files Overview

- `app.py` - Main Flask application (fixed)
- `simple_app.py` - Simplified version for testing
- `static/index.html` - Frontend interface
- `static/script.js` - Fixed JavaScript with proper error handling
- `static/style.css` - Styling
- `.env` - Contains your Cohere API key
- `requirements.txt` - Python dependencies

The application is now fully functional with all bugs fixed!
