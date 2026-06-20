%global debug_package %{nil}

Name:           catppuccin-whiskers
Version:        2.9.0
Release:        %autorelease
Summary:        Soothing port creation tool for the high-spirited!

License:        MIT
URL:            https://github.com/catppuccin/whiskers

ExclusiveArch:  x86_64

Source0:        %{url}/releases/download/v%{version}/whiskers-x86_64-unknown-linux-gnu

Provides:       whiskers = %{version}-%{release}

%description
Soothing port creation tool for the high-spirited!

%install
install -D -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/whiskers

%files
%{_bindir}/whiskers

%changelog
%autochangelog