%global forgeurl https://github.com/pipeseroni/pipes.sh
%global commit   581792d4e0ea51e15889ba14a85db1bc9727b83d

%forgemeta

Name:           pipes.sh
Version:        1.3.0
Release:        1%{?dist}
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