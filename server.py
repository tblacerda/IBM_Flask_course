"""
Flask web server for the Emotion Detection application.
Provides routes for the home page and emotion analysis using the EmotionDetection package.
"""
from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

# Home page (renders index.html that is already provided in templates/)
@app.route("/")
def index():
    """Render the home page (index.html)."""
    return render_template("index.html")


# Emotion detection endpoint
@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    """Detect the emotion of a text provided as a query parameter.
    Query Parameter:
        textToAnalyze (str): Text to analyze for emotions.
    Returns:
        str: Formatted string with emotion scores and dominant emotion, or
             an error message if input is invalid.
    """
    # get statement from query parameter (?text=...)
    text_to_analyse = request.args.get("textToAnalyze", "").strip()

    if not text_to_analyse:
        return "Invalid text! Please try again!"

    # run the emotion detection
    result = emotion_detector(text_to_analyse)

    if result.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    # format the response string as per requirement
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
