from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
        ),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            parameters=[
                {
                    'robot_description': ParameterValue(
                        Command(['xacro ', '/home/tomer/arm_ws/src/arm_description/urdf/Arm_description.urdf']),
                        value_type=str
                    )
                }
            ],
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
        )
    ])
