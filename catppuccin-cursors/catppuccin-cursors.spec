%global forgeurl https://github.com/catppuccin/cursors

Name:           catppuccin-cursors
Version:        2.0.0
Release:        %autorelease
Summary:        Catppuccin cursor themes

License:        GPL-2.0-only

%forgemeta

URL:            %{forgeurl}
Source0:        %{forgesource}

Patch:          remove-bundled-license-and-authors-files.patch
Patch:          use-explicit-whiskers-version-constraint.patch

BuildArch:      noarch
BuildRequires:  python3-pyside6
BuildRequires:  catppuccin-whiskers
BuildRequires:  xcursorgen
BuildRequires:  inkscape
BuildRequires:  just

Requires:       %{name}-latte = %{version}-%{release}
Requires:       %{name}-frappe = %{version}-%{release}
Requires:       %{name}-macchiato = %{version}-%{release}
Requires:       %{name}-mocha = %{version}-%{release}

%description
Meta package that installs all Catppuccin cursor themes:
Latte, Frappe, Macchiato, and Mocha.

%package latte
Summary:        Catppuccin Latte cursor theme

%description latte
Catppuccin Latte flavor cursor theme.

%package frappe
Summary:        Catppuccin Frappe cursor theme

%description frappe
Catppuccin Frappe flavor cursor theme.

%package macchiato
Summary:        Catppuccin Macchiato cursor theme

%description macchiato
Catppuccin Macchiato flavor cursor theme.

%package mocha
Summary:        Catppuccin Mocha cursor theme

%description mocha
Catppuccin Mocha flavor cursor theme.

%prep
%forgeautosetup -p1

%build
just all

%install
install -d %{buildroot}%{_datadir}/icons
cp -a dist/. %{buildroot}%{_datadir}/icons/

%check
# No test suite available

%files
%license LICENSE
%doc CHANGELOG.md
%doc README.md

%files latte
%license LICENSE
%doc CHANGELOG.md
%doc README.md
%{_datadir}/icons/catppuccin-latte-*-cursors

%files frappe
%license LICENSE
%doc CHANGELOG.md
%doc README.md
%{_datadir}/icons/catppuccin-frappe-*-cursors

%files macchiato
%license LICENSE
%doc CHANGELOG.md
%doc README.md
%{_datadir}/icons/catppuccin-macchiato-*-cursors

%files mocha
%license LICENSE
%doc CHANGELOG.md
%doc README.md
%{_datadir}/icons/catppuccin-mocha-*-cursors

%changelog
%autochangelog