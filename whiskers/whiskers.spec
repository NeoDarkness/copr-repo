Name:           whiskers
Version:        2.9.0
Release:        %autorelease
Summary:        Soothing port creation tool

License:        MIT
URL:            https://github.com/catppuccin/whiskers
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cargo

%description
Whiskers CLI tool used to generate Catppuccin ports.

%prep
%autosetup

%build
cargo build --release --locked

%install
install -Dm0755 target/release/whiskers %{buildroot}%{_bindir}/whiskers

%check
cargo test --release --locked

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/whiskers

%changelog
%autochangelog