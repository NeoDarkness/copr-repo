%global forgeurl https://github.com/pipeseroni/pipes.sh

Name:           pipes.sh
Version:        1.3.0
Release:        %autorelease
Summary:        Animated pipes terminal screensaver

License:        MIT

%forgemeta

URL:            https://github.com/pipeseroni/pipes.sh
Source0:        %forgesource

BuildArch:      noarch
BuildRequires:  make

%description
pipes.sh is an animated pipes terminal screensaver inspired by the classic pipes screensaver.

%prep
%forgeautosetup

%install
%make_install

%files
%license LICENSE
%doc README.rst
%{_bindir}/pipes.sh
%{_mandir}/man6/pipes.sh.6*

%changelog
%autochangelog