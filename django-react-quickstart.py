import os,sys

BIN_LOC = '/home/dayo/.local/bin'

def add_to_line(FILE, line, content):
        with open(FILE, 'r') as f:
            contents = f.readlines()

        contents[line] = contents[line].rstrip() + content

        with open(FILE, 'w') as f:
            f.writelines(contents)


def edit_files(project_name, app_name):
    """Update settings.py and package.json for rest_framework """
    SETTINGS = f'{project_name}/backend/backend/settings.py'
    PACKAGE_JSON = f'{project_name}/frontend/package.json'


    c1 = f"\n \t'corsheaders', \n\t'rest_framework', \n\t'{app_name}',\n"
    add_to_line(SETTINGS, 32, c1 )

    c2 = f"\n \t'corsheaders.middleware.CorsMidleware',\n"
    add_to_line(SETTINGS, 44, c2 )
        
    with open(SETTINGS, 'a+') as f:
        f.write("\nCORS_ORIGIN_WHITELIST = ['localhost:3000/']")

    c3 = '\n\t"proxy": "http://localhost:8000",\n'
    add_to_line(PACKAGE_JSON, 3, c3)
    


def make_proj(folder_name, app_name, dest=None):
    """Create project folder and install dependencies"""

    #defaults to creating in desktop
    if dest == None:
        os.chdir("/mnt/c/Users/Oromidayo/Desktop")

    os.mkdir(f'{folder_name}')
    os.chdir(f'{folder_name}')

    pipenv_loc  = BIN_LOC + '/pipenv'
    django_admin_loc  = BIN_LOC + '/django-admin'

    #backend setup
    os.system(f'{pipenv_loc} install django')
    os.system(f'{django_admin_loc} startproject backend')
    os.chdir('backend')
    os.system(f'python3 manage.py startapp {app_name}')
    os.system('python3 manage.py migrate')
    os.system(f'{pipenv_loc} install djangorestframework django-cors-headers')

    os.chdir('..')

    #frontend setup
    os.system('npm install -g create react app && create-react-app frontend')
    os.chdir('frontend')
    os.system('yarn add axios bootstrap reactstrap ')

    os.chdir("../..")

    edit_files(folder_name, app_name)

# sudo npm install -g create react app && create-react-app frontend && cd frontend && yarn add axios bootstrap reactstrap 
   

if __name__ == "__main__":
    try : 
        make_proj(sys.argv[1], sys.argv[2], sys.argv[3])
    except:
        make_proj(sys.argv[1], sys.argv[2])


