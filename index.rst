.. _documentation_home:

Welcome to the ros2_control documentation - Jazzy!（欢迎来到 ros2_control 文档 - Jazzy！）
==================================================

.. toctree::
   :hidden:

   doc/getting_started/getting_started.rst
   doc/ros2_control/doc/index.rst
   doc/ros2_controllers/doc/controllers_index.rst
   doc/ros2_control_demos/doc/index.rst
   doc/utilities.rst
   doc/simulators/simulators.rst
   doc/release_notes/release_notes.rst
   doc/migration/migration.rst
   doc/api_list/api_list.rst
   doc/supported_robots/supported_robots.rst
   doc/resources/resources.rst
   doc/contributing/contributing.rst
   doc/governance/governance.rst
   doc/acknowledgements/acknowledgements.rst
   doc/statistics.rst

The ros2_control is a framework for (real-time) control of robots using (`ROS 2 <https://docs.ros.org/en/rolling/>`_).

ros2_control 是一个使用 (`ROS 2 <https://docs.ros.org/en/rolling/>`_) 进行机器人（实时）控制的框架。

Its packages are a rewrite of `ros_control <http://wiki.ros.org/ros_control>`_ packages used in ``ROS`` (`Robot Operating System <https://wiki.ros.org>`_).

其包是在 ``ROS``（`Robot Operating System <https://wiki.ros.org>`_）中使用的 `ros_control <http://wiki.ros.org/ros_control>`_ 包的重写。

ros2_control's goal is to simplify integrating new hardware and overcome some drawbacks.

ros2_control 的目标是简化新硬件的集成并克服一些缺点。

If you are not familiar with the control theory, please get some idea about it (e.g., at `Wikipedia <https://en.wikipedia.org/wiki/Control_theory>`_) to get familiar with the terms used in this manual.

如果您不熟悉控制理论，请先了解一些相关知识（例如，在 `Wikipedia <https://en.wikipedia.org/wiki/Control_theory>`_），以熟悉本手册中使用的术语。


``ros2_control`` Repositories（``ros2_control`` 仓库）
-------------------------------------------
The framework consists of the following Github repositories hosted under the `ros-controls`_ Github organization:

该框架由以下托管在 `ros-controls`_ Github 组织下的 Github 仓库组成：

* `ros2_control`_ - the main interfaces and components of the framework;

* `ros2_control`_ - 框架的主要接口和组件；

* `ros2_controllers`_ - widely used controllers, such as forward command controller, joint trajectory controller, differential drive controller;

* `ros2_controllers`_ - 广泛使用的控制器，如前向命令控制器、关节轨迹控制器、差分驱动控制器；

* `control_toolbox`_ - some widely-used control theory implementations (e.g. PID) used by controllers;

* `control_toolbox`_ - 一些控制器使用的广泛使用的控制理论实现（例如 PID）；

* `realtime_tools`_ - general toolkit for realtime support, e.g., realtime buffers and publishers;

* `realtime_tools`_ - 用于实时支持的通用工具包，例如实时缓冲区和发布者；

* `control_msgs`_ - common messages;

* `control_msgs`_ - 通用消息；

* `kinematics_interface`_ - for using C++ kinematics frameworks;

* `kinematics_interface`_ - 用于使用 C++ 运动学框架；

* `gz_ros2_control`_ - Plugin for Gazebo;

* `gz_ros2_control`_ - Gazebo 插件；

* `topic_based_hardware_interfaces`_ - hardware_interfaces for simulators and other hardware that only support ROS topic-based communication;

* `topic_based_hardware_interfaces`_ - 用于仿真器和其他仅支持基于 ROS topic 通信的硬件的 hardware_interfaces；


Additionally, the following (unreleased) packages are relevant for documentation and project management:

此外，以下（未发布的）包与文档和项目管理相关：

* `ros2_control_demos`_ - example implementations of common use-cases for a smooth start;

* `ros2_control_demos`_ - 常见用例的示例实现，以便顺利开始；

* `roadmap`_ - planning and design docs for the project;

* `roadmap`_ - 项目的规划和设计文档；

* `ros2_control_ci`_ - reusable Github actions and Docker images for Ubuntu, RHEL, and Debian CI jobs;

* `ros2_control_ci`_ - 适用于 Ubuntu、RHEL 和 Debian CI 作业的可重用 Github actions 和 Docker 镜像；

* `.github`_ - Github organization-wide files, such as issue templates;

* `.github`_ - Github 组织范围内的文件，如问题模板；

* `ros2_control_cmake`_ - CMake macros for the project;

* `ros2_control_cmake`_ - 项目的 CMake 宏；

* `ros2_control_ci`_ - reusable Github actions;

* `ros2_control_ci`_ - 可重用的 Github actions；

* `control.ros.org`_ - this documentation page.

* `control.ros.org`_ - 此文档页面。

Development Organisation and Communication（开发组织和沟通）
-------------------------------------------
OSRA
   The ros-controls project is governed by the `Open Source Robotics Alliance (OSRA) <https://osralliance.org/>`__. See :ref:`Governance` for more details.

OSRA
   ros-controls 项目由 `Open Source Robotics Alliance (OSRA) <https://osralliance.org/>`__ 管理。有关更多详细信息，请参见 :ref:`Governance`。

Questions
   Please use `Robotics Stack Exchange <https://robotics.stackexchange.com>`_ and tag your questions with ``ros2_control``.

Questions
   请使用 `Robotics Stack Exchange <https://robotics.stackexchange.com>`_ 并用 ``ros2_control`` 标记您的问题。

PMC Meeting
   Every second Wednesday there is a PMC meeting.
   To join the meeting check the announcement on `ROS Discourse`_.
   You can join the meeting through `google groups <https://groups.google.com/forum/#!forum/ros-control-working-group-invites>`_ or directly on Zoom (check the announcement).
   To propose new discussion points, or review notes from previous meetings, check `this document <https://docs.google.com/document/d/1818AoYucI2z82awL_-8sAA5pMCV_g_wXCJiM6SQmhSQ/edit?usp=sharing>`_.

PMC Meeting
   每隔一个星期三举行 PMC 会议。
   要参加会议，请查看 `ROS Discourse`_ 上的公告。
   您可以通过 `google groups <https://groups.google.com/forum/#!forum/ros-control-working-group-invites>`_ 或直接在 Zoom 上参加会议（查看公告）。
   要提出新的讨论要点或查看以前会议的记录，请查看 `此文档 <https://docs.google.com/document/d/1818AoYucI2z82awL_-8sAA5pMCV_g_wXCJiM6SQmhSQ/edit?usp=sharing>`_。

Projects
   GitHub `projects under ros-control organization <https://github.com/orgs/ros-controls/projects>`_ are used to track the work.

Projects
   GitHub `ros-control 组织下的项目 <https://github.com/orgs/ros-controls/projects>`_ 用于跟踪工作。

Bug reports and feature requests
   Use the issue tracker in the corresponding repository for this.
   Give a short summary of the problem
   Make sure to provide a minimal list of steps one can follow to reproduce the issue you found
   Provide relevant information regarding the operating system, ROS distribution, etc.

Bug reports and feature requests
   为此请使用相应仓库中的问题跟踪器。
   给出问题的简短摘要
   确保提供可以遵循以重现您发现的问题的最小步骤列表
   提供有关操作系统、ROS 发行版等的相关信息。

General discussions
   Please use `ROS Discourse`_.

General discussions
   请使用 `ROS Discourse`_。


.. _ros2_control: https://github.com/ros-controls/ros2_control
.. _ros2_controllers: https://github.com/ros-controls/ros2_controllers
.. _control_msgs: https://github.com/ros-controls/control_msgs
.. _realtime_tools: https://github.com/ros-controls/realtime_tools
.. _topic_based_hardware_interfaces: https://github.com/ros-controls/topic_based_hardware_interfaces
.. _control_toolbox: https://github.com/ros-controls/control_toolbox
.. _kinematics_interface: https://github.com/ros-controls/kinematics_interface
.. _ros2_control_demos: https://github.com/ros-controls/ros2_control_demos
.. _gz_ros2_control: https://github.com/ros-controls/gz_ros2_control
.. _ros2_control_ci: https://github.com/ros-controls/ros2_control_ci
.. _.github: https://github.com/ros-controls/.github
.. _ros2_control_cmake: https://github.com/ros-controls/ros2_control_cmake
.. _control.ros.org: https://github.com/ros-controls/control.ros.org
.. _ros-controls: https://github.com/ros-controls
.. _controller_manager_msgs: https://github.com/ros-controls/ros2_control/tree/{REPOS_FILE_BRANCH}/controller_manager_msgs
.. _Controller Manager: https://github.com/ros-controls/ros2_control/blob/{REPOS_FILE_BRANCH}/controller_manager/src/controller_manager.cpp
.. _ControllerInterface: https://github.com/ros-controls/ros2_control/blob/{REPOS_FILE_BRANCH}/controller_interface/include/controller_interface/controller_interface.hpp
.. _ros2_control node: https://github.com/ros-controls/ros2_control/blob/{REPOS_FILE_BRANCH}/controller_manager/src/ros2_control_node.cpp

.. _Resource Manager: https://github.com/ros-controls/ros2_control/blob/{REPOS_FILE_BRANCH}/hardware_interface/src/resource_manager.cpp
.. _Node Lifecycle Design: https://design.ros2.org/articles/node_lifecycle.html
.. _ros2controlcli: https://github.com/ros-controls/ros2_control/tree/{REPOS_FILE_BRANCH}/ros2controlcli
.. _Hardware Access through Controllers design document: https://github.com/ros-controls/roadmap/blob/master/design_drafts/hardware_access.md
.. _ROS2 Control Components URDF Examples design document: https://github.com/ros-controls/roadmap/blob/master/design_drafts/components_architecture_and_urdf_examples.md
.. _roadmap: https://github.com/ros-controls/roadmap
.. _ROS Discourse: https://discourse.ros.org


----

.. |date| date::
.. |time| date:: %H:%M

Built on |date| at |time| GMT
