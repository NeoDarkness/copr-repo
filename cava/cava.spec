%global forgeurl https://github.com/karlstav/cava

Version:        1.0.0

%global tag %{version}

%forgemeta

Name:           cava
Release:        %autorelease
Summary:        Console-based Audio Visualizer for ALSA

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(iniparser)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(ncursesw)

%description
C.A.V.A. is a bar spectrum analyzer for audio using ALSA for input.

%prep
%forgeautosetup
%autoreconf

%build
%configure --with-fontdir=/lib/kbd/consolefonts LIBS="-lrt"
%make_build

%install
%make_install

%check

%files
%license LICENSE
%doc README.md
%doc example_files
%{_bindir}/cava
/lib/kbd/consolefonts/cava.psf

%changelog
%autochangelog