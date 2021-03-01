import os
import argparse
import textwrap


string = '''\
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# PEP 582; used by e.g. github.com/David-OConnor/pyflow
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# input data and models
input/
models/


# data files
*.csv
*.h5
*.pkl
*.pth'''



if __name__ == "__main__":


	currpath = os. getcwd()
	parser = argparse.ArgumentParser()

	parser.add_argument(
		"--pname",
		type=str
	)

	args = parser.parse_args()
	path = os.path.join(currpath, args.pname)

	if os.path.isdir(path) == False:
		os.mkdir(path)

		os.mkdir(os.path.join(path, 'input'))
		os.mkdir(os.path.join(path, 'models'))
		os.mkdir(os.path.join(path, 'notebooks'))
		os.mkdir(os.path.join(path, 'src'))

		f = open(os.path.join(path, 'notebooks', 'exploration_data.ipynb'), 'w+')

		for fname in ['__init__.py', 'config.py', 'create_folds.py', 'dispatcher.py', 'engine.py', 'feature_generator.py', 'loss.py', 'metrics.py', 'models.py', 'predict.py', 'train.py', 'utils.py']:
			f = open(os.path.join(path, 'src', fname), 'w+')
			f.close()

		
		val = str(textwrap.dedent(string))

		f = open(os.path.join(path, '.gitignore'), 'w+')
		
		f.write(val)
			
		f.close()


		for fname in ['LICENCE', 'README.md', 'run.sh']:
			f = open(os.path.join(path, fname), 'w+')
			f.close()


	else:
		print('Already exists')
			
			
			
