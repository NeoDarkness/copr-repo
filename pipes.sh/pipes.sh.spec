%global forgeurl https://github.com/pipeseroni/pipes.sh
%global version0 1.3.0

%forgemeta

Name:           pipes.sh
Version:        %{forgeversion}
Release:        %autorelease
Summary:        Animated pipes terminal screensaver

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch

BuildRequires:  make

%description
pipes.sh is an animated terminal screensaver inspired by
the classic pipes screensaver.

It renders colorful animated pipes directly in the terminal.

%prep
%forgeautosetup

%build

%install
%make_install PREFIX=%{_prefix} DESTDIR=%{buildroot}

%check

%files
%license LICENSE
%doc README.rst
%{_bindir}/pipes.sh
%{_mandir}/man6/pipes.sh.6*

%changelog
%autochangelog