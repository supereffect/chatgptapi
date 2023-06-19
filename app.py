from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

# Flask uygulamasını oluşturun
app = Flask(__name__)
CORS(app)
# API anahtarını ayarlayın
openai.api_key = 'apikey giriniz'
# API endpoint'ini tanımlayın
@app.route('/ask', methods=['POST'])
def get_persons():
    # JSON isteğini al
    #
#     {
#     "soru":"sen kimsin",
#     "tanimlar":["Adın Egehan AI,Kısa cevaplar ver"]
#     }
    #
    data = request.get_json()
    # Kullanıcıdan soruyu al
    input_text = data['soru']
    tanimlar = data['tanimlar']
    messages = [
        {"role": "user", "content": f"{input_text}"},
    ]
    for tanim in tanimlar:
        messages.append({"role": "system", "content": tanim})
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',  
        messages=messages,
        max_tokens=50,  # İstenilen cevap uzunluğu
        temperature=0,
        frequency_penalty=0,
        presence_penalty=0
    )
    # Cevabın JSON döndürülmesi
    cevap = response["choices"][0]["message"]["content"]
    return jsonify({'cevap': cevap})

# Flask uygulaması çalıştırılması.
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8081)


#docker build -t app .
