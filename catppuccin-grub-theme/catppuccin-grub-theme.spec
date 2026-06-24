%global forgeurl https://github.com/catppuccin/grub
%global commit   0a37ab19f654e77129b409fed371891c01ffd0b9

%global themedir /boot/grub2/themes

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
Meta package that installs Catppuccin GRUB2 themes:
Frappe, Latte, Macchiato, and Mocha.

%package latte
Summary:        Catppuccin Latte GRUB2 theme

%description latte
Catppuccin Latte flavor theme for GRUB2.

%package frappe
Summary:        Catppuccin Frappe GRUB2 theme

%description frappe
Catppuccin Frappe flavor theme for GRUB2.

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

%build
# Nothing to build

%install
install -d %{buildroot}%{themedir}
cp -a src/* %{buildroot}%{themedir}/

%check
# No test suite available

%files
%license LICENSE
%doc README.md

%files latte
%license LICENSE
%doc README.md
%{themedir}/catppuccin-latte-grub-theme/

%files frappe
%license LICENSE
%doc README.md
%{themedir}/catppuccin-frappe-grub-theme/

%files macchiato
%license LICENSE
%doc README.md
%{themedir}/catppuccin-macchiato-grub-theme/

%files mocha
%license LICENSE
%doc README.md
%{themedir}/catppuccin-mocha-grub-theme/

%changelog
%autochangelog