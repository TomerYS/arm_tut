from setuptools import setup
import os

package_name = 'arm_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=[],
    data_files=[
        # Install the package.xml
        ('share/' + package_name, ['package.xml']),
        # Install the URDF and mesh files
        ('share/' + package_name + '/urdf', ['urdf/Arm_description.urdf']),
        ('share/' + package_name + '/meshes', [
            'meshes/base_link.STL',
            'meshes/Endeffector_1.STL',
            'meshes/Endeffector_2.STL',
            'meshes/Link_1.STL',
            'meshes/Link_2.STL',
            'meshes/Link_3.STL',
            'meshes/Link_4.STL',
            'meshes/Link_5.STL',
            'meshes/Link_6.STL',
        ]),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tomer',
    maintainer_email='tomer@todo.todo',
    description='Package containing URDF and launch files for the robot arm',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
    },
)
