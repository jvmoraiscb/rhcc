import launch
from launch.substitutions import Command, LaunchConfiguration
import launch_ros
import os

def generate_launch_description():
    pkg_share = launch_ros.substitutions.FindPackageShare(package='ros2-ackermann').find('ros2-ackermann')
    default_model_path = os.path.join(pkg_share, 'src/description/ackermann_description.urdf')
    default_rviz_config_path = os.path.join(pkg_share, 'rviz/nav_config.rviz')

    robot_state_publisher_node = launch_ros.actions.Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': Command(['xacro ', LaunchConfiguration('model')])}]
    )
    joint_state_publisher_node = launch_ros.actions.Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
    )
    ackermann_node = launch_ros.actions.Node(
        package='ros2-ackermann',
        executable='ackermann_tf2_broadcaster',
        name='broadcaster_ackermann',
        parameters=[
            {'odom_topic_name': 'virtual_odom'},
            {'odom_frame_id': 'odom'},
            {'child_frame_id': 'base_link'}
        ]
    )
    rviz_node = launch_ros.actions.Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', LaunchConfiguration('rvizconfig')],
    )

    return launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(name='model', default_value=default_model_path,
                                            description='Absolute path to robot urdf file'),
        launch.actions.DeclareLaunchArgument(name='rvizconfig', default_value=default_rviz_config_path,
                                            description='Absolute path to rviz config file'),
        joint_state_publisher_node,
        robot_state_publisher_node,
        ackermann_node,
        rviz_node
    ])