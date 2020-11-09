from flask import Flask, request, jsonify
from flasgger import Swagger
import Scraper_league_headless

app = Flask(__name__)
Swagger(app)

@app.route('/')
def wel():
    return "Welcome!"

@app.route('/search_username', methods=['POST'])
def prediction():
    """Who do you want to search?
    ---
    parameters:
        - name: Username 1
          in: query
          type: string
          required: true
    responses:
        200:
            description: The output value          
    """
    
    u1 = request.args.get("Username 1")
    # u2 = request.args.get("Username 2")
    # u3 = request.args.get("Username 3")

    goal = Scraper_league_headless.scrape(u1)
    return str(goal)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

        # - name: Username 2
        #   in: query
        #   type: string
        #   required: false
        # - name: Username 3
        #   in: query
        #   type: string
        #   required: false   