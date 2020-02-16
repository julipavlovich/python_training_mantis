from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def get_project_list(self, username, password):
        client = Client(self.app.base_url + "/api/soap/mantisconnect.php" + "?wsdl")
        try:
            list = []
            result=client.service.mc_projects_get_user_accessible(username, password)
            for project in result:
                project = Project(id=project.id, name=str(project.name), status=project.status, enabled=project.enabled, view_status=project.view_status, description=project.description)
                return list.append(project)
        except WebFault:
            return ('SOAP Error')
