# without this no-undefined flag gets passed in the pkgconfig file
%define _disable_ld_no_undefined 1

%define major 1
%define libname %mklibname ssh2_ %{major}
%define devname %mklibname ssh2 -d

Summary:	A library implementing the SSH2 protocol
Name:		libssh2
Version:	1.11.1
Release:	1
Group:		System/Libraries
License:	BSD
Url:		https://www.libssh2.org/
Source0:	http://www.libssh2.org/download/%{name}-%{version}.tar.gz
Source1:	http://www.libssh2.org/download/%{name}-%{version}.tar.gz.asc
BuildRequires:	libtool
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	hostname

%description
libssh2 is a library implementing the SSH2 protocol as defined by Internet
Drafts: SECSH-TRANS(22), SECSH-USERAUTH(25), SECSH-CONNECTION(23),
SECSH-ARCH(20), SECSH-FILEXFER(06)*, SECSH-DHGEX(04), and SECSH-NUMBERS(10).

%package -n	%{libname}
Summary:	A library implementing the SSH2 protocol
Group:		System/Libraries

%description -n	%{libname}
libssh2 is a library implementing the SSH2 protocol as defined by Internet
Drafts: SECSH-TRANS(22), SECSH-USERAUTH(25), SECSH-CONNECTION(23),
SECSH-ARCH(20), SECSH-FILEXFER(06)*, SECSH-DHGEX(04), and SECSH-NUMBERS(10).

%package -n	%{devname}
Summary:	Development library and header files for the %{name} library
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Provides:	ssh2-devel = %{version}-%{release}
Requires:	%{libname} >= %{version}-%{release}

%description -n	%{devname}
libssh2 is a library implementing the SSH2 protocol as defined by Internet
Drafts: SECSH-TRANS(22), SECSH-USERAUTH(25), SECSH-CONNECTION(23),
SECSH-ARCH(20), SECSH-FILEXFER(06)*, SECSH-DHGEX(04), and SECSH-NUMBERS(10).

This package contains the static %{name} library and its header files.

%prep
%autosetup -p1
%configure \
	--without-libgcrypt-prefix \
	--with-openssl=%{_prefix} \
	--with-libz=%{_prefix} \
	--disable-static \
	--disable-examples-build

%build
%make_build

##%check
#make check <- barfs at "Failed requesting pty", works as root

%install
%make_install

%files -n %{libname}
%doc COPYING 
%{_libdir}/libssh2.so.%{major}*

%files -n %{devname}
%doc docs/AUTHORS docs/BINDINGS.md docs/HACKING.md docs/TODO ChangeLog NEWS README RELEASE-NOTES
%{_includedir}/*
%{_libdir}/*.so
%{_mandir}/man3/*
%{_libdir}/pkgconfig/*.pc
