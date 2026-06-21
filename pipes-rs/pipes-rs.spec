Name:           pipes-rs
Version:        1.6.4
Release:        %autorelease
Summary:        Animated terminal screensaver inspired by pipes.sh

License:        BlueOak-1.0.0
URL:            https://github.com/lhvy/pipes-rs
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cargo

%description
pipes-rs is a Rust-based animated terminal screensaver inspired by pipes.sh.

%prep
%autosetup

%build
cargo build --release --locked

%install
install -Dm0755 target/release/pipes-rs %{buildroot}%{_bindir}/pipes-rs

%check
cargo test --release --locked

%files
%license LICENSE.md
%doc README.md
%{_bindir}/pipes-rs

%changelog
%autochangelog