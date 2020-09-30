from constantes.const import TOKEN_GITHUB
from flask import Flask, render_template
from bs4 import BeautifulSoup
from github import Github

repositorios=[]
repositorio=[]
Git_Hub="https://github.com/NicoCaz?tab=repositories"

g = Github(TOKEN_GITHUB)

app=Flask(__name__,template_folder="templates")

@app.route('/')
def home():
    for repo in g.get_user().get_repos():

        if repo.url.find("NicoCaz"):    

            repositorio.append(repo.name)
            repositorio.append(repo.url)
            repositorios.append(repositorio)
            repositorio.clear()

    return render_template("Home.html",repositorios=repositorios)
    
@app.route("/about")
def about():
    return render_template("about.html")


if __name__ ==  "__main__":
    app.run(debug=True)