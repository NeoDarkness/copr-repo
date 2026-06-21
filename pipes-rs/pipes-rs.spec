%bcond_without check

%global cargo_install_lib 0
%global __cargo_common_opts %{?_smp_mflags} --workspace --locked

%global debug_package %{nil}
%global __strip /bin/true

Name:           pipes-rs
Version:        1.6.4
Release:        %autorelease
Summary:        Animated terminal screensaver inspired by pipes.sh

License:        BlueOak-1.0.0
URL:            https://github.com/lhvy/pipes-rs
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

ExclusiveArch:  %{rust_arches}

BuildRequires:  cargo-rpm-macros >= 26

%description
pipes-rs is a Rust-based animated terminal screensaver inspired by pipes.sh.

%prep
%autosetup
%cargo_prep -N

sed -i 's/^offline = true$//' .cargo/config.toml

%build
%cargo_build

%install
%cargo_install --package pipes-rs

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE.md
%doc README.md
%{_bindir}/pipes-rs

%changelog
%autochangelog