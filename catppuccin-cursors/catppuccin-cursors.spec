%global forgeurl https://github.com/catppuccin/cursors

Name:           catppuccin-cursors
Version:        2.0.0
Release:        %autorelease
Summary:        Catppuccin cursor themes

License:        GPL-2.0-only
URL:            %{forgeurl}

%forgemeta

Source:         %{forgesource}

Patch:          remove-bundled-license-and-authors-files.patch
Patch:          use-explicit-whiskers-version-constraint.patch

BuildArch:      noarch

BuildRequires:  catppuccin-whiskers
BuildRequires:  inkscape
BuildRequires:  just
BuildRequires:  python3-pyside6
BuildRequires:  xcursorgen

Requires:       %{name}-latte = %{version}-%{release}
Requires:       %{name}-frappe = %{version}-%{release}
Requires:       %{name}-macchiato = %{version}-%{release}
Requires:       %{name}-mocha = %{version}-%{release}

%description
Meta package that installs all Catppuccin cursor themes.

%package latte
Summary:        Catppuccin Latte cursor theme

%description latte
Catppuccin Latte cursor theme.

%package frappe
Summary:        Catppuccin Frappe cursor theme

%description frappe
Catppuccin Frappe cursor theme.

%package macchiato
Summary:        Catppuccin Macchiato cursor theme

%description macchiato
Catppuccin Macchiato cursor theme.

%package mocha
Summary:        Catppuccin Mocha cursor theme

%description mocha
Catppuccin Mocha cursor theme.

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