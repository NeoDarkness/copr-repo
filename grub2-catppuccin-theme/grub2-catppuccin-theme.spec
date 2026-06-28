%global forgeurl https://github.com/catppuccin/grub
%global commit 0a37ab19f654e77129b409fed371891c01ffd0b9

%global _grubthemedir /boot/grub2/themes

Name:           grub2-catppuccin-theme
Version:        1.0.0
Release:        %autorelease
Summary:        Common files for Catppuccin GRUB2 themes

License:        MIT
URL:            %{forgeurl}

%forgemeta

Source0:        %{forgesource}

BuildArch:      noarch

%description
Common files for Catppuccin GRUB2 themes.

%package all
Summary:        Meta package for all Catppuccin GRUB2 themes

Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-latte = %{version}-%{release}
Requires:       %{name}-frappe = %{version}-%{release}
Requires:       %{name}-macchiato = %{version}-%{release}
Requires:       %{name}-mocha = %{version}-%{release}

%description all
Meta package that installs all Catppuccin GRUB2 themes.

%package latte
Summary:        Catppuccin Latte theme for GRUB2

Requires:       %{name} = %{version}-%{release}
Requires:       grub2-common

%description latte
Catppuccin Latte theme for GRUB2.

%package frappe
Summary:        Catppuccin Frappe theme for GRUB2

Requires:       %{name} = %{version}-%{release}
Requires:       grub2-common

%description frappe
Catppuccin Frappe theme for GRUB2.

%package macchiato
Summary:        Catppuccin Macchiato theme for GRUB2

Requires:       %{name} = %{version}-%{release}
Requires:       grub2-common

%description macchiato
Catppuccin Macchiato theme for GRUB2.

%package mocha
Summary:        Catppuccin Mocha theme for GRUB2

Requires:       %{name} = %{version}-%{release}
Requires:       grub2-common

%description mocha
Catppuccin Mocha theme for GRUB2.

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
%license LICENSE
%doc README.md

%files all

%files latte
%{_grubthemedir}/catppuccin-latte-grub-theme

%files frappe
%{_grubthemedir}/catppuccin-frappe-grub-theme

%files macchiato
%{_grubthemedir}/catppuccin-macchiato-grub-theme

%files mocha
%{_grubthemedir}/catppuccin-mocha-grub-theme

%changelog
%autochangelog