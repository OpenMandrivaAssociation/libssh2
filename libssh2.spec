%define major	1
%define libname	%mklibname ssh2_ %{major}
%define devname	%mklibname ssh2 -d

Summary:	A library implementing the SSH2 protocol
Name:		libssh2
Version:	1.4.3
Release:	9
Group:		System/Libraries
License:	BSD
Url:		http://www.libssh2.org/
Source0:	http://www.libssh2.org/download/%{name}-%{version}.tar.gz
Source1:	http://www.libssh2.org/download/%{name}-%{version}.tar.gz.asc
BuildRequires:	libtool
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(zlib)

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
%setup -q

%build
%configure2_5x \
	--without-libgcrypt-prefix \
	--with-openssl=%{_prefix} \
	--with-libz=%{_prefix} \
	--disable-static \
	--disable-examples-build

%make

##%check
#make check <- barfs at "Failed requesting pty", works as root

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libssh2.so.%{major}*

%files -n %{devname}
%doc AUTHORS COPYING ChangeLog NEWS README
%{_includedir}/*
%{_libdir}/*.so
%{_mandir}/man3/*
%{_libdir}/pkgconfig/*.pc

