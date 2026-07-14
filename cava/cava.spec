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

BuildRequires:  alsa-lib-devel
BuildRequires:  fftw-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  pipewire-devel
BuildRequires:  iniparser-devel
BuildRequires:  make

%description
C.A.V.A. is a bar spectrum analyzer for audio using ALSA for input.

%prep
%forgeautosetup
./autogen.sh

%build
%configure FONT_DIR=/lib/kbd/consolefonts
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