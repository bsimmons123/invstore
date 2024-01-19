from flask_cors import CORS

from application import create_app

app = create_app()


def main():
    app.run()

    # enable CORS
    CORS(app, resources={r'/*': {'origins': '*'}})


if __name__ == '__main__':
    main()
