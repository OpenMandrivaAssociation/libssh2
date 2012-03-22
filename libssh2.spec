%define rname libssh2

%define major 1
%define libname %mklibname ssh2_ %{major}
%define develname %mklibname ssh2 -d

Summary:	A library implementing the SSH2 protocol
Name:		%{rname}
Version:	1.4.0
Release:	2
Group:		System/Libraries
License:	BSD
URL:		http://www.libssh2.org/
Source0:	http://www.libssh2.org/download/%{rname}-%{version}.tar.gz
Source1:	http://www.libssh2.org/download/%{rname}-%{version}.tar.gz.asc
BuildRequires:	pkgconfig
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool

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

%package -n	%{develname}
Summary:	Static library and header files for the %{rname} library
Group:		Development/C
Provides:	%{rname}-devel = %{version}
Provides:	libssh-devel = %{version}
Provides:	ssh2-devel = %{version}
Requires:	%{libname} >= %{version}-%{release}

%description -n	%{develname}
libssh2 is a library implementing the SSH2 protocol as defined by Internet
Drafts: SECSH-TRANS(22), SECSH-USERAUTH(25), SECSH-CONNECTION(23),
SECSH-ARCH(20), SECSH-FILEXFER(06)*, SECSH-DHGEX(04), and SECSH-NUMBERS(10).

This package contains the static %{rname} library and its header files.

%prep
%setup -q -n %{rname}-%{version}

%build
%configure2_5x \
    --without-libgcrypt-prefix \
    --with-openssl=%{_prefix} \
    --with-libz=%{_prefix} \
    --disable-static

%make

##%check
#make check <- barfs at "Failed requesting pty", works as root

%install
%makeinstall_std

%files -n %{libname}
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so
%if %{mdvver} < 201200
%{_libdir}/*.la
%endif
%{_mandir}/man3/*
%{_libdir}/pkgconfig/*.pc
