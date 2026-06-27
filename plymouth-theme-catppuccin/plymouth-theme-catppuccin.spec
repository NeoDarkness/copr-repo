%global forgeurl https://github.com/catppuccin/plymouth
%global commit 198eba2071d80e4a23b8f51a5859e8f4acf8de6c

Name:           plymouth-theme-catppuccin
Version:        0
Release:        %autorelease
Summary:        Soothing pastel themes for Plymouth

License:        MIT
URL:            %{forgeurl}

%forgemeta

Source:         %{forgesource}

BuildArch:      noarch

Requires:       %{name}-latte = %{version}-%{release}
Requires:       %{name}-frappe = %{version}-%{release}
Requires:       %{name}-macchiato = %{version}-%{release}
Requires:       %{name}-mocha = %{version}-%{release}

%description
Meta package that installs all Catppuccin Plymouth themes.

%package latte
Summary:        Catppuccin Latte Plymouth theme
Requires:       plymouth-plugin-two-step
Requires:       plymouth-system-theme

%description latte
Catppuccin Latte theme for Plymouth.

%package frappe
Summary:        Catppuccin Frappe Plymouth theme
Requires:       plymouth-plugin-two-step
Requires:       plymouth-system-theme

%description frappe
Catppuccin Frappe theme for Plymouth.

%package macchiato
Summary:        Catppuccin Macchiato Plymouth theme
Requires:       plymouth-plugin-two-step
Requires:       plymouth-system-theme

%description macchiato
Catppuccin Macchiato theme for Plymouth.

%package mocha
Summary:        Catppuccin Mocha Plymouth theme
Requires:       plymouth-plugin-two-step
Requires:       plymouth-system-theme

%description mocha
Catppuccin Mocha theme for Plymouth.

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
%license LICENSE
%doc README.md

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