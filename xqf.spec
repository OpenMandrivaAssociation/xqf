%define name     xqf
%define version  1.0.5
%define release  %mkrel 1
%define title       A network game browser
%define longtitle   A network game browser

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        A network game browser
License:        GPL
Group:          Games/Other
Source:         http://prdownloads.sourceforge.net/xqf/%{name}-%{version}.tar.bz2
URL:            http://www.linuxgames.com/xqf
Requires:       qstat >= 2.5c-4mdk
Requires:       gzip
Requires:       wget
BuildRequires:  libgdk-pixbuf-devel
BuildRequires:  desktop-file-utils
BuildRequires:  perl-XML-Parser
Buildroot:      %{_tmppath}/%{name}-%{version}

%description
XQF is a network game browser (e.g. Quake, Sin, etc.). It helps you
locate and connect to game servers.  It has configurable server and
player filters so you can find a server running your favorite game type
or that has a buddy.

%prep
%setup -q

%build
%configure --with-qstat=%_bindir/qstat-quake
%make

%install
rm -rf %{buildroot}
%makeinstall

# menu entry
desktop-file-install --vendor="" \
    --remove-category="Application" \
    --add-category="ArcadeGame" \
    --dir %{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/*

#Menu icons
install -D -m 644 %{buildroot}%{_datadir}/pixmaps/%{name}_22x22.png %{buildroot}%{_miconsdir}/%{name}.png
install -D -m 644 %{buildroot}%{_datadir}/pixmaps/%{name}_32x32.png %{buildroot}%{_iconsdir}/%{name}.png
install -D -m 644 %{buildroot}%{_datadir}/pixmaps/%{name}_48x48.png %{buildroot}%{_liconsdir}/%{name}.png

%{find_lang} %{name}

%post
%{update_menus}

%postun
%{clean_menus}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS BUGS COPYING ChangeLog NEWS README TODO
%doc docs/*html docs/PreLaunch.example
%{_bindir}/*
%{_mandir}/man6/xqf.*
%{_datadir}/xqf
%{_datadir}/pixmaps/*
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_datadir}/applications/%{name}.desktop


