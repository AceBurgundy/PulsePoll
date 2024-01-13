from flask import render_template, Blueprint
from Engine.models import Candidate
from typing import List

index: Blueprint = Blueprint('index', __name__, template_folder='templates/index', static_folder='static/index')

@index.get("/")
def _index():
    """
    Load the root page.

    Returns:
    --------
        render_template: Rendered HTML template with necessary data.
    """

    return render_template("index.html")

