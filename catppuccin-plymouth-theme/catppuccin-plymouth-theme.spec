%global commit      198eba2071d80e4a23b8f51a5859e8f4acf8de6c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate  20250428

Name:           catppuccin-plymouth-theme
Version:        0^%{commitdate}git%{shortcommit}
Release:        %autorelease
Summary:        Soothing pastel themes for Plymouth

License:        MIT
URL:            https://github.com/catppuccin/plymouth
Source0:        %{url}/archive/%{commit}/plymouth-%{commit}.tar.gz

BuildArch:      noarch

Description:
Catppuccin Plymouth themes for all variants (Frappé, Latte, Macchiato, Mocha).

%package latte
Summary:        Catppuccin Latte Plymouth theme
Requires:       %{name} = %{version}-%{release}
Requires:       plymouth-plugin-two-step
Requires:       plymouth-system-theme

%description latte
Catppuccin Latte flavor theme for Plymouth.

%package frappe
Summary:        Catppuccin Frappé Plymouth theme
Requires:       %{name} = %{version}-%{release}
Requires:       plymouth-plugin-two-step
Requires:       plymouth-system-theme

%description frappe
Catppuccin Frappé flavor theme for Plymouth.

%package macchiato
Summary:        Catppuccin Macchiato Plymouth theme
Requires:       %{name} = %{version}-%{release}
Requires:       plymouth-plugin-two-step
Requires:       plymouth-system-theme

%description macchiato
Catppuccin Macchiato flavor theme for Plymouth.

%package mocha
Summary:        Catppuccin Mocha Plymouth theme
Requires:       %{name} = %{version}-%{release}
Requires:       plymouth-plugin-two-step
Requires:       plymouth-system-theme

%description mocha
Catppuccin Mocha flavor theme for Plymouth.

%prep
%autosetup -n plymouth-%{commit}

%install
install -d %{buildroot}%{_datadir}/plymouth/themes
cp -a themes/* %{buildroot}%{_datadir}/plymouth/themes/

%files
%license LICENSE
%doc README.md

%files latte
%{_datadir}/plymouth/themes/catppuccin-latte*

%files frappe
%{_datadir}/plymouth/themes/catppuccin-frappe*

%files macchiato
%{_datadir}/plymouth/themes/catppuccin-macchiato*

%files mocha
%{_datadir}/plymouth/themes/catppuccin-mocha*

%changelog
%autochangelog