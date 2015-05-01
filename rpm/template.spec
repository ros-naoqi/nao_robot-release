Name:           ros-jade-nao-robot
Version:        0.5.7
Release:        0%{?dist}
Summary:        ROS nao_robot package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/nao_robot
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-jade-nao-apps
Requires:       ros-jade-nao-bringup
Requires:       ros-jade-nao-description
Requires:       ros-jade-nao-pose
BuildRequires:  ros-jade-catkin

%description
The nao_robot metapackage contains some useful nodes to integrate the Nao
humanoid robot into ROS. Check out the nao_extras stack for more functionality.
The humanoid_navigation stack contains some more general packages for
humanoid/biped robots.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Fri May 01 2015 Séverin Lemaignan <severin.lemaignan@epfl.ch> - 0.5.7-0
- Autogenerated by Bloom

