%global commit a7eb08527dcce01010fa0ec46fa2bc4c3154f0d4
%global shortcommit %(printf '%.7s' %{commit})
%global commitdate 20250222

Name:           catppuccin-cursors
Version:        0^%{commitdate}git%{shortcommit}
Release:        %autorelease
Summary:        Soothing pastel mouse cursors

License:        GPL-2.0-only
URL:            https://github.com/catppuccin/cursors
Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch0:         remove-bundled-license-and-authors-files.diff

BuildArch:      noarch

BuildRequires:  catppuccin-whiskers
BuildRequires:  inkscape
BuildRequires:  just
BuildRequires:  python3-pyside6
BuildRequires:  xcursorgen

Provides:       %{name}-mocha = %{version}-%{release}

%description
Soothing pastel mouse cursors (Mocha flavor by default).

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

%prep
%autosetup -n cursors-%{commit} -p1

%build
just all

%install
install -d %{buildroot}%{_datadir}/icons
cp -a dist/* %{buildroot}%{_datadir}/icons/

%files
%license LICENSE
%doc README.md
%doc CHANGELOG.md
%{_datadir}/icons/catppuccin-mocha-*-cursors

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

%changelog
%autochangelog