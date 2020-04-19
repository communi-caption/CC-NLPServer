import tensorflow as tf
import json
from flask import Flask, request, jsonify
from deepsegment import DeepSegment

app = Flask(__name__)
segmenter = None

@app.route("/", methods=['GET'])
def index():
    return "ok"

@app.route("/segment", methods=['POST'])
def train():
    res = segmenter.segment_long("bu bir yazıdır bu da bi yazıdır", n_window=7)
    return json.dumps(res)

if __name__ == '__main__':
    data_set = "trained/altyazilar_not_456_senteces"
    f_checkpoint = data_set + "/checkpoint"
    f_params = data_set + "/params"
    f_utils = data_set + "/utils"

    segmenter = DeepSegment(lang_code=None, checkpoint_path=f_checkpoint, params_path=f_params, utils_path=f_utils, tf_serving=False, checkpoint_name=None)
    
    app.run(debug=False, threaded=False, port=5007)