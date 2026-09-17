%global commit 0a37ab19f654e77129b409fed371891c01ffd0b9
%global shortcommit %(printf '%.7s' %{commit})
%global commitdate 20250711

%global _grubthemedir /boot/grub2/themes

Name:           grub2-theme-catppuccin
Version:        0^%{commitdate}git%{shortcommit}
Release:        %autorelease
Summary:        Soothing pastel theme for GRUB2

License:        MIT
URL:            https://github.com/catppuccin/grub
Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildArch:      noarch

Requires:       grub2-common
Provides:       %{name}-mocha = %{version}-%{release}

%description
Soothing pastel theme for GRUB2 (Mocha flavor by default).

%package latte
Summary:        Soothing pastel theme for GRUB2 - Latte

Requires:       grub2-common

%description latte
Soothing pastel theme for GRUB2 - Latte.

%package frappe
Summary:        Soothing pastel theme for GRUB2 - Frappe

Requires:       grub2-common

%description frappe
Soothing pastel theme for GRUB2 - Frappe.

%package macchiato
Summary:        Soothing pastel theme for GRUB2 - Macchiato

Requires:       grub2-common

%description macchiato
Soothing pastel theme for GRUB2 - Macchiato.

%prep
%autosetup -n grub-%{commit} -p1

%install
install -d %{buildroot}%{_grubthemedir}
cp -a src/* %{buildroot}%{_grubthemedir}/

%files
%license LICENSE
%doc README.md
%{_grubthemedir}/catppuccin-mocha-grub-theme

%files latte
%license LICENSE
%doc README.md
%{_grubthemedir}/catppuccin-latte-grub-theme

%files frappe
%license LICENSE
%doc README.md
%{_grubthemedir}/catppuccin-frappe-grub-theme

%files macchiato
%license LICENSE
%doc README.md
%{_grubthemedir}/catppuccin-macchiato-grub-theme

%changelog
%autochangelog