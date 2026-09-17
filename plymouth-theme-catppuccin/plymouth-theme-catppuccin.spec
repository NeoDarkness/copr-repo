%global commit 198eba2071d80e4a23b8f51a5859e8f4acf8de6c
%global shortcommit %(printf '%.7s' %{commit})
%global commitdate 20260428

%global _plymouththemedir %{_datadir}/plymouth/themes

Name:           plymouth-theme-catppuccin
Version:        0^%{commitdate}git%{shortcommit}
Release:        %autorelease
Summary:        Soothing pastel theme for Plymouth

License:        MIT
URL:            https://github.com/catppuccin/plymouth
Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildArch:      noarch

Requires:       plymouth-plugin-two-step
Requires:       plymouth-system-theme
Provides:       %{name}-mocha = %{version}-%{release}

%description
Soothing pastel theme for Plymouth (Mocha flavor by default).

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

%prep
%autosetup -n plymouth-%{commit} -p1

%install
install -d %{buildroot}%{_plymouththemedir}
cp -a themes/* %{buildroot}%{_plymouththemedir}/

%postun
export PLYMOUTH_PLUGIN_PATH=%{_libdir}/plymouth/
if [ $1 -eq 0 ]; then
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" = "catppuccin-mocha" ]; then
        %{_sbindir}/plymouth-set-default-theme --reset
    fi
fi

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

%files
%license LICENSE
%doc README.md
%{_plymouththemedir}/catppuccin-mocha

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

%changelog
%autochangelog