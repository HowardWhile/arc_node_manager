from setuptools import setup

package_name = "arc_node_manager"

setup(
    name=package_name,
    version="0.0.0",
    packages=[package_name],
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools"],

    zip_safe=True,
    maintainer="Howard Cheng",
    maintainer_email="makubex49@gmail.com",
    description="ros2 node manager",
    license="LGPL-3.0-only",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": ["node_manager = arc_node_manager.arc_node_manager:main"],
    },
)
