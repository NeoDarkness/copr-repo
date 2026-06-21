Name:           catppuccin-whiskers
Version:        2.9.0
Release:        %autorelease
Summary:        Soothing port creation tool for the high-spirited!

License:        MIT
URL:            https://github.com/catppuccin/whiskers
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  rust-packaging

%description
Whiskers is a CLI tool used to generate Catppuccin ports.

%generate_buildrequires
%cargo_generate_buildrequires

%prep
%autosetup -n whiskers-%{version}

%cargo_prep

%build
%cargo_build --locked

%install
%cargo_install --locked

%check
%cargo_test --locked

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/whiskers

%changelog
%autochangelog