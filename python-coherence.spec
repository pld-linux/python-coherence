Summary:	A DLNA/UPnP MediaServer protocol implementation
Name:		python-coherence
Version:	0.4.0
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	https://coherence.beebits.net/download/Coherence-%{version}.tar.gz
# Source0-md5:	b3fdc0de8ae46c6c9efdc4e7d6204417
URL:		https://coherence.beebits.net/
BuildRequires:	python-devel >= 1:2.5.0
Requires:	python-Louie
Requires:	python-TwistedCore
Requires:	python-TwistedWeb
Requires:	python-configobj
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
As a stand-alone application Coherence acts as a DLNA/UPnP MediaServer
and exports local and remote media files via its plugins to other UPnP
clients.

And together with GStreamer it forms a controllable DLNA/UPnP
MediaRenderer.

%prep
%setup -q -n Coherence-%{version}

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
