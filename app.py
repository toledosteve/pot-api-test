from flask import Flask, jsonify
from potnlp.normalizer.base import DataNormalizer
from potnlp.transliterator import Transliterator, LWS_WNALP
from potnlp.tokenizer.potawatomi import PotawatomiTokenizer
from potnlp.stem.base import PotawatomiLemmatizer

app = Flask(__name__)

@app.route('/stem/vii/<string:message>/target/<string:word>', methods=['GET'])
def stem(message, word):
    normalizer = DataNormalizer()
    text = normalizer.normalize(text=message)
    translit = Transliterator(mapping=LWS_WNALP)
    processed = translit.transliterate(text)
    target_word = translit.transliterate(word)

    tokenizer = PotawatomiTokenizer()
    lemmatizer = PotawatomiLemmatizer()
    
    
    return jsonify({
        "request": {
            "original": message,
            "transliterated": processed
        },
        'stem': lemmatizer.lemmatize(tokenizer.tokenize(processed), target_word)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0')
