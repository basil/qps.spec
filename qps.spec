Name:           qps
Summary:        Qt process viewer and manager
Version:        2.12.0
Release:        1%{?dist}

License:        GPL-2.0-or-later
URL:            https://lxqt-project.org/
Source0:        https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(lxqt)
BuildRequires:  perl

Requires:       hicolor-icon-theme

%description
Qps is a visual process manager for X11, a graphical equivalent of top or ps.
It displays processes in a window and lets you sort and manipulate them.

Qps can:

* Change the nice value of a process.
* Alter a process's scheduling policy and soft real-time priority.
* Display TCP and UDP sockets used by a process and the names of connected
  hosts (Linux only).
* Display a process's memory mappings (which files and shared libraries are
  loaded and where).
* Display a process's open files and the state of its Unix domain sockets.
* Kill processes or send any other signal to selected processes.
* Display the load average as a graph and use it as the icon when the window is
  iconified.
* Show current CPU, memory, and swap usage as graphs or numbers.
* Sort the process table by any attribute (size, CPU usage, owner, etc.).
* On SMP systems running Linux 2.1 or later (or on Solaris), display
  per-processor CPU usage and indicate which CPU each process is running on.
* Display the environment variables of any process.
* Show the process table as a tree, displaying parent–child relationships.
* Execute user-defined commands on selected processes.
* Display MOSIX-specific fields and migrate processes to other nodes in a
  cluster.

Qps runs on Linux and Solaris.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-qt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.lxqt.Qps.appdata.xml

%files -f %{name}.lang
%license COPYING
%doc CHANGELOG README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_metainfodir}/org.lxqt.Qps.appdata.xml
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_mandir}/man1/%{name}.1.gz

%changelog
* Tue Dec 23 2025 Basil Crow <me@basilcrow.com> - 2.12.0-1
- Initial packaging
