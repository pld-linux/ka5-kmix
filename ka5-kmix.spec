%define		kdeappsver	21.04.2
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		kmix
Summary:	kmix
Name:		ka5-%{kaname}
Version:	21.04.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	ea5c22fee3d61baba56478eb41a636ec
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcompletion-devel >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-kglobalaccel-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kiconthemes-devel >= %{kframever}
BuildRequires:	kf5-knotifications-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kwindowsystem-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	kf5-plasma-framework-devel >= %{kframever}
BuildRequires:	kf5-solid-devel >= %{kframever}
BuildRequires:	ninja
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
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/{lt,sr}
%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/autostart/kmix_autostart.desktop
/etc/xdg/autostart/restore_kmix_volumes.desktop
%attr(755,root,root) %{_bindir}/kmix
%attr(755,root,root) %{_bindir}/kmixctrl
%attr(755,root,root) %{_bindir}/kmixremote
%{_libdir}/qt5/plugins/kf5/kded/kmixd.so
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
%dir %{_datadir}/kxmlgui5/kmix
%{_datadir}/kxmlgui5/kmix/kmixui.rc
%{_datadir}/metainfo/org.kde.kmix.appdata.xml
%{_libdir}/libkmixcore.so.*.*.*
%ghost %{_libdir}/libkmixcore.so.5
%{_datadir}/config.kcfg/kmixsettings.kcfg
%{_datadir}/qlogging-categories5/kmix.categories
