%global forgeurl https://github.com/catppuccin/grub
%global commit 0a37ab19f654e77129b409fed371891c01ffd0b9

%global _grubthemedir /boot/grub2/themes

Name:           grub2-catppuccin-theme
Version:        1.0.0
Release:        %autorelease
Summary:        Soothing pastel themes for GRUB2

License:        MIT
URL:            %{forgeurl}

%forgemeta

Source0:        %{forgesource}

BuildArch:      noarch

Requires:       grub2-catppuccin-latte-theme = %{version}-%{release}
Requires:       grub2-catppuccin-frappe-theme = %{version}-%{release}
Requires:       grub2-catppuccin-macchiato-theme = %{version}-%{release}
Requires:       grub2-catppuccin-mocha-theme = %{version}-%{release}

%description
Meta package that installs all Catppuccin GRUB2 themes.

%package -n grub2-catppuccin-latte-theme
Summary:        Catppuccin Latte theme for GRUB2
Requires:       grub2-common

%description -n grub2-catppuccin-latte-theme
Catppuccin Latte theme for GRUB2.

%package -n grub2-catppuccin-frappe-theme
Summary:        Catppuccin Frappe theme for GRUB2
Requires:       grub2-common

%description -n grub2-catppuccin-frappe-theme
Catppuccin Frappe theme for GRUB2.

%package -n grub2-catppuccin-macchiato-theme
Summary:        Catppuccin Macchiato theme for GRUB2
Requires:       grub2-common

%description -n grub2-catppuccin-macchiato-theme
Catppuccin Macchiato theme for GRUB2.

%package -n grub2-catppuccin-mocha-theme
Summary:        Catppuccin Mocha theme for GRUB2
Requires:       grub2-common

%description -n grub2-catppuccin-mocha-theme
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

%files -n grub2-catppuccin-latte-theme
%license LICENSE
%doc README.md
%{_grubthemedir}/catppuccin-latte-grub-theme

%files -n grub2-catppuccin-frappe-theme
%license LICENSE
%doc README.md
%{_grubthemedir}/catppuccin-frappe-grub-theme

%files -n grub2-catppuccin-macchiato-theme
%license LICENSE
%doc README.md
%{_grubthemedir}/catppuccin-macchiato-grub-theme

%files -n grub2-catppuccin-mocha-theme
%license LICENSE
%doc README.md
%{_grubthemedir}/catppuccin-mocha-grub-theme

%changelog
%autochangelog