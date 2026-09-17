%global commit 054a297d303a5bac4f1652a13b17d78a13201c0e
%global shortcommit %(printf '%.7s' %{commit})
%global commitdate 20260620

%global _obsthemedir %{_datadir}/obs/obs-studio/themes

Name:           catppuccin-obs-theme
Version:        0^%{commitdate}git%{shortcommit}
Release:        %autorelease
Summary:        Soothing pastel theme for OBS Studio

License:        MIT
URL:            https://github.com/catppuccin/obs
Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildArch:      noarch

Requires:       obs-studio

%description
Soothing pastel theme for OBS Studio.

%prep
%autosetup -n obs-%{commit} -p1

%install
install -d %{buildroot}%{_obsthemedir}
cp -a themes/* %{buildroot}%{_obsthemedir}/

%files
%license LICENSE
%doc README.md
%{_obsthemedir}/Catppuccin*

%changelog
%autochangelog