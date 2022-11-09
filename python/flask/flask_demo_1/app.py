from flask import Flask, render_template, request, jsonify

app = Flask(__name__)



@app.route('/url_test')
def url_test():

    # http://127.0.0.1:5000/url_test?val1=1&val2=9   


    test1=request.args.get('val1')
    test2=request.args.get('val2')
    test3=int(test1)+int(test2)
    return "<h1> my result is {} </h1> ".format(test3)



if __name__ == '__main__':
    app.run()
