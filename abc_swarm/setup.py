from setuptools import setup
import os
from glob import glob

package_name = 'abc_swarm'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.launch.py'))),
        (os.path.join('share', package_name, 'abc_swarm'), glob(os.path.join('abc_swarm', '*.py'))),
        (os.path.join('share', package_name, 'config'), glob(os.path.join('config', '*.cfg'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='chuwei',
    maintainer_email='asdfghjkl@sjtu.edu.cn',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'tribot_tf=abc_swarm.tribot_tf:main',
            'tribot_rmtt_tf=abc_swarm.tribot_rmtt_tf:main',
        ],
    },
)
