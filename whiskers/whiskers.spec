%global debug_package %{nil}

Name:           whiskers
Version:        2.9.0
Release:        %autorelease
Summary:        Soothing port creation tool

License:        MIT
URL:            https://github.com/catppuccin/whiskers
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

ExclusiveArch:  %{rust_arches}

BuildRequires:  cargo

%description
Whiskers CLI tool used to generate Catppuccin ports.

%prep
%autosetup

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release --locked

%install
install -Dm0755 target/release/whiskers %{buildroot}%{_bindir}/whiskers

%check
export RUSTFLAGS="%{build_rustflags}"
cargo test --release --locked

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/whiskers

%changelog
%autochangelog