import os
import argparse
import textwrap


if __name__ == "__main__":

    currpath = os. getcwd()
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--name",
        type=str
    )

    args = parser.parse_args()
    path = os.path.join(currpath, args.name)

    if os.path.isdir(path) == False:
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
            f = open(os.path.join(path, 'src', fname), 'w+')
            f.close()

        os.mkdir(os.path.join(path, 'src', 'features'))

        f = open(os.path.join(path, 'src', 'feature_generator.py'), 'w+')
        f.close()

        os.mkdir(os.path.join(path, 'src', 'models'))

        for fname in ['config.py', 'dispatcher.py', 'engine.py', 'loss.py', 'metrics.py', 'models.py', 'predict.py', 'train.py', 'utils.py']:
            f = open(os.path.join(path, 'src', fname), 'w+')
            f.close()

        os.mkdir(os.path.join(path, 'src', 'visualization'))

        for fname in ['visualize.py']:
            f = open(os.path.join(path, 'src', fname), 'w+')
            f.close()

        # Gitignore
        with open('./data/gitignore_content.txt') as f:
            lines = f.readlines()

        f = open(os.path.join(path, '.gitignore'), 'w+')
        f.write(str(textwrap.dedent(lines)))
        f.close()

        # Helping files
        for fname in ['LICENCE', 'Makefile', 'README.md', 'requirements.txt', 'run.sh']:
            f = open(os.path.join(path, fname), 'w+')
            f.close()

    else:
        print('Already exists')
