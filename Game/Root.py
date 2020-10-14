import os


""" root class-
    parameters: 

   attributes:             
                1.project_root- the path of the project (string) 
                2.project_files_root- the path of the files directory of the project,
                 the pictures and the text files of this project are in this directory.(string)  
    """


class Root:
    # Constructor
    def __init__(self):
        self.project_root = os.path.dirname(os.path.dirname(__file__))
        self.project_files_root = f'{self.project_root}\Files'
