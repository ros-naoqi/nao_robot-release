Name:           ros-indigo-nao-description
Version:        0.5.12
Release:        0%{?dist}
Summary:        ROS nao_description package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/nao_description
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-message-filters
Requires:       ros-indigo-robot-state-publisher
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-tf
Requires:       ros-indigo-urdf
Requires:       ros-indigo-xacro
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-message-filters
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-tf
BuildRequires:  ros-indigo-urdf
BuildRequires:  ros-indigo-xacro

%description
Description of the Nao robot model that can be used with robot_state_publisher
to display the robot's state of joint angles.

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
* Fri Jan 01 2016 Séverin Lemaignan <severin.lemaignan@epfl.ch> - 0.5.12-0
- Autogenerated by Bloom

* Tue Aug 11 2015 Séverin Lemaignan <severin.lemaignan@epfl.ch> - 0.5.11-0
- Autogenerated by Bloom

* Fri Jul 31 2015 Séverin Lemaignan <severin.lemaignan@epfl.ch> - 0.5.10-0
- Autogenerated by Bloom

* Thu Jul 30 2015 Séverin Lemaignan <severin.lemaignan@epfl.ch> - 0.5.9-0
- Autogenerated by Bloom

* Tue Apr 28 2015 Séverin Lemaignan <severin.lemaignan@epfl.ch> - 0.5.7-0
- Autogenerated by Bloom

* Fri Feb 27 2015 Séverin Lemaignan <severin.lemaignan@epfl.ch> - 0.5.6-0
- Autogenerated by Bloom

* Tue Feb 17 2015 Séverin Lemaignan <severin.lemaignan@epfl.ch> - 0.5.5-0
- Autogenerated by Bloom

* Tue Feb 17 2015 Séverin Lemaignan <severin.lemaignan@epfl.ch> - 0.5.4-0
- Autogenerated by Bloom

* Sun Dec 14 2014 Séverin Lemaignan <severin.lemaignan@epfl.ch> - 0.5.3-0
- Autogenerated by Bloom

* Thu Dec 04 2014 Séverin Lemaignan <severin.lemaignan@epfl.ch> - 0.5.2-0
- Autogenerated by Bloom

* Thu Nov 13 2014 Séverin Lemaignan <severin.lemaignan@epfl.ch> - 0.5.1-0
- Autogenerated by Bloom

* Fri Nov 07 2014 Séverin Lemaignan <severin.lemaignan@epfl.ch> - 0.5.0-0
- Autogenerated by Bloom

