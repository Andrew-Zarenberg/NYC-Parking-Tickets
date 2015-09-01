
from flask import Flask, request, render_template
from search import search_plate

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search")
def search():

    plate = request.args.get("plate").upper()

#    r = "<h1>" + plate + "</h1>"

#    r += "<table><tr><th>Date</th><th>Violation</th><th>Borough</th><th>Location</th><th>Fine</th></tr>"
#    r += searchPlate(plate)
#    r += "</table>"

    plate_info = search_plate(plate)

    return render_template("search.html", 
                           plate=plate, 
                           violation_table = plate_info["violation_table"],
                           total_fines = plate_info["total_fines"])




if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0",port=7777)
