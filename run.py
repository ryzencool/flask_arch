import os, sys

sys.path.append(os.path.abspath("../../"))

from app import app_starter

if __name__ == "__main__":
    app_starter.run(debug=True)