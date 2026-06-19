%global commit      198eba2071d80e4a23b8f51a5859e8f4acf8de6c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate  20250428

Name:           catppuccin-plymouth-theme
Version:        0^%{commitdate}git%{shortcommit}
Release:        %autorelease
Summary:        Catppuccin themes for Plymouth boot splash

License:        MIT
URL:            https://github.com/catppuccin/plymouth
Source0:        https://github.com/catppuccin/plymouth/archive/%{commit}/plymouth-%{commit}.tar.gz

BuildArch:      noarch

Requires:       catppuccin-frappe-plymouth-theme = %{version}-%{release}
Requires:       catppuccin-latte-plymouth-theme = %{version}-%{release}
Requires:       catppuccin-macchiato-plymouth-theme = %{version}-%{release}
Requires:       catppuccin-mocha-plymouth-theme = %{version}-%{release}

%description
Meta package for all Catppuccin Plymouth themes.

%package -n catppuccin-frappe-plymouth-theme
Summary:        Catppuccin Frappé theme for Plymouth

Requires:       plymouth-plugin-two-step
Requires:       plymouth-system-theme

%description -n catppuccin-frappe-plymouth-theme
Catppuccin Frappé theme for Plymouth.

%package -n catppuccin-latte-plymouth-theme
Summary:        Catppuccin Latte theme for Plymouth

Requires:       plymouth-plugin-two-step
Requires:       plymouth-system-theme

%description -n catppuccin-latte-plymouth-theme
Catppuccin Latte theme for Plymouth.

%package -n catppuccin-macchiato-plymouth-theme
Summary:        Catppuccin Macchiato theme for Plymouth

Requires:       plymouth-plugin-two-step
Requires:       plymouth-system-theme

%description -n catppuccin-macchiato-plymouth-theme
Catppuccin Macchiato theme for Plymouth.

%package -n catppuccin-mocha-plymouth-theme
Summary:        Catppuccin Mocha theme for Plymouth

Requires:       plymouth-plugin-two-step
Requires:       plymouth-system-theme

%description -n catppuccin-mocha-plymouth-theme
Catppuccin Mocha theme for Plymouth.

%prep
%autosetup -n plymouth-%{commit}

%install
install -d %{buildroot}%{_datadir}/plymouth/themes

cp -a themes/* \
    %{buildroot}%{_datadir}/plymouth/themes/

find %{buildroot}%{_datadir}/plymouth/themes \
    -type f \
    -exec chmod 0644 {} +

%files
%license LICENSE
%doc README.md

%files -n catppuccin-frappe-plymouth-theme
%{_datadir}/plymouth/themes/catppuccin-frappe/

%files -n catppuccin-latte-plymouth-theme
%{_datadir}/plymouth/themes/catppuccin-latte/

%files -n catppuccin-macchiato-plymouth-theme
%{_datadir}/plymouth/themes/catppuccin-macchiato/

%files -n catppuccin-mocha-plymouth-theme
%{_datadir}/plymouth/themes/catppuccin-mocha/

%changelog
%autochangelog
