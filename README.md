# Profile website - XSS vulnerability

Repositório criado para a workshop de ataques de segurança realizada no Colégio Internato dos Carvalhos a 24/05/2023.

Para comandos em windows é recomendado utilizar a PowerShell.

Na pasta `/project` encontra-se o website criado usando [Flask](https://flask.palletsprojects.com/en/2.3.x/quickstart/). 

Na pasta `/evil_website` encontram-se o website de phishing (`/evil_website/project`) e os scripts de XSS (`evilscript.js` e `evilscript_base.js`).

A apresentação encontra-se na pasta `/presentation`.

## Para iniciar website vulnerável:

### Com Python

Necessita de ter `python3` instalado. Executar na pasta raiz que contem o repositório:

```
pip install -r requirements.txt
export FLASK_APP='project' # em windows powershell: $env:FLASK_APP = 'project'
export FLASK_DEBUG='1' # em windows powershell: $env:FLASK_DEBUG = '1'
flask run --host=0.0.0.0 --port=5000
```

### Com Docker
Com [Docker engine](https://www.docker.com/products/docker-desktop/) instalado e a correr:
```
docker image build -t profile_app .

docker run -p 5000:5000 -d profile_app
```

## Para iniciar website phishing:

### Com Python

Necessita de ter `python3` instalado. Executar na pasta `evil_website`:

```
pip install -r requirements.txt
export FLASK_APP='project' # em windows powershell: $env:FLASK_APP = 'project'
export FLASK_DEBUG='1' # em windows powershell: $env:FLASK_DEBUG = '1'
flask run --host=0.0.0.0 --port=4000
```

### Com Docker
Com [Docker engine](https://www.docker.com/products/docker-desktop/) instalado e a correr:
```
docker image build -t evil_app .

docker run -p 4000:4000 -d evil_app
```

## Links para self learning:

- [XSS Google game - Experimentar XSS](https://xss-game.appspot.com/)
- [TryHackMe - Introdução a segurança informática prática e Capture the Flag](https://tryhackme.com/)
- [OWASP WebGoat - Website com lições hosted localmente para aprendizagem de vulnerabilidades comuns](https://github.com/WebGoat/WebGoat)
