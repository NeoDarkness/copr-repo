%global forgeurl https://github.com/catppuccin/obs
%global commit   054a297d303a5bac4f1652a13b17d78a13201c0e

%forgemeta

Name:           catppuccin-obs-theme
Version:        %{forgeversion}
Release:        %autorelease
Summary:        Soothing pastel theme for OBS Studio

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch

%description
Soothing pastel theme for OBS Studio.

%prep
%forgeautosetup

%build

%install
install -d %{buildroot}%{_datadir}/obs/obs-studio/themes
cp -a themes/. %{buildroot}%{_datadir}/obs/obs-studio/themes/

%check

%files
%license LICENSE
%doc README.md
%{_datadir}/obs/obs-studio/themes/Catppuccin.obt
%{_datadir}/obs/obs-studio/themes/Catppuccin_Frappe.ovt
%{_datadir}/obs/obs-studio/themes/Catppuccin_Latte.ovt
%{_datadir}/obs/obs-studio/themes/Catppuccin_Macchiato.ovt
%{_datadir}/obs/obs-studio/themes/Catppuccin_Mocha.ovt

%changelog
%autochangelog