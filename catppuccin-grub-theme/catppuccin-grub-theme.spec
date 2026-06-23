%global forgeurl https://github.com/catppuccin/grub
%global commit   0a37ab19f654e77129b409fed371891c01ffd0b9

Name:           catppuccin-grub-theme
Version:        1.0.0
Release:        %autorelease
Summary:        Soothing pastel themes for GRUB2

License:        MIT

%forgemeta

URL:            https://github.com/catppuccin/grub
Source0:        %forgesource

BuildArch:      noarch

Requires:       %{name}-latte = %{version}-%{release}
Requires:       %{name}-frappe = %{version}-%{release}
Requires:       %{name}-macchiato = %{version}-%{release}
Requires:       %{name}-mocha = %{version}-%{release}

%description
Meta package that installs Catppuccin GRUB2 themes (Frappé, Latte, Macchiato, Mocha).

%package latte
Summary:        Catppuccin Latte GRUB2 theme

%description latte
Catppuccin Latte flavor theme for GRUB2.

%package frappe
Summary:        Catppuccin Frappé GRUB2 theme

%description frappe
Catppuccin Frappé flavor theme for GRUB2.

%package macchiato
Summary:        Catppuccin Macchiato GRUB2 theme

%description macchiato
Catppuccin Macchiato flavor theme for GRUB2.

%package mocha
Summary:        Catppuccin Mocha GRUB2 theme

%description mocha
Catppuccin Mocha flavor theme for GRUB2.

%prep
%forgeautosetup

%install
install -d %{buildroot}/boot/grub2/themes
cp -a src/* %{buildroot}/boot/grub2/themes/

%files
%license LICENSE
%doc README.md

%files latte
%license LICENSE
%doc README.md
/boot/grub2/themes/catppuccin-latte-grub-theme

%files frappe
%license LICENSE
%doc README.md
/boot/grub2/themes/catppuccin-frappe-grub-theme

%files macchiato
%license LICENSE
%doc README.md
/boot/grub2/themes/catppuccin-macchiato-grub-theme

%files mocha
%license LICENSE
%doc README.md
/boot/grub2/themes/catppuccin-mocha-grub-theme

%changelog
%autochangelog