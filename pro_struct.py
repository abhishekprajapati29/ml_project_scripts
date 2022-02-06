import os
import argparse


if __name__ == "__main__":

    currpath = os.getcwd()
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--name",
        type=str
    )

    parser.add_argument(
        "--ename",
        type=str
    )

    args = parser.parse_args()

    if args.name:
        path = os.path.join(currpath, args.name)
        if os.path.isdir(path) == True:
            print("Folder already Exists")
            quit()

        os.mkdir(path)

        # Data
        os.mkdir(os.path.join(path, 'data'))

        os.mkdir(os.path.join(path, 'data', 'external'))
        os.mkdir(os.path.join(path, 'data', 'interim'))
        os.mkdir(os.path.join(path, 'data', 'processed'))
        os.mkdir(os.path.join(path, 'data', 'raw'))

        # Docs
        os.mkdir(os.path.join(path, 'docs'))

        # Models
        os.mkdir(os.path.join(path, 'models'))

        # Notebooks
        os.mkdir(os.path.join(path, 'notebooks'))

        # Reports
        os.mkdir(os.path.join(path, 'report'))

        # Src
        os.mkdir(os.path.join(path, 'src'))

        f = open(os.path.join(path, 'src', '__init__.py'), 'w+')
        f.close()

        os.mkdir(os.path.join(path, 'src', 'data'))

        for fname in ['dataset.py', 'create_folds.py']:
            f = open(os.path.join(path, 'src/data', fname), 'w+')
            f.close()

        os.mkdir(os.path.join(path, 'src', 'features'))

        f = open(os.path.join(path, 'src/features',
                 'feature_generator.py'), 'w+')
        f.close()

        os.mkdir(os.path.join(path, 'src', 'models'))

        for fname in ['config.py', 'dispatcher.py', 'engine.py', 'loss.py', 'metrics.py', 'models.py', 'predict.py', 'train.py', 'utils.py']:
            f = open(os.path.join(path, 'src/models', fname), 'w+')
            f.close()

        os.mkdir(os.path.join(path, 'src', 'visualization'))

        for fname in ['visualize.py']:
            f = open(os.path.join(path, 'src/visualization', fname), 'w+')
            f.close()

        # Gitignore
        with open(os.path.join(currpath, 'data/gitignore_content.txt'), 'r') as f:
            lines = f.readlines()

        with open(os.path.join(path, '.gitignore'), 'w+') as f:
            f.write("\n". join(lines))

        # Helping files
        for fname in ['LICENCE', 'Makefile', 'README.md', 'requirements.txt', 'run.sh']:
            f = open(os.path.join(path, fname), 'w+')
            f.close()

        print('Project Structure Successfully Created\n\n')

        if args.ename:
            ename = os.path.join(currpath, args.name, args.ename)
            os.mkdir(ename)

            # Data
            os.mkdir(os.path.join(ename, 'data'))

            # Docker File
            for fname in ['Dockerfile', 'README.md']:
                f = open(os.path.join(ename, fname), 'w+')
                f.close()

            with open(os.path.join(currpath, "data", "dockerfile.txt"), 'r') as f:
                lines = f.readlines()

            with open(os.path.join(ename, "Dockerfile"), 'w+') as f:
                f.write("\n".join(lines))

            os.system("docker build -t " + args.ename + " " + ename)

            os.system("docker run --name " + args.ename + "_container" + " -v /" + args.ename + ":/" +
                      args.ename + "  -w /" + args.ename + " -p 8888:8888 " + args.ename)

            # Successful

    else:
        print('Project Name Required!')

    # Environment Path
