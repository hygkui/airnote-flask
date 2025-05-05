from flask import Flask, jsonify, request
import os
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)


@app.route('/')
def index():
    video_id = request.args.get('videoId')
    print(video_id)

    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    print(transcript)

    output=''
    for x in transcript:
        sentence = x['text']
        output += f' {sentence}\n'

    print(output)
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅 ghh", "transcript": output})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
