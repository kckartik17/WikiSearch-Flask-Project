from flask import Flask, request, render_template
import wikipedia

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")

    else:
        query = request.form.get('query')
        summary = ""
        try:
            summary = wikipedia.summary(query)
        except wikipedia.exceptions.DisambiguationError as e:
            summary="Too many results for searched keyword. Try specific from {}".format(e.options)
        except wikipedia.exceptions.PageError:
            summary="Error: Query doesn't match any results."
        
        return render_template("summary.html",summary=summary,query=query)

if __name__ == "__main__":
    app.run(use_reloader=True)