from model.project import Project


def test_add_project(app):
    old_projects = app.soap.get_project_list("administrator", "root")
    project = Project(name="Project for test 24")
    app.project.add_project(project)
    new_projects = app.soap.get_project_list("administrator", "root")
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
