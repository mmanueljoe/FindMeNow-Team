from flask  import Flask,render_template
from config import Config

app = Flask(__name__)

#Add database
app.config.from_object(Config)
db = SQLAlchemy(app)




