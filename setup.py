from setuptools import setup

package_name = 'ros2_unity_example'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Andy Ponce',
    maintainer_email='andy.ponce@outlook.com',
    description='An example of ros2 communication with unity',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'unity_talker = ros2_unity_example.unity_talker:main'
        ],
    },
)
