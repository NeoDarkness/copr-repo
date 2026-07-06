%global forgeurl https://github.com/catppuccin/plymouth
%global commit 198eba2071d80e4a23b8f51a5859e8f4acf8de6c
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           plymouth-theme-catppuccin
Version:        0^git%{shortcommit}
Release:        %autorelease
Summary:        Soothing pastel theme for Plymouth

License:        MIT
URL:            %{forgeurl}

%forgemeta

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
%forgeautosetup

%build
# Nothing to build

%install
install -d %{buildroot}%{_datadir}/plymouth/themes
cp -a themes/. %{buildroot}%{_datadir}/plymouth/themes/

%global plymouth_postun(theme) \
export PLYMOUTH_PLUGIN_PATH=%{_libdir}/plymouth/ \
if [ $1 -eq 0 ]; then \
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" = "%{theme}" ]; then \
        %{_sbindir}/plymouth-set-default-theme --reset \
    fi \
fi \
%{nil}

%postun latte
%plymouth_postun catppuccin-latte

%postun frappe
%plymouth_postun catppuccin-frappe

%postun macchiato
%plymouth_postun catppuccin-macchiato

%postun mocha
%plymouth_postun catppuccin-mocha

%check
# No test suite available

%files

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