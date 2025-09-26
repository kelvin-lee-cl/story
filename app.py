from flask import Flask, request, jsonify
import cohere
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder='static', static_url_path='')
co = cohere.Client(os.getenv('COHERE_API_KEY'))

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/generate-story', methods=['POST'])
def generate_story():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No data provided'}), 400
            
        theme = data.get('theme', 'adventure')
        setting = data.get('setting', 'modern day')
        plot = data.get('plot', 'a journey')
        characters = data.get('characters', 'a hero')
        length = data.get('length', 'short')

        prompt = f"""Write a {length} story with the following elements:
        Theme: {theme}
        Setting: {setting}
        Plot: {plot}
        Characters: {characters}
        
        Make it engaging and creative while maintaining a coherent narrative structure."""

        # Check if API key is available
        if not os.getenv('COHERE_API_KEY'):
            return jsonify({'error': 'Cohere API key not configured'}), 500

        response = co.chat(
            message=prompt,
            max_tokens=2000,
            temperature=0.8
        )

        return jsonify({'story': response.text})
        
    except Exception as e:
        print(f"Error generating story: {str(e)}")
        return jsonify({'error': f'Failed to generate story: {str(e)}'}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
