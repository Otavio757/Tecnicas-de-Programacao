from flask import Flask
from flask import request
from uni_string_builder import StringBuilder
from uni_twitter import * 

app = Flask(__name__)

@app.route('/')
def index():
    # sb = StringBuilder()
    sb = ""
    # sb.Append("Informe o termo de pesquisa: ")
    # sb.Append("<form method='get' action='/'>")
    # sb.Append("<input type='text' name='hashtag' />")
    # sb.Append("<input type='submit' value='Pesquisar' />")
    # sb.Append("</form>")
    sb+=("Informe o termo de pesquisa: ")
    sb+=("<form method='get' action='/pesquisar'>")
    sb+=("<input type='text' name='hashtag' />")
    sb+=("<input type='submit' value='Pesquisar' />")
    sb+=("</form>")
    sb+="<hr/>"
    sb+=("Leaked password checker: ")
    sb+=("<form method='get' action='/pwned'>")
    sb+=("<input type='text' name='hashtag' />")
    sb+=("<input type='submit' value='Pesquisar' />")
    sb+=("</form>")
    return sb

@app.route('/pesquisar')
def twitter_search():
    hashtag = request.args.get('hashtag')
    return single_query_twitter(hashtag)

# @app.route('/pwned')
# def twitter_search():
#     hashtag = request.args.get('hashtag')
#     obj = Dataset()
#     return obj.query_external_api(hashtag)