%define rname libssh2

%define major 1
%define libname %mklibname ssh2_ %{major}
%define develname %mklibname ssh2 -d

Summary:	A library implementing the SSH2 protocol
Name:		%{rname}
Version:	1.4.3
Release:	1
Group:		System/Libraries
License:	BSD
URL:		http://www.libssh2.org/
Source0:	http://www.libssh2.org/download/%{rname}-%{version}.tar.gz
Source1:	http://www.libssh2.org/download/%{rname}-%{version}.tar.gz.asc
BuildRequires:	pkgconfig(openssl)
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
Provides:	%{rname}-devel = %{version}-%{release}
Provides:	libssh-devel = %{version}-%{release}
Provides:	ssh2-devel = %{version}-%{release}
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
    --disable-static \
    --disable-examples-build

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
%{_mandir}/man3/*
%{_libdir}/pkgconfig/*.pc


%changelog
* Sun May 20 2012 Oden Eriksson <oeriksson@mandriva.com> 1.4.2-1
+ Revision: 799732
- 1.4.2

* Thu Apr 05 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.4.1-1
+ Revision: 789335
- version update 1.4.1

* Thu Mar 22 2012 Andrey Bondrov <abondrov@mandriva.org> 1.4.0-2
+ Revision: 786089
- Disable static build in configure instead of manual removal, keep .la in 2011

  + Alexander Khrukin <akhrukin@mandriva.org>
    - rm -rf buildroot removed

* Tue Feb 07 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.4.0-1
+ Revision: 771624
- version update 1.4.0

* Sat Dec 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-2
+ Revision: 737454
- drop the static lib and the libtool *.la file
- don't use the serverbuild macro here
- various fixes

* Sun Sep 11 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-1
+ Revision: 699401
- 1.3.0

* Thu Aug 25 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.9-1
+ Revision: 696549
- 1.2.9

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.8-2
+ Revision: 662417
- mass rebuild

* Sun Apr 10 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.8-1
+ Revision: 652248
- 1.2.8

* Fri Aug 20 2010 Funda Wang <fwang@mandriva.org> 1.2.7-1mdv2011.0
+ Revision: 571454
- update to new version 1.2.7

* Mon Jul 12 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.6-1mdv2011.0
+ Revision: 551254
- 1.2.6

* Wed Apr 14 2010 Funda Wang <fwang@mandriva.org> 1.2.5-1mdv2010.1
+ Revision: 534634
- update to new version 1.2.5

* Thu Apr 08 2010 Eugeni Dodonov <eugeni@mandriva.com> 1.2.4-3mdv2010.1
+ Revision: 533140
- Rebuild for new openssl

* Fri Feb 26 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.4-2mdv2010.1
+ Revision: 511589
- rebuilt against openssl-0.9.8m

* Sun Feb 14 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.4-1mdv2010.1
+ Revision: 505697
- 1.2.4

* Thu Feb 04 2010 Funda Wang <fwang@mandriva.org> 1.2.3-1mdv2010.1
+ Revision: 500807
- New version 1.2.3

* Tue Nov 17 2009 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-1mdv2010.1
+ Revision: 466899
- 1.2.2

* Tue Sep 29 2009 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-1mdv2010.0
+ Revision: 450936
- 1.2.1

* Tue Aug 11 2009 Oden Eriksson <oeriksson@mandriva.com> 1.2-1mdv2010.0
+ Revision: 414888
- 1.2

* Wed Jun 10 2009 Oden Eriksson <oeriksson@mandriva.com> 1.1-1mdv2010.0
+ Revision: 384812
- 1.1

* Tue Feb 17 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0-1mdv2009.1
+ Revision: 341530
- 1.0
- disable make check for now (passes as root).

* Tue Dec 16 2008 Oden Eriksson <oeriksson@mandriva.com> 0.18-5mdv2009.1
+ Revision: 314882
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.18-4mdv2009.0
+ Revision: 223004
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sat Jan 19 2008 Anssi Hannula <anssi@mandriva.org> 0.18-3mdv2008.1
+ Revision: 155073
- provide ssh2-devel

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Nov 13 2007 Oden Eriksson <oeriksson@mandriva.com> 0.18-2mdv2008.1
+ Revision: 108418
- rebuild
- fix build on older distros

* Sun Nov 11 2007 Oden Eriksson <oeriksson@mandriva.com> 0.18-1mdv2008.1
+ Revision: 107530
- 0.18

* Tue Aug 07 2007 Oden Eriksson <oeriksson@mandriva.com> 0.17-1mdv2008.0
+ Revision: 59909
- 0.17

* Mon Aug 06 2007 Oden Eriksson <oeriksson@mandriva.com> 0.16-1mdv2008.0
+ Revision: 59479
- 0.16

* Tue Jun 26 2007 Oden Eriksson <oeriksson@mandriva.com> 0.15-2mdv2008.0
+ Revision: 44407
- fix correct libname, thanks mrl and anssi
- it has a major (1) now, so use it
- make it build
- run the test suite
- use the %%serverbuild macro

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - new version
    - new devel library policy


* Tue Oct 31 2006 Oden Eriksson <oeriksson@mandriva.com> 0.14-2mdv2007.0
+ Revision: 74579
- bunzip patches
- fix deps
- Import libssh2

* Tue Jul 25 2006 Emmanuel Andry <eandry@mandriva.org> 0.14-1mdv2007.0
- 0.14
- %%mkrel
- rediff P0

* Sun Nov 13 2005 Oden Eriksson <oeriksson@mandriva.com> 0.12-1mdk
- 0.12

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 0.10-2mdk
- added one lib64 fix

* Sat Jul 02 2005 Oden Eriksson <oeriksson@mandriva.com> 0.10-1mdk
- 0.10
- added one lib64 fix
- fix requires-on-release

* Sun Jun 19 2005 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.5-2mdk
- add BuildRequires: zlib-devel

* Sat Feb 12 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 0.5-1mdk
- 0.5

* Sat Jan 08 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 0.4-2mdk
- second try + one lib64 fix (P1)

* Sat Jan 08 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 0.4-1mdk
- initial mandrake package

