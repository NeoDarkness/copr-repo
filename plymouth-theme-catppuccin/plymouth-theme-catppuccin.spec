%global forgeurl https://github.com/catppuccin/plymouth
%global commit 198eba2071d80e4a23b8f51a5859e8f4acf8de6c

%global _plymouththemedir %{_datadir}/plymouth/themes

%forgemeta

Name:           plymouth-theme-catppuccin
Version:        0^20260428.g198eba2
Release:        %autorelease
Summary:        Soothing pastel theme for Plymouth

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch

%description
Soothing pastel theme for Plymouth.

%package latte
Summary:        Soothing pastel theme for Plymouth - Latte

Requires:       plymouth-plugin-two-step
Requires:       plymouth-system-theme

%description latte
Soothing pastel theme for Plymouth - Latte.

%package frappe
Summary:        Soothing pastel theme for Plymouth - Frappe

Requires:       plymouth-plugin-two-step
Requires:       plymouth-system-theme

%description frappe
Soothing pastel theme for Plymouth - Frappe.

%package macchiato
Summary:        Soothing pastel theme for Plymouth - Macchiato

Requires:       plymouth-plugin-two-step
Requires:       plymouth-system-theme

%description macchiato
Soothing pastel theme for Plymouth - Macchiato.

%package mocha
Summary:        Soothing pastel theme for Plymouth - Mocha

Requires:       plymouth-plugin-two-step
Requires:       plymouth-system-theme

%description mocha
Soothing pastel theme for Plymouth - Mocha.

%prep
%forgeautosetup -p1

%build

%install
install -d %{buildroot}%{_plymouththemedir}
cp -r themes/* %{buildroot}%{_plymouththemedir}/

%postun latte
export PLYMOUTH_PLUGIN_PATH=%{_libdir}/plymouth/
if [ $1 -eq 0 ]; then
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" = "catppuccin-latte" ]; then
        %{_sbindir}/plymouth-set-default-theme --reset
    fi
fi

%postun frappe
export PLYMOUTH_PLUGIN_PATH=%{_libdir}/plymouth/
if [ $1 -eq 0 ]; then
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" = "catppuccin-frappe" ]; then
        %{_sbindir}/plymouth-set-default-theme --reset
    fi
fi

%postun macchiato
export PLYMOUTH_PLUGIN_PATH=%{_libdir}/plymouth/
if [ $1 -eq 0 ]; then
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" = "catppuccin-macchiato" ]; then
        %{_sbindir}/plymouth-set-default-theme --reset
    fi
fi

%postun mocha
export PLYMOUTH_PLUGIN_PATH=%{_libdir}/plymouth/
if [ $1 -eq 0 ]; then
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" = "catppuccin-mocha" ]; then
        %{_sbindir}/plymouth-set-default-theme --reset
    fi
fi

%check

%files

%files latte
%license LICENSE
%doc README.md
%{_plymouththemedir}/catppuccin-latte

%files frappe
%license LICENSE
%doc README.md
%{_plymouththemedir}/catppuccin-frappe

%files macchiato
%license LICENSE
%doc README.md
%{_plymouththemedir}/catppuccin-macchiato

%files mocha
%license LICENSE
%doc README.md
%{_plymouththemedir}/catppuccin-mocha

%changelog
%autochangelog