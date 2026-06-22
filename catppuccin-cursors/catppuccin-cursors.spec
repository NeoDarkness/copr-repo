Name:           catppuccin-cursors
Version:        2.0.0
Release:        %autorelease
Summary:        Catppuccin cursor themes (Frappé, Latte, Macchiato, Mocha)

License:        GPL-2.0-only
URL:            https://github.com/catppuccin/cursors
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3
BuildRequires:  python3-pyside6
BuildRequires:  whiskers
BuildRequires:  xcursorgen
BuildRequires:  inkscape
BuildRequires:  just

%description
Catppuccin cursor themes generated using whiskers.

%prep
%autosetup -n cursors-%{version}

%build
just all

%install
install -d %{buildroot}%{_datadir}/icons
cp -a dist/. %{buildroot}%{_datadir}/icons/

%files
%license LICENSE
%doc README.md AUTHORS
%{_datadir}/icons/catppuccin-*-cursors

%changelog
%autochangelog