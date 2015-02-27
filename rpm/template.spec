Name:           ros-hydro-nao-apps
Version:        0.5.6
Release:        0%{?dist}
Summary:        ROS nao_apps package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  ros-hydro-catkin

%description
Applications for NAO using the NAOqi API

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Fri Feb 27 2015 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.5.6-0
- Autogenerated by Bloom

* Tue Feb 17 2015 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.5.5-0
- Autogenerated by Bloom

* Tue Feb 17 2015 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.5.4-0
- Autogenerated by Bloom

* Sun Dec 14 2014 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.5.3-0
- Autogenerated by Bloom

* Thu Dec 04 2014 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.5.2-0
- Autogenerated by Bloom

* Thu Nov 13 2014 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.5.1-0
- Autogenerated by Bloom

* Fri Nov 07 2014 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.5.0-0
- Autogenerated by Bloom

