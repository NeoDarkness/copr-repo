%global forgeurl https://github.com/catppuccin/whiskers

Name:           whiskers
Version:        2.9.0
Release:        %autorelease
Summary:        Soothing port creation tool

License:        MIT

%forgemeta

URL:            https://github.com/catppuccin/whiskers
Source0:        %forgesource

ExclusiveArch:  %{rust_arches}

BuildRequires:  cargo

%description
Whiskers CLI tool used to generate Catppuccin ports.

%prep
%forgeautosetup

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release --locked

%install
install -Dm0755 target/release/whiskers \
    %{buildroot}%{_bindir}/whiskers

%check
export RUSTFLAGS="%{build_rustflags}"
cargo test --release --locked

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/whiskers

%changelog
%autochangelog