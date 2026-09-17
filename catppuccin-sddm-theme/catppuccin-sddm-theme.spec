%global commit 28699090372cce33c12a923cf8fc297a9cae2cd4
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20250908

%global _sddmthemedir %{_datadir}/sddm/themes

Name:           catppuccin-sddm-theme
Version:        0^%{commitdate}git.%{shortcommit}
Release:        %autorelease
Summary:        Soothing pastel theme for SDDM

License:        MIT
URL:            https://github.com/catppuccin/sddm
Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildArch:      noarch

BuildRequires:  catppuccin-whiskers
BuildRequires:  just

Requires:       sddm

%description
Soothing pastel theme for SDDM.

%prep
%autosetup -n sddm-%{commit} -p1

%build
just build

%install
install -d %{buildroot}%{_sddmthemedir}
cp -a themes/* %{buildroot}%{_sddmthemedir}/

%files
%license LICENSE
%doc README.md
%doc CHANGELOG.md
%{_sddmthemedir}/catppuccin-*

%changelog
%autochangelog