%define name cgoban1
%define version 1.9.14
%define release %mkrel 14
%define rname cgoban

Summary: A Go game client
Summary(fr): Un client pour le jeu de Go
Name: %{name}
Version: %{version}
Release: %{release}
License: GPLv2+
Group: Games/Boards
Source:	http://ovh.dl.sourceforge.net/sourceforge/cgoban1/%rname-%version.tar.bz2
Source2: %name-mini.png
Source3: %name.png
URL: http://cgoban1.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  pkgconfig(x11)
Provides: %rname = %{version}

%description
Cgoban (Complete Goban) is for Unix systems with X11.  It has the ability
to be a computerized go board, view and edit smart-go files, and connect to
go servers on the Internet.
Cgoban is also a smart interface for GNU Go.

%prep
%setup -q -n %rname-%version

%build
mv src/cgoban.c src/cgoban.c.orig
sed -e 's|\"./goDummy\"|\"/usr/games/gnugo --quiet\"|' <src/cgoban.c.orig >src/cgoban.c
mv configure configure.orig
sed -e "s|-O2 -fomit-frame-pointer|$RPM_OPT_FLAGS|g" <configure.orig >configure
chmod +x configure
%configure2_5x --program-suffix=1 
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6
mkdir -p $RPM_BUILD_ROOT%{_iconsdir}{,/mini,/large}
%makeinstall_std

cp cgoban_icon.png $RPM_BUILD_ROOT%{_iconsdir}/large/cgoban1.png
cp %{SOURCE2} $RPM_BUILD_ROOT%{_iconsdir}/mini/cgoban1.png 
cp %{SOURCE3} $RPM_BUILD_ROOT%{_iconsdir}/cgoban1.png 

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=CGoban
Comment=Graphical game of Go
Exec=%{_bindir}/%{name}
Icon=cgoban1
Terminal=false
Type=Application
Categories=Game;BoardGame;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc README TODO seigen-minoru.sgf
%{_bindir}/*
%{_mandir}/man6/*
%{_datadir}/applications/*.desktop
%{_iconsdir}/cgoban1.png
%{_iconsdir}/*/cgoban1.png


%changelog
* Wed Feb 02 2011 Funda Wang <fwang@mandriva.org> 1.9.14-14mdv2011.0
+ Revision: 635081
- drop fr translation
- rebuild
- tighten BR

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.9.14-13mdv2011.0
+ Revision: 616994
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 1.9.14-12mdv2010.0
+ Revision: 424797
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.9.14-11mdv2009.0
+ Revision: 243479
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Tue Mar 25 2008 Pascal Terjan <pterjan@mandriva.org> 1.9.14-9mdv2008.1
+ Revision: 189892
- Convert the description into UTF-8

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Dec 02 2007 Funda Wang <fwang@mandriva.org> 1.9.14-8mdv2008.1
+ Revision: 114364
- rebuild for new era

  + Thierry Vignaud <tv@mandriva.org>
    - kill hardcoded icon extension
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'


* Tue Jan 09 2007 Pascal Terjan <pterjan@mandriva.org> 1.9.14-7mdv2007.0
+ Revision: 106212
- Use autoconf 2.5
- XDG menu
- Import cgoban1

* Wed May 10 2006 Pascal Terjan <pterjan@mandriva.org> 1.9.14-6mdk
- mkrel

* Tue Mar 15 2005 Pascal Terjan <pterjan@mandrake.org> 1.9.14-5mdk
- rebuild to get the right menu section

* Sat May 15 2004 Pascal Terjan <pterjan@mandrake.org> 1.9.14-4mdk
- Rebuild
- use macros
- use cgoban1 for menu and icon
- add normal and mini icon

