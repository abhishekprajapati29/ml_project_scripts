import os


class ProjectCreate:
    def __init__(self, name, ename):
        self.name = name
        self.ename = ename
        self.currpath = os.getcwd()
        self.path = os.path.join(self.currpath, self.name)

    def ProjectStructure(self):
        if os.path.isdir(self.path) == True:
            print("Folder already Exists")
            quit()

        os.mkdir(self.path)

        # Data
        os.mkdir(os.path.join(self.path, 'data'))

        os.mkdir(os.path.join(self.path, 'data', 'external'))
        os.mkdir(os.path.join(self.path, 'data', 'interim'))
        os.mkdir(os.path.join(self.path, 'data', 'processed'))
        os.mkdir(os.path.join(self.path, 'data', 'raw'))

        # Docs
        os.mkdir(os.path.join(self.path, 'docs'))

        # Models
        os.mkdir(os.path.join(self.path, 'models'))

        # Notebooks
        os.mkdir(os.path.join(self.path, 'notebooks'))

        # Reports
        os.mkdir(os.path.join(self.path, 'report'))

        # Src
        os.mkdir(os.path.join(self.path, 'src'))

        f = open(os.path.join(self.path, 'src', '__init__.py'), 'w+')
        f.close()

        os.mkdir(os.path.join(self.path, 'src', 'data'))

        for fname in ['dataset.py', 'create_folds.py']:
            f = open(os.path.join(self.path, 'src/data', fname), 'w+')
            f.close()

        os.mkdir(os.path.join(self.path, 'src', 'features'))

        f = open(os.path.join(self.path, 'src/features',
                 'feature_generator.py'), 'w+')
        f.close()

        os.mkdir(os.path.join(self.path, 'src', 'models'))

        for fname in ['config.py', 'dispatcher.py', 'engine.py', 'loss.py', 'metrics.py', 'models.py', 'predict.py', 'train.py', 'utils.py']:
            f = open(os.path.join(self.path, 'src/models', fname), 'w+')
            f.close()

        os.mkdir(os.path.join(self.path, 'src', 'visualization'))

        for fname in ['visualize.py']:
            f = open(os.path.join(self.path, 'src/visualization', fname), 'w+')
            f.close()

        # Gitignore
        with open(os.path.join(self.currpath, 'data/gitignore_content.txt'), 'r') as f:
            lines = f.readlines()

        with open(os.path.join(self.path, '.gitignore'), 'w+') as f:
            f.write("\n". join(lines))

        # Helping files
        for fname in ['LICENCE', 'Makefile', 'README.md', 'requirements.txt', 'run.sh']:
            f = open(os.path.join(self.path, fname), 'w+')
            f.close()

        print('Project Structure Successfully Created\n\n')

    # Docker

    def DockerEnv(self):
        docker_path = os.path.join(self.currpath, self.name, self.ename)
        os.mkdir(docker_path)

        # Data
        os.mkdir(os.path.join(docker_path, 'data'))

        # Docker File
        for fname in ['Dockerfile', 'README.md']:
            f = open(os.path.join(docker_path, fname), 'w+')
            f.close()

        with open(os.path.join(self.currpath, "data", "dockerfile.txt"), 'r') as f:
            lines = f.readlines()

        with open(os.path.join(docker_path, "Dockerfile"), 'w+') as f:
            f.write("\n".join(lines))

        os.system("docker build -t " + self.ename + " " + docker_path)

        os.system("docker run --name " + self.ename + "_container" + " -v /" + self.ename + ":/" +
                  self.ename + "  -w /" + self.ename + " -p 8888:8888 " + self.ename)


if __name__ == "__main__":
    print("Create your Project:-")
    print("Project Name: ", end="")
    name = str(input())
    print("Docker Container Name: ", end="")
    ename = str(input())

    obj = ProjectCreate(name, ename)
    obj.ProjectStructure()
    obj.DockerEnv()
