from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/mantisbt-2.23.0/")


    def open_project_manage_page(self):
        wd = self.app.wd
        wd.get("http://localhost/mantisbt-2.23.0/manage_proj_page.php")

    def add_project(self, project):
        wd = self.app.wd
        self.open_project_manage_page()
        wd.find_element_by_xpath("//button[@type='submit']").click()
        self.fill_project_info(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.open_project_manage_page()

    def fill_project_info(self, project):
        wd = self.app.wd
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)

    def delete_project(self, project):
        wd = self.app.wd
        self.open_project_manage_page()
        wd.find_element_by_link_text(project).click()
        # wd.find_element_by_xpath("(//a[contains(text(),'%s')])[3]" % project).click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()

    project_cache = None

    def get_project_list(self):
        # if self.project_cache is None:
        wd = self.app.wd
        self.open_project_manage_page()
        self.project_cache = []
        # list_projects = wd.find_elements_by_css_selector("tbody")
        for element in wd.find_elements_by_css_selector("tbody td a"):
            projectname = element.text
             # projectname = row.text
             # if projectname != "General":
            self.project_cache.append(Project(name=projectname))
        return list(self.project_cache)
