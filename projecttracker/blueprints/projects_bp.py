from ..models.project import Project
from ..extensions import db
from flask import Blueprint, jsonify,request
from datetime import datetime
from ..models.schemas import project_schema, projects_schema

project_bp=Blueprint("project_bp",__name__, url_prefix='/projects')

@project_bp.route("/")
def get_projects():
    """
        Return a list of all projects
    """
    all_projects = Project.query.all()
    return projects_Schema.dump(all_projects), 200


@project_bp.route("/", methods=["POST"])
def create_project():
    data = request.get_json()
    title=data.get("title")
    budget=data.get("budget")

    start_date=datetime.strptime(data.get("start_date"),  "%m/%d/%Y")
    input_date1 = data.get("start_date")
    input_date2 = data.get("expected_due")

    # Parse the date with the correct format (MM/DD/YYYY)
    start_date = datetime.strptime(input_date1, "%m/%d/%Y")
   
   
    expected_due = datetime.strptime(input_date2, "%m/%d/%Y")
   

    if not all([title, budget, start_date, expected_due]):
        return jsonify({"message": "Missing required fields", "request_data": data}), 400

    new_project=Project(title=title, budget=budget, start_date=start_date, expected_due=expected_due)
    new_project.save()
    # print(new_project)

    return project_Schema.dump(new_project), 201


@project_bp.route("/project/<int:id>", methods=["PUT"])
def update_project(id):
    data = request.get_json()
    project = Project.query.filter_by(id=id).first()
    if not project:
        return jsonify({"message":"Project Not Found"}), 404
    
    project.title = data.get("title", project.title)
    project.budget = data.get("budget", project.budget)
    project.start_date = datetime.strptime(data.get("start_date"), "%m/%d/%Y")
    # project.expected_due = datetime.strptime(data.get("expected_due"), "%m/%d/%Y")
    db.session.commit()
    return project_Schema.dump(project), 200

@project_bp.route("/project/<int:id>/complete", methods=["PUT"])
def complete_project(id):
    project = Project.query.filter_by(id=id).first()
    if not project:
        return jsonify({"message":"Project Not Found"}), 404
    project.actual_due = datetime.now()
    db.session.commit()
    return project_Schema.dump(project), 200



@project_bp.route("/project/<int:id>", methods=["DELETE"])
def delete_project(id):
    project = Project.query.filter_by(id=id).first()
    if not project:
        return jsonify({"message":"Project Not Found"}), 404
    db.session.delete(project)
    db.session.commit()
    return jsonify({"message":"Project Deleted"}), 200


