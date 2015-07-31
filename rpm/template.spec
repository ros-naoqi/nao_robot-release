Name:           ros-indigo-nao-robot
Version:        0.5.10
Release:        0%{?dist}
Summary:        ROS nao_robot package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/nao_robot
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-nao-apps
Requires:       ros-indigo-nao-bringup
Requires:       ros-indigo-nao-description
BuildRequires:  ros-indigo-catkin

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

