%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		kmix
Summary:	kmix
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	7e84451af562bf4b599c083919e973e1
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kcompletion-devel >= 5.14.0
BuildRequires:	kf5-kconfig-devel >= 5.14.0
BuildRequires:	kf5-kconfigwidgets-devel >= 5.14.0
BuildRequires:	kf5-kcrash-devel >= 5.14.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.14.0
BuildRequires:	kf5-kdoctools-devel >= 5.14.0
BuildRequires:	kf5-kglobalaccel-devel >= 5.14.0
BuildRequires:	kf5-ki18n-devel >= 5.14.0
BuildRequires:	kf5-kiconthemes-devel >= 5.14.0
BuildRequires:	kf5-knotifications-devel >= 5.14.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.14.0
BuildRequires:	kf5-kwindowsystem-devel >= 5.14.0
BuildRequires:	kf5-kxmlgui-devel >= 5.14.0
BuildRequires:	kf5-plasma-framework-devel >= 5.14.0
BuildRequires:	kf5-solid-devel >= 5.14.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KMix is an application to allow you to change the volume of your sound
card. Though small, it is full-featured, and it supports several
platforms and sound drivers. Though small, it is full-featured, and it
supports several platforms and sound drivers.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/autostart/kmix_autostart.desktop
/etc/xdg/autostart/restore_kmix_volumes.desktop
%attr(755,root,root) %{_bindir}/kmix
%attr(755,root,root) %{_bindir}/kmixctrl
%attr(755,root,root) %{_bindir}/kmixremote
%ghost %{_libdir}/libkmixcore.so.5
%{_libdir}/libkmixcore.so.5.*.*
%{_libdir}/qt5/plugins/kf5/kded/kmixd.so
%{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_mixer.so
%{_desktopdir}/org.kde.kmix.desktop
%{_datadir}/dbus-1/interfaces/org.kde.kmix.control.xml
%{_datadir}/dbus-1/interfaces/org.kde.kmix.mixer.xml
%{_datadir}/dbus-1/interfaces/org.kde.kmix.mixset.xml
%{_iconsdir}/hicolor/128x128/actions/kmix.png
%{_iconsdir}/hicolor/16x16/actions/kmix.png
%{_iconsdir}/hicolor/32x32/actions/kmix.png
%{_iconsdir}/hicolor/48x48/actions/kmix.png
%{_iconsdir}/hicolor/64x64/actions/kmix.png
%{_datadir}/kmix
%{_datadir}/knotifications5/kmix.notifyrc
%{_datadir}/kservices5/kmixctrl_restore.desktop
%{_datadir}/kservices5/plasma-dataengine-mixer.desktop
%dir %{_datadir}/kxmlgui5/kmix
%{_datadir}/kxmlgui5/kmix/kmixui.rc
%{_datadir}/metainfo/org.kde.kmix.appdata.xml
%{_datadir}/plasma/services/mixer.operations
