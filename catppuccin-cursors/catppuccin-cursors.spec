%global forgeurl https://github.com/catppuccin/cursors

Version:        2.0.0

%forgemeta

Name:           catppuccin-cursors
Release:        %autorelease
Summary:        Soothing pastel mouse cursors

License:        GPL-2.0-only
URL:            %{forgeurl}
Source0:        %{forgesource}
Patch0:         remove-bundled-license-and-authors-files.diff
Patch1:         use-explicit-whiskers-version-constraint.diff

BuildArch:      noarch

BuildRequires:  catppuccin-whiskers
BuildRequires:  inkscape
BuildRequires:  just
BuildRequires:  python3-pyside6
BuildRequires:  xcursorgen

%description
Soothing pastel mouse cursors.

%package latte
Summary:        Soothing pastel mouse cursors - Latte

%description latte
Soothing pastel mouse cursors - Latte.

%package frappe
Summary:        Soothing pastel mouse cursors - Frappe

%description frappe
Soothing pastel mouse cursors - Frappe.

%package macchiato
Summary:        Soothing pastel mouse cursors - Macchiato

%description macchiato
Soothing pastel mouse cursors - Macchiato.

%package mocha
Summary:        Soothing pastel mouse cursors - Mocha

%description mocha
Soothing pastel mouse cursors - Mocha.

%prep
%autosetup -n %{archivename} -p1

%build
just all

%install
install -d %{buildroot}%{_datadir}/icons
cp -a dist/. %{buildroot}%{_datadir}/icons/

%check

%files

%files latte
%license LICENSE
%doc README.md
%doc CHANGELOG.md
%{_datadir}/icons/catppuccin-latte-*-cursors

%files frappe
%license LICENSE
%doc README.md
%doc CHANGELOG.md
%{_datadir}/icons/catppuccin-frappe-*-cursors

%files macchiato
%license LICENSE
%doc README.md
%doc CHANGELOG.md
%{_datadir}/icons/catppuccin-macchiato-*-cursors

%files mocha
%license LICENSE
%doc README.md
%doc CHANGELOG.md
%{_datadir}/icons/catppuccin-mocha-*-cursors

%changelog
%autochangelog