from flask import Flask
app = Flask(__name__)

@app.route("/locations/<state>")
def getPostsByState(state):
    
    # return list of posts
    return {}

if __name__ == "__main__":
    app.run(debug=True)