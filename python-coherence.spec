Summary:	A DLNA/UPnP MediaServer protocol implementation
Summary(pl.UTF-8):	Implementacja protokołu  DLNA/UPnP MediaServer
Name:		python-coherence
Version:	0.4.0
Release:	2
License:	MIT
Group:		Libraries/Python
Source0:	https://coherence.beebits.net/download/Coherence-%{version}.tar.gz
# Source0-md5:	b3fdc0de8ae46c6c9efdc4e7d6204417
Patch0:		%{name}-syntax.patch
URL:		https://coherence.beebits.net/
BuildRequires:	python-devel >= 1:2.5.0
BuildRequires:	python-setuptools
Requires:	python-Louie
Requires:	python-TwistedCore
Requires:	python-TwistedWeb
Requires:	python-configobj
Requires:	python-setuptools
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
As a stand-alone application Coherence acts as a DLNA/UPnP MediaServer
and exports local and remote media files via its plugins to other UPnP
clients.

And together with GStreamer it forms a controllable DLNA/UPnP
MediaRenderer.

%description -l pl.UTF-8
Wolno stojąca aplikacja Coherence służy jako DLNA/UPnP MediaServer i 
udostępnia lokalne i zdalne pliki multimedialne przez jego wtyczki do
innych klientów UPnP.

%prep
%setup -q -n Coherence-%{version}
%patch0 -p1

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name "*.py" | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/*
