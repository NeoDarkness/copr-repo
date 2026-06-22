%global commit      198eba2071d80e4a23b8f51a5859e8f4acf8de6c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate  20250428

Name:           catppuccin-plymouth-theme
Version:        0^%{commitdate}git%{shortcommit}
Release:        %autorelease
Summary:        Catppuccin Plymouth themes (Frappé, Latte, Macchiato, Mocha)

License:        MIT
URL:            https://github.com/catppuccin/plymouth
Source0:        %{url}/archive/%{commit}/plymouth-%{commit}.tar.gz

BuildArch:      noarch

Requires:       plymouth-plugin-two-step
Requires:       plymouth-system-theme

%description
Catppuccin Plymouth themes for all variants (Frappé, Latte, Macchiato, Mocha).

%prep
%autosetup -n plymouth-%{commit}

%install
install -d %{buildroot}%{_datadir}/plymouth/themes
cp -a themes/. %{buildroot}%{_datadir}/plymouth/themes/

%files
%license LICENSE
%doc README.md
%{_datadir}/plymouth/themes/catppuccin-*

%changelog
%autochangelog