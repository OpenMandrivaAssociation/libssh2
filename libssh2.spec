%define	rname libssh2

%define	major 1
%define libname	%mklibname ssh2_ %{major}
%define develname %mklibname ssh2 -d

Summary:	A library implementing the SSH2 protocol
Name:		%{rname}
Version:	0.18
Release:	%mkrel 3
Group:		System/Libraries
License:	BSD
URL:		http://www.libssh2.org/
Source0:	http://prdownloads.sourceforge.net/libssh2/%{rname}-%{version}.tar.gz
BuildRequires:	pkgconfig
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{rname}-%{version}-buildroot

%description
libssh2 is a library implementing the SSH2 protocol as defined by Internet
Drafts: SECSH-TRANS(22), SECSH-USERAUTH(25), SECSH-CONNECTION(23),
SECSH-ARCH(20), SECSH-FILEXFER(06)*, SECSH-DHGEX(04), and SECSH-NUMBERS(10).

%package -n     %{libname}
Summary:	A library implementing the SSH2 protocol
Group:		System/Libraries

%description -n %{libname}
libssh2 is a library implementing the SSH2 protocol as defined by Internet
Drafts: SECSH-TRANS(22), SECSH-USERAUTH(25), SECSH-CONNECTION(23),
SECSH-ARCH(20), SECSH-FILEXFER(06)*, SECSH-DHGEX(04), and SECSH-NUMBERS(10).

%package -n	%{develname}
Summary:	Static library and header files for the %{rname} library
Group:		Development/C
Provides:	%{rname}-devel = %{version}
Provides:	libssh-devel = %{version}
Provides:	ssh2-devel = %{version}
Requires:	%{libname} = %{version}

%description -n	%{develname}
libssh2 is a library implementing the SSH2 protocol as defined by Internet
Drafts: SECSH-TRANS(22), SECSH-USERAUTH(25), SECSH-CONNECTION(23),
SECSH-ARCH(20), SECSH-FILEXFER(06)*, SECSH-DHGEX(04), and SECSH-NUMBERS(10).

This package contains the static %{rname} library and its header files.

%prep

%setup -q -n %{rname}-%{version}

# this is a mess
perl -pi -e "s|/lib/|/%{_lib}/|g" configure.in
perl -pi -e "s|/lib\b|/%{_lib}|g" configure.in

%build
rm -f configure
libtoolize --copy --force; aclocal -I m4; autoconf; automake --add-missing

%serverbuild

%configure2_5x \
    --without-libgcrypt-prefix \
    --with-openssl=%{_prefix} \
    --with-libz=%{_prefix}

%make

%check
make check

%install
rm -rf %{buildroot}

%makeinstall_std

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_mandir}/man3/*
