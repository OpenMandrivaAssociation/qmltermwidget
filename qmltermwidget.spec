%global debug_package %{nil}
%define snapshot 20260531
%define commit 8913504fa2ebd220ebe7c680c32954e1b3c035c5

Summary:	Terminal widget for QML
Name:		qmltermwidget
Version:	0.7.0
Release:	%{?snapshot:0.%{snapshot}.}1
License:	GPLv2
Source0:	https://github.com/Swordfish90/qmltermwidget/archive/%{commit}.tar.gz#/%{name}-%{snapshot}.tar.gz
Group:		System/Libraries
BuildRequires:	qmake-qt6
BuildRequires:	make
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Quick)
BuildRequires:	pkgconfig(Qt6QmlModels)
BuildRequires:	pkgconfig(Qt6Qml)
BuildRequires:	pkgconfig(Qt6Network)
BuildRequires:	pkgconfig(gl)

%description
Terminal widget for QML

%prep
%autosetup -p1 -n %{name}-%{commit}

# Rename KProcess to KTermProcess to avoid clashes with
# KF CoreAddons
# Based on https://github.com/Swordfish90/qmltermwidget/pull/31
find . -type f |xargs sed -i -e 's,KProcess,KTermProcess,g'

%{_qtdir}/bin/qmake *.pro

%build
%make_build

%install
make install INSTALL_ROOT=%{buildroot}

%files
%{_libdir}/qt6/qml/QMLTermWidget
