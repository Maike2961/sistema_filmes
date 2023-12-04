from flask import Flask, render_template, request
import urllib.request, json


app = Flask(__name__)

avaliacoes = []

@app.route("/")
def home():
    return render_template("menu.html")

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        if request.form.get("nome") and request.form.get("nota"):
            avaliacoes.append({"nome": request.form.get("nome"), "nota": request.form.get("nota")})
    return render_template("cadastro.html", avaliacoes=avaliacoes)

@app.route("/filmes/<propriedade>")
def lista(propriedade):
    
    if propriedade == 'populares':
        url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=c9f8d754d895a1934300c630740ed857"
    elif propriedade == 'kids':
        url = "https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key=c9f8d754d895a1934300c630740ed857"
    elif propriedade == '2010':
        url = "https://api.themoviedb.org/3/discover/movie?primary_release_year=2010&sort_by=vote_average.desc&api_key=c9f8d754d895a1934300c630740ed857"
    elif propriedade == 'drama':
        url = "https://api.themoviedb.org/3/discover/movie?with_genres=18&sort_by=vote_average.desc&vote_count.gte=10&api_key=c9f8d754d895a1934300c630740ed857"
    elif propriedade == 'tom_cruise':
        url = "https://api.themoviedb.org/3/discover/movie?with_genres=878&with_cast=500&sort_by=vote_average.desc&api_key=c9f8d754d895a1934300c630740ed857"
    
    resposta = urllib.request.urlopen(url)
    dados = resposta.read()
    jsondata = json.loads(dados)
    return render_template("lista.html", filmes=jsondata['results'])

if __name__ == ("__init__"):
    app(debug=True)