from flask import Flask, g, request, render_template # Flask imports


import nltk
nltk.download("punkt")
import numpy as np
from FlagEmbedding import FlagReranker
from sentence_transformers import SentenceTransformer, util
import numpy as np
from scipy import spatial
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')



app = Flask(__name__)


@app.route('/process-text', methods=['POST'])
def process_text():
    data = request.json
    text = data.get('text', '')
    text = text.replace('\n', ' ')

    sentences = nltk.sent_tokenize(text)

    encoded = {} # [encoded] => i
    textdict = {} # [i] => plaintext
    i = 0
    for sentence in sentences:
        encoded[model.encode(sentence)] = i
        textdict[i] = sentence
        i += 1

    shared = []
    shared[0] = encoded
    shared[1] = textdict
    g.shared_data = shared



@app.route('/return-top-queries')
def index():
    data = request.json
    query = data.get('query', '')
    query = model.encode(query)

    comparer = -1000
    encoded = g.shared_data[0] # Dictionary from [encoded] => i
    textdict = g.shared_data[1] # Dictionary from [i] => plaintext

    toret = {
        0 : 
    }
    for i in range(textdict.len()):



if __name__ == '__main__':
    app.run(debug=True)