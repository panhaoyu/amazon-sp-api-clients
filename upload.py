import os
import shutil


def main():
    # shutil.rmtree('dist', ignore_errors=True)
    version = 'patch'  # patch, minor, major, prepatch, preminor, premajor, prerelease
    # os.system(f'poetry version {version}')
    # os.system(f'poetry publish --build')
    os.system(f'git add "pyproject.toml"')
    version_number = os.popen('poetry version').read().split(' ')[1]
    os.system(f'git commit -m "v{version_number}: new {version} version"')
    os.system('git push origin HEAD')


if __name__ == '__main__':
    main()
