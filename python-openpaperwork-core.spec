%global module openpaperwork-core

Summary:	OpenPaperwork's core
Name:		python-%{module}
Version:	2.1.2
Release:	1
License:	GPL-3.0-or-later
Group:		Development/Python
URL:		https://pypi.org/project/openpaperwork-core/
Source0:	https://pypi.org/packages/source/o/%{module}/%{module}-%{version}.tar.gz
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(psutil)
BuildArch:	noarch

%description
The core manages Plugins, Callbacks and Interfaces. This package also
provide some basic plugins that may be used in any kind of application.

%files
%{py_puresitedir}/openpaperwork_core
%{py_puresitedir}/openpaperwork_core-*.*-info

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n %{module}-%{version}

%build
%py_build

%install
%py_install

