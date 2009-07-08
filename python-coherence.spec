Summary:	A DLNA/UPnP MediaServer protocol implementation
Summary(pl.UTF-8):	Implementacja protokołu DLNA/UPnP MediaServer
Name:		python-coherence
Version:	0.6.2
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	https://coherence.beebits.net/download/Coherence-%{version}.tar.gz
# Source0-md5:	feaeeaa68cae420c0c365c3c27b2a21e
URL:		https://coherence.beebits.net/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
Requires:	python-Louie
Requires:	python-TwistedCore
Requires:	python-TwistedWeb
Requires:	python-configobj
Requires:	python-setuptools
%pyrequires_eq	python-modules
# For applet:
Suggests:	python-PyQt4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
As a stand-alone application Coherence acts as a DLNA/UPnP MediaServer
and exports local and remote media files via its plugins to other UPnP
clients.

And together with GStreamer it forms a controllable DLNA/UPnP
MediaRenderer.

%description -l pl.UTF-8
Samodzielna aplikacja Coherence służy jako serwer mediów DLNA/UPnP,
udostępniając lokalne i zdalne pliki multimedialne poprzez wtyczki dla
innych klientów UPnP.

Wraz z GStreamerem tworzy sterowalny renderer mediów DLNA/UPnP.

%prep
%setup -q -n Coherence-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name "*.py" | xargs rm
rm -rf $RPM_BUILD_ROOT%{py_sitescriptdir}/misc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/*
