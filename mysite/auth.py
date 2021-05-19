from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/')
def home():
  return """<div>
              <form action="/">
                <label for="fname">First name:</label>
                <input type="text" id="fname" name="fname"><br><br>
                <label for="lname">Last name:</label>
                <input type="text" id="lname" name="lname"><br><br>
                <input type="submit" value="Submit">
              </form>
            </div>"""