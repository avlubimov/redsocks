Name:	    redsocks
Version:	0.5
Release:	4%{?dist}
Summary:	Transparent redirector of any TCP connection to a SOCKS or HTTPS proxy

Group:		Applications/System
License:	Apache 2.0
URL:		http://darkk.net.ru/redsocks/
Source0:        %{name}-%{version}.tar.gz

BuildRequires:	libevent-devel >= 2.0.0
Requires:	libevent >= 2.0.0
Requires(pre):     /usr/sbin/useradd, /usr/bin/getent
Requires(postun):  /usr/sbin/userdel


%description
This tool allows you to redirect any TCP connection to SOCKS or HTTPS
proxy using your firewall, so redirection is system-wide.

%prep
%autosetup -n %{name}-%{version}


%build
make %{?_smp_mflags}

%install
install -D %name                 %{buildroot}%{_bindir}/
install -D %{name}.service       %{buildroot}/usr/lib/systemd/system
install -D %{name}.conf.example  %{buildroot}%{_sysconfdir}/%{name}


%files
%doc README README.html doc/*
%{_bindir}/redsocks
%{_sysconfdir}/%{name}
/usr/lib/systemd/system/*

%pre
echo create system user account %{name} and system group %{name}
/usr/bin/getent group %{name} > /dev/null  || /usr/sbin/groupadd -r %{name}
/usr/bin/getent passwd %{name} > /dev/null || /usr/sbin/useradd -r -d /etc/%{name} -s /sbin/nologin -g %{name} %{name}

%postun
echo remove system user account %{name} and system group %{name}
/usr/sbin/userdel %{name}



%changelog
* Sun Feb 19 2017 avl <avlubimov@gmail.com> 0.5-3
- add extra docs (avlubimov@gmail.com)

* Sun Feb 19 2017 avl <avlubimov@gmail.com> 0.5-2
- fix rpm spec (avlubimov@gmail.com)


* Sun Feb 19 2017 avl <avlubimov@gmail.com> 0.5-1
- init rpm package




