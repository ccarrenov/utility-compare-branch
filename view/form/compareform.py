import sys, os, shutil, git
from  PyQt5 import QtWidgets, QtCore, QtGui
from util.git_local_repository import GitLocalRepoUtil
from view.build.doprop import LoadProperties
from view.build.qtcomponents import createPushButton, createLabel,createLabelTitle, createLineEdit, createLineEditDisabled

#load properties
prop = LoadProperties()

class CloneToCompareForm():
   
    def btn_browse_destination(self):
        self.browseButton.clicked.connect(lambda:self.on_click_browse_destination())
        return self.browseButton

    def on_click_browse_destination(self):
        print("ON CLICK BROWSER")
        self.destination.setText(QtWidgets.QFileDialog.getExistingDirectory(self.display, prop.getConfig().get("FORM_PARAMETERS", "form.label.select.folder.destination"), prop.getHome(),QtWidgets.QFileDialog.ShowDirsOnly))

    def cmb_items_projects(self):
        projects = prop.getConfig().get("FORM_PARAMETERS", "form.combobox.projects").split(",")
        self.cmbProjects.addItems(sorted(projects))
        return self.cmbProjects

    def btn_add_project(self):
        self.btnAdd.clicked.connect(lambda:self.on_click_add_project())
        return self.btnAdd
    
    def on_click_add_project(self):
        print("ON CLICK ADD PROJECT")
        selected = self.cmbProjects.currentText()
        if selected not in self.projects:
            self.projects.append(selected)
            self.listSelected.addItem(selected)
        print("selected : {0}".format(selected))

    def btn_clone(self):
        self.btnClone.clicked.connect(lambda:self.on_click_clone())
        return self.btnClone

    def on_click_clone(self):
        #self.loading.start()
        try:
            print("ON CLICK CLONE")
            print("CREATE DIRECTORY")
            directory = self.destination.text()
            rootFolder = os.path.join(directory, prop.getOutPutFolder())
            newfirstFolder = os.path.join(rootFolder, self.firstBranch.text())
            newsecondFolder = os.path.join(rootFolder, self.secondBranch.text())
            print("new folder -> {0}", newfirstFolder)
            print("new folder -> {0}", newsecondFolder)
            url = self.gitrepo.text().split("//")
            originUrl = self.gitrepo.text()
            gitbase = "{0}//{1}:{2}@{3}".format(url[0], prop.getConfig().get("GIT_PARAMETERS", "git.user"), prop.getConfig().get("GIT_PARAMETERS", "git.token"), url[1])
            if os.path.exists(rootFolder):
                shutil.rmtree(rootFolder)
            os.mkdir(rootFolder)
            os.mkdir(newfirstFolder)
            os.mkdir(newsecondFolder)
            for i in range(self.listSelected.count()):
                print("CLONE REPOSITORY")
                project = self.listSelected.item(i).text()
                projectUrl = "{0}/{1}.git".format(gitbase, project)
                projectUrlPrint = "{0}/{1}.git".format(originUrl, project)
                print("CLONE -> {0}".format(projectUrlPrint))            
                branch1 = self.firstBranch.text()
                branch2 =self.secondBranch.text()
                projectPath1 = os.path.join(newfirstFolder, project)
                projectPath2 = os.path.join(newsecondFolder, project)
                branchFirsBranch = git.Repo.clone_from(projectUrl, projectPath1, branch=branch1)
                branchSecondBranch = git.Repo.clone_from(projectUrl, projectPath2, branch=branch2)
            print("FINISH CLONE")
            QtWidgets.QMessageBox.about(self.display, prop.getConfig().get("FORM_PARAMETERS", "form.msg.clone.success.title"), prop.getConfig().get("FORM_PARAMETERS", "form.msg.clone.success.detail"))
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            QtWidgets.QMessageBox.about(self.display, prop.getConfig().get("FORM_PARAMETERS", "form.msg.clone.error.title"), prop.getConfig().get("FORM_PARAMETERS", "form.msg.clone.error.detail"))
        #self.loading.stop()

    def btn_exit(self):
        self.btnExit.clicked.connect(lambda:self.on_click_exit())
        return self.btnExit

    def on_click_exit(self):
        print("ON CLICK EXIT")
        sys.exit()

    def btn_commit_tag(self):
        self.btnCommintTag.clicked.connect(lambda:self.on_click_commit_tag())
        return self.btnCommintTag

    def on_click_commit_tag(self):
        #self.loading.start()
        print("ON CLICK COMMIT & TAG")
        directory = self.destination.text()
        rootFolder = os.path.join(directory, prop.getOutPutFolder())
        print("rootFolder -> {0}".format(rootFolder))
        
        for i in range(self.listSelected.count()):
            print("LOAD REPOSITORY")
            projectFolder = os.path.join(rootFolder,self.branchCommit.text(), self.listSelected.item(i).text())
            print("REPOSITORY -> {0}".format(projectFolder))
            gitCommand = GitLocalRepoUtil(projectFolder)
            gitCommand.addCommitPushCreatePushTag(self.branchComment.text(), self.tag.text())
        print("FIN COMMIT & TAG")
        #self.loading.stop()

    def getFormLayout(self):
        return self.formLayout

    def __init__(self, display, parent=None):
        # PARENT CONSTRUCT
        super().__init__()
        # CLASS PARAMETERS
        self.projects = []
        self.browseButton = createPushButton("form.button.browser");
        self.gitrepo = createLineEdit("form.line.edit.gitrepo")
        self.cmbProjects = QtWidgets.QComboBox()
        self.btnAdd = QtWidgets.QPushButton(prop.getConfig().get("FORM_PARAMETERS", "form.button.add"))
        self.secondBranch = createLineEdit("form.line.edit.second.branch")
        self.listSelected = QtWidgets.QListWidget()
        self.btnClone = createPushButton("form.button.clone")
        self.btnExit = QtWidgets.QPushButton(prop.getConfig().get("FORM_PARAMETERS", "form.button.exit"))
        self.branchCommit = createLineEdit("form.line.edit.branch.commit")
        self.branchComment = createLineEdit("form.line.edit.branch.comment")
        self.tag = createLineEdit("form.line.edit.branch.tag")
        self.btnCommintTag = QtWidgets.QPushButton(prop.getConfig().get("FORM_PARAMETERS", "form.button.commit.tag"))
        self.display = display        
        self.chkCommit = QtWidgets.QCheckBox(prop.getConfig().get("FORM_PARAMETERS", "form.check.commit"))
        self.chkPush = QtWidgets.QCheckBox(prop.getConfig().get("FORM_PARAMETERS", "form.check.push"))
        self.chkTag = QtWidgets.QCheckBox(prop.getConfig().get("FORM_PARAMETERS", "form.check.tag"))  
       
        self.formLayout = QtWidgets.QGridLayout()
        # FORM DEFINITION
        # ROW 1 
        self.formLayout.addWidget(createLabelTitle("form.section.clone"), 0, 1, 1, 1)              
        # ROW 2 
        self.destination = createLineEditDisabled(prop.getHome(), True)
        self.formLayout.addWidget(createLabel("form.label.select.folder.destination"), 2, 1, 1, 1)
        self.formLayout.addWidget(self.destination, 2, 2, 1, 2)
        self.formLayout.addWidget(self.btn_browse_destination(), 2, 4, 1, 1)                    
        # ROW 3
        self.formLayout.addWidget(createLabel("form.label.select.git.base"),3, 1, 1, 1)
        self.formLayout.addWidget(self.gitrepo, 3, 2, 1, 2)
        # ROW 4
        self.firstBranch = createLineEdit("form.line.edit.first.branch")
        self.formLayout.addWidget(createLabel("form.label.select.first.branch"),4, 1, 1, 1)
        self.formLayout.addWidget(self.firstBranch, 4, 2, 1, 2)
        # ROW 5
        self.formLayout.addWidget(createLabel("form.label.select.second.branch"), 5, 1, 1, 1)
        self.formLayout.addWidget(self.secondBranch, 5, 2, 1, 2)
        # ROW 6
        self.formLayout.addWidget(createLabel("form.label.select.project"), 6, 1, 1, 1)
        self.formLayout.addWidget(self.cmb_items_projects(), 6, 2, 1, 2)
        self.formLayout.addWidget(self.btn_add_project(), 6, 4, 1, 1)                    
        # ROW 7
        self.formLayout.addWidget(self.listSelected, 7, 1, 1, 4)
        # ROW 8
        self.formLayout.addWidget(self.btn_clone(), 8, 3, 1, 1)
        self.formLayout.addWidget(self.btn_exit(), 8, 4, 1, 1)
        # ROW 9
        self.formLayout.addWidget(createLabel("form.section.update"), 9, 1, 1, 1)              
        # ROW 10
        self.formLayout.addWidget(createLabel("form.label.select.branch.commit"), 10, 1, 1, 1)
        self.formLayout.addWidget(self.branchCommit, 10, 2, 1, 2)
        # ROW 11
        self.formLayout.addWidget(createLabel("form.label.select.branch.comment"), 11, 1, 1, 1)
        self.formLayout.addWidget(self.branchComment, 11, 2, 1, 2)
        # ROW 12
        self.formLayout.addWidget(createLabel("form.label.select.branch.tag"), 12, 1, 1, 1)
        self.formLayout.addWidget(self.tag, 12, 2, 1, 2)
        # ROW 13
        self.formLayout.addWidget(self.chkCommit, 13, 1, 1, 1)
        self.formLayout.addWidget(self.chkPush, 13, 2, 1, 1)
        self.formLayout.addWidget(self.chkTag, 13, 3, 1, 1)
        # ROW 14
        self.formLayout.addWidget(self.btn_commit_tag(), 14, 4, 1, 1)
        # ROW 15
        #self.lblGif = QtWidgets.QLabel()
        #self.loading = QtGui.QMovie(prop.getLoadGift())     
        #self.lblGif.setMovie(self.loading)        
        #self.formLayout.addWidget(self.lblGif, 15, 1, 1, 1)
        #self.loading.start()