%global main_commit     f83671d17ea67e335b34f8028a7e6d78bca735d7
%global upstream_commit 0f838ee5679229e3a3e97e3b333c222c9e9615b4

%global shortcommit     %(c=%{main_commit}; echo ${c:0:7})
%global date            20260619

%global debug_package   %{nil}

Name:           papirus-folders-catppuccin
Version:        %{date}git%{shortcommit}
Release:        1%{?dist}
Summary:        Catppuccin folder colors for Papirus

License:        GPL-3.0-only
URL:            https://github.com/catppuccin/papirus-folders

Source0:        https://github.com/catppuccin/papirus-folders/archive/%{main_commit}.tar.gz#/papirus-folders-catppuccin-%{main_commit}.tar.gz
Source1:        https://github.com/PapirusDevelopmentTeam/papirus-folders/archive/%{upstream_commit}.tar.gz#/papirus-folders-upstream-%{upstream_commit}.tar.gz

BuildArch:      noarch
Requires:       papirus-icon-theme

%description
Papirus folders utility bundled with Catppuccin folder colors.

%prep
# Ekstrak Source0 (Catppuccin) sebagai direktori utama build
%autosetup -n papirus-folders-%{main_commit}

# Ekstrak Source1 (Upstream) ke dalam sub-direktori 'upstream'
mkdir upstream
tar -xzf %{SOURCE1} -C upstream --strip-components=1

%install
# Install executable script dari folder upstream
install -Dm755 upstream/papirus-folders %{buildroot}%{_bindir}/papirus-folders

# Install folder icon Catppuccin ke direktori system
install -dm755 %{buildroot}%{_datadir}/icons/Papirus
cp -a src/. %{buildroot}%{_datadir}/icons/Papirus/

%files
%license LICENSE
%doc README.md

%{_bindir}/papirus-folders
%{_datadir}/icons/Papirus/

%changelog
%autochangelog
