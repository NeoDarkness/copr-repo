%global commit 28699090372cce33c12a923cf8fc297a9cae2cd4
%global shortcommit %(printf '%.7s' %{commit})
%global commitdate 20250908

%global _sddmthemedir %{_datadir}/sddm/themes

Name:           catppuccin-sddm-theme
Version:        0^%{commitdate}git%{shortcommit}
Release:        %autorelease
Summary:        Soothing pastel theme for SDDM

License:        MIT
URL:            https://github.com/catppuccin/sddm
Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildArch:      noarch

BuildRequires:  catppuccin-whiskers
BuildRequires:  just

Requires:       sddm
Provides:       %{name}-mocha = %{version}-%{release}

%description
Soothing pastel theme for SDDM (Mocha flavor by default).

%package latte
Summary:        Soothing pastel theme for SDDM - Latte

Requires:       sddm

%description latte
Soothing pastel theme for SDDM - Latte.

%package frappe
Summary:        Soothing pastel theme for SDDM - Frappe

Requires:       sddm

%description frappe
Soothing pastel theme for SDDM - Frappe.

%package macchiato
Summary:        Soothing pastel theme for SDDM - Macchiato

Requires:       sddm

%description macchiato
Soothing pastel theme for SDDM - Macchiato.

%prep
%autosetup -n sddm-%{commit} -p1

%build
just build

%install
install -d %{buildroot}%{_sddmthemedir}
cp -a themes/* %{buildroot}%{_sddmthemedir}/

%files
%license LICENSE
%doc README.md
%doc CHANGELOG.md
%{_sddmthemedir}/catppuccin-mocha-*

%files latte
%license LICENSE
%doc README.md
%doc CHANGELOG.md
%{_sddmthemedir}/catppuccin-latte-*

%files frappe
%license LICENSE
%doc README.md
%doc CHANGELOG.md
%{_sddmthemedir}/catppuccin-frappe-*

%files macchiato
%license LICENSE
%doc README.md
%doc CHANGELOG.md
%{_sddmthemedir}/catppuccin-macchiato-*

%changelog
%autochangelog