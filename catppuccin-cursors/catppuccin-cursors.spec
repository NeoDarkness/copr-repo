%global forgeurl https://github.com/catppuccin/cursors

Name:           catppuccin-cursors
Version:        2.0.0
Release:        %autorelease
Summary:        Catppuccin cursor themes

License:        GPL-2.0-only

%forgemeta

URL:            https://github.com/catppuccin/cursors
Source0:        %forgesource

BuildArch:      noarch
BuildRequires:  python3-pyside6
BuildRequires:  whiskers
BuildRequires:  xcursorgen
BuildRequires:  inkscape
BuildRequires:  just

Requires:       %{name}-latte = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-frappe = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-macchiato = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-mocha = %{?epoch:%{epoch}:}%{version}-%{release}

%description
Meta package that installs all Catppuccin cursor themes (Latte, Frappé, Macchiato, Mocha).

%package latte
Summary:        Catppuccin Latte cursor theme

%description latte
Catppuccin Latte flavor cursor theme.

%package frappe
Summary:        Catppuccin Frappé cursor theme

%description frappe
Catppuccin Frappé flavor cursor theme.

%package macchiato
Summary:        Catppuccin Macchiato cursor theme

%description macchiato
Catppuccin Macchiato flavor cursor theme.

%package mocha
Summary:        Catppuccin Mocha cursor theme

%description mocha
Catppuccin Mocha flavor cursor theme.

%prep
%forgeautosetup

%build
just all

%install
install -d %{buildroot}%{_datadir}/icons
cp -a dist/* %{buildroot}%{_datadir}/icons/

%files latte
%license LICENSE
%doc README.md CHANGELOG.md AUTHORS
%{_datadir}/icons/catppuccin-latte-*-cursors
%exclude %{_datadir}/icons/catppuccin-latte-*-cursors/LICENSE
%exclude %{_datadir}/icons/catppuccin-latte-*-cursors/AUTHORS
%exclude %{_datadir}/icons/catppuccin-latte-*-cursors/manifest.hl

%files frappe
%license LICENSE
%doc README.md CHANGELOG.md AUTHORS
%{_datadir}/icons/catppuccin-frappe-*-cursors
%exclude %{_datadir}/icons/catppuccin-frappe-*-cursors/LICENSE
%exclude %{_datadir}/icons/catppuccin-frappe-*-cursors/AUTHORS
%exclude %{_datadir}/icons/catppuccin-frappe-*-cursors/manifest.hl

%files macchiato
%license LICENSE
%doc README.md CHANGELOG.md AUTHORS
%{_datadir}/icons/catppuccin-macchiato-*-cursors
%exclude %{_datadir}/icons/catppuccin-macchiato-*-cursors/LICENSE
%exclude %{_datadir}/icons/catppuccin-macchiato-*-cursors/AUTHORS
%exclude %{_datadir}/icons/catppuccin-macchiato-*-cursors/manifest.hl

%files mocha
%license LICENSE
%doc README.md CHANGELOG.md AUTHORS
%{_datadir}/icons/catppuccin-mocha-*-cursors
%exclude %{_datadir}/icons/catppuccin-mocha-*-cursors/LICENSE
%exclude %{_datadir}/icons/catppuccin-mocha-*-cursors/AUTHORS
%exclude %{_datadir}/icons/catppuccin-mocha-*-cursors/manifest.hl

%changelog
%autochangelog