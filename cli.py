from reviewhub import create_app

def run():
    app = create_app()
    app.run(debug=True, use_reloader=True)
