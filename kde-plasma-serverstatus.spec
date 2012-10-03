Name:           kde-plasma-serverstatus
Version:        1.5.1
Release:        1%{?dist}
Summary:        This widget/applet/plasmoid lets you monitor one or more servers

License:        GPLv2
URL:            http://gitorious.org/serverstatuswidget/pages/Home
Source0:        http://kde-look.org/CONTENT/content-files/101336-serverstatuswidget-%{version}.tar.bz2

BuildRequires:  kde-filesystem
BuildRequires:  kde-workspace-devel
BuildRequires:  qt4-devel
BuildRequires:  cmake

%description
The Server Status Widget is a Plasma widget (a.k.a. applet or Plasmoid) for
your KDE desktop.
This widget/applet/plasmoid lets you monitor one or more servers via pings, TCP
connects or custom unix commands in a configurable interval. The icon changes
if a server does not respond to a check, optionally triggering configurable KDE
notifications.

%prep
%setup -q -n serverstatuswidget-%{version}


%build
%cmake
make %{?_smp_mflags}


%install
%make_install
%find_lang plasma-applet-serverstatus

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f plasma-applet-serverstatus.lang
%doc COPYING README
%{_kde4_libdir}/kde4/plasma_applet_serverstatus.so
%{_kde4_datadir}/kde4/apps/plasma-applet-serverstatus/plasma-applet-serverstatus.notifyrc
%{_kde4_datadir}/kde4/services/plasma-applet-serverstatus.desktop


%changelog
* Wed Oct 03 2012 Vasiliy N. Glazov <vascom2@gmail.com> 1.5.1-1.R
- Initial release
