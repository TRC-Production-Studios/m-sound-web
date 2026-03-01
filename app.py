from flask import Flask, render_template, abort
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'data'))
from products import PRODUCTS

app = Flask(__name__)

# ── Team ────────────────────────────────────────────────────
TEAM = [
    {
        "name": "Jurschujit1",
        "role": "Founder",
        "bio": "No bio yet :(",
        "avatar": "Jur"
    },
    {
        "name": "TheROcraft",
        "role": "Co-Founder & Website-Developer",
        "bio": "I am good at designing and backend programming of systems.",
        "avatar": "Trc"
    },
    {
        "name": "Taco",
        "role": "Co-Owner",
        "bio": "No bio yet :(",
        "avatar": "🌮"
    }
]

# ── FAQ ─────────────────────────────────────────────────────
FAQ = [
    {
        "q": "Does M sound also rent out their equipment?",
        "a": "No, we do not rent our products. Our Roblox sound products are available for purchase only. With your purchase, you receive a license to use the respective product."
    },
    {
        "q": "Is there technical support after purchase?",
        "a": "Of course! You can simply create a ticket on our Discord server if you need help with a product! However, if you configure the product yourself, i.e., change the model or add your own script, we will not be able to help you!"
    },
    {
        "q": "Can I test products before buying?",
        "a": "Of course! We have a testing experience on roblox where you can test all of our products!"
    }
]

# ── YouTube Trailer (Video-ID anpassen) ────────────────────
YOUTUBE_VIDEO_ID = "g1Ih64NYpwk"  # ← Hier deine YouTube-Video-ID eintragen

# ── Routes ──────────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html",
                           team=TEAM, faq=FAQ,
                           youtube_id=YOUTUBE_VIDEO_ID,
                           page="home")

@app.route("/shop")
def shop():
    tag = None
    products = PRODUCTS
    return render_template("shop.html", products=products, page="shop")

@app.route("/shop/<product_id>")
def product_detail(product_id):
    product = next((p for p in PRODUCTS if p["id"] == product_id), None)
    if not product:
        abort(404)
    return render_template("product_detail.html", product=product, page="shop")

@app.route("/datenschutz")
def datenschutz():
    return render_template("datenschutz.html", page="datenschutz")

@app.route("/impressum")
def impressum():
    return render_template("impressum.html", page="impressum")

if __name__ == "__main__":
    app.run(debug=True)
