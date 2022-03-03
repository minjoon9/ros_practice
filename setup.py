import os
from glob import glob
from setuptools import setup

package_name = 'minjoon'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', 'minjoon'), glob('launch/*_launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='minjoon',
    maintainer_email='minjoon@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = minjoon.minjoon_pub:main',
            'listener = minjoon.minjoon_sub:main',
            'service = minjoon.service_member_function:main',
            'client = minjoon.client_member_function:main',
            'param_talker = minjoon.python_parameters_node:main',
        ],
    },
)
