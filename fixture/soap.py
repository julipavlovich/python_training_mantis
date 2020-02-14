from suds.client import Client
from suds import WebFault


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def get_project_list(self, username, password):
        client = Client(self.app.base_url + "/api/soap/mantisconnect.php" + "?wsdl")
        try:
            return client.service.mc_projects_get_user_accessible(username, password)
        except WebFault:
            return ('SOAP Error')
