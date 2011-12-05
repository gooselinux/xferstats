Summary: Compiles information about file transfers from logfiles
Name: xferstats
Version: 2.16
Release: 21%{?dist}
URL: http://xferstats.off.net/
Source0: ftp://xferstats.off.net/%{name}-%{version}.tar.gz
Patch0: xferstats.patch
Patch1: xferstats-2.16-config-loc.patch
Patch2: xferstats-2.16-display.patch
Patch3: xferstats-glib2.patch
License: GPLv2+
Group: Applications/System
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: glib2-devel
BuildRequires: autoconf

%description
xferstats compiles information about file transfers from logfiles.

%prep
%setup -q

%patch0 -p1
%patch1 -p1 -b .config
%patch2 -p1 -b .display
%patch3 -p1 -b .glib2

%build
sed -e "s,PKG_PROG_PKG_CONFIG.*,PKG_CONFIG=%{_bindir}/pkg-config," %{_datadir}/aclocal/glib-2.0.m4 >aclocal.m4
autoconf
%configure

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{_datadir}/xferstats/
cp -a graphs %{buildroot}%{_datadir}/xferstats/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog
%config(noreplace) %{_sysconfdir}/xferstats.cfg
%{_bindir}/xferstats
%{_mandir}/*/*
%{_datadir}/xferstats

%changelog
* Wed Jan  6 2010 Jiri Moskovcak <jmoskovc@redhat.com> 2.16-21
- spec file fixes based on rpmlint warnings
- Resolves: #543948

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.16-20.1
- Rebuilt for RHEL 6

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.16-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.16-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Aug 12 2008 Jason L Tibbitts III <tibbs@math.uh.edu> - 2.16-18
- Fix license tag.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.16-17
- Autorebuild for GCC 4.3

* Tue Jan 08 2008 Than Ngo <than@redhat.com> 2.16-16
- rebuilt

* Thu Oct 18 2007  2.16-15 Than Ngo <than@redhat.com> 2.16-15
- rebuild

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.16-14.1
- rebuild

* Tue Apr 14 2006 Bill Nottingham <notting@redhat.com> - 2.16-14
- build against glib2

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.16-13.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.16-13.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Mar 16 2005 Than Ngo <than@redhat.com> 2.16-13
- rebuilt against gcc 4

* Wed Feb 09 2005 Than Ngo <than@redhat.com> 2.16-12
- rebuilt

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu May 20 2004 Than Ngo <than@redhat.com> 2.16-10
- add BuildRequires on glib-devel, bug #123761

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun  3 2003 Than Ngo <than@redhat.com> 2.16-7
- add a patch file from Gilbert, which fixes incorrect line
  counting for output reports #bug 91852

* Wed May 28 2003 Than Ngo <than@redhat.com> 2.16-6
- add mising "completed transfers" column from Gilbert E. Detillieux

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Dec 11 2002 Tim Powers <timp@redhat.com> 2.16-4
- rebuild on all arches

* Thu Jul 11 2002 Preston Brown <pbrown@redhat.com>
- rebuild for mainline distro inclusion

* Mon Apr 23 2001 Tim Powers <timp@redhat.com>
- fix where xferstats is expecting a config file, was in
/usr/local/etc, fixed to point to /etc (bug #36559)

* Thu Dec 14 2000 Tim Powers <timp@redhat.com>
- Initial build.
- there aren't any docs outside of the Changelog for this, well, the
  INSTALL file is there but that doesn't apply to the package at all

