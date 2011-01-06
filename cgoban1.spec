%define name cgoban1
%define version 1.9.14
%define release %mkrel 13
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
BuildRequires:  libx11-devel
Provides: %rname = %{version}

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
