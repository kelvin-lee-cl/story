#!/usr/bin/env python3
from flask import Flask, request, jsonify, send_from_directory
import cohere
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create Flask app
app = Flask(__name__)

# Initialize Cohere client
api_key = os.getenv('COHERE_API_KEY')
if not api_key:
    print("ERROR: COHERE_API_KEY not found!")
    exit(1)

print(f"API key loaded: {api_key[:10]}...")
co = cohere.Client(api_key)

@app.route('/')
def home():
    return send_from_directory('static', 'index.html')

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

@app.route('/generate-story', methods=['POST'])
def generate_story():
    try:
        print("Received story generation request")
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
            
        theme = data.get('theme', 'adventure')
        setting = data.get('setting', '')
        plot = data.get('plot', '')
        characters = data.get('characters', '')
        length = data.get('length', 'short')
        
        print(f"Generating story with theme: {theme}, setting: {setting}")
        
        prompt = f"""Write a {length} story with the following elements:
Theme: {theme}
Setting: {setting}
Plot: {plot}
Characters: {characters}

Make it engaging and creative while maintaining a coherent narrative structure."""

        print("Calling Cohere API...")
        response = co.chat(
            model='command-r-08-2024',
            message=prompt,
            max_tokens=1500,
            temperature=0.8
        )
        
        print("Story generated successfully")
        return jsonify({'story': response.text})
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': f'Failed to generate story: {str(e)}'}), 500

if __name__ == '__main__':
    print("Starting Flask app...")
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port, debug=False)
