from flaskr import app
from flaskr.aws import auto_scaling

# start auto-scaling
auto_scaling.auto_scaling()

app.run('127.0.0.1', port=5001, debug=False)