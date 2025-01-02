from ..models.project import Project
from ..extensions import db
from flask import Blueprint, jsonify,request
from datetime import datetime

project_bp=Blueprint("project_bp",__name__, url_prefix='/projects')

@project_bp.route("/")
def get_projects():
    """
        Return a list of all projects
    """
    all_projects = Project.query.all()
    return jsonify({"projects":all_projects})


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
        return jsonify({"message": "Missing required fields"}), 400

    new_project=Project(title=title, budget=budget, start_date=start_date, expected_due=expected_due)
    new_project.save()

    return jsonify({"new Project":new_project.id})
