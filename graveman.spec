%define realver %version-5

Name: 	 	graveman
Summary: 	Simple frontend for CD creation
Version: 	0.3.12
Release: 	14

Source:		http://graveman.tuxfamily.org/sources/%{name}-%{realver}.tar.bz2
Patch: graveman-0.3.12-5-cdrkit.patch
URL:		https://graveman.tuxfamily.org/index-e.php
License:	GPLv2+
Group:		Archiving/Cd burning
BuildRequires:	imagemagick
BuildRequires:	gtk2-devel libglade2.0-devel libid3tag-devel
BuildRequires:	pkgconfig(vorbis) libmad-devel
BuildRequires:	pkgconfig(flac)
BuildRequires:	mng-devel
BuildRequires:	perl-XML-Parser
BuildRequires: desktop-file-utils
Requires:	cdrkit cdrkit-genisoimage sox dvd+rw-tools sox cdrdao

%description
Another frontend for cdrecord, mkisofs, readcd and sox!
With graveman you can burn audio cds (wav, ogg, mp3), data cds,
and duplicate cds.

%prep
%setup -q -n %name-%realver
%patch -p1 -b .cdrkit

%build
%configure2_5x
%make
										
%install
mkdir -p %buildroot/%_mandir/man1
cp man/%name.man %buildroot/%_mandir/man1/%name.1
bzip2 %buildroot/%_mandir/man1/%name.1
mkdir -p %buildroot/%_mandir/fr/man1
cp man/%name.fr.man %buildroot/%_mandir/fr/man1/%name.1
bzip2 %buildroot/%_mandir/fr/man1/%name.1
perl -p -i -e 's/install\:/none\:/g' man/Makefile
%makeinstall_std

#menu
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-System-Archiving-CDBurning" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

#icons
mkdir -p %{buildroot}/%_liconsdir
convert -size 48x48 pixmaps/graver.png %{buildroot}/%_liconsdir/%name.png
mkdir -p %{buildroot}/%_iconsdir
convert -size 32x32 pixmaps/graver.png %{buildroot}/%_iconsdir/%name.png
mkdir -p %{buildroot}/%_miconsdir
convert -size 16x16 pixmaps/graver.png %{buildroot}/%_miconsdir/%name.png

%find_lang %name

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS THANKS README*
%{_bindir}/%name
%{_datadir}/applications/*
%{_datadir}/%name
%{_datadir}/pixmaps/*
%{_mandir}/man1/*
%{_mandir}/fr/man1/*
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png




%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.12-11mdv2011.0
+ Revision: 619252
- the mass rebuild of 2010.0 packages

* Sat May 16 2009 JÃ©rÃ´me Brenier <incubusss@mandriva.org> 0.3.12-10mdv2010.0
+ Revision: 376325
- fix license (GPLv2+)

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 0.3.12-9mdv2009.0
+ Revision: 218421
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Thierry Vignaud <tv@mandriva.org>
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Tue Feb 06 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.3.12-9mdv2007.0
+ Revision: 116812
- replace remaining strings with their cdrkit versions

* Mon Jan 08 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.3.12-8mdv2007.1
+ Revision: 106004
- it's called genisoimage, stupid

* Mon Jan 08 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.3.12-7mdv2007.1
+ Revision: 105934
- patch for cdrkit

* Mon Dec 11 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.3.12-6mdv2007.1
+ Revision: 95022
- Import graveman

* Mon Dec 11 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.3.12-6mdv2007.1
- Rebuild

* Thu Aug 03 2006 Götz Waschk <waschk@mandriva.org> 0.3.12-5mdv2007.0
- xdg menu

* Tue Jun 13 2006 Michael Scherer <misc@mandriva.org> 0.3.12-4mdv2007.0
- from dovix ( dovix2003@yahoo.com )
  - New release 0.3.12.5, fix #23048
- add %%{1}mdv2007.1

* Thu Jun 16 2005 Götz Waschk <waschk@mandriva.org> 0.3.12-3mdk
- update to patchlevel 4

* Thu May 19 2005 Götz Waschk <waschk@mandriva.org> 0.3.12-2mdk
- fix buildrequires

* Wed May 18 2005 Götz Waschk <waschk@mandriva.org> 0.3.12-1mdk
- fix URL
- New release 0.3.12

* Thu May 12 2005 Götz Waschk <waschk@mandriva.org> 0.3.11-2mdk
- fix buildrequires

* Sat May 07 2005 Götz Waschk <waschk@mandriva.org> 0.3.11-1mdk
- new URLs
- New release 0.3.11

* Tue Apr 05 2005 Austin Acton <austin@mandrake.org> 0.3.10-1mdk
- New release 0.3.10
- fudge man install for now
- fix source URL

* Sun Apr 03 2005 Austin Acton <austin@mandrake.org> 0.3.9-1mdk
- 0.3.9
- require flac and cdrdao

* Tue Feb 15 2005 Austin Acton <austin@mandrake.org> 0.3.8-1mdk
- 0.3.8
- require sox

* Sun Feb 13 2005 Austin Acton <austin@mandrake.org> 0.3.7-1mdk
- 0.3.7

* Thu Feb 03 2005 Austin Acton <austin@mandrake.org> 0.3.6-1mdk
- 0.3.6
- require dvd+rw-tools
- source URL

* Tue Feb 01 2005 Lenny Cartier <lenny@mandrakesoft.com> 0.3.5-2mdk
- url

* Tue Feb 01 2005 Lenny Cartier <lenny@mandrakesoft.com> 0.3.5-1mdk
- 0.3.5

* Tue Jan 25 2005 Austin Acton <austin@mandrake.org> 0.3.4-1mdk
- 0.3.4

* Mon Jan 24 2005 Lenny Cartier <lenny@mandrakesoft.com> 0.3.2-1mdk
- 0.3.2

* Thu Jan 20 2005 Austin Acton <austin@mandrake.org> 0.3.1-1mdk
- 0.3.1
- buildrequires libmad

* Tue Jan 18 2005 Austin Acton <austin@mandrake.org> 0.3.0-1mdk
- 0.3.0

* Mon Jan 17 2005 Austin Acton <austin@mandrake.org> 0.2.20050117-1mdk
- 0.2.20050117

* Wed Jan 12 2005 Austin Acton <austin@mandrake.org> 0.2.20050112-1mdk
- 0.2.20050112

* Mon Jan 10 2005 Austin Acton <austin@mandrake.org> 0.2.20050110-1mdk
- initial package

