import sys, os, shutil,configparser, git

class GitLocalRepoUtil():

    def status(self):
        try:
            print (self.repo.git.status())
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)

    def repo(self):
        return self.repo

    def add(self):
        try:
            self.repo.git.add(".")
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)

    def commit(self, comment):
        try:
            self.repo.git.commit(m=comment)
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)

    def push(self):
        try:
            origin = self.repo.remote("origin")
            origin.push()  
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)

    def createPushTag(self, tag, comment):
        try:
            origin = self.repo.remote("origin")
            self.repo.create_tag(tag, message=comment)
            origin.push(tag)  
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e) 

    def addCommitPushCreatePushTag(self, comment, tag):                                                                
        self.add()
        self.status()
        self.commit(comment)
        self.push()
        self.createPushTag(tag, comment)

    def __init__(self, projectFolder, parent=None):
        self.projectFolder = projectFolder
        self.repo = git.Repo(projectFolder)       