%global forgeurl https://github.com/catppuccin/plymouth
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

Requires:       %{name}-latte = %{version}-%{release}
Requires:       %{name}-frappe = %{version}-%{release}
Requires:       %{name}-macchiato = %{version}-%{release}
Requires:       %{name}-mocha = %{version}-%{release}

%description
Meta package that installs all Catppuccin Plymouth themes:
Frappe, Latte, Macchiato, and Mocha.

%package latte
Summary:        Catppuccin Latte Plymouth theme
Requires:       plymouth-plugin-two-step
Requires:       plymouth-system-theme

%description latte
Catppuccin Latte flavor theme for Plymouth.

%package frappe
Summary:        Catppuccin Frappe Plymouth theme
Requires:       plymouth-plugin-two-step
Requires:       plymouth-system-theme

%description frappe
Catppuccin Frappe flavor theme for Plymouth.

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

%build
# Nothing to build

%install
install -d %{buildroot}%{_datadir}/plymouth/themes
cp -a themes/* %{buildroot}%{_datadir}/plymouth/themes/

%postun latte
export PLYMOUTH_PLUGIN_PATH=%{_libdir}/plymouth/
if [ $1 -eq 0 ]; then
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" == "catppuccin-latte" ]; then
        %{_sbindir}/plymouth-set-default-theme --reset
    fi
fi

%postun frappe
export PLYMOUTH_PLUGIN_PATH=%{_libdir}/plymouth/
if [ $1 -eq 0 ]; then
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" == "catppuccin-frappe" ]; then
        %{_sbindir}/plymouth-set-default-theme --reset
    fi
fi

%postun macchiato
export PLYMOUTH_PLUGIN_PATH=%{_libdir}/plymouth/
if [ $1 -eq 0 ]; then
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" == "catppuccin-macchiato" ]; then
        %{_sbindir}/plymouth-set-default-theme --reset
    fi
fi

%postun mocha
export PLYMOUTH_PLUGIN_PATH=%{_libdir}/plymouth/
if [ $1 -eq 0 ]; then
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" == "catppuccin-mocha" ]; then
        %{_sbindir}/plymouth-set-default-theme --reset
    fi
fi

%check
# No test suite available

%files
%license LICENSE
%doc README.md

%files latte
%license LICENSE
%doc README.md
%dir %{_datadir}/plymouth/themes/catppuccin-latte
%{_datadir}/plymouth/themes/catppuccin-latte/

%files frappe
%license LICENSE
%doc README.md
%dir %{_datadir}/plymouth/themes/catppuccin-frappe
%{_datadir}/plymouth/themes/catppuccin-frappe/

%files macchiato
%license LICENSE
%doc README.md
%dir %{_datadir}/plymouth/themes/catppuccin-macchiato
%{_datadir}/plymouth/themes/catppuccin-macchiato/

%files mocha
%license LICENSE
%doc README.md
%dir %{_datadir}/plymouth/themes/catppuccin-mocha
%{_datadir}/plymouth/themes/catppuccin-mocha/

%changelog
%autochangelog