%define name cgoban1
%define version 1.9.14
%define release %mkrel 7
%define rname cgoban

Summary: A Go game client
Summary(fr): Un client pour le jeu de Go
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Games/Boards
Source:	%rname-%version.tar.bz2
Source2: %name-mini.png
Source3: %name.png
URL: http://cgoban1.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires:  XFree86-devel
BuildRequires:	autoconf2.5
Provides: %rname = %{version}
#Requires: gnugo

%description
Cgoban (Complete Goban) is for Unix systems with X11.  It has the ability
to be a computerized go board, view and edit smart-go files, and connect to
go servers on the Internet.
Cgoban is also a smart interface for GNU Go.

%description -l fr
Cgoban (Complete Goban) est un programme pour X11. Il peut servir de goban
virtuel, à afficher ou éditer des fichiers smart-go et à se connecter à
des serveurs de go par Internet.
CGoban peut aussi servir d'interface à GNU Go.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n %rname-%version

%build
mv src/cgoban.c src/cgoban.c.orig
sed -e 's|\"./goDummy\"|\"/usr/games/gnugo --quiet\"|' <src/cgoban.c.orig >src/cgoban.c
mv configure configure.orig
sed -e "s|-O2 -fomit-frame-pointer|$RPM_OPT_FLAGS|g" <configure.orig >configure
chmod +x configure
%configure2_5x --program-suffix=1 
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6
mkdir -p $RPM_BUILD_ROOT%{_iconsdir}{,/mini,/large}
%makeinstall
cp cgoban_icon.png $RPM_BUILD_ROOT%{_iconsdir}/large/cgoban1.png
cp %{SOURCE2} $RPM_BUILD_ROOT%{_iconsdir}/mini/cgoban1.png 
cp %{SOURCE3} $RPM_BUILD_ROOT%{_iconsdir}/cgoban1.png 

mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat > $RPM_BUILD_ROOT%{_menudir}/cgoban1 <<EOF
?package(%name): \
 needs="x11" \
 section="More Applications/Games/Boards" \
 title="CGoban" \
 longtitle="Graphical game of Go" \
 command="/usr/bin/cgoban1" \
 icon="cgoban1.png" \
 xdg="true"
EOF

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=CGoban
Comment="Graphical game of Go
Exec=%{_bindir}/%{name}
Icon=cgoban1.png
Terminal=false
Type=Application
Categories=GTK;X-MandrivaLinux-MoreApplications-Games-Boards;Game;BoardGame;
Encoding=UTF-8
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus

%postun
%clean_menus

%files
%defattr(-,root,root)
%doc README COPYING TODO seigen-minoru.sgf
%{_bindir}/*
%{_mandir}/man6/*
%{_menudir}/cgoban1
%{_datadir}/applications/*.desktop
%{_iconsdir}/cgoban1.png
%{_iconsdir}/*/cgoban1.png


