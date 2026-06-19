%global commit      198eba2071d80e4a23b8f51a5859e8f4acf8de6c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date        20260619

Name:           catppuccin-plymouth-theme
Version:        0^%{date}git%{shortcommit}
Release:        %autorelease
Summary:        Catppuccin themes for Plymouth boot splash

License:        MIT
URL:            https://github.com/catppuccin/plymouth
Source0:        https://github.com/catppuccin/plymouth/archive/%{commit}/plymouth-%{commit}.tar.gz

BuildArch:      noarch

Requires:       %{name}-mocha = %{version}-%{release}
Requires:       %{name}-macchiato = %{version}-%{release}
Requires:       %{name}-frappe = %{version}-%{release}
Requires:       %{name}-latte = %{version}-%{release}

%description
Meta package for all Catppuccin Plymouth themes.

%package mocha
Summary:        Catppuccin Mocha theme for Plymouth
Requires:       plymouth-system-theme
Requires:       plymouth-plugin-two-step
%description mocha
Catppuccin Mocha theme for Plymouth.

%package macchiato
Summary:        Catppuccin Macchiato theme for Plymouth
Requires:       plymouth-system-theme
Requires:       plymouth-plugin-two-step
%description macchiato
Catppuccin Macchiato theme for Plymouth.

%package frappe
Summary:        Catppuccin Frappé theme for Plymouth
Requires:       plymouth-system-theme
Requires:       plymouth-plugin-two-step
%description frappe
Catppuccin Frappé theme for Plymouth.

%package latte
Summary:        Catppuccin Latte theme for Plymouth
Requires:       plymouth-system-theme
Requires:       plymouth-plugin-two-step
%description latte
Catppuccin Latte theme for Plymouth.

%prep
%autosetup -n plymouth-%{commit}

%install
install -dm755 %{buildroot}%{_datadir}/plymouth/themes
cp -a themes/. %{buildroot}%{_datadir}/plymouth/themes/
find %{buildroot}%{_datadir}/plymouth/themes -type f -exec chmod 0644 {} +

%files
%license LICENSE
%doc README.md

%files mocha
%{_datadir}/plymouth/themes/catppuccin-mocha/

%files macchiato
%{_datadir}/plymouth/themes/catppuccin-macchiato/

%files frappe
%{_datadir}/plymouth/themes/catppuccin-frappe/

%files latte
%{_datadir}/plymouth/themes/catppuccin-latte/

%changelog
%autochangelog
