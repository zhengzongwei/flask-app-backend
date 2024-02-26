export FLASK_APP=app

flask db init

flask db migrate


flask db upgrade