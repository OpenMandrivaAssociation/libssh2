%define	rname libssh2

%define	major 2
%define libname	%mklibname ssh %{major}
%define develname %mklibname ssh -d

Summary:	A library implementing the SSH2 protocol
Name:		%{rname}
Version:	0.15
Release:	%mkrel 1
Group:		System/Libraries
License:	BSD
URL:		http://www.libssh2.org/
Source0:	http://prdownloads.sourceforge.net/libssh2/%{rname}-%{version}.tar.bz2
Patch0:		libssh2-0.14-soname.diff
Patch1:		libssh2-0.4-lib64.diff
BuildRequires:	pkgconfig
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{rname}-%{version}-buildroot

%description
libssh2 is a library implementing the SSH2 protocol as defined by
Internet Drafts: SECSH-TRANS(22), SECSH-USERAUTH(25),
SECSH-CONNECTION(23), SECSH-ARCH(20), SECSH-FILEXFER(06)*,
SECSH-DHGEX(04), and SECSH-NUMBERS(10).

%if "%{_lib}" != "lib"
%package -n     %{libname}
Summary:	A library implementing the SSH2 protocol
Group:		System/Libraries

%description -n %{libname}
libssh2 is a library implementing the SSH2 protocol as defined by
Internet Drafts: SECSH-TRANS(22), SECSH-USERAUTH(25),
SECSH-CONNECTION(23), SECSH-ARCH(20), SECSH-FILEXFER(06)*,
SECSH-DHGEX(04), and SECSH-NUMBERS(10).
%endif

%package -n	%{develname}
Summary:	Static library and header files for the %{rname} library
Group:		Development/C
Provides:	%{rname}-devel = %{version}
Provides:	libssh-devel = %{version}
Requires:	%{libname} = %{version}

%description -n	%{develname}
libssh2 is a library implementing the SSH2 protocol as defined by
Internet Drafts: SECSH-TRANS(22), SECSH-USERAUTH(25),
SECSH-CONNECTION(23), SECSH-ARCH(20), SECSH-FILEXFER(06)*,
SECSH-DHGEX(04), and SECSH-NUMBERS(10).

This package contains the static %{rname} library and its header
files.

%prep

%setup -q -n %{rname}-%{version}
%patch0 -p0
%patch1 -p1

%build

%configure2_5x

# this is a mess
find -name Makefile | xargs perl -pi -e "s|^LDFLAGS.*|LDFLAGS=-L%{_libdir} -lssl -lcrypto -ldl -lz|g"

%make
%make -C src libssh2.a

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_includedir}
install -d %{buildroot}%{_libdir}

install -m0644 include/*.h  %{buildroot}%{_includedir}/
install -m0755 src/libssh2.a %{buildroot}%{_libdir}/
install -m0755 src/libssh2.so.%{major} %{buildroot}%{_libdir}/
ln -snf libssh2.so.%{major} %{buildroot}%{_libdir}/libssh2.so

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc INSTALL LICENSE README
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
