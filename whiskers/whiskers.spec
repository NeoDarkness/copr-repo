%bcond_without check

%global debug_package %{nil}
%global cargo_install_lib 0
%global __cargo_common_opts %{?_smp_mflags} --locked

Name:           whiskers
Version:        2.9.0
Release:        %autorelease
Summary:        Soothing port creation tool

License:        MIT
URL:            https://github.com/catppuccin/whiskers
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

ExclusiveArch:  %{rust_arches}

BuildRequires:  cargo-rpm-macros >= 26

%description
Whiskers CLI tool used to generate Catppuccin ports.

%prep
%autosetup
%cargo_prep -N

sed -i 's/^offline = true$//' .cargo/config.toml || true

%build
%cargo_build

%install
%cargo_install -p whiskers

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/whiskers

%changelog
%autochangelog