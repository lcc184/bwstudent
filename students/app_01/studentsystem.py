from students.app_01 import app_1
from ..models import Student
from .. import db
from flask import render_template, request, redirect, url_for

# 主页面 GET POST
@app_1.route("/",methods=["GET"])
def get_index():
    students = Student.query.all()
    print("students",students)
    error1 = request.args.get("error1")

    if error1:
        return render_template("index.html", error1=error1,students=students)

    if not students:
        return render_template("index.html", error="暂无数据信息")
    else:

        return render_template('index.html',students=students)
@app_1.route("/post_index",methods=["POST"])
def post_index():
    id = request.form.get("id")
    name = request.form.get("name")
    english = request.form.get("english")
    python = request.form.get("python")
    c = request.form.get("c")
    if all([id,name,english,python,c]):
        artcle1 = Student(id=id, name=name, English=english, Python=python, C=c,
                          Grade_num=int(english)+int(python)+int(c))
        db.session.add(artcle1)
        db.session.commit()
        return redirect(url_for("app_1.get_index"))
    else:
        return redirect(url_for("app_1.get_index",error1="请输入完整"))

# 修改功能GET POST
@app_1.route("/get_alter/<int:id>",methods=['GET'])
def get_alter(id):
    student_one = Student.query.filter_by(id=id).first()
    print("stu",student_one)
    return render_template("alter.html",student_one=student_one)
@app_1.route("/post_alter/<int:id>",methods=['POST'])
def post_alter(id):
    print(id,"id")
    name = request.form.get("name")
    english = request.form.get("english")
    python = request.form.get("python")
    c = request.form.get("c")
    if all([id, name, english, python, c]):
        student_one = Student.query.filter_by(id=id).first()
        print("student_one",student_one)
        student_one.id=id
        student_one.name=name
        student_one.English=english
        student_one.Python=python
        student_one.C=c
        student_one.Grade_num=int(float(english))+int(float(python))+int(float(c))
        db.session.commit()
        return redirect(url_for("app_1.get_alter",id=id))
    else:
        return redirect(url_for("app_1.get_alter", error1="请输入完整"))

# 删除功能 GET
@app_1.route("/delete/<int:id>",methods=['GET'])
def delete(id):
    try:
        student_one = Student.query.filter_by(id=id).first()
        db.session.delete(student_one)
        db.session.commit()
    except Exception:
        return redirect(url_for("app_1.get_index",error1="无法删除，没有此数据"))
    return redirect(url_for("app_1.get_index"))

# 查询功能POST（此处有bug）
@app_1.route("/post_search",methods=["POST"])
def post_search():
    search = request.form.get("search")
    print(search)
    try:
        search = int(search)
        students = Student.query.filter_by(id=search)
    except Exception as e:

        students = Student.query.filter(Student.name.endswith(search)).all()
        print("students_searchstudents_search",students)
    if not students:
        return redirect(url_for("app_1.get_index",error1="暂无数据信息"))
    return render_template('index.html',students=students)

