from model.project import Project
import random


def test_del_project(app):
    # app.session.login("administrator", "root")
    if len(app.soap.get_project_list("administrator", "root")) == 0:
        project = Project(name="Project for test 0")
        app.projects.create_project(project)
    old_projects = app.soap.get_project_list("administrator", "root")
    project = random.choice(old_projects)
    project_name = project.name
    app.project.delete_project(project_name)
    new_projects = app.soap.get_project_list("administrator", "root")
    assert len(old_projects)-1 == len(new_projects)
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
