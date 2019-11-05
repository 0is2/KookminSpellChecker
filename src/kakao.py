from flask import Flask, request, jsonify
from hanspell import spell_checker
import sys
app = Flask(__name__)


@app.route('/keyboard')
def Keyboard():
    dataSend = {
    }
    return jsonify(dataSend)

@app.route('/message', methods=['POST'])
def Message():

    content = request.get_json()
    
    print(content)
    
    content = content['action']
    content = content['params']
    content = content['SpellCheck']
    

    result = spell_checker.check(content)

    dataSend = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "basicCard": {
                        "description": result,
                        "buttons": [
                            {
                                "action":  "block",
                                "label": "맞춤법 검사 또 하기",
                                "blockId": "5da40268ffa7480001daee8c"
                            },
                            {
                                "action":  "block",
                                "label": "이번에는 글자 수 세기",
                                "blockId": "5da4028e8192ac00011584a3"
                            }
                        ]
                    }
                    
                }
            ]
        }
    }
    return jsonify(dataSend)


@app.route('/count', methods=['POST'])
def Count():
    content = request.get_json()
    
    print(content)
    
    content = content['action']
    content = content['params']
    content = content['SpellCheck']
    

    result = "총 " + str(len(content))+"글자입니다."
    
    dataSend = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "basicCard": {
                        "description": result,
                        "buttons": [
                            {
                                "action":  "block",
                                "label": "이번에는 맞춤법 검사하기",
                                "blockId": "5da40268ffa7480001daee8c"
                            },
                            {
                                "action":  "block",
                                "label": "다시 한 번 글자 수 세기",
                                "blockId": "5da4028e8192ac00011584a3"
                            }
                        ]
                    }
                    
                }
            ]
        }
    }
    return jsonify(dataSend)
    
    
    
    

if __name__ == "__main__":
    app.run(host='0.0.0.0')