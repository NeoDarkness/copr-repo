%global commit 198eba2071d80e4a23b8f51a5859e8f4acf8de6c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20260428

%global _plymouththemedir %{_datadir}/plymouth/themes

Name:           plymouth-theme-catppuccin
Version:        0^%{commitdate}git.%{shortcommit}
Release:        %autorelease
Summary:        Soothing pastel theme for Plymouth

License:        MIT
URL:            https://github.com/catppuccin/plymouth
Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildArch:      noarch

Requires:       plymouth-plugin-two-step
Requires:       plymouth-system-theme

%description
Soothing pastel theme for Plymouth.

%prep
%autosetup -n plymouth-%{commit} -p1

%install
install -d %{buildroot}%{_plymouththemedir}
cp -a themes/* %{buildroot}%{_plymouththemedir}/

%files
%license LICENSE
%doc README.md
%{_plymouththemedir}/catppuccin-*

%changelog
%autochangelog