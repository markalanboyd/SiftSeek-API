"""
The run.py file is the entrypoint for running SiftSeek app. Pay close attention
to which app config is fed into the app factory.
"""

from siftseek import create_app

app = create_app("dev")

if __name__ == "__main__":
    app.run(debug=True)
