Summary:	A network game browser
Name:		xqf
Version:	1.0.5
Release:	%mkrel 9
License:	GPLv2+
Group:          Games/Other
URL:		http://www.linuxgames.com/xqf
Source:         http://prdownloads.sourceforge.net/xqf/%{name}-%{version}.tar.bz2
Patch0:		xqf-1.0.5-do-not-hang-after-game-launch.patch
Requires:	qstat >= 2.5c-4mdk
BuildRequires:	desktop-file-utils
BuildRequires:	perl(XML::Parser)
BuildRequires:	libbzip2-devel
BuildRequires:	libgeoip-devel
BuildRequires:	libgtk+2-devel
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
XQF is a network game browser (e.g. Quake, Sin, etc.). It helps you
locate and connect to game servers.  It has configurable server and
player filters so you can find a server running your favorite game type
or that has a buddy.

%prep
%setup -q
%patch0 -p1

%build
sed -i 's/_32x32.png//g;' %{name}.desktop.in
%configure2_5x \
	--with-qstat=%{_bindir}/qstat-quake \
	--disable-gtk \
	--enable-gtk2 \
	--enable-bzip2 \
	--enable-geoip

%make

%install
rm -rf %{buildroot}
%makeinstall_std

# menu entry
desktop-file-install \
    --remove-category="Application" \
    --remove-category="X-SuSE-Core-Game" \
    --remove-category="ActionGame" \
    --add-category="ArcadeGame" \
    --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

mkdir -p %{buildroot}%{_iconsdir}/hicolor/{22x22,32x32,48x48}/apps/
mv -f %{buildroot}%{_datadir}/pixmaps/%{name}_22x22.png %{buildroot}%{_iconsdir}/hicolor/22x22/apps/%{name}.png
mv -f %{buildroot}%{_datadir}/pixmaps/%{name}_32x32.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
mv -f %{buildroot}%{_datadir}/pixmaps/%{name}_48x48.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
rm -rf %{buildroot}%{_datadir}/pixmaps

%find_lang %{name}

%if %mdkversion < 200900
%post
%{update_menus}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%clean_icon_cache hicolor
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%doc docs/*html docs/PreLaunch.example
%dir %{_datadir}/%{name}
%{_bindir}/*
%{_mandir}/man?/*
%{_datadir}/%{name}/*
%{_iconsdir}/hicolor/*/apps/*.png
%{_datadir}/applications/%{name}.desktop
