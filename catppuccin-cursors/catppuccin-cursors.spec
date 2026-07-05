%global forgeurl https://github.com/catppuccin/cursors
%global commit a7eb08527dcce01010fa0ec46fa2bc4c3154f0d4

Name:           catppuccin-cursors
Version:        2.0.0
Release:        %autorelease
Summary:        Common files for Catppuccin cursor themes

License:        GPL-2.0-only
URL:            %{forgeurl}

%forgemeta

Source0:        %{forgesource}

Patch0:         remove-bundled-license-and-authors-files.patch
Patch1:         use-explicit-whiskers-version-constraint.patch

BuildArch:      noarch

BuildRequires:  catppuccin-whiskers
BuildRequires:  inkscape
BuildRequires:  just
BuildRequires:  python3-pyside6
BuildRequires:  xcursorgen

%description
Common files for Catppuccin cursor themes.

%package all
Summary:        Meta package for all Catppuccin cursor themes

Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-latte = %{version}-%{release}
Requires:       %{name}-frappe = %{version}-%{release}
Requires:       %{name}-macchiato = %{version}-%{release}
Requires:       %{name}-mocha = %{version}-%{release}

%description all
Meta package that installs all Catppuccin cursor themes.

%package latte
Summary:        Catppuccin Latte cursor theme

Requires:       %{name} = %{version}-%{release}

%description latte
Catppuccin Latte cursor theme.

%package frappe
Summary:        Catppuccin Frappe cursor theme

Requires:       %{name} = %{version}-%{release}

%description frappe
Catppuccin Frappe cursor theme.

%package macchiato
Summary:        Catppuccin Macchiato cursor theme

Requires:       %{name} = %{version}-%{release}

%description macchiato
Catppuccin Macchiato cursor theme.

%package mocha
Summary:        Catppuccin Mocha cursor theme

Requires:       %{name} = %{version}-%{release}

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
%doc README.md

%files all

%files latte
%{_datadir}/icons/catppuccin-latte-*-cursors

%files frappe
%{_datadir}/icons/catppuccin-frappe-*-cursors

%files macchiato
%{_datadir}/icons/catppuccin-macchiato-*-cursors

%files mocha
%{_datadir}/icons/catppuccin-mocha-*-cursors

%changelog
%autochangelog