Name:           ros-indigo-nao-bringup
Version:        0.5.7
Release:        0%{?dist}
Summary:        ROS nao_bringup package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/nao_robot
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-diagnostic-aggregator
Requires:       ros-indigo-nao-description
Requires:       ros-indigo-nao-pose
Requires:       ros-indigo-naoqi-driver
Requires:       ros-indigo-naoqi-sensors
Requires:       ros-indigo-robot-state-publisher
BuildRequires:  ros-indigo-catkin

%description
Launch files and scripts needed to bring ROS interfaces for Nao up into a
running state.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Apr 28 2015 Séverin Lemaignan <severin.lemaignan@epfl.ch> - 0.5.7-0
- Autogenerated by Bloom

* Fri Feb 27 2015 Séverin Lemaignan <severin.lemaignan@epfl.ch> - 0.5.6-0
- Autogenerated by Bloom

* Tue Feb 17 2015 Séverin Lemaignan <severin.lemaignan@epfl.ch> - 0.5.5-0
- Autogenerated by Bloom

* Tue Feb 17 2015 Séverin Lemaignan <severin.lemaignan@epfl.ch> - 0.5.4-0
- Autogenerated by Bloom

