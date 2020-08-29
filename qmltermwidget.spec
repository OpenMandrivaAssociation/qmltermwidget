%global debug_package %{nil}
%define snapshot 20200829

Summary:	Terminal widget for QML
Name:		qmltermwidget
Version:	0.7.0
Release:	%{?snapshot:0.%{snapshot}.}1
License:	GPLv2
Source0:	https://github.com/Swordfish90/qmltermwidget/archive/master/%{name}-%{snapshot}.tar.gz
Group:		System/Libraries
BuildRequires:	qmake5
BuildRequires:	make
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5QmlModels)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(gl)

%description
Terminal widget for QML

%prep
%autosetup -p1 -n qmltermwidget-master
qmake-qt5 *.pro

%build
%make_build

%install
make install INSTALL_ROOT=%{buildroot}

%files
%{_libdir}/qt5/qml/QMLTermWidget
