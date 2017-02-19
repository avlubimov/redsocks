Name:	    redsocks
Version:	0.5
Release:	1%{?dist}
Summary:	Transparent redirector of any TCP connection to a SOCKS or HTTPS proxy

Group:		Applications/System
License:	Apache 2.0
URL:		http://darkk.net.ru/redsocks/
Source0:        %{name}-%{version}.tar.gz

BuildRequires:	libevent-devel >= 2.0.0
Requires:	libevent >= 2.0.0

%description
This tool allows you to redirect any TCP connection to SOCKS or HTTPS
proxy using your firewall, so redirection is system-wide.

%prep
%autosetup -n %{name}-release-%{version}


%build
make %{?_smp_mflags}


%install
mkdir -p %{buildroot}%{_bindir}/
cp -p redsocks %{buildroot}%{_bindir}/


%files
%{_bindir}/redsocks



%changelog
* Sun Feb 19 2017 avl <avlubimov@gmail.com> 0.5-1
- init rpm package 


