%global forgeurl https://github.com/catppuccin/grub
%global commit 0a37ab19f654e77129b409fed371891c01ffd0b9

%global _grubthemedir /boot/grub2/themes

Name:           catppuccin-grub-theme
Version:        1.0.0
Release:        %autorelease
Summary:        Soothing pastel theme for GRUB2

License:        MIT
URL:            %{forgeurl}

%forgemeta

Source0:        %{forgesource}

BuildArch:      noarch

%description
Soothing pastel theme for GRUB2.

%package -n catppuccin-latte-grub-theme
Summary:        Soothing pastel theme for GRUB2 - Latte

Requires:       grub2-common

%description -n catppuccin-latte-grub-theme
Soothing pastel theme for GRUB2 - Latte.

%package -n catppuccin-frappe-grub-theme
Summary:        Soothing pastel theme for GRUB2 - Frappe

Requires:       grub2-common

%description -n catppuccin-frappe-grub-theme
Soothing pastel theme for GRUB2 - Frappe.

%package -n catppuccin-macchiato-grub-theme
Summary:        Soothing pastel theme for GRUB2 - Macchiato

Requires:       grub2-common

%description -n catppuccin-macchiato-grub-theme
Soothing pastel theme for GRUB2 - Macchiato.

%package -n catppuccin-mocha-grub-theme
Summary:        Soothing pastel theme for GRUB2 - Mocha

Requires:       grub2-common

%description -n catppuccin-mocha-grub-theme
Soothing pastel theme for GRUB2 - Mocha.

%prep
%forgeautosetup

%build
# Nothing to build

%install
install -d %{buildroot}%{_grubthemedir}
cp -a src/. %{buildroot}%{_grubthemedir}/

%check
# No test suite available

%files

%files -n catppuccin-latte-grub-theme
%license LICENSE
%doc README.md
%{_grubthemedir}/catppuccin-latte-grub-theme

%files -n catppuccin-frappe-grub-theme
%license LICENSE
%doc README.md
%{_grubthemedir}/catppuccin-frappe-grub-theme

%files -n catppuccin-macchiato-grub-theme
%license LICENSE
%doc README.md
%{_grubthemedir}/catppuccin-macchiato-grub-theme

%files -n catppuccin-mocha-grub-theme
%license LICENSE
%doc README.md
%{_grubthemedir}/catppuccin-mocha-grub-theme

%changelog
%autochangelog