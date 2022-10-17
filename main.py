from flask import Flask
from functions import get_all, format_candidates, get_by_pk, get_by_skills

app = Flask(__name__)


@app.route("/")
def page_main():
    """
    Главная страница
    """
    candidates = get_all()
    result = format_candidates(candidates)

    return result


@app.route("/candidate/<int:uid>")
def page_candidate(uid):
    """
    Поиск кандидата
    """
    candidate = get_by_pk(uid)
    if candidate in get_all():
        result = f"<img src='({candidate['picture']})'>"
        result += format_candidates([candidate])
    else:
        result = "Нет такого кандидата"
    return result


@app.route("/skills/<skill>")
def page_skills(skill):
    """
    Поиск кандидата по навыку
    """
    candidate = get_by_skills(skill.lower())
    result = format_candidates(candidate)
    return result


app.run()
