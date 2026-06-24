%global forgeurl https://github.com/catppuccin/cursors

Name:           catppuccin-cursors
Version:        2.0.0
Release:        %autorelease
Summary:        Catppuccin cursor themes

License:        GPL-2.0-only

%forgemeta

URL:            %{forgeurl}
Source0:        %{forgesource}

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
%forgeautosetup

%build
just all

%install
install -d %{buildroot}%{_datadir}/icons
cp -a dist/* %{buildroot}%{_datadir}/icons/

find %{buildroot}%{_datadir}/icons/ \
    \( -name "LICENSE" -o -name "AUTHORS" -o -name "manifest.hl" \) \
    -delete

%check
# No test suite available

%files
%license LICENSE
%doc CHANGELOG.md
%doc README.md 

%files latte
%license LICENSE
%doc CHANGELOG.md README.md
%{_datadir}/icons/catppuccin-latte-rosewater-cursors
%{_datadir}/icons/catppuccin-latte-flamingo-cursors
%{_datadir}/icons/catppuccin-latte-pink-cursors
%{_datadir}/icons/catppuccin-latte-mauve-cursors
%{_datadir}/icons/catppuccin-latte-red-cursors
%{_datadir}/icons/catppuccin-latte-maroon-cursors
%{_datadir}/icons/catppuccin-latte-peach-cursors
%{_datadir}/icons/catppuccin-latte-yellow-cursors
%{_datadir}/icons/catppuccin-latte-green-cursors
%{_datadir}/icons/catppuccin-latte-teal-cursors
%{_datadir}/icons/catppuccin-latte-sky-cursors
%{_datadir}/icons/catppuccin-latte-sapphire-cursors
%{_datadir}/icons/catppuccin-latte-blue-cursors
%{_datadir}/icons/catppuccin-latte-lavender-cursors
%{_datadir}/icons/catppuccin-latte-dark-cursors
%{_datadir}/icons/catppuccin-latte-light-cursors

%files frappe
%license LICENSE
%doc CHANGELOG.md README.md
%{_datadir}/icons/catppuccin-frappe-rosewater-cursors
%{_datadir}/icons/catppuccin-frappe-flamingo-cursors
%{_datadir}/icons/catppuccin-frappe-pink-cursors
%{_datadir}/icons/catppuccin-frappe-mauve-cursors
%{_datadir}/icons/catppuccin-frappe-red-cursors
%{_datadir}/icons/catppuccin-frappe-maroon-cursors
%{_datadir}/icons/catppuccin-frappe-peach-cursors
%{_datadir}/icons/catppuccin-frappe-yellow-cursors
%{_datadir}/icons/catppuccin-frappe-green-cursors
%{_datadir}/icons/catppuccin-frappe-teal-cursors
%{_datadir}/icons/catppuccin-frappe-sky-cursors
%{_datadir}/icons/catppuccin-frappe-sapphire-cursors
%{_datadir}/icons/catppuccin-frappe-blue-cursors
%{_datadir}/icons/catppuccin-frappe-lavender-cursors
%{_datadir}/icons/catppuccin-frappe-dark-cursors
%{_datadir}/icons/catppuccin-frappe-light-cursors

%files macchiato
%license LICENSE
%doc CHANGELOG.md README.md
%{_datadir}/icons/catppuccin-macchiato-rosewater-cursors
%{_datadir}/icons/catppuccin-macchiato-flamingo-cursors
%{_datadir}/icons/catppuccin-macchiato-pink-cursors
%{_datadir}/icons/catppuccin-macchiato-mauve-cursors
%{_datadir}/icons/catppuccin-macchiato-red-cursors
%{_datadir}/icons/catppuccin-macchiato-maroon-cursors
%{_datadir}/icons/catppuccin-macchiato-peach-cursors
%{_datadir}/icons/catppuccin-macchiato-yellow-cursors
%{_datadir}/icons/catppuccin-macchiato-green-cursors
%{_datadir}/icons/catppuccin-macchiato-teal-cursors
%{_datadir}/icons/catppuccin-macchiato-sky-cursors
%{_datadir}/icons/catppuccin-macchiato-sapphire-cursors
%{_datadir}/icons/catppuccin-macchiato-blue-cursors
%{_datadir}/icons/catppuccin-macchiato-lavender-cursors
%{_datadir}/icons/catppuccin-macchiato-dark-cursors
%{_datadir}/icons/catppuccin-macchiato-light-cursors

%files mocha
%license LICENSE
%doc CHANGELOG.md README.md
%{_datadir}/icons/catppuccin-mocha-rosewater-cursors
%{_datadir}/icons/catppuccin-mocha-flamingo-cursors
%{_datadir}/icons/catppuccin-mocha-pink-cursors
%{_datadir}/icons/catppuccin-mocha-mauve-cursors
%{_datadir}/icons/catppuccin-mocha-red-cursors
%{_datadir}/icons/catppuccin-mocha-maroon-cursors
%{_datadir}/icons/catppuccin-mocha-peach-cursors
%{_datadir}/icons/catppuccin-mocha-yellow-cursors
%{_datadir}/icons/catppuccin-mocha-green-cursors
%{_datadir}/icons/catppuccin-mocha-teal-cursors
%{_datadir}/icons/catppuccin-mocha-sky-cursors
%{_datadir}/icons/catppuccin-mocha-sapphire-cursors
%{_datadir}/icons/catppuccin-mocha-blue-cursors
%{_datadir}/icons/catppuccin-mocha-lavender-cursors
%{_datadir}/icons/catppuccin-mocha-dark-cursors
%{_datadir}/icons/catppuccin-mocha-light-cursors

%changelog
%autochangelog