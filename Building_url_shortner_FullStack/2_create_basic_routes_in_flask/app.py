from flask import Flask, request, redirect, render_template, url_for, flash
import random
import string
from models import (
    init_db,
    insert_url,
    get_url,
    get_all_urls,
    increment_visit_count,
    delete_url_by_code
)

app = Flask(__name__)
app.secret_key = "supersecretkey" 
init_db()


def generate_short_code(length=6):
    """Generate a random short code."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


@app.route("/", methods=["GET", "POST"])
def index():
    """Home page – show all URLs and form to add a new one."""
    if request.method == "POST":
        original_url = request.form["url"]
        short_code = generate_short_code()

        # Handle duplicate short_code case
        while get_url(short_code):
            short_code = generate_short_code()

        insert_url(original_url, short_code)
        flash(f"Short URL created: http://localhost:5000/{short_code}", "success")
        return redirect(url_for("index"))

    all_urls = get_all_urls()
    return render_template("index.html", all_urls=all_urls)


@app.route("/<short_code>")
def redirect_to_url(short_code):
    """Redirect to the original URL when short link is visited."""
    url_data = get_url(short_code)
    if url_data:
        increment_visit_count(short_code)
        return redirect(url_data["original_url"])
    else:
        flash("Short URL not found!", "error")
        return redirect(url_for("index"))


@app.route("/delete/<short_code>", methods=["POST"])
def delete_url(short_code):
    """Delete a short URL."""
    delete_url_by_code(short_code)
    flash("URL deleted successfully.", "info")
    return redirect(url_for("index"))


@app.route("/about")
def about_page():
    """Simple About page."""
    return "This is the About page."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


