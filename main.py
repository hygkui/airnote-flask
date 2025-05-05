from flask import Flask, jsonify, request
import os
import time
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.proxies import WebshareProxyConfig

ytt_api = YouTubeTranscriptApi(
    proxy_config=WebshareProxyConfig(
        proxy_username="qxqpylkl",
        proxy_password="zx1am1p88x8h",
    )
)

app = Flask(__name__)


@app.route('/')
def index():
    video_id = request.args.get('videoId')
    print('video_id', video_id)

    start_time = time.time()
    transcript = ytt_api.fetch(video_id)
    end_time = time.time()

    fetch_duration = end_time - start_time
    print(f'got transcript len {len(transcript)}, fetch time: {fetch_duration:.4f} seconds')

    # output=''
    # for x in transcript:
    #     sentence = x['text']
    #     output += f' {sentence}\n'

    # print(output)
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅 ghh", "transcript": transcript})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
