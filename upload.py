import os
import shutil


def submit():
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    shutil.rmtree('dist')
    shutil.rmtree('build')
    shutil.rmtree('drf_display_integer_choice_field.egg-info')


if __name__ == '__main__':
    submit()
