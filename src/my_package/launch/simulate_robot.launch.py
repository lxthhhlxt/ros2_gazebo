from launch import LaunchDescription, LaunchContext
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution, TextSubstitution
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    pkg_share = FindPackageShare('my_package')

    context = LaunchContext()
    world_file = PathJoinSubstitution([pkg_share, 'worlds', 'empty.world'])

    urdf_file = PathJoinSubstitution([pkg_share, 'urdf', 'my_robot.urdf'])

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([PathJoinSubstitution([FindPackageShare('ros_gz_sim'), 'launch', 'gz_sim.launch.py'])]),
            launch_arguments={'gz_args': ['-world ', world_file]}.items()
        )
    ])

        # Node(
        #     package = 'robot_state_publisher',
        #     executable = 'robot_state_publisher',
        #     name = 'robot_state_publisher',
        #     output = 'screen',
        #     parameters = [{'robot_description': Command(['cat ', urdf_file])}]
        # ),

        # Node(
        #     package = 'ros_gz_sim',
        #     executable = 'create',
        #     arguments = [
        #         '-name', 'my_robot',
        #         '-topic', 'robot_description',
        #         '-x', '0.0',
        #         '-y', '0.0',
        #         '-z', '0.1'
        #     ],
        #     output = 'screen'
        # ),

        # Node(
        #     package = 'joint_state_publisher',
        #     executable = 'joint_state_publisher',
        #     name = 'joint_state_publisher'
        # )
    # ])