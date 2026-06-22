Name:           whiskers
Version:        2.9.0
Release:        %autorelease
Summary:        Soothing port creation tool

License:        MIT

%forgemeta

URL:            https://github.com/catppuccin/whiskers
Source0:        %forgesource

ExclusiveArch:  %{rust_arches}

BuildRequires:  cargo-rpm-macros >= 24

%description
Whiskers CLI tool used to generate Catppuccin ports.

%prep
%forgeautosetup
%cargo_prep
%generate_buildrequires
%cargo_generate_buildrequires -a

%build
%cargo_build -a

%check
%cargo_test -a

%install
install -Dm0755 target/rpm/whiskers \
    %{buildroot}%{_bindir}/whiskers

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/whiskers

%changelog
%autochangelog