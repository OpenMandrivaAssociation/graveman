%define name	graveman
%define version 0.3.12
%define realver %version-5
%define release %mkrel 9

Name: 	 	%{name}
Summary: 	Simple frontend for CD creation
Version: 	%{version}
Release: 	%{release}

Source:		http://graveman.tuxfamily.org/sources/%{name}-%{realver}.tar.bz2
Patch: graveman-0.3.12-5-cdrkit.patch
URL:		http://graveman.tuxfamily.org/index-e.php
License:	GPL
Group:		Archiving/Cd burning
BuildRequires:	ImageMagick
BuildRequires:	gtk2-devel libglade2.0-devel libid3tag-devel
BuildRequires:	libvorbis-devel libmad-devel
BuildRequires:	libflac-devel
BuildRequires:	libmng-devel
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
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot/%_mandir/man1
cp man/%name.man %buildroot/%_mandir/man1/%name.1
bzip2 %buildroot/%_mandir/man1/%name.1
mkdir -p %buildroot/%_mandir/fr/man1
cp man/%name.fr.man %buildroot/%_mandir/fr/man1/%name.1
bzip2 %buildroot/%_mandir/fr/man1/%name.1
perl -p -i -e 's/install\:/none\:/g' man/Makefile
%makeinstall_std

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="%{name}.png" needs="x11" title="Graveman" longtitle="Simple CD Burning" section="System/Archiving/CD Burning" xdg="true"
EOF
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-System-Archiving-CDBurning" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 pixmaps/graver.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 pixmaps/graver.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 pixmaps/graver.png $RPM_BUILD_ROOT/%_miconsdir/%name.png

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS THANKS README*
%{_bindir}/%name
%{_datadir}/applications/*
%{_datadir}/%name
%{_datadir}/pixmaps/*
%{_mandir}/man1/*
%{_mandir}/fr/man1/*
%{_menudir}/%name
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png


