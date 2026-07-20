%global forgeurl https://github.com/catppuccin/grub
%global commit 0a37ab19f654e77129b409fed371891c01ffd0b9

%global _grubthemedir /boot/grub2/themes

%forgemeta

Name:           grub2-theme-catppuccin
Version:        0^20250711.g0a37ab1
Release:        %autorelease
Summary:        Soothing pastel theme for GRUB2

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch

%description
Soothing pastel theme for GRUB2.

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

%package mocha
Summary:        Soothing pastel theme for GRUB2 - Mocha

Requires:       grub2-common

%description mocha
Soothing pastel theme for GRUB2 - Mocha.

%prep
%forgeautosetup -p1

%build

%install
install -d %{buildroot}%{_grubthemedir}
cp -r src/* %{buildroot}%{_grubthemedir}/

%check

%files

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

%files mocha
%license LICENSE
%doc README.md
%{_grubthemedir}/catppuccin-mocha-grub-theme

%changelog
%autochangelog