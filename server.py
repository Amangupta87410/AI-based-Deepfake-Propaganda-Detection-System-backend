# This Python script uses the Flask framework to create a simple web server (API).
# When the frontend sends a request to the '/api/analyze' endpoint, this server
# processes it, simulates an AI analysis, and returns the results as JSON.

# --- Required Libraries ---
# To run this code, you need to install Flask:
# pip install Flask
# pip install Flask-Cors

from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import time

# --- Flask App Initialization ---
# Create a new Flask web server application.
app = Flask(__name__)
# Enable CORS (Cross-Origin Resource Sharing) to allow our HTML page 
# to make requests to this server from a different origin.
CORS(app)


# --- AI Model Simulation ---
# In a real-world application, this function would contain the complex logic
# to load a pre-trained AI model (like TensorFlow or PyTorch), download the
# content from the URL, and perform the actual deepfake analysis.
# For this prototype, it just returns a random pre-defined result.
def perform_ai_analysis(url):
    """
    Simulates a time-consuming AI analysis on the given URL.
    Returns a dictionary with the analysis results.
    """
    print(f"Received URL for analysis: {url}")
    print("Starting simulated AI analysis...")
    
    # Simulate the time it takes for the model to run
    time.sleep(3) 

    # --- Mock Scenarios ---
    # These are the same scenarios we used in the frontend, but now they live
    # on the server. The server will pick one randomly and send it back.
    scenarios = [
        { "isDeepfake": True, "confidence": 96.5, "manipulationType": 'Facial Synthesis, Voice Cloning', "threat": { "name": 'Harmful Propaganda', "level": 'High', "color": 'bg-red-500/80' }, "authDetails": 'Content does NOT match any video in the official government archives. Significant digital artifacts detected.', "counterNarrate": 'This viral video is AI-generated. Analysis shows facial and voice manipulation. Here is the authentic version released by [Source/Govt].' },
        { "isDeepfake": False, "confidence": 88.2, "manipulationType": 'Misleading Context (Edited Clip)', "threat": { "name": 'Misleading', "level": 'Medium', "color": 'bg-yellow-500/80' }, "authDetails": 'The video clip is authentic but has been edited and presented out of its original context to create a false narrative.', "counterNarrate": 'This clip is being shared with a false claim. The original, unedited video shows a different context. View the full footage here: [Link to Source].' },
        { "isDeepfake": True, "confidence": 91.0, "manipulationType": 'Lip Sync Manipulation', "threat": { "name": 'Satirical / Joke', "level": 'Low', "color": 'bg-blue-500/80' }, "authDetails": 'Content is clearly marked as parody. Facial manipulation detected, consistent with entertainment purposes.', "counterNarrate": 'This video is a parody created for entertainment. While it uses AI technology, it is not intended to deceive.' },
        { "isDeepfake": False, "confidence": 99.8, "manipulationType": 'None Detected', "threat": { "name": 'Authentic Content', "level": 'None', "color": 'bg-green-500/80' }, "authDetails": 'Content cross-verified with 3 official sources. No signs of digital tampering found. The content is authentic.', "counterNarrate": 'This content has been verified as authentic and can be trusted.' }
    ]
    
    result = random.choice(scenarios)
    print("Analysis complete. Sending result to frontend.")
    return result


# --- API Endpoint Definition ---
# This defines the URL that our frontend will call.
# It's set to handle POST requests at the '/api/analyze' path.
@app.route('/api/analyze', methods=['POST'])
def analyze_content():
    """
    This function is executed when the frontend sends a request here.
    """
    try:
        # Get the JSON data sent from the frontend
        data = request.get_json()
        
        # Check if the 'url' key exists in the received data
        if not data or 'url' not in data:
            return jsonify({"error": "URL is missing from request"}), 400

        content_url = data['url']
        
        # Call our AI analysis function
        analysis_result = perform_ai_analysis(content_url)
        
        # Return the result as a JSON response
        return jsonify(analysis_result)

    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": "An internal server error occurred"}), 500


# --- Main Execution Block ---
# This code runs when you execute the script directly (e.g., `python server.py`).
if __name__ == '__main__':
    # Starts the Flask development server.
    # It will be accessible at http://127.0.0.1:5000
    # The `debug=True` argument enables auto-reloading when you save changes.
    app.run(host='0.0.0.0', port=5000, debug=True)