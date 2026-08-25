%global forgeurl https://github.com/catppuccin/obs
%global commit 054a297d303a5bac4f1652a13b17d78a13201c0e

%global _obsthemedir %{_datadir}/obs/obs-studio/themes

%forgemeta

Name:           catppuccin-obs-theme
Version:        0^20260620.g054a297
Release:        %autorelease
Summary:        Soothing pastel theme for OBS Studio

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch

Requires:       obs-studio

%description
Soothing pastel theme for OBS Studio.

%prep
%forgeautosetup -p1

%build

%install
install -d %{buildroot}%{_obsthemedir}
cp -r themes/* %{buildroot}%{_datadir}/

%check

%files
%license LICENSE
%doc README.md
%{_obsthemedir}/Catppuccin*

%changelog
%autochangelog