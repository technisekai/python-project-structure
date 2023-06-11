import os
import sys

def create_dir_structure(root_dir: str):
    """
        Function to create project structure
        param:
            - root_dir:
                type: string
                explain: name of root directory/project name
        output:
            - project directory
    """
    # store function/classes which needed by project
    os.makedirs(f"{root_dir}/{root_dir}/helpers")
    os.makedirs(f"{root_dir}/{root_dir}/constants")
    open(f"{root_dir}/{root_dir}/constants/constants.py", 'x')
    # save raw / processed data 
    os.makedirs(f"{root_dir}/data/processed")
    os.makedirs(f"{root_dir}/data/raw")
    # create your jupyter notebook here
    os.makedirs(f"{root_dir}/experiments")
    open(f"{root_dir}/experiments/{root_dir}.ipynb", 'x')
    # tests the scripts
    os.makedirs(f"{root_dir}/tests")
    open(f"{root_dir}/tests/tests.py", 'x')
    # make main py
    open(f"{root_dir}/main.py", 'x')

def show_helps():
    """
        Function will print available flag in this program.
        Param:
            None
        Output:
            None
    """
    print("\033[1;37m Available flag: ")
    print("       -p [project_name] : will create project directory with name [project_name]")

if __name__ == '__main__':
    flag = sys.argv[1]
    if flag == '-p':
        project_name = sys.argv[2]
        create_dir_structure(project_name)
        print(f"\033[1;32m[ \u2713 ] Success create project {project_name} \n")
    else:
        print("\033[1;31m[ \u2717 ] Flag is not Available!")
        show_helps()
