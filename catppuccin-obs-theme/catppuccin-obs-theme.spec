%global forgeurl https://github.com/catppuccin/obs
%global commit 054a297d303a5bac4f1652a13b17d78a13201c0e
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           catppuccin-obs-theme
Version:        0^git%{shortcommit}
Release:        %autorelease
Summary:        Soothing pastel theme for OBS Studio

License:        MIT
URL:            %{forgeurl}

%forgemeta

Source0:        %{forgesource}

BuildArch:      noarch

%description
Soothing pastel theme for OBS Studio.

%prep
%forgeautosetup

%build
# Nothing to build

%install
install -d %{buildroot}%{_datadir}/obs/obs-studio/themes
cp -a themes/. %{buildroot}%{_datadir}/obs/obs-studio/themes/

%check
# No test suite available

%files
%license LICENSE
%doc README.md
%{_datadir}/obs/obs-studio/themes/*

%changelog
%autochangelog