.. _getting_started:

#################
Getting Started（入门指南）
#################

Installation（安装）
============

Binary packages（二进制包）
------------------
The ros2_control framework is released for ROS 2 {DISTRO} on Ubuntu and RHEL according to `REP-2000 <https://www.ros.org/reps/rep-2000.html>`__.

ros2_control 框架根据 `REP-2000 <https://www.ros.org/reps/rep-2000.html>`__ 为 Ubuntu 和 RHEL 上的 ROS 2 {DISTRO} 发布。

To use it, you have to install ``ros-{DISTRO}-ros2-control`` and ``ros-{DISTRO}-ros2-controllers`` packages, e.g., by running the following commands:

要使用它，您必须安装 ``ros-{DISTRO}-ros2-control`` 和 ``ros-{DISTRO}-ros2-controllers`` 包，例如，通过运行以下命令：

For Ubuntu deb packages

Ubuntu deb 包：

  .. code-block:: shell

    sudo apt install ros-{DISTRO}-ros2-control ros-{DISTRO}-ros2-controllers

For RHEL (RPM) packages

RHEL (RPM) 包：

  .. code-block:: shell

    sudo dnf install ros-{DISTRO}-ros2-control ros-{DISTRO}-ros2-controllers




Building from Source（从源码构建）
---------------------------

To receive the latest features and bug fixes or if you want to contribute to the framework, you can build the framework from source.

要获得最新功能和错误修复，或者如果您想为框架做贡献，您可以从源码构建框架。

You can choose between the following options:

您可以选择以下选项之一：

   * Stable version: The changes in these branches will be tagged and released to the ROS 2 distribution binaries.

   * 稳定版本：这些分支中的更改将被标记并发布到 ROS 2 发行版二进制文件中。

    .. raw:: html

        <a href="https://github.com/ros-controls/ros2_control_ci/actions/workflows/{DISTRO}-binary-build.yml">
            <img src="https://github.com/ros-controls/ros2_control_ci/actions/workflows/{DISTRO}-binary-build.yml/badge.svg" alt="{DISTRO} Binary Build"/></a>

   * Development version: We thrive to make the rolling development version (from the master branches) of the ros2_control stack compatible with earlier releases of ROS2. This is done by building the rolling version of the stack from source with the earlier releases of ROS2.

   * 开发版本：我们努力使 ros2_control 堆栈的滚动开发版本（来自主分支）与 ROS2 的早期版本兼容。这通过使用 ROS2 的早期版本从源码构建堆栈的滚动版本来实现。

    .. raw:: html

        <a href="https://github.com/ros-controls/ros2_control_ci/actions/workflows/rolling-compatibility-{DISTRO}-binary-build.yml">
            <img src="https://github.com/ros-controls/ros2_control_ci/actions/workflows/rolling-compatibility-{DISTRO}-binary-build.yml/badge.svg" alt="Rolling Compatibility {DISTRO}"/></a>

* Download all repositories:

* 下载所有仓库：

  .. tabs::

    .. group-tab:: Stable version

        .. code-block:: shell

          mkdir -p ~/ros2_ws/src
          cd ~/ros2_ws/
          vcs import --input https://raw.githubusercontent.com/ros-controls/ros2_control_ci/master/ros_controls.$ROS_DISTRO.repos src

    .. group-tab:: Development version

        .. code-block:: shell

          mkdir -p ~/ros2_ws/src
          cd ~/ros2_ws/
          vcs import --input https://raw.githubusercontent.com/ros-controls/ros2_control_ci/master/ros_controls.rolling-on-$ROS_DISTRO.repos src

* Install dependencies:

* 安装依赖项：

  .. code-block:: shell

    rosdep update --rosdistro=$ROS_DISTRO
    sudo apt-get update
    rosdep install --from-paths src --ignore-src -r -y

* Build everything, e.g. with:

* 构建所有内容，例如使用：

  .. code-block:: shell

    . /opt/ros/${ROS_DISTRO}/setup.sh
    colcon build --symlink-install

* Do not forget to source ``setup.bash`` from the ``install`` folder!

* 不要忘记从 ``install`` 文件夹中 source ``setup.bash``！


Architecture（架构）
============
The source code for the ros2_control framework can be found in the `ros2_control`_ and `ros2_controllers`_ GitHub repositories. The following figure shows the architecture of the ros2_control framework.

ros2_control 框架的源代码可以在 `ros2_control`_ 和 `ros2_controllers`_ GitHub 仓库中找到。下图显示了 ros2_control 框架的架构。

|ros2_control_architecture|

The following UML Class Diagram describes the internal implementation of the ros2_control framework.

以下 UML 类图描述了 ros2_control 框架的内部实现。

|uml_class_diagram|

Controller Manager（控制器管理器）
------------------
The `Controller Manager`_ (CM) connects the controllers and hardware-abstraction sides of the ros2_control framework.

`Controller Manager`_（CM）连接了 ros2_control 框架的控制器和硬件抽象两侧。

It also serves as the entry-point for users via ROS services.

它还通过 ROS 服务作为用户的入口点。

The CM implements a node without an executor so that it can be integrated into a custom setup.

CM 实现了一个没有执行器的节点，以便它可以集成到自定义设置中。

However, it's usually recommended to use the default node-setup implemented in `ros2_control_node <https://github.com/ros-controls/ros2_control/blob/{REPOS_FILE_BRANCH}/controller_manager/src/ros2_control_node.cpp>`_ file from the ``controller_manager`` package.

但是，通常建议使用 ``controller_manager`` 包中的 `ros2_control_node <https://github.com/ros-controls/ros2_control/blob/{REPOS_FILE_BRANCH}/controller_manager/src/ros2_control_node.cpp>`_ 文件中实现的默认节点设置。

This manual assumes that you use this default node-setup.

本手册假设您使用这个默认的节点设置。

On the one hand, CM manages (e.g. loads, activates, deactivates, unloads) controllers and the interfaces they require.

一方面，CM 管理（例如加载、激活、停用、卸载）控制器及其所需的接口。

On the other hand, it has access (via the Resource Manager) to the hardware components, i.e. their interfaces.

另一方面，它可以访问（通过 Resource Manager）硬件组件，即它们的接口。

The Controller Manager matches *required* and *provided* interfaces, granting controllers access to hardware when enabled, or reporting an error if there is an access conflict.

Controller Manager 匹配 *required* 和 *provided* 接口，在启用时授予控制器对硬件的访问权限，或在存在访问冲突时报告错误。


The execution of the control-loop is managed by the CM's ``update()`` method.

控制循环的执行由 CM 的 ``update()`` 方法管理。

It reads data from the hardware components, updates outputs of all active controllers, and writes the result to the components.

它从硬件组件读取数据，更新所有活动控制器的输出，并将结果写入组件。

Resource Manager（资源管理器）
----------------
The `Resource Manager`_ (RM) abstracts physical hardware and its drivers (called *hardware components*) for the ros2_control framework.

`Resource Manager`_（RM）为 ros2_control 框架抽象了物理硬件及其驱动程序（称为 *硬件组件*）。

The RM loads the components using the ``pluginlib``-library, manages their lifecycle and components' state and command interfaces.

RM 使用 ``pluginlib`` 库加载组件，管理它们的生命周期以及组件的状态和命令接口。

The abstraction provided by RM allows reuse of implemented hardware components, e.g., robot and gripper, without any implementation, and flexible hardware application for state and command interfaces, e.g., separate hardware/communication libraries for motor control and encoder reading.

RM 提供的抽象允许重用已实现的硬件组件，例如机器人和夹爪，无需任何实现，并为状态和命令接口提供灵活的硬件应用，例如用于电机控制和编码器读取的独立硬件/通信库。

In the control loop execution, the RM's ``read()`` and ``write()`` methods handle the communication with the hardware components.

在控制循环执行中，RM 的 ``read()`` 和 ``write()`` 方法处理与硬件组件的通信。

.. _overview-controllers:

Controllers（控制器）
-----------
The controllers in the ros2_control framework are based on control theory. They compare the reference value with the measured output and, based on this error, calculate a system's input.

ros2_control 框架中的控制器基于控制理论。它们将参考值与测量输出进行比较，并基于此误差计算系统的输入。

The controllers are objects derived from `ControllerInterface`_ (``controller_interface`` package in `ros2_control`_) and exported as plugins using ``pluginlib``-library.

控制器是从 `ControllerInterface`_（`ros2_control`_ 中的 ``controller_interface`` 包）派生的对象，并使用 ``pluginlib`` 库作为插件导出。

For an example of a controller check the `ForwardCommandController implementation`_ in the `ros2_controllers`_ repository.

有关控制器的示例，请查看 `ros2_controllers`_ 仓库中的 `ForwardCommandController implementation`_。

The controller lifecycle is based on the LifecycleNode class, which implements the state machine described in the Node Lifecycle Design document.

控制器生命周期基于 LifecycleNode 类，该类实现了 Node Lifecycle Design 文档中描述的状态机。

When the control-loop is executed, the ``update()`` method is called.

当执行控制循环时，会调用 ``update()`` 方法。

This method can access the latest hardware state and enable the controller to write to the hardware command interfaces.

此方法可以访问最新的硬件状态，并使控制器能够写入硬件命令接口。

User Interfaces（用户接口）
---------------
Users interact with the ros2_control framework using `Controller Manager`_'s services.

用户使用 `Controller Manager`_ 的服务与 ros2_control 框架交互。

For a list of services and their definitions, check the ``srv`` folder in the `controller_manager_msgs`_ package.

有关服务列表及其定义，请查看 `controller_manager_msgs`_ 包中的 ``srv`` 文件夹。

While service calls can be used directly from the command line or via nodes, there exists a user-friendly ``Command Line Interface`` (CLI) which integrates with the ``ros2 cli``. This supports auto-complete and has a range of common commands available. The base command is ``ros2 control``.

虽然服务调用可以直接从命令行或通过节点使用，但存在一个用户友好的 ``Command Line Interface``（CLI），它与 ``ros2 cli`` 集成。这支持自动完成并有一系列常用命令可用。基本命令是 ``ros2 control``。

For the description of our CLI capabilities, see the :ref:`Command Line Interface (CLI) documentation <ros2controlcli_userdoc>`.

有关我们的 CLI 功能的描述，请参见 :ref:`Command Line Interface (CLI) documentation <ros2controlcli_userdoc>`。

.. _overview_hardware_components:

Hardware Components（硬件组件）
===================
The *hardware components* realize communication to physical hardware and represent its abstraction in the ros2_control framework.

*硬件组件* 实现与物理硬件的通信，并在 ros2_control 框架中表示其抽象。

The components have to be exported as plugins using ``pluginlib``-library.

组件必须使用 ``pluginlib`` 库作为插件导出。

The `Resource Manager`_ dynamically loads those plugins and manages their lifecycle.

`Resource Manager`_ 动态加载这些插件并管理它们的生命周期。

There are three basic types of components:

有三种基本的组件类型：

System
  Complex (multi-DOF) robotic hardware like industrial robots.
  The main difference between the *Actuator* component is the possibility to use complex transmissions like needed for humanoid robot's hands.
  This component has reading and writing capabilities.
  It is used when there is only one logical communication channel to the hardware (e.g., KUKA-RSI).

System
  复杂的（多自由度）机器人硬件，如工业机器人。
  与 *Actuator* 组件的主要区别是可以使用复杂的传动装置，如仿人机器人手部所需的。
  该组件具有读写功能。
  当只有一个逻辑通信通道连接到硬件时使用（例如，KUKA-RSI）。

Sensor
  Robotic hardware is used for sensing its environment.
  A sensor component is related to a joint (e.g., encoder) or a link (e.g., force-torque sensor).
  This component type has only reading capabilities.

Sensor
  机器人硬件用于感知其环境。
  传感器组件与关节（例如，编码器）或连杆（例如，力-扭矩传感器）相关。
  此组件类型仅具有读取功能。

Actuator
  Simple (1 DOF) robotic hardware like motors, valves, and similar.
  An actuator implementation is related to only one joint.
  This component type has reading and writing capabilities. Reading is not mandatory if not possible (e.g., DC motor control with Arduino board).
  The actuator type can also be used with a multi-DOF robot if its hardware enables modular design, e.g., CAN-communication with each motor independently.

Actuator
  简单的（1 自由度）机器人硬件，如电机、阀门等。
  执行器实现仅与一个关节相关。
  此组件类型具有读写功能。如果不可能的话，读取不是强制性的（例如，使用 Arduino 板的直流电机控制）。
  如果硬件支持模块化设计，执行器类型也可以用于多自由度机器人，例如，与每个电机独立进行 CAN 通信。


A detailed explanation of hardware components is given in the `Hardware Access through Controllers design document`_.

硬件组件的详细说明在 `Hardware Access through Controllers design document`_ 中给出。

.. _hardware_description_in_urdf:

Hardware Description in URDF（URDF 中的硬件描述）
----------------------------
The ros2_control framework uses the ``<ros2_control>``-tag in the robot's URDF file to describe its components, i.e., the hardware setup.

ros2_control 框架在机器人的 URDF 文件中使用 ``<ros2_control>`` 标签来描述其组件，即硬件设置。

The chosen structure enables tracking together multiple ``xacro``-macros into one without any changes.

所选择的结构能够将多个 ``xacro`` 宏跟踪到一个中，而无需任何更改。

The example hereunder shows a position-controlled robot with 2-DOF (RRBot), an external 1-DOF force-torque sensor, and an externally controlled 1-DOF parallel gripper as its end-effector.

下面的示例显示了一个位置控制的 2 自由度机器人（RRBot），一个外部 1 自由度力-扭矩传感器，以及一个外部控制的 1 自由度并联夹爪作为其末端执行器。

For more examples and detailed explanations, check the :ref:`ros2_control_demos site <ros2_control_demos>` and `ROS 2 Control Components URDF Examples design document`_.

有关更多示例和详细说明，请查看 :ref:`ros2_control_demos site <ros2_control_demos>` 和 `ROS 2 Control Components URDF Examples design document`_。

.. code:: xml

   <ros2_control name="RRBotSystemPositionOnly" type="system">
    <hardware>
      <plugin>ros2_control_demo_hardware/RRBotSystemPositionOnlyHardware</plugin>
      <param name="example_param_write_for_sec">2</param>
      <param name="example_param_read_for_sec">2</param>
    </hardware>
    <joint name="joint1">
      <command_interface name="position">
        <param name="min">-1</param>
        <param name="max">1</param>
      </command_interface>
      <state_interface name="position"/>
    </joint>
    <joint name="joint2">
      <command_interface name="position">
        <param name="min">-1</param>
        <param name="max">1</param>
      </command_interface>
      <state_interface name="position"/>
    </joint>
   </ros2_control>
   <ros2_control name="RRBotForceTorqueSensor1D" type="sensor">
    <hardware>
      <plugin>ros2_control_demo_hardware/ForceTorqueSensor1DHardware</plugin>
      <param name="example_param_read_for_sec">0.43</param>
    </hardware>
    <sensor name="tcp_fts_sensor">
      <state_interface name="force"/>
      <param name="frame_id">rrbot_tcp</param>
      <param name="min_force">-100</param>
      <param name="max_force">100</param>
    </sensor>
   </ros2_control>
   <ros2_control name="RRBotGripper" type="actuator">
    <hardware>
      <plugin>ros2_control_demo_hardware/PositionActuatorHardware</plugin>
      <param name="example_param_write_for_sec">1.23</param>
      <param name="example_param_read_for_sec">3</param>
    </hardware>
    <joint name="gripper_joint ">
      <command_interface name="position">
        <param name="min">0</param>
        <param name="max">50</param>
      </command_interface>
      <state_interface name="position"/>
      <state_interface name="velocity"/>
    </joint>
   </ros2_control>


Running the Framework for Your Robot（为您的机器人运行框架）
------------------------------------
To run the ros2_control framework, do the following.

要运行 ros2_control 框架，请执行以下操作。

The example files can be found in the `ros2_control_demos`_ repository.

示例文件可以在 `ros2_control_demos`_ 仓库中找到。

#. Create a YAML file with the configuration of the controller manager and two controllers. (`Example configuration for RRBot <https://github.com/ros-controls/ros2_control_demos/blob/{REPOS_FILE_BRANCH}/example_1/bringup/config/rrbot_controllers.yaml>`_)

#. 创建一个包含 Controller Manager 和两个控制器配置的 YAML 文件。（`RRBot 的示例配置 <https://github.com/ros-controls/ros2_control_demos/blob/{REPOS_FILE_BRANCH}/example_1/bringup/config/rrbot_controllers.yaml>`_）

#. Extend the robot's URDF description with needed ``<ros2_control>`` tags.
   It is recommended to use macro files (xacro) instead of pure URDF. (`Example URDF for RRBot <https://github.com/ros-controls/ros2_control_demos/blob/{REPOS_FILE_BRANCH}/example_1/description/ros2_control/rrbot.ros2_control.xacro>`_)

#. 使用所需的 ``<ros2_control>`` 标签扩展机器人的 URDF 描述。
   建议使用宏文件（xacro）而不是纯 URDF。（`RRBot 的示例 URDF <https://github.com/ros-controls/ros2_control_demos/blob/{REPOS_FILE_BRANCH}/example_1/description/ros2_control/rrbot.ros2_control.xacro>`_）

#. Create a launch file to start the node with `Controller Manager`_.
   You can use a default `ros2_control node`_ (recommended) or integrate the controller manager in your software stack.
   (`Example launch file for RRBot <https://github.com/ros-controls/ros2_control_demos/blob/{REPOS_FILE_BRANCH}/example_1/bringup/launch/rrbot.launch.py>`_)

#. 创建一个启动文件来启动带有 `Controller Manager`_ 的节点。
   您可以使用默认的 `ros2_control node`_（推荐）或将 Controller Manager 集成到您的软件堆栈中。
   （`RRBot 的示例启动文件 <https://github.com/ros-controls/ros2_control_demos/blob/{REPOS_FILE_BRANCH}/example_1/bringup/launch/rrbot.launch.py>`_）

*NOTE:* You could alternatively use a script to create setup a `skeleton of the "robot bringup" package by using the scripts <https://rtw.b-robotized.com/master/use-cases/ros_packages/setup_robot_bringup_package.html>`_ provided by one of our maintainers. Extension of xacro for ros2_control file you can find in the `templates for "robot description" package <https://rtw.b-robotized.com/master/use-cases/ros_packages/setup_robot_description_package.html>`_.

*注意：* 您也可以使用脚本通过我们维护者之一提供的 `脚本创建"机器人启动"包的骨架 <https://rtw.b-robotized.com/master/use-cases/ros_packages/setup_robot_bringup_package.html>`_。ros2_control 文件的 xacro 扩展可以在 `"机器人描述"包的模板 <https://rtw.b-robotized.com/master/use-cases/ros_packages/setup_robot_description_package.html>`_ 中找到。


.. _ros2_control: https://github.com/ros-controls/ros2_control
.. _ros2_controllers: https://github.com/ros-controls/ros2_controllers
.. _ros2_control_demos: https://github.com/ros-controls/ros2_control_demos
.. _controller_manager_msgs: https://github.com/ros-controls/ros2_control/tree/master/controller_manager_msgs
.. _ControllerInterface: https://github.com/ros-controls/ros2_control/blob/master/controller_interface/include/controller_interface/controller_interface.hpp
.. _ros2_control node: https://github.com/ros-controls/ros2_control/blob/master/controller_manager/src/ros2_control_node.cpp
.. _ForwardCommandController implementation: https://github.com/ros-controls/ros2_controllers/blob/master/forward_command_controller/src/forward_command_controller.cpp
.. _ros2controlcli: https://github.com/ros-controls/ros2_control/tree/master/ros2controlcli
.. _Hardware Access through Controllers design document: https://github.com/ros-controls/roadmap/blob/master/design_drafts/hardware_access.md
.. _ROS 2 Control Components URDF Examples design document: https://github.com/ros-controls/roadmap/blob/master/design_drafts/components_architecture_and_urdf_examples.md

.. |ros2_control_architecture| image:: images/components_architecture.png
   :alt: "ros2_control Architecture"

.. |uml_class_diagram| image:: images/uml_class_diagram.png
   :alt: "UML Class Diagram"
