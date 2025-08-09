.. _diff_to_ros1:

Differences to ros_control (ROS 1)（与 ros_control (ROS 1) 的差异）
==================================

Hardware Structures - classes（硬件结构 - 类）
-----------------------------

The ros_control framework uses the ``RobotHW`` class as a rigid structure to handle any hardware.

ros_control 框架使用 ``RobotHW`` 类作为处理任何硬件的刚性结构。

This makes it impossible to extend the existing robot with additional hardware, like sensors, actuators, and tools, without coding.

这使得在不编码的情况下无法使用额外的硬件（如传感器、执行器和工具）扩展现有机器人。

The ``CombinedRobotHardware`` corrects this drawback.

``CombinedRobotHardware`` 纠正了这个缺点。

Still, this solution is not optimal, especially when combining robots with external sensors.

尽管如此，这个解决方案仍然不是最优的，特别是在将机器人与外部传感器结合时。

The ros2_control framework defines three types of hardware ``Actuator``, ``Sensor`` and ``System``.

ros2_control 框架定义了三种类型的硬件：``Actuator``、``Sensor`` 和 ``System``。

Using a combination (composition) of those basic components, any physical robotic cell (robot and its surrounding) can be described.

使用这些基本组件的组合（组合），可以描述任何物理机器人单元（机器人及其周围环境）。

This also means that multi-robot, robot-sensor, robot-gripper combinations are supported out of the box.

这也意味着多机器人、机器人-传感器、机器人-夹爪组合都是开箱即用的。

Section :ref:`Hardware Components <overview_hardware_components>` describes this in detail.

:ref:`Hardware Components <overview_hardware_components>` 部分详细描述了这一点。

Hardware Interfaces（硬件接口）
-------------------

The ros_control framework allows only three types of interfaces (joints), i.e., ``position``, ``velocity``, and ``effort``. The ``RobotHW`` class makes it very hard to use any other data to control the robot.

ros_control 框架只允许三种类型的接口（关节），即 ``position``、``velocity`` 和 ``effort``。``RobotHW`` 类使得很难使用任何其他数据来控制机器人。

The ros2_control approach does not enforce a fixed set of interface types, but they are defined as strings in :ref:`hardware's description <hardware_description_in_urdf>`.

ros2_control 方法不强制使用固定的接口类型集，而是在 :ref:`硬件描述 <hardware_description_in_urdf>` 中将它们定义为字符串。

To ensure compatibility of standard controllers, standard interfaces are defined as constants in `hardware_interface package <https://github.com/ros-controls/ros2_control/blob/master/hardware_interface/include/hardware_interface/types/hardware_interface_type_values.hpp>`__.

为了确保标准控制器的兼容性，标准接口在 `hardware_interface package <https://github.com/ros-controls/ros2_control/blob/master/hardware_interface/include/hardware_interface/types/hardware_interface_type_values.hpp>`__ 中定义为常量。

Controller's Access to Hardware（控制器对硬件的访问）
-------------------------------

In ros_control, the controllers had direct access to the ``RobotHW`` class requesting access to its interfaces (joints).

在 ros_control 中，控制器可以直接访问 ``RobotHW`` 类，请求访问其接口（关节）。

The hardware itself then took care of registered interfaces and resource conflicts.

硬件本身处理注册的接口和资源冲突。

In ros2_control, ``ResourceManager`` takes care of the state of available interfaces in the framework and enables controllers to access the hardware.

在 ros2_control 中，``ResourceManager`` 负责管理框架中可用接口的状态，并使控制器能够访问硬件。

Also, the controllers do not have direct access to hardware anymore, but they register their interfaces to the ``ControllerManager``.

此外，控制器不再直接访问硬件，而是将其接口注册到 ``ControllerManager``。

Migration Guide to ros2_control（ros2_control 迁移指南）
===============================

RobotHardware to Components（RobotHardware 到组件）
---------------------------
#. The implementation of ``RobotHW`` is not used anymore.

#. 不再使用 ``RobotHW`` 的实现。

   This should be migrated to `SystemInterface`_ class or, for more granularity, `SensorInterface`_ and `ActuatorInterface`_.
   
   这应该迁移到 `SystemInterface`_ 类，或者为了更好的粒度，使用 `SensorInterface`_ 和 `ActuatorInterface`_。
   
   See the above description of "Hardware Components" to choose a suitable strategy.
   
   请参见上面"硬件组件"的描述来选择合适的策略。

#. Decide which component type is suitable for your case. Maybe it makes sense to separate ``RobotHW`` into multiple components.

#. 决定哪种组件类型适合您的情况。也许将 ``RobotHW`` 分离成多个组件是有意义的。

#. Implement `ActuatorInterface`_, `SensorInterface`_ or `SystemInterface`_ classes as follows:

#. 按以下方式实现 `ActuatorInterface`_、`SensorInterface`_ 或 `SystemInterface`_ 类：

   #. In the constructor, initialize all variables needed for communication with your hardware or define the default one.
   
   #. 在构造函数中，初始化与您的硬件通信所需的所有变量或定义默认变量。
   
   #. In the configure function, read all the parameters your hardware needs from the parsed URDF snippet (i.e., from the `HardwareInfo`_ structure). Here you can cross-check if all joints and interfaces in URDF have allowed values or a combination of values.
   
   #. 在 configure 函数中，从解析的 URDF 片段（即从 `HardwareInfo`_ 结构）中读取您的硬件需要的所有参数。在这里，您可以交叉检查 URDF 中的所有关节和接口是否具有允许的值或值的组合。
   
   #. Define interfaces to and from your hardware using ``export_*_interfaces`` functions.
      The names are ``<joint>/<interface>`` (e.g., ``joint_a2/position``).
      This can be extracted from the `HardwareInfo`_ structure or be hard-coded if sensible.
   
   #. 使用 ``export_*_interfaces`` 函数定义与您的硬件之间的接口。
      名称是 ``<joint>/<interface>``（例如，``joint_a2/position``）。
      这可以从 `HardwareInfo`_ 结构中提取，或者如果合理的话可以硬编码。
   #. Implement ``start()`` and ``stop()`` methods for your hardware.
      This usually includes changing the hardware state to receive commands or set it into a safe state before interrupting the command stream.
      It can also include starting and stopping communication.
   
   #. 为您的硬件实现 ``start()`` 和 ``stop()`` 方法。
      这通常包括更改硬件状态以接收命令或在中断命令流之前将其设置为安全状态。
      它还可以包括启动和停止通信。
   
   #. Implement ``read()`` and ``write()`` methods to exchange commands with the hardware.
      This method is equivalent to those from ``RobotHW``-class in ROS 1.
   
   #. 实现 ``read()`` 和 ``write()`` 方法以与硬件交换命令。
      此方法等同于 ROS 1 中 ``RobotHW`` 类的方法。
   
   #. Do not forget the ``PLUGINLIB_EXPORT_CLASS`` macro at the end of the .cpp file.
   
   #. 不要忘记在 .cpp 文件末尾添加 ``PLUGINLIB_EXPORT_CLASS`` 宏。

#. Create .xml library description for the pluginlib, for example see `RRBotSystemPositionOnlyHardware <https://github.com/ros-controls/ros2_control_demos/blob/master/example_1/ros2_control_demo_example_1.xml>`_.

#. 为 pluginlib 创建 .xml 库描述，例如参见 `RRBotSystemPositionOnlyHardware <https://github.com/ros-controls/ros2_control_demos/blob/master/example_1/ros2_control_demo_example_1.xml>`_。


Controller Migration（控制器迁移）
--------------------
An excellent example of a migrated controller is the `JointTrajectoryController`_.

迁移控制器的一个优秀示例是 `JointTrajectoryController`_。

The real-time critical methods are marked as such.

实时关键方法被标记为这样。

#. Implement `ControllerInterface`_ class as follows:

#. 按以下方式实现 `ControllerInterface`_ 类：

   #. If there are any member variables, initialized those in the constructor.
   
   #. 如果有任何成员变量，在构造函数中初始化它们。
   
   #. In the ``init()`` method, first call ``ControllerInterface::init()`` to initialize the lifecycle of the controller. Following this, declare all parameters defining their default values.
   
   #. 在 ``init()`` 方法中，首先调用 ``ControllerInterface::init()`` 来初始化控制器的生命周期。接下来，声明所有参数并定义其默认值。
   
   #. Implement the ``state_interface_configuration()`` and ``command_interface_configuration()`` methods.
   
   #. 实现 ``state_interface_configuration()`` 和 ``command_interface_configuration()`` 方法。
   
   #. Design the ``update()`` function for the controller. (**real-time**)
   
   #. 为控制器设计 ``update()`` 函数。（**实时**）
   #. Add the required lifecycle management methods (others are optional):
         * ``on_configure()`` - reads parameters and configures controller.
         * ``on_activate()`` - called when controller is activated (started) (**real-time**)
         * ``on_deactivate()`` - called when controller is deactivated (stopped) (**real-time**)
   
   #. 添加所需的生命周期管理方法（其他是可选的）：
         * ``on_configure()`` - 读取参数并配置控制器。
         * ``on_activate()`` - 当控制器被激活（启动）时调用（**实时**）
         * ``on_deactivate()`` - 当控制器被停用（停止）时调用（**实时**）
   
   #. Finally, do not forget to add the ``PLUGINLIB_EXPORT_CLASS`` macro at the end of the .cpp file.
   
   #. 最后，不要忘记在 .cpp 文件末尾添加 ``PLUGINLIB_EXPORT_CLASS`` 宏。

#. Create .xml library description for the pluginlib, for example see `joint_trajectory_plugin.xml <https://github.com/ros-controls/ros2_controllers/blob/master/joint_trajectory_controller/joint_trajectory_plugin.xml>`_.

#. 为 pluginlib 创建 .xml 库描述，例如参见 `joint_trajectory_plugin.xml <https://github.com/ros-controls/ros2_controllers/blob/master/joint_trajectory_controller/joint_trajectory_plugin.xml>`_。


.. _ActuatorInterface: https://github.com/ros-controls/ros2_control/blob/master/hardware_interface/include/hardware_interface/actuator_interface.hpp
.. _SensorInterface: https://github.com/ros-controls/ros2_control/blob/master/hardware_interface/include/hardware_interface/sensor_interface.hpp
.. _SystemInterface: https://github.com/ros-controls/ros2_control/blob/master/hardware_interface/include/hardware_interface/system_interface.hpp
.. _HardwareInfo: https://github.com/ros-controls/ros2_control/blob/master/hardware_interface/include/hardware_interface/hardware_info.hpp
.. _JointTrajectoryController: https://github.com/ros-controls/ros2_controllers/blob/master/joint_trajectory_controller/src/joint_trajectory_controller.cpp
.. _ControllerInterface: https://github.com/ros-controls/ros2_control/blob/master/controller_interface/include/controller_interface/controller_interface.hpp
