Name:           catppuccin-cursors
Version:        2.0.0
Release:        %autorelease
Summary:        Catppuccin cursor themes

License:        GPL-2.0-only
URL:            https://github.com/catppuccin/cursors
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-pyside6
BuildRequires:  whiskers
BuildRequires:  xcursorgen
BuildRequires:  inkscape
BuildRequires:  just

Recommends:     %{name}-latte = %{?epoch:%{epoch}:}%{version}-%{release}
Recommends:     %{name}-frappe = %{?epoch:%{epoch}:}%{version}-%{release}
Recommends:     %{name}-macchiato = %{?epoch:%{epoch}:}%{version}-%{release}
Recommends:     %{name}-mocha = %{?epoch:%{epoch}:}%{version}-%{release}

%description
Catppuccin cursor themes generated using whiskers.

%package latte
Summary:        Catppuccin Latte cursor theme
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description latte
Catppuccin Latte flavor cursor theme.

%package frappe
Summary:        Catppuccin Frappé cursor theme
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description frappe
Catppuccin Frappé flavor cursor theme.

%package macchiato
Summary:        Catppuccin Macchiato cursor theme
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description macchiato
Catppuccin Macchiato flavor cursor theme.

%package mocha
Summary:        Catppuccin Mocha cursor theme
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description mocha
Catppuccin Mocha flavor cursor theme.

%prep
%autosetup -n cursors-%{version}

%build
just all

%install
install -d %{buildroot}%{_datadir}/icons
cp -a dist/* %{buildroot}%{_datadir}/icons/

%files
%license LICENSE AUTHORS
%doc README.md CHANGELOG.md

%files latte
%{_datadir}/icons/catppuccin-latte-*-cursors/*
%exclude %{_datadir}/icons/catppuccin-latte-*-cursors/LICENSE
%exclude %{_datadir}/icons/catppuccin-latte-*-cursors/AUTHORS
%exclude %{_datadir}/icons/catppuccin-latte-*-cursors/manifest.hl

%files frappe
%{_datadir}/icons/catppuccin-frappe-*-cursors/*
%exclude %{_datadir}/icons/catppuccin-frappe-*-cursors/LICENSE
%exclude %{_datadir}/icons/catppuccin-frappe-*-cursors/AUTHORS
%exclude %{_datadir}/icons/catppuccin-frappe-*-cursors/manifest.hl

%files macchiato
%{_datadir}/icons/catppuccin-macchiato-*-cursors/*
%exclude %{_datadir}/icons/catppuccin-macchiato-*-cursors/LICENSE
%exclude %{_datadir}/icons/catppuccin-macchiato-*-cursors/AUTHORS
%exclude %{_datadir}/icons/catppuccin-macchiato-*-cursors/manifest.hl

%files mocha
%{_datadir}/icons/catppuccin-mocha-*-cursors/*
%exclude %{_datadir}/icons/catppuccin-mocha-*-cursors/LICENSE
%exclude %{_datadir}/icons/catppuccin-mocha-*-cursors/AUTHORS
%exclude %{_datadir}/icons/catppuccin-mocha-*-cursors/manifest.hl

%changelog
%autochangelog