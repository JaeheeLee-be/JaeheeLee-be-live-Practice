# TODO: app폴더에서 create_app을 import하세요
from app import create_app

# TODO: create_app()을 활용하여 Flask 앱을 생성하세요
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)