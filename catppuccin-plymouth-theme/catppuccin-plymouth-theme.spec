%global commit   198eba2071d80e4a23b8f51a5859e8f4acf8de6c

Name:           catppuccin-plymouth-theme
Version:        1.0.0
Release:        %autorelease
Summary:        Soothing pastel themes for Plymouth

License:        MIT

%forgemeta

URL:            https://github.com/catppuccin/plymouth
Source0:        %forgesource

BuildArch:      noarch

Requires:       %{name}-latte = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-frappe = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-macchiato = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-mocha = %{?epoch:%{epoch}:}%{version}-%{release}

%description
Meta package that installs all Catppuccin Plymouth themes (Frappé, Latte, Macchiato, Mocha).

%package latte
Summary:        Catppuccin Latte Plymouth theme
Requires:       plymouth-plugin-two-step
Requires:       plymouth-system-theme

%description latte
Catppuccin Latte flavor theme for Plymouth.

%package frappe
Summary:        Catppuccin Frappé Plymouth theme
Requires:       plymouth-plugin-two-step
Requires:       plymouth-system-theme

%description frappe
Catppuccin Frappé flavor theme for Plymouth.

%package macchiato
Summary:        Catppuccin Macchiato Plymouth theme
Requires:       plymouth-plugin-two-step
Requires:       plymouth-system-theme

%description macchiato
Catppuccin Macchiato flavor theme for Plymouth.

%package mocha
Summary:        Catppuccin Mocha Plymouth theme
Requires:       plymouth-plugin-two-step
Requires:       plymouth-system-theme

%description mocha
Catppuccin Mocha flavor theme for Plymouth.

%prep
%forgeautosetup

%install
install -d %{buildroot}%{_datadir}/plymouth/themes
cp -a themes/* %{buildroot}%{_datadir}/plymouth/themes/

%files latte
%license LICENSE
%doc README.md
%{_datadir}/plymouth/themes/catppuccin-latte

%files frappe
%license LICENSE
%doc README.md
%{_datadir}/plymouth/themes/catppuccin-frappe

%files macchiato
%license LICENSE
%doc README.md
%{_datadir}/plymouth/themes/catppuccin-macchiato

%files mocha
%license LICENSE
%doc README.md
%{_datadir}/plymouth/themes/catppuccin-mocha

%changelog
%autochangelog