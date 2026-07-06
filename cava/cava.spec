%global forgeurl https://github.com/karlstav/cava
%global commit 4b12c2b043723f42567ddbfd5a516566bdf52316

Name:           cava
Version:        1.0.0
Release:        %autorelease
Summary:        Console-based Audio Visualizer for Alsa

License:        MIT
URL:            %{forgeurl}

%forgemeta

Source0:        %{forgesource}

BuildRequires:  alsa-lib-devel
BuildRequires:  fftw-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
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
# No test suite available

%files
%license LICENSE
%doc README.md
%doc example_files
%{_bindir}/cava
/lib/kbd/consolefonts/cava.psf

%changelog
%autochangelog