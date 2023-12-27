from flask import Flask
from vii import InanimateIntransitive_Stemmer

app = Flask(__name__)

@app.route('/stem/vii/<string:verb>', methods=['GET'])
def stem(verb):
    vii = InanimateIntransitive_Stemmer()
    return vii.is_potential_vii_ending(verb)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
