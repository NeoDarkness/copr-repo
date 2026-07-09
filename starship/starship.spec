%bcond check 0

%global forgeurl https://github.com/starship/starship
%global commit   6530bea7e06949a647d5694792ed7699cab05743

%forgemeta

Name:           starship
Version:        1.26.0
Release:        %autorelease
Summary:        The minimal, blazing-fast, and infinitely customizable prompt

SourceLicense:  ISC
License:        ISC

URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        vendor.tar.gz

BuildRequires:  cargo-rpm-macros

%description
The cross-shell prompt for astronauts.

%prep
%autosetup -n %{archivename} -p1 -a1
%cargo_prep -v vendor

%build
%cargo_build

%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}

# Generate shell completions
target/rpm/starship completions bash > starship.bash
target/rpm/starship completions fish > starship.fish
target/rpm/starship completions zsh > _starship

# Generate man page
target/rpm/starship man > starship.1

%install
install -Dpm0755 \
    target/rpm/starship \
    %{buildroot}%{_bindir}/starship

install -Dpm0644 \
    starship.bash \
    %{buildroot}%{bash_completions_dir}/starship

install -Dpm0644 \
    starship.fish \
    %{buildroot}%{fish_completions_dir}/starship.fish

install -Dpm0644 \
    _starship \
    %{buildroot}%{zsh_completions_dir}/_starship

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%doc CHANGELOG.md
%{_bindir}/starship
%{bash_completions_dir}/starship
%{fish_completions_dir}/starship.fish
%{zsh_completions_dir}/_starship

%changelog
%autochangelog